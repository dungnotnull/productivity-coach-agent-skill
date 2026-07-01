# Productivity Coach Agent Skill

> Coaches personal time management and work-process optimization using Pomodoro, GTD, and evidence-based focus methods

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Skill Cluster](https://img.shields.io/badge/Cluster-lifestyle--personal-green.svg)](https://github.com/dungnotnull/productivity-coach-agent-skill)
[![Phase](https://img.shields.io/badge/Phase-Production%20Ready-brightgreen.svg)](https://github.com/dungnotnull/productivity-coach-agent-skill)
[![Status](https://img.shields.io/badge/Status-Complete%20%26%20Open%20Source%20Ready-success.svg)](https://github.com/dungnotnull/productivity-coach-agent-skill)

## Overview

Productivity Coach is a comprehensive AI-powered coaching harness that diagnoses workflow problems and designs personalized systems from proven methodologies including Getting Things Done (GTD), Pomodoro Technique, Eisenhower Matrix, Deep Work principles, and the Pareto Principle.

This skill works research-first, grounding every judgment in named world-renowned frameworks, and provides quantitative, evidence-based assessments with actionable improvement roadmaps.

## Problem It Solves

People stay busy but unproductive because:
- Tasks are unprioritized
- Focus is fragmented
- Workload is unsustainable
- Systems are overcomplicated

This skill diagnoses your workflow and prescribes a personalized, sustainable productivity system.

## Features

### Research-Backed Frameworks

- **Getting Things Done (GTD)** - Capture-clarify-organize-reflect-engage workflow
- **Pomodoro Technique** - Time-boxed focus/break cycles for sustainable pacing
- **Eisenhower Matrix** - Urgent vs. important prioritization
- **Deep Work** - Distraction-free cognitive blocks for knowledge work
- **Pareto Principle** - High-leverage focus on impactful tasks

### Multi-Dimensional Scoring

The skill evaluates your productivity across five dimensions:

| Dimension | Weight | What It Assesses |
|-----------|--------|------------------|
| Prioritization Quality | 25% | Eisenhower/Pareto-sound task ranking |
| Time-Structure Fit | 20% | Pomodoro/time-blocking matched to your patterns |
| Focus & Distraction Control | 20% | Deep-work conditions, interruption defense |
| Workload Sustainability | 20% | Realistic capacity, burnout-aware planning |
| System Simplicity & Adherence | 15% | Low-friction, durable habits |

### Professional Deliverables

Each coaching session produces a comprehensive report including:

1. **Executive Summary** - Overall grade (A-D) and headline findings
2. **Context & Scope** - What was assessed and chosen frameworks
3. **Dimension Scores** - Detailed scoring with evidence citations
4. **Findings & Risks** - Analysis of strengths and weaknesses
5. **Improvement Roadmap** - Prioritized actions (effort × impact)
6. **Limitations & Certainty** - Evidence quality assessment
7. **Sources** - Complete citation list

## How It Works

### The Coaching Harness

```
/productivity-coach (main.md)
   ├── 1. Intake ............. Gather your context, challenges, and goals
   ├── 2. Framework Selector . Choose the best methodologies for you
   ├── 3. Research ........... Gather latest evidence from authoritative sources
   ├── 4. Scoring Engine ..... Evaluate across 5 evidence-based dimensions
   ├── 5. Challenge ........... Test assumptions and grade certainty
   ├── 6. Roadmap ............ Generate prioritized improvement recommendations
   └── 7. Synthesis .......... Assemble professional report with quality gates
```

### Example Use Cases

**Overwhelm**: "I have too much to do"
- Skill prioritizes using Eisenhower Matrix
- Designs day plan and workflow
- Scores current state
- Provides step-by-step improvement roadmap

**Focus Issues**: "I can't concentrate"
- Skill prescribes deep-work principles + Pomodoro technique
- Analyzes interruption patterns
- Scores focus and distraction control
- Creates environment and protocol recommendations

**System Design**: "Set up GTD for me"
- Skill builds complete GTD workflow
- Designs capture, clarify, organize system
- Scores simplicity and adherence factors
- Provides phased implementation plan

**Goal Alignment**: "Align my week to my OKRs"
- Skill maps tasks to goals using Pareto analysis
- Identifies high-leverage activities
- Scores strategic alignment
- Creates focus framework

## Installation

### For Claude Code Users

Clone this repository to your local skills directory:

```bash
git clone https://github.com/dungnotnull/productivity-coach-agent-skill.git
```

The skill will be available through the Skill tool in Claude Code.

### Knowledge Base Updates

Run the knowledge updater periodically to keep the research current:

```bash
cd tools
python knowledge_updater.py
```

Recommended: Set up a weekly cron job for automatic updates.

## Architecture

### Sub-Skills

The harness consists of four specialized sub-skills:

1. **sub-intake** - Structured context gathering with targeted questioning
2. **sub-framework-selector** - Framework selection with decision matrix
3. **sub-scoring-engine** - Evidence-based multi-dimensional scoring
4. **sub-improvement-roadmap** - Prioritized, effort/impact-ranked recommendations

### Knowledge Pipeline

- **Sources**: Harvard Business Review, James Clear, Todoist, Cal Newport
- **Evidence Hierarchy**: Systematic reviews > RCTs > Framework authors > HBR > Practitioner sources
- **Update Mechanism**: Weekly crawl via Python tool with deduplication

### Testing

Comprehensive test suite with 8 scenarios covering:
- Happy path workflows
- Edge cases (mixed profiles, minimal time, team coordination)
- Degraded mode operation
- Regression testing framework

## Documentation

- **PROJECT-detail.md** - Complete technical specification
- **PROJECT-DEVELOPMENT-PHASE-TRACKING.md** - Phase completion tracking
- **CLAUDE.md** - Project instructions and cluster documentation
- **SECOND-KNOWLEDGE-BRAIN.md** - Self-improving knowledge base
- **skills/*.md** - Individual skill implementations
- **tests/test-scenarios.md** - Test scenarios and validation criteria

## Research & Evidence

This skill is grounded in peer-reviewed research and established frameworks:

- **David Allen** - Getting Things Done (2001, 2015)
- **Francesco Cirillo** - The Pomodoro Technique (2006)
- **Stephen Covey** - The 7 Habits of Highly Effective People (1989)
- **Cal Newport** - Deep Work (2016)
- **Richard Koch** - The 80/20 Principle (1997)
- **James Clear** - Atomic Habits (2018)

All recommendations cite sources from:
- Harvard Business Review
- Journal of Applied Psychology
- Annual Review of Psychology
- Academy of Management Journal
- Primary framework authors

## Quality Assurance

Every recommendation passes through multiple quality gates:

- All scores cite a source or framework
- Challenge stage tests key assumptions
- Roadmap items are traceable to findings
- Limitations and certainty are explicit
- Evidence hierarchy is respected

## Development Status

All phases complete:

- Phase 0 - Research & Architecture: Complete
- Phase 1 - Core Sub-Skills: Complete
- Phase 2 - Main Harness: Complete
- Phase 3 - Knowledge Pipeline: Complete
- Phase 4 - Testing: Complete
- Phase 5 - Integration: Complete

Status: Production-ready, open-source complete

## Contributing

Contributions are welcome! Areas for enhancement:

- Additional regression cases from real user runs
- Expanded research coverage
- Framework refinements based on emerging evidence
- Integration with sibling skills in lifestyle-personal cluster

## License

MIT License - See LICENSE file for details

## Acknowledgments

Built with frameworks and research from:
- David Allen (GTD)
- Francesco Cirillo (Pomodoro Technique)
- Stephen Covey (Eisenhower Matrix)
- Cal Newport (Deep Work)
- Richard Koch (Pareto Principle)
- James Clear (Habit formation)

Knowledge sources:
- Harvard Business Review
- Journal of Applied Psychology
- Annual Review of Psychology
- Todoist Productivity Methods
- FranklinCovey

---

**Skill ID**: 164 | **Cluster**: lifestyle-personal | **Status**: Production-Ready

For updates and issues, visit: https://github.com/dungnotnull/productivity-coach-agent-skill
