#!/usr/bin/env python3
"""Offline tests: never invoke an account or convert the real corpus."""
import copy
import fcntl
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

import showtell_convert as loop


def response():
    def beat(bid, pattern, props):
        return {'beat_id': bid, 'narration_text': 'An explanation.', 'voice': 'am_onyx',
                'engine': 'kokoro', 'proof_gate': 'SHOW', 'lane': 'bookend',
                'shot': {'show': [{'at': 0.1, 'event': 'object arrives'}],
                         'remotion': {'pattern': pattern, 'props': props}}}
    intro = beat('BIDEA', 'BrutalistHesitantWriter', {'text': 'Only text', 'triggerWords': 'text', 'replacementWords': 'images'})
    intro.update(narration_text='Hallo. This is Liam, in for Bear.', lead_silence_s=0.8)
    terms = beat('BDEFS', 'ClaudeDefinitions', {'terms': [{'term': 'image', 'meaning': 'A drawing'}, {'term': 'voice', 'meaning': 'Spoken explanation'}]})
    body = beat('B00', '', {})
    body['lane'] = 'manim'
    body['shot'].update(manim={'class': 'B00_Box'}, visual_intent='A box opens', motion_claim='Contents emerge')
    handoff = beat('BHTF', 'ClaudeComposerAsk', {'greeting': 'Your turn.', 'topic': 'YOUR TURN', 'command': 'Draw a box.', 'output': ['Check one', 'Check two']})
    handoff['narration_text'] = 'Your turn. Draw a box.'
    outro = beat('BOUT', 'ClaudeTitleOutro', {'handle': '@NikBearBrown'})
    outro.update(narration_text='Boxes. At Nik Bear Brown.', kind='outro_voice', tail_silence_s=1.0)
    return {'sheet': {'metadata': {'title': 'Boxes', 'skill': 'show-tell', 'style_preset': 'show-tell',
        'channel': 'claude-liam', 'voice': 'am_onyx', 'engine': 'kokoro', 'palette': 'claude',
        'caption_policy': 'none', 'width': 3840, 'height': 2160, 'bookend_exempt': ['cold-open', 'bvdt'],
        'bookend_exempt_reason': 'Show-tell spine'}, 'beats': [intro, terms, body, handoff, outro]},
        'coverage': [{'source_index': 0, 'target_beats': ['B00'], 'reason': 'Illustrates the original idea'}],
        'notes': 'Account quota is discussed as source content; no new fact checking.'}


class LoopTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='showtell-loop-test-')
        self.root = Path(self.temp.name)
        self.source = {'metadata': {'title': 'Boxes'}, 'beats': [{'narration_text': 'A box holds things.'}]}

    def tearDown(self):
        self.temp.cleanup()

    def put(self, name, content=None):
        p = self.root / name
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps(self.source if content is None else content))
        return p

    def test_discovery(self):
        self.put('nested space/beat_sheet.json')
        self.put('nested space/beat_sheet.nbb.json')
        self.put('nested space/beat_sheet.pre-rebuild.json')
        self.put('show-tell-conversions/x/beat_sheet.json')
        self.put('_superseded/beat_sheet.json')
        self.put('done/beat_sheet.json', response()['sheet'])
        (self.root / 'alias').symlink_to(self.root / 'nested space', target_is_directory=True)
        items, stats = loop.discover(self.root)
        self.assertEqual(len(items), 2)
        self.assertEqual(stats['already_show_tell'], 1)
        self.assertEqual(len(loop.discover(self.root, True)[0]), 3)

    def test_bad_sheet_is_recorded(self):
        self.put('beat_sheet.json', {'beats': []})
        self.assertIn('error', loop.discover(self.root)[0][0])

    def test_lecture_segments_preserve_nested_content(self):
        lecture = {'title': 'Lecture', 'segments': [{'id': 'S01', 'body_html': '<p>A box</p>',
                   'beats': [{'text': 'A box holds things.'}]}]}
        self.put('lecture/beat_sheet.json', lecture)
        self.assertNotIn('error', loop.discover(self.root)[0][0])
        normalized = loop.normalize_source(lecture)
        self.assertEqual(normalized['beats'], lecture['segments'])
        loop.validate(response(), normalized)

    def test_contract(self):
        loop.validate(response(), self.source)
        for change in ('spine', 'voice', 'coverage', 'timing', 'card'):
            result = response()
            if change == 'spine': result['sheet']['beats'].reverse()
            if change == 'voice': result['sheet']['metadata']['voice'] = 'wrong'
            if change == 'coverage': result['coverage'] = []
            if change == 'timing': result['sheet']['beats'][2]['audio_file'] = 'old.mp3'
            if change == 'card': result['sheet']['beats'][2]['lane'] = 'card'
            with self.subTest(change=change), self.assertRaises(ValueError):
                loop.validate(result, self.source)

    def test_dry_is_read_only(self):
        self.put('beat_sheet.json')
        before = list(self.root.iterdir())
        self.assertEqual(loop.main([str(self.root), '--dry']), 0)
        self.assertEqual(before, list(self.root.iterdir()))

    def fake(self, result=None):
        fixture = self.put('fixture.json', {'structured_output': result or response()})
        worker = self.root / 'fake-claude'
        worker.write_text('#!' + sys.executable + '\nimport sys\nfrom pathlib import Path\nsys.stdin.read()\nprint(Path(' + repr(str(fixture)) + ').read_text())\n')
        worker.chmod(0o755)
        return str(worker)

    def test_real_subprocess_resume_rebuild_and_source_change(self):
        src = self.put('path with spaces/beat_sheet.json')
        original = src.read_bytes()
        worker = self.fake()
        args = [str(self.root), '--claude', worker, '--once']
        self.assertEqual(loop.main(args), 0)
        state = loop.load_state(self.root)
        record = state['items']['path with spaces/beat_sheet.json']
        first = self.root / record['output']
        self.assertTrue(first.exists())
        self.assertEqual(src.read_bytes(), original)
        self.assertEqual(loop.main(args), 0)
        self.assertEqual(loop.load_state(self.root)['items']['path with spaces/beat_sheet.json']['output'], record['output'])
        self.assertEqual(loop.main(args + ['--rebuild']), 0)
        self.assertTrue(first.exists())
        self.assertNotEqual(loop.load_state(self.root)['items']['path with spaces/beat_sheet.json']['output'], record['output'])
        src.write_text(json.dumps(dict(self.source, extra='changed')))
        self.assertEqual(loop.main(args), 0)

    def test_duplicate_worker_refused(self):
        self.put('beat_sheet.json')
        state_dir = self.root / loop.STATE_NAME
        state_dir.mkdir()
        with (state_dir / 'worker.lock').open('w') as lock:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
            self.assertEqual(loop.main([str(self.root), '--claude', self.fake()]), 2)

    def test_failure_and_explicit_retry(self):
        self.put('beat_sheet.json')
        bad = response()
        bad['coverage'] = []
        args = [str(self.root), '--claude', self.fake(bad)]
        self.assertEqual(loop.main(args), 1)
        record = loop.load_state(self.root)['items']['beat_sheet.json']
        self.assertEqual(record['status'], 'failed')
        self.fake()
        self.assertEqual(loop.main(args), 1)
        self.assertEqual(loop.load_state(self.root)['items']['beat_sheet.json']['attempt'], record['attempt'])
        self.assertEqual(loop.main(args + ['--retry-failed']), 0)

    def test_account_error_halts(self):
        self.put('beat_sheet.json')
        self.put('next/beat_sheet.json')
        worker = self.fake()
        self.put('fixture.json', {'is_error': True, 'result': 'Monthly spend limit reached'})
        self.assertEqual(loop.main([str(self.root), '--claude', worker]), 1)
        state = loop.load_state(self.root)
        self.assertEqual(len(state['items']), 1)
        self.assertEqual(state['items']['beat_sheet.json']['status'], 'blocked')


if __name__ == '__main__':
    unittest.main()
