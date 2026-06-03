# Investigation Notes

## #codebase data-flow map

* Stages Copilot identified in order
<span style="color:red"></span>

* Files Copilot cited for each stage
<span style="color:red"></span>

* Verification notes after checking src/pipeline, src/services, src/models
* Did Copilot name every participating file?
<span style="color:red"></span>
* Did Copilot correctly classify src/services/reporting.py as a consumer?
<span style="color:red"></span>
* Did Copilot mention infra/runtime_defaults.py? If yes/no, why?
<span style="color:red"></span>

## Agent discovery pattern

* File read order observed in Agent Logs
<span style="color:red"></span>

* Read pattern: concentrated by directory or scattered across directories
<span style="color:red"></span>

* Evidence of grep, semantic search, or symbol lookups
<span style="color:red"></span>

* Files Agent edited without being explicitly named
<span style="color:red"></span>

* Test execution behavior observed (whether, when, response to result)
<span style="color:red"></span>

## Audit findings

* Residual references Copilot missed
<span style="color:red"></span>

* False positives Copilot reported
<span style="color:red"></span>

* Miss categories (string literals, dict keys, test data, docstrings, comments)
<span style="color:red"></span>

* Cold test result after refactor claim (pytest -v)
<span style="color:red"></span>

## Self-correction

* Original miss selected
<span style="color:red"></span>

* Prompt form used to provide missing context
<span style="color:red"></span>

* Whether correction surfaced additional misses
<span style="color:red"></span>

* Verification result after correction and retest
<span style="color:red"></span>

## Summary

* How completely did #codebase map the codebase on first ask?
<span style="color:red"></span>

* How completely did Agent Mode execute the refactor on first try?
<span style="color:red"></span>

* Which category of references was most likely to be missed, and why?
<span style="color:red"></span>

## Hidden config search (Optional)

* Files read before locating infra/runtime_defaults.py
<span style="color:red"></span>

* Signal used to locate value (semantic, import-follow, grep)
<span style="color:red"></span>

* Incorrect assumptions observed during search
<span style="color:red"></span>

* What would make this value harder to find?
<span style="color:red"></span>

## Space-grounded comparison (Optional)

* File-change delta between ungrounded and grounded runs
<span style="color:red"></span>

* Naming differences between runs
<span style="color:red"></span>

* Whether explanation referenced spec language (for example billing/canonical identifier)
<span style="color:red"></span>

* First-pass test outcome in grounded run
<span style="color:red"></span>

* Dependency map cross-check notes (including infra/runtime_defaults.py edges)
<span style="color:red"></span>
