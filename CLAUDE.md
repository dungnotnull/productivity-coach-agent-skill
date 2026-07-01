# CLAUDE.md — Productivity Coach (Pomodoro/GTD) (Skill #164)

**Slug:** `productivity-coach`  •  **Cluster:** `lifestyle-personal`  •  **Source idea:** 164  •  **Phase:** Built (v1)

## Tagline
Coaches personal time management and work-process optimization using Pomodoro, GTD, and evidence-based focus methods.

## Problem This Skill Solves
People stay busy but unproductive because tasks are unprioritized, focus is fragmented, and workload is unsustainable. This skill diagnoses the workflow and prescribes a personalized, sustainable productivity system.

## Harness Flow Summary
1. **Intake** (`sub-intake`) — gather structured inputs, scope, goals.

2. **Framework selection** (`sub-framework-selector`) — choose named world-renowned framework(s).
3. **Research** (WebSearch/WebFetch + SECOND-KNOWLEDGE-BRAIN) — gather highest-tier evidence.
4. **Scoring** (`sub-scoring-engine`) — multi-dimensional weighted scores with citations.
5. **Challenge** — devil's-advocate review of assumptions and weak evidence.

**Roadmap** (`sub-improvement-roadmap`) — prioritized effort/impact recommendations.
**Synthesize** — assemble the professional deliverable; pass Quality Gates.

## Gates
- No mandatory safety/compliance gate for this cluster, but the standard Quality Gates below still apply.

## Sub-skills
- `skills/sub-intake.md` — Intake & Context Gathering: Collect the structured inputs, scope, and goals needed to run the analysis; ask clarifying questions when key facts are missing.
- `skills/sub-framework-selector.md` — Evaluation Framework Selector: Pick the most appropriate named world-renowned framework(s) for the case and justify the choice.
- `skills/sub-scoring-engine.md` — Scoring Engine: Apply the multi-dimensional rubric to produce weighted scores with evidence citations for each dimension.
- `skills/sub-improvement-roadmap.md` — Improvement Roadmap: Generate a prioritized, effort/impact-ranked set of recommendations traceable to the scored findings.

## Tools Required
- `WebSearch`, `WebFetch` — live evidence and standards updates
- `Read`, `Write` — load knowledge base, emit deliverables
- `Bash` — run `tools/knowledge_updater.py`
- Skill tool — invoke sub-skills in sequence

## Knowledge Sources
- ArXiv: (none — non-paper domain; rely on authoritative web sources)
- Authoritative domain sources:
  - https://hbr.org
  - https://jamesclear.com
  - https://todoist.com/productivity-methods
  - https://www.calnewport.com
- Crawl queries: productivity methods research; deep work focus evidence; time management GTD pomodoro; procrastination behavioral science

## Supporting Tools
- `tools/knowledge_updater.py` — crawl4ai pipeline that grows `SECOND-KNOWLEDGE-BRAIN.md` (weekly cron recommended).

## Active Development Tasks
- [x] Scaffold full deliverable set
- [x] Define 4 sub-skills
- [ ] Expand SECOND-KNOWLEDGE-BRAIN with first live crawl
- [ ] Add regression cases from real user runs

## Related Root Docs
- `PROJECT-detail.md` — full technical spec
- `PROJECT-DEVELOPMENT-PHASE-TRACKING.md` — phase roadmap
- `SECOND-KNOWLEDGE-BRAIN.md` — self-improving knowledge base
