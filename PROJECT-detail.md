# PROJECT-detail.md — Productivity Coach (Pomodoro/GTD) (Skill #164)

## Executive Summary
Coaches personal time management and work-process optimization using Pomodoro, GTD, and evidence-based focus methods. This skill is a full Claude harness in the **lifestyle-personal** cluster. It runs a research-first, framework-grounded workflow that scores the subject against named world-renowned methodologies and returns a prioritized improvement roadmap, while continuously updating its knowledge base.

## Problem Statement
People stay busy but unproductive because tasks are unprioritized, focus is fragmented, and workload is unsustainable. This skill diagnoses the workflow and prescribes a personalized, sustainable productivity system.

## Target Users & Use Cases
Practitioners, reviewers, and decision-makers who need an expert-grade, evidence-based assessment in this domain. Trigger examples:
1. **Overwhelm** — User: "I have too much to do" -> Skill prioritizes (Eisenhower), designs day plan, scores.
2. **Focus** — User: "I can't concentrate" -> Skill prescribes deep-work + Pomodoro, scores fit.
3. **System** — User: "Set up GTD for me" -> Skill builds GTD workflow, scores simplicity.
4. **Goals** — User: "Align my week to my OKRs" -> Skill maps tasks to goals (Pareto), scores.
5. **Degraded mode** — User: "Coach offline" -> Falls back to brain methods, flags trend tips stale.

## Harness Architecture
```
/productivity-coach (main.md)
   ├── sub-intake .................... Intake & Context Gathering
   ├── sub-framework-selector ........ Evaluation Framework Selector
   ├── sub-scoring-engine ............ Scoring Engine
   ├── sub-improvement-roadmap ....... Improvement Roadmap
   ├── [research] WebSearch/WebFetch + SECOND-KNOWLEDGE-BRAIN
   ├── [challenge] devil's-advocate assumption review
   └── synthesize ................... professional deliverable + quality gates
```

## Full Sub-Skill Catalog
### sub-intake — Intake & Context Gathering
- **Purpose:** Collect the structured inputs, scope, and goals needed to run the analysis; ask clarifying questions when key facts are missing.
- **Inputs:** case context from prior stage.
- **Outputs:** structured result passed to the next stage.
- **Tools:** Read, WebSearch/WebFetch (as needed).
- **Quality gate:** output is complete, evidence-cited, and consistent with frameworks before proceeding.
### sub-framework-selector — Evaluation Framework Selector
- **Purpose:** Pick the most appropriate named world-renowned framework(s) for the case and justify the choice.
- **Inputs:** case context from prior stage.
- **Outputs:** structured result passed to the next stage.
- **Tools:** Read, WebSearch/WebFetch (as needed).
- **Quality gate:** output is complete, evidence-cited, and consistent with frameworks before proceeding.
### sub-scoring-engine — Scoring Engine
- **Purpose:** Apply the multi-dimensional rubric to produce weighted scores with evidence citations for each dimension.
- **Inputs:** case context from prior stage.
- **Outputs:** structured result passed to the next stage.
- **Tools:** Read, WebSearch/WebFetch (as needed).
- **Quality gate:** output is complete, evidence-cited, and consistent with frameworks before proceeding.
### sub-improvement-roadmap — Improvement Roadmap
- **Purpose:** Generate a prioritized, effort/impact-ranked set of recommendations traceable to the scored findings.
- **Inputs:** case context from prior stage.
- **Outputs:** structured result passed to the next stage.
- **Tools:** Read, WebSearch/WebFetch (as needed).
- **Quality gate:** output is complete, evidence-cited, and consistent with frameworks before proceeding.

## Evaluation Frameworks (World-Renowned, Citable)
| Framework / Standard | Role in this skill |
|---|---|
| Getting Things Done (Allen) | Capture-clarify-organize-reflect-engage. |
| Pomodoro technique | Time-boxed focus/break cycles. |
| Eisenhower matrix | Urgent/important prioritization. |
| Deep Work (Newport) | Distraction-free cognitive blocks. |
| Pareto / OKR | High-leverage focus and goal alignment. |

## Scoring Model
| Dimension | Weight | What is assessed |
|---|---|---|
| Prioritization quality | 25% | Eisenhower/Pareto-sound task ranking |
| Time-structure fit | 20% | Pomodoro/time-blocking matched to person |
| Focus & distraction control | 20% | deep-work conditions, interruption defense |
| Workload sustainability | 20% | realistic, burnout-aware |
| System simplicity & adherence | 15% | low-friction, durable |
Each dimension is scored 0-100 with cited evidence; the weighted total yields an overall grade (A: 90+, B: 75-89, C: 60-74, D: <60).

## Skill File Format Specification
- Frontmatter: `name`, `description`.
- Required sections: Role & Persona, Workflow (Harness Flow), Sub-skills Available, Tools, Output Format, Quality Gates.

## E2E Execution Flow
1. Parse user request; if inputs are insufficient, `sub-intake` asks targeted questions.

3. `sub-framework-selector` picks framework(s) and justifies the choice.
4. Research stage gathers highest-tier evidence (see evidence hierarchy); degrade gracefully to SECOND-KNOWLEDGE-BRAIN if offline.
5. `sub-scoring-engine` scores each dimension with citations.
6. Challenge stage stress-tests conclusions.

8. `sub-improvement-roadmap` produces ranked actions.
9. Synthesize deliverable; run Quality Gates; present.

**Error handling:** missing inputs -> ask; conflicting evidence -> present both and grade certainty; tool failure -> fallback + explicit limitation notice.

## SECOND-KNOWLEDGE-BRAIN Integration
- Sources: https://hbr.org, https://jamesclear.com, https://todoist.com/productivity-methods, https://www.calnewport.com
- ArXiv categories: (none)
- Crawl queries: productivity methods research; deep work focus evidence; time management GTD pomodoro; procrastination behavioral science
- Append format: dated entries with Title, Authors, Year, Venue, DOI/URL, key finding, relevance.

## Supporting Tools Spec
`tools/knowledge_updater.py`: inputs = source list + queries; outputs = appended SECOND-KNOWLEDGE-BRAIN entries; schedule = weekly cron; dedup by URL/DOI hash.

## Quality Gates (must all pass before final output)
- Every score cites at least one source or the chosen framework.
- Challenge stage completed; key assumptions tested.
- Roadmap items are prioritized by effort and impact and traceable to findings.
- Limitations and evidence certainty are stated explicitly.

## Test Scenarios
1. **Overwhelm** — User: "I have too much to do" -> Skill prioritizes (Eisenhower), designs day plan, scores.
2. **Focus** — User: "I can't concentrate" -> Skill prescribes deep-work + Pomodoro, scores fit.
3. **System** — User: "Set up GTD for me" -> Skill builds GTD workflow, scores simplicity.
4. **Goals** — User: "Align my week to my OKRs" -> Skill maps tasks to goals (Pareto), scores.
5. **Degraded mode** — User: "Coach offline" -> Falls back to brain methods, flags trend tips stale.

## Key Design Decisions
1. Framework-grounded scoring (no ad-hoc criteria).
2. Research-first with graceful degradation to the local knowledge brain.
3. Mandatory challenge stage to counter confirmation bias.
4. standard quality gates enforced before delivery.
5. Self-improving knowledge base via weekly crawl.
