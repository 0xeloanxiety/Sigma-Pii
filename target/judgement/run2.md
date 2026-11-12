# Judgment Results

| ID | Verdict | Justification |
|---|---|---|
| H-01 | MISS |  |
| H-02 | MISS |  |
| H-03 | EXACT | Matched Finding [1], as both identify that transferVesting resets releaseRate = totalAmount / numOfSteps without accounting for already-claimed amounts and steps, allowing grantors to overclaim, and both prescribe recalculating the rate using remaining amounts and remaining steps. |
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
| M-17 | PARTIAL | Matched Finding [2], which correctly identifies that integer truncation in stepDuration = (_endTime - _startTime) / _numOfSteps yields zero when duration is less than steps and causes a division-by-zero DoS in claimable(), but suggests a narrower fix (requiring duration to be at least the number of steps) rather than ensuring exact divisibility. |
| M-18 | MISS |  |
| M-19 | MISS |  |
| M-20 | MISS |  |

**Summary:** 1 EXACT, 1 PARTIAL, 21 MISS (23 total)
