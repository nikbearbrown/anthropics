# Source Details — knowledge-work-plugins--claude-liam-nextflow-development

Generated: 2026-09-05T11:09:01

## Reel
- Question: Claude, Nextflow Development.
- Family: knowledge-work-plugins
- Source sheet: /Users/nik/Documents/books/anthropics/knowledge-work-plugins/youtube/claude-liam-nextflow-development/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/knowledge-work-plugins/bio-research/skills/nextflow-development/SKILL.md
- Name: nextflow-development
- Description: Run nf-core bioinformatics pipelines (rnaseq, sarek, atacseq) on sequencing data. Use when analyzing RNA-seq, WGS/WES, or ATAC-seq data—either local FASTQs or public datasets from GEO/SRA. Triggers on nf-core, Nextflow, FASTQ analysis, variant calling, gene expression, differential expression, GEO reanalysis, GSE/GSM/SRR accessions, or samplesheet creation.

## Capabilities To Name On Screen
- Run nf-core bioinformatics pipelines (rnaseq
- atacseq) on sequencing data
- Use when analyzing RNA-seq
- or ATAC-seq data—either local FASTQs or public datasets from GEO/SRA
- Triggers on nf-core

## Constraints / Failure Modes
- [ ] Step 1: Environment check (MUST pass)
- [ ] Step 3: Run test profile (MUST pass)
- ## Step 0: Acquire Data (GEO/SRA Only)
- All critical checks must pass. If any fail, provide fix instructions:
- Do not proceed until all checks pass. For HPC/Singularity, see references/troubleshooting.md
- Validates environment with small data. MUST pass before real data

## Procedure / Sequence
- Acquire Data (GEO/SRA Only): Skip this step if user has local FASTQ files. For public datasets, fetch from GEO/SRA first. See…
- Environment Check: Run first. Pipeline will fail without passing environment. All critical checks must pass. If any fail, provide fix…
- Select Pipeline: DECISION POINT: Confirm with user before proceeding. | Data Type | Pipeline | Version | Goal |…
- Run Test Profile: Validates environment with small data. MUST pass before real data. | Pipeline | Command | |----------|---------| |…
- Create Samplesheet
- Configure & Run
- Verify Outputs

## Supporting Files And Signals
- Referenced: sudo usermod -aG docker $USER
- Referenced: curl -s https://get.nextflow.io \| bash && mv nextflow ~/bin/
- Referenced: nextflow self-update
- Referenced: sudo apt install openjdk-11-jdk
- Referenced: nextflow run nf-core/rnaseq -r 3.22.2 -profile test,docker --outdir test_rnaseq
- Referenced: nextflow run nf-core/sarek -r 3.7.1 -profile test,docker --outdir test_sarek
- Referenced: nextflow run nf-core/atacseq -r 2.1.2 -profile test,docker --outdir test_atacseq
- Referenced: -r
- Referenced: -profile docker
- Referenced: --genome
- Signal: code block: bash
- Signal: code block: csv

## Source Sections
- Workflow Checklist
- Step 0: Acquire Data (GEO/SRA Only)
- Step 1: Environment Check
- Docker issues
- Nextflow issues
- Java issues
- Step 2: Select Pipeline
- Step 3: Run Test Profile
- Step 4: Create Samplesheet
- Generate automatically

## Batch Log Match
- Row: 319
- Canonical path: anthropics/knowledge-work-plugins/bio-research/skills/nextflow-development/SKILL.md
- MP4 path: anthropics/knowledge-work-plugins/youtube/claude-liam-nextflow-development/mp4/claude-liam-nextflow-development.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.
