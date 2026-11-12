# Judgment Results

| ID | Verdict | Justification |
|---|---|---|
| H-01 | PARTIAL | Matched by Finding [9], which identifies the underlying defect of VestingManager pooling all listings under a single shared stepsClaimed state, but focuses on premature unlocks rather than listing-order dependency and lacks a remediation. |
| H-02 | PARTIAL | Matched by Finding [9], which identifies the exact defect where stepsClaimed remains fixed at the manager's initial listing value and lets buyers prematurely unlock tokens, but omits a fix and is classified as Medium rather than High. |
| H-03 | EXACT | Matched by Finding [3], which identifies the exact defect where transferVesting recalculates grantorVesting.releaseRate using total steps instead of remaining steps and unclaimed balance, and proposes the same fix. |
| M-01 | MISS |  |
| M-02 | MISS |  |
| M-03 | MISS |  |
| M-04 | EXACT | Matched by Finding [4], which identifies the exact defect where _tokenOwner allows multiple owners per token and deployer wrappers fail to verify that the caller is the specific plan's creator/issuer. |
| M-05 | MISS |  |
| M-06 | EXACT | Matched by Finding [6], which identifies the exact defect where integer rounding in claimable allows currentStep and stepsClaimed to exceed numOfSteps, causing subsequent allocation and claim underflows. |
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
| M-17 | PARTIAL | Matched by Finding [2], which identifies stepDuration rounding down to zero and causing division-by-zero reverts in claimable(), but offers a narrower fix (duration >= steps) that does not address non-exact divisibility. |
| M-18 | MISS |  |
| M-19 | MISS |  |
| M-20 | MISS |  |

**Summary:** 3 EXACT, 3 PARTIAL, 17 MISS (23 total)
