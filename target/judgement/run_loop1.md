# Judgment Results

| ID | Verdict | Justification |
|---|---|---|
| H-01 | PARTIAL | Matched Finding [8], which correctly identifies that listing order causes vestings pooled under the manager to inherit the first seller's stepsClaimed (delaying claims for earlier-stage allocations), but does not provide an explicit fix. |
| H-02 | PARTIAL | Matched Finding [8], which identifies that manager-held listings retain a static stepsClaimed allowing new buyers to unlock tokens prematurely, but lacks an explicit fix. |
| H-03 | EXACT | Matched Finding [2], identifying the exact same defect where transferVesting recalculates releaseRate without deducting claimed amounts and steps, and proposing the exact same fix. |
| M-01 | MISS |  |
| M-02 | MISS |  |
| M-03 | MISS |  |
| M-04 | MISS |  |
| M-05 | MISS |  |
| M-06 | PARTIAL | Matched Finding [6], which identifies that stepDuration truncation causes currentStep to exceed numOfSteps and leaves stepsClaimed > numOfSteps, but targets capping currentStep rather than handling the subtraction underflow in claimable. |
| M-07 | MISS |  |
| M-08 | MISS |  |
| M-09 | MISS |  |
| M-10 | MISS |  |
| M-11 | MISS |  |
| M-12 | MISS |  |
| M-13 | MISS |  |
| M-14 | PARTIAL | Matched Finding [5], which explicitly notes the flawed subtraction math in referralFeeCost (buyerFeeTotal - ... instead of a percentage calculation), but primarily focused on referral rewards never being disbursed on-chain and omitted the standalone fix formula. |
| M-15 | MISS |  |
| M-16 | MISS |  |
| M-17 | PARTIAL | Matched Finding [3], which identifies that stepDuration = (endTime - startTime) / numOfSteps can truncate to zero and cause a division-by-zero DoS in claimable, but only addresses the zero-value case rather than the broader divisibility rounding issue. |
| M-18 | MISS |  |
| M-19 | MISS |  |
| M-20 | MISS |  |

**Summary:** 1 EXACT, 5 PARTIAL, 17 MISS (23 total)
