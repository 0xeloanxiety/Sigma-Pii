ID   │ Verdict │ Justification
  ──────┼─────────┼─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
   H-01 │ MISS    │ No finding identifies the defect where SecondSwap_VestingManager inherits and aggregates stepsClaimed across listings, causing claimable
        │         │ amounts to vary depending on listing order.
   H-02 │ MISS    │ No finding identifies the defect where stepsClaimed remains static on the SecondSwap_VestingManager across sales, allowing buyers to inherit
        │         │ stale claim steps and unlock tokens prematurely.
   H-03 │ EXACT   │ Finding [1] identifies the exact same defect where transferVesting recalculates the grantor's releaseRate as totalAmount / numOfSteps without
        │         │ accounting for already claimed amounts or steps, and provides the exact same formula fix (totalAmount - amountClaimed) / (numOfSteps -
        │         │ stepsClaimed).
   M-01 │ MISS    │ No finding identifies the inverted condition (!= instead of ==) that bypasses minimum purchase amount validation for partial listings.
   M-02 │ MISS    │ No finding identifies the rounding error where discounted prices cause baseAmount to round down to zero and revert purchases.
   M-03 │ MISS    │ No finding identifies the lack of an admin function to remove depegged tokens from isTokenSupport.
   M-04 │ MISS    │ No finding identifies the mapping collision in SecondSwap_VestingDeployer (_tokenOwner[_owner] = token) that allows multiple owners of the same
        │         │ token to interfere with each other's vesting plans.
   M-05 │ MISS    │ No finding identifies the price granularity limitation caused by payment token decimals preventing listings priced under 1 wei of payment
        │         │ token.
   M-06 │ PARTIAL │ Finding [3] matches the underlying defect where integer division rounding in stepDuration allows currentStep to exceed numOfSteps and push
        │         │ stepsClaimed > numOfSteps, but it focuses on allocation underflow in _createVesting and lacks the explicit bounds-checking fix for claimable().
   M-07 │ MISS    │ No finding identifies that marketplace platform fees (buyFee and sellFee) can be modified after a listing has been created.
   M-08 │ MISS    │ No finding identifies that early delisting penalties charge updated fee rates rather than caching the rate established at listing time.
   M-09 │ MISS    │ No finding identifies that users can evade protocol reallocation by listing their unvested allocations on the marketplace.
   M-10 │ MISS    │ No finding identifies that transferVesting allows reallocation of tokens that have already vested and are owned by the beneficiary but remain
        │         │ unclaimed.
   M-11 │ MISS    │ No finding identifies that the maxSellPercent cap can be bypassed over time by reselling previously bought vestings.
   M-12 │ MISS    │ No finding identifies the unauthorized increase of maxSellPercent to 20% in setSellable after plan creation.
   M-13 │ MISS    │ No finding identifies that changing the marketplace address in SecondSwap_VestingManager orphans and locks existing marketplace listings.
   M-14 │ MISS    │ No finding identifies the inverted arithmetic formula in referralFeeCost; Finding [4] examines the same code section but reports an unrelated
        │         │ defect regarding missing on-chain transfers when referral fees were designed to settle off-chain.
   M-15 │ MISS    │ No finding identifies the omitted sellability check in completePurchase that allows purchasing tokens marked unsellable by the admin.
   M-16 │ MISS    │ No finding identifies the front-running denial of service where a beneficiary claims tokens to revert an in-flight transferVesting reallocation
        │         │ call.
   M-17 │ PARTIAL │ Finding [2] identifies the division-by-zero revert in claimable() when stepDuration rounds down to zero in (_endTime - _startTime) /
        │         │ _numOfSteps, but only covers schedules shorter than the step count and lacks the broader non-divisibility mitigation from the ground truth.
   M-18 │ MISS    │ No finding identifies the locking of tokens that occurs when delisting an allocation after claiming additional steps.
   M-19 │ MISS    │ No finding identifies that schedules with very large step counts round releaseRate down to zero or distort token distribution schedules.
   M-20 │ MISS    │ No finding identifies that delisting after claiming additional steps improperly deducts the full amount from sold and breaks the maxSellPercent