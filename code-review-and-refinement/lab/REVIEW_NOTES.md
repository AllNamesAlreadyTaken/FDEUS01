# Review Notes

## 2.2 Getting Started Baseline

* Starter test result (expected: 3 passed)
<span style="color:red">it failed</span>

* Notes about starter baseline risk (tests passing is not proof of correctness)
<span style="color:red"></span>

## /fix baseline (orders.py)

* Issues surfaced by /fix for process_order
<span style="color:red">Added input validation for item_name/quantity/coupon_percent, handled missing stock (`None`) safely, removed duplicate tax multiplication, corrected coupon percentage math, and verified inventory update success before returning a total.</span>

* Which issues likely require cross-file context to detect?
<span style="color:red">The duplicate-tax issue requires understanding that `calculate_price` in `pricing.py` already applies tax, and the coupon helper in `utils.py` appears suspicious because it divides by 10000 rather than 100.</span>

## #codebase review

* Findings grouped by file
<span style="color:red">fixed only 1 function's segment of code.</span>

* Cross-file issues section
<span style="color:red">This review will take more than 5 steps across multiple files, so before I start: This task looks like it will take more than 5 steps. Which supervision mode do you want: checkpoint or tight?</span>

* Comparison with /fix baseline
* Which issues appeared in #codebase but not /fix?
<span style="color:red">I gave the global space skills to check in, this was different in codebase because I asked it not to go more than 5 steps in without checking in.  The issues were ranked by impact and priority to fix in a full codebase scan.  Also cross-file issues were called out specifically.</span>
* Which issues appeared in /fix but not #codebase?
<span style="color:red">singular perspective issues without understanding the bigger picture as a whole</span>

## /doc corrections

* Undocumented functions selected
<span style="color:red">The AI did not explain what or where it added, it just did.</span>

* Generated docstring corrections applied
<span style="color:red"></span>

* Why correction was needed (name/behavior mismatch, return mismatch, etc.)
<span style="color:red">It seems to trip when asked to find where there is a mismatch "this is where the documentation doensn't match what the funciton does" then it proceeds to tell me it matches perfectly.</span>

## /explain interrogations

* Original suggestion selected for interrogation
<span style="color:red"></span>

* Copilot explanation summary
<span style="color:red"></span>

* Was the explanation convincing?
<span style="color:red"></span>

* Decision: accept | modify | reject
<span style="color:red"></span>

## Decisions

### Issue: <short description>
- File/line:
<span style="color:red"></span>
- Suggestion:
<span style="color:red"></span>
- Decision: accept | modify | reject
<span style="color:red"></span>
- Reasoning:
<span style="color:red"></span>

### Issue: <short description>
- File/line:
<span style="color:red"></span>
- Suggestion:
<span style="color:red"></span>
- Decision: accept | modify | reject
<span style="color:red"></span>
- Reasoning:
<span style="color:red"></span>

### Issue: <short description>
- File/line:
<span style="color:red"></span>
- Suggestion:
<span style="color:red"></span>
- Decision: accept | modify | reject
<span style="color:red"></span>
- Reasoning:
<span style="color:red"></span>

## Refinement

* Right idea from original suggestion
<span style="color:red"></span>

* Wrong detail in original suggestion
<span style="color:red"></span>

* Refinement prompt used
<span style="color:red"></span>

* Why the refined output is better
<span style="color:red"></span>

* Final verification result (pytest -v)
<span style="color:red"></span>

## PR review vs Chat review (Optional)

* One issue PR review caught that Chat #codebase missed
<span style="color:red"></span>

* One issue Chat #codebase caught that PR review missed
<span style="color:red"></span>

* Hypothesis for differences (scope, diff-only vs repo-wide, prompt framing)
<span style="color:red"></span>

## Instructions-file impact (Optional)

* How focus changed after adding instruction file
<span style="color:red"></span>

* Did depth improve for targeted concern?
<span style="color:red"></span>

* Were other categories suppressed, de-emphasized, or unaffected?
<span style="color:red"></span>

* Reliability conclusion for instruction-scoped reviews
<span style="color:red"></span>
