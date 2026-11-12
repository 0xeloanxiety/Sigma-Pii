   ID   │ Verdict │ Justification
  ──────┼─────────┼─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
   H-01 │ MISS    │ No finding addresses the VestingManager inheriting stepsClaimed across multiple listings.
   H-02 │ MISS    │ No finding identifies that buyers inherit an inaccurate stepsClaimed value from the VestingManager upon purchasing a vesting.
   H-03 │ PARTIAL │ Matched Finding [1], which identifies the same defect where transferVesting recalculates releaseRate without accounting for already claimed
        │         │ amounts/steps, but omits the ground-truth fix formula or suggests capping in claimable().
   M-01 │ MISS    │ No finding identifies the inverted != listing-type validation check in listVesting.
   M-02 │ MISS    │ No finding identifies that discounted prices can cause baseAmount to round down to zero and revert purchases.
   M-03 │ MISS    │ No finding identifies the missing functionality to remove supported tokens from isTokenSupport.
   M-04 │ MISS    │ No finding identifies the token-owner mapping collision in VestingDeployer allowing creators to affect others' vesting plans.
   M-05 │ MISS    │ No finding identifies that payment-token decimal precision restricts minimum listing prices for low-value tokens.
   M-06 │ MISS    │ No finding identifies the underflow bug in claimable() when stepsClaimed exceeds numOfSteps.
   M-07 │ MISS    │ No finding identifies that mutable platform fees can retroactively alter costs for existing listings.
   M-08 │ MISS    │ No finding identifies that delisting penalty calculations can use outdated fee values.
   M-09 │ MISS    │ No finding identifies that beneficiaries can evade reallocation by listing their vestings on the marketplace.
   M-10 │ MISS    │ No finding identifies that transferVesting permits transferring already-vested but unclaimed tokens away from users.
   M-11 │ MISS    │ No finding identifies that maxSellPercent can be bypassed over time by reselling previously bought vestings.
   M-12 │ MISS    │ No finding identifies the unauthorized increase of maxSellPercent to 20% in setSellable.
   M-13 │ MISS    │ No finding identifies that changing the marketplace contract address in VestingManager strands existing marketplace listings.
   M-14 │ MISS    │ Finding [3] touches the same code block but misdiagnoses intended off-chain fee distribution as a missing token transfer rather than
        │         │ identifying the inverted mathematical formula defect in referralFeeCost.
   M-15 │ MISS    │ No finding identifies the missing sellability check in completePurchase.
   M-16 │ MISS    │ No finding identifies the DoS scenario where claiming tokens frontruns and reverts an admin vest transfer.
   M-17 │ PARTIAL │ Matched Finding [2], which captures the division-by-zero defect when stepDuration rounds down to zero, but has a narrower scope and fix than
        │         │ the ground truth's exact divisibility requirement.
   M-18 │ MISS    │ No finding identifies that unlisting after claiming additional steps relocks tokens that should remain claimable.
   M-19 │ MISS    │ No finding identifies that large step counts relative to token amount cause releaseRate to round down to zero.
   M-20 │ MISS    │ No finding identifies that delisting after claiming steps corrupts the sold counter and breaks maxSellPercent.