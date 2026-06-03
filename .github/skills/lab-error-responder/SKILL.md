---
name: lab-error-responder
description: Detect compilation, runtime, code, and interpreter errors during labs, verify whether each error is intended by the lab guide, resolve unintended blockers, and document resolution details for learner continuity.
---

# Lab Error Responder

Use this skill in any lab workflow when an error appears, including compile failures, runtime exceptions, failing tests, static analysis findings, environment/interpreter mismatches, or dependency/import errors.

## Inputs this skill expects

- Active module path (for example: guided-multi-step-coding-task/lab).
- Lab section context from AIC-1102-LabGuide.html.
- Current error evidence (stack trace, test output, diagnostics, linter/analysis output).

## Required policy

1. Check guide intent first.
   - Look up the active lesson and step in AIC-1102-LabGuide.html.
   - Determine whether the observed error is explicitly intended for observation in this step.
2. If the error is intended, do not "fix" it immediately.
   - Mark it as an observed learning point.
   - Continue with the guide flow unless user asks to remediate anyway.
3. If the error is not intended (or blocks progression), resolve it.
   - Troubleshoot and apply the smallest safe fix that unblocks the lab.
   - Continue until the lab can proceed.
4. If intent is unclear from the guide, stop and ask the user.
   - Do not assume.

## Logging requirements for unintended errors

When an error is unintended or unresolved at first pass, write or update:

- <active-module>/solutions/labErrorResolutionDetails.md

The log entry must include:

1. Date/time and lesson/module name.
2. Error type and exact observed symptom.
3. Why the error is considered unintended (guide cross-check result).
4. Root cause analysis.
5. Resolution steps taken (ordered, reproducible).
6. Final verification that progression is unblocked.
7. Recurrence signal (one-off, occasional, frequent).
8. Sub-agent recommendation:
   - Create dedicated sub-agent: yes/no.
   - If yes, include scope and trigger conditions.

## Resolution workflow

1. Reproduce and capture the error.
2. Validate against guide intent.
3. Apply minimal corrective change.
4. Re-verify with the relevant command/check.
5. Confirm the current lab step can continue.
6. Record details in labErrorResolutionDetails.md.
7. Decide whether frequency warrants a dedicated sub-agent.

## Guardrails

- Prefer minimal, targeted fixes over broad refactors.
- Preserve lab learning objectives and starter intent.
- If multiple possible fixes exist, choose the least disruptive option first.
- Ask the user before taking actions when guide intent is ambiguous.
