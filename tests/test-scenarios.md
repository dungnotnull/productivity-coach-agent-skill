# Test Scenarios — Productivity Coach (Pomodoro/GTD) (Skill #164)

These scenarios validate the harness end-to-end: stage order, framework grounding, scoring with citations, gates, roadmap, and graceful degradation. Each scenario includes detailed expected outputs and validation criteria.

## Scenario 1: Overwhelm

### User Input
"I have too much to do, I'm drowning in tasks and can't keep up with everything hitting me at once."

### Expected Behavior
Skill prioritizes using Eisenhower Matrix, designs day plan, scores current state, and produces improvement roadmap.

### Stage-by-Stage Expected Outputs

**Stage 1 - Intake**:
- Questions asked: role, task volume, deadline pressure, interruption frequency
- Collected data: Knowledge work role, 50+ tasks, constant deadlines, frequent interruptions
- Output schema complete with all required fields

**Stage 2 - Framework Selection**:
- Selected frameworks: Eisenhower Matrix (score: 11/12), GTD (score: 9/12)
- Rationale: Eisenhower for immediate prioritization, GTD for workflow management
- Excluded: Deep Work (requires schedule control not yet available), Pomodoro (secondary to prioritization)

**Stage 3 - Research**:
- Evidence gathered: Eisenhower effectiveness studies, GTD workflow research, overwhelm management
- Minimum sources: 3 authoritative sources with relevant findings

**Stage 4 - Scoring**:
```
Expected score profile:
- Prioritization Quality: 45-55/100 (primary gap)
- Time-Structure Fit: 60-70/100 (moderate)
- Focus & Distraction Control: 55-65/100 (challenged)
- Workload Sustainability: 50-60/100 (at risk)
- System Simplicity & Adherence: 60-70/100 (moderate)
Overall: C grade (58-62 range)
```

**Stage 5 - Challenge**:
- Tested assumption: Is overwhelm caused by poor prioritization or excessive volume?
- Alternative considered: Could delegation reduce volume before prioritization?
- Certainty: Medium (need observation of actual task list for high certainty)

**Stage 6 - Roadmap**:
```
Expected quick wins:
- Daily Eisenhower triage (Impact: 3, Effort: 1)
- Immediate deferral protocol (Impact: 2, Effort: 1)

Phase 1 recommendations:
- GTD capture system setup (Impact: 3, Effort: 2)
- Weekly review ritual (Impact: 3, Effort: 2)
- Priority criteria establishment (Impact: 2, Effort: 2)
```

**Stage 7 - Synthesis**:
- Complete report with all 7 sections
- Grade C with prioritization focus
- 6-8 total recommendations
- Implementation timeline: 6-8 weeks

### Pass Criteria
- [ ] Correct stage order maintained
- [ ] Framework named and justified
- [ ] All scores have citations
- [ ] Roadmap is prioritized by impact/effort
- [ ] Limitations stated
- [ ] Quality gates all pass

### Regression Test
Run this scenario after any changes to:
- Framework selection logic
- Scoring rubric for prioritization dimension
- Roadmap prioritization formula
- Quality gate checks

---

## Scenario 2: Focus Issues

### User Input
"I can't concentrate. I'm constantly distracted, switch tasks constantly, and never seem to get into deep focus on my work."

### Expected Behavior
Skill prescribes deep-work + Pomodoro techniques, scores fit, and provides environment and protocol recommendations.

### Stage-by-Stage Expected Outputs

**Stage 1 - Intake**:
- Identified scenario: Focus
- Key data collected: Interruption frequency, work environment, task types, schedule control level

**Stage 2 - Framework Selection**:
- Selected frameworks: Deep Work (score: 11/12), Pomodoro (score: 10/12)
- Rationale: Deep Work for environment and ritual design, Pomodoro for focus sustainability

**Stage 3 - Research**:
- Evidence gathered: Attention residue research, digital distraction studies, focus training research
- Sources: Rochester (2009), HBR (2021), Newport (2016)

**Stage 4 - Scoring**:
```
Expected score profile:
- Prioritization Quality: 65-75/100 (likely adequate)
- Time-Structure Fit: 55-65/100 (challenged by switching)
- Focus & Distraction Control: 40-50/100 (critical gap)
- Workload Sustainability: 60-70/100 (moderate)
- System Simplicity & Adherence: 55-65/100 (fragmented)
Overall: C- grade (55-60 range)
```

**Stage 5 - Challenge**:
- Tested: Is issue lack of skill or environment design?
- Alternative: Could underlying anxiety be causing distraction rather than protocols?

**Stage 6 - Roadmap**:
```
Expected quick wins:
- Notification audit and blocking (Impact: 3, Effort: 1)
- Single-tasking commitment (Impact: 2, Effort: 1)

Phase 1 recommendations:
- Deep work block scheduling (Impact: 3, Effort: 2)
- Focus ritual design (Impact: 3, Effort: 2)
- Environment optimization (Impact: 2, Effort: 2)
```

