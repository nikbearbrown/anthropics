def dedupe(items):
    return list({repr(x): x for x in items}.values())
