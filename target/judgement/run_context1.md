# Judgment Results

| ID | Verdict | Justification |
|---|---|---|
| H-01 | MISS |  |
| H-02 | MISS |  |
| H-03 | PARTIAL | Matched Finding [1], which identifies the same defect where transferVesting recalculates releaseRate without accounting for already claimed amounts/steps, but omits the ground-truth fix formula or suggests capping in claimable(). |
| M-01 | MISS |  |
| M-02 | MISS |  |
| M-03 | MISS |  |
| M-04 | MISS |  |
| M-05 | MISS |  |
| M-06 | MISS |  |
| M-07 | MISS |  |
| M-08 | MISS |  |
| M-09 | MISS |  |
| M-10 | MISS |  |
| M-11 | MISS |  |
| M-12 | MISS |  |
| M-13 | MISS |  |
| M-14 | MISS |  |
| M-15 | MISS |  |
| M-16 | MISS |  |
| M-17 | PARTIAL | Matched Finding [2], which captures the division-by-zero defect when stepDuration rounds down to zero, but has a narrower scope and fix than the ground truth's exact divisibility requirement. |
| M-18 | MISS |  |
| M-19 | MISS |  |
| M-20 | MISS |  |

**Summary:** 0 EXACT, 2 PARTIAL, 21 MISS (23 total)