### Pass Criteria
- [ ] Focus-specific frameworks selected
- [ ] Focus & Distraction Control is lowest-scoring dimension
- [ ] Environment and ritual recommendations present
- [ ] Citations from attention research included
- [ ] Roadmap includes immediate, implementable changes

---

## Scenario 3: System Design

### User Input
"Set up GTD for me. I want a complete productivity system that I can actually stick to."

### Expected Behavior
Skill builds GTD workflow, scores simplicity/adherence potential, and provides implementation roadmap with maintenance protocols.

### Stage-by-Stage Expected Outputs

**Stage 1 - Intake**:
- Identified scenario: System design
- Key data: Current tools, time available for maintenance, change tolerance, technology preferences

**Stage 2 - Framework Selection**:
- Selected framework: GTD (score: 12/12 - perfect fit)
- Possibly supplementing with: Eisenhower (for engagement prioritization)

**Stage 3 - Research**:
- Evidence gathered: GTD effectiveness studies, system design principles, habit formation research
- Sources: Allen (2015), Clear (2018), HBR case studies on system adoption

**Stage 4 - Scoring**:
```
Expected score profile (baseline before implementation):
- Prioritization Quality: 50-60/100 (no current system)
- Time-Structure Fit: 55-65/100 (ad-hoc)
- Focus & Distraction Control: 55-65/100 (variable)
- Workload Sustainability: 55-65/100 (no capacity planning)
- System Simplicity & Adherence: 30-40/100 (no existing system)
Overall: D+ grade (50-55 range) - baseline for new system
```

**Stage 5 - Challenge**:
- Tested: Is user ready for GTD complexity or need simpler start?
- Alternative: Could start with capture-only before full system?

**Stage 6 - Roadmap**:
```
Expected Phase 1 (Weeks 1-2):
- Capture system setup (Impact: 3, Effort: 2)
- Clarify and organize practices (Impact: 3, Effort: 2)
- Weekly review ritual establishment (Impact: 3, Effort: 2)

Expected Phase 2 (Weeks 3-4):
- Context-based organization (Impact: 2, Effort: 2)
- Next actions definition (Impact: 2, Effort: 2)
- Project planning templates (Impact: 2, Effort: 2)

Success metrics:
- Weekly review completed: 4 weeks consecutively
- Inbox zero maintained: 80% of days
- Trusted system status: User reports relying on system
```

### Pass Criteria
- [ ] GTD selected as primary framework
- [ ] Implementation is phased (not all at once)
- [ ] Weekly review emphasized as critical component
- [ ] Simplicity/adherence scored accurately as baseline
- [ ] Success metrics include maintenance behaviors
- [ ] System adoption challenges addressed

---

## Scenario 4: Goal Alignment

### User Input
"Align my week to my OKRs. I have too many objectives and I'm not spending time on the ones that actually matter."

### Expected Behavior
Skill maps tasks to goals using Pareto analysis, scores alignment, and provides focus framework.

### Stage-by-Stage Expected Outputs

**Stage 1 - Intake**:
- Identified scenario: Goal alignment
- Key data: OKR/objective list, current task distribution, time spent analysis

**Stage 2 - Framework Selection**:
- Selected frameworks: Pareto/OKR (score: 11/12), Eisenhower (score: 8/12 - complementary)
- Rationale: Pareto for 80/20 focus, Eisenhower for daily prioritization

**Stage 3 - Research**:
- Evidence gathered: OKR effectiveness studies, Pareto distribution in business outcomes, strategic alignment research
- Sources: Koch (1997), HBR (2019), OKR case studies

**Stage 4 - Scoring**:
```
Expected score profile:
- Prioritization Quality: 55-65/100 (strategic alignment weak)
- Time-Structure Fit: 60-70/100 (some structure exists)
- Focus & Distraction Control: 60-70/100 (adequate)
- Workload Sustainability: 55-65/100 (spread too thin)
- System Simplicity & Adherence: 60-70/100 (system exists but misaligned)
Overall: C grade (58-65 range)
```

**Stage 5 - Challenge**:
- Tested: Are OKRs realistic or too numerous?
- Alternative: Could reduce objectives before alignment process?

**Stage 6 - Roadmap**:
```
Expected quick wins:
- OKR audit and reduction (Impact: 3, Effort: 2)
- Weekly OKR review (Impact: 3, Effort: 1)

Expected Phase 1 recommendations:
- Pareto analysis of current tasks (Impact: 3, Effort: 2)
- OKR-to-task mapping (Impact: 3, Effort: 2)
- Weekly goal alignment ritual (Impact: 2, Effort: 1)

Success metrics:
- Time on top-3 objectives: 60%+ of week
- Low-value tasks reduced: 40%+
- OKR progress tracking: Weekly review established
```

### Pass Criteria
- [ ] Pareto/OKR frameworks selected
- [ ] Prioritization quality scored as gap
- [ ] Alignment-specific recommendations included
- [ ] Success metrics measure goal connection
- [ ] Pareto principle applied to task analysis

---

## Scenario 5: Degraded Mode

### User Input
"Coach offline. I need help but my internet is down and I can't access research sources."

### Expected Behavior
Falls back to SECOND-KNOWLEDGE-BRAIN methods, provides recommendations, explicitly flags limitation.

### Stage-by-Stage Expected Outputs

**Stage 1 - Intake**:
- Proceeds normally using cached knowledge
- All intake questions asked as usual

**Stage 2 - Framework Selection**:
- Frameworks selected based on SECOND-KNOWLEDGE-BRAIN framework descriptions
- Selection logic proceeds normally

**Stage 3 - Research**:
```
Expected degraded behavior:
- Falls back to SECOND-KNOWLEDGE-BRAIN.md
- Uses cached sources and findings
- Does NOT attempt WebSearch/WebFetch
- Explicitly states: "Using cached knowledge base; live research unavailable"
- Notes limitation in final report
```

**Stage 4 - Scoring**:
- Scores based on framework principles in cached knowledge
- Uses evidence citations from SECOND-KNOWLEDGE-BRAIN
- Proceeds with full scoring process

**Stage 5 - Challenge**:
- Proceeds normally using cached framework knowledge
- Assumptions tested based on cached research

**Stage 6 - Roadmap**:
- Recommendations generated from cached principles
- All roadmap elements produced normally

**Stage 7 - Synthesis**:
```
Expected limitation statement:
"⚠️ DEGRADED MODE: This assessment used cached knowledge base dated [date].
Live research was unavailable. For the most current evidence and updated
recommendations, please re-run this assessment when full tool access is available.

Time-sensitive recommendations may be particularly affected. Framework
foundations remain valid, but specific evidence citations may not reflect
the latest research."
```

### Pass Criteria
- [ ] No errors or failures in degraded mode
- [ ] Limitation explicitly stated in report
- [ ] All stages complete successfully
- [ ] Recommendations remain actionable
- [ ] Framework application remains valid
- [ ] User informed what would improve with full access

---

## Additional Regression Scenarios

### Scenario 6: Mixed Profile (Complex Case)
**User**: Software developer with 25 tickets, wants focus time but also has 10 meetings weekly

Expected behavior:
- Multi-framework selection (Pomodoro + Deep Work + Eisenhower)
- Balanced scoring across multiple dimensions
- Recommendations address conflicting demands (meetings vs. focus)

### Scenario 7: Minimal Time Availability
**User**: "I have zero time for system maintenance. Make it as simple as possible."

Expected behavior:
- Framework selection accounts for minimal time budget
- Recommendations exclude high-maintenance systems (full GTD)
- Focus on automated or low-friction approaches
- Simplicity/adherence dimension heavily weighted

### Scenario 8: Team Coordination Required
**User**: Product manager needing team to adopt new prioritization approach

Expected behavior:
- Roadmap includes stakeholder management steps
- Recommendations address communication protocols
- Success metrics include team adoption measures
- Phased approach starting with individual before team rollout

---

## Test Execution Protocol

### Running Scenarios
For each scenario:
1. Provide user input exactly as specified
2. Document all stage outputs
3. Verify against expected outputs
4. Check all pass criteria
5. Note any deviations for regression

### Regression Tracking
When bugs or deviations found:
1. Document in "Regression Notes" section
2. Track fix implementation
3. Re-test scenario after fixes
4. Mark scenario as passing after successful re-test

### Performance Benchmarks
Each scenario should complete within:
- Intake: 5-10 questions or immediate if sufficient data
- Framework selection: Immediate (1-2 reasoning steps)
- Research: 2-5 source queries (or degraded mode fallback)
- Scoring: All 5 dimensions scored with citations
- Challenge: At least 2 assumptions tested
- Roadmap: 6-10 recommendations with phases
- Synthesis: Complete 7-section report

---

## Regression Notes

### Known Issues
(Initially empty; populated as issues discovered)

### Fixes Applied
(Initially empty; populated as fixes implemented)

### Scenario Status
- Scenario 1 (Overwhelm): Ready for testing
- Scenario 2 (Focus): Ready for testing
- Scenario 3 (System): Ready for testing
- Scenario 4 (Goals): Ready for testing
- Scenario 5 (Degraded): Ready for testing
- Scenario 6 (Mixed): Ready for testing
- Scenario 7 (Minimal time): Ready for testing
- Scenario 8 (Team): Ready for testing

### Test History
(Record test runs here with dates and results)
