   ID   │ Verdict │ Justification
  ──────┼─────────┼───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
   H-01 │ PARTIAL │ Matched by Finding [9], which identifies the underlying defect of VestingManager pooling all listings under a single shared stepsClaimed state, but focuses on premature
        │         │ unlocks rather than listing-order dependency and lacks a remediation.
   H-02 │ PARTIAL │ Matched by Finding [9], which identifies the exact defect where stepsClaimed remains fixed at the manager's initial listing value and lets buyers prematurely unlock tokens,
        │         │ but omits a fix and is classified as Medium rather than High.
   H-03 │ EXACT   │ Matched by Finding [3], which identifies the exact defect where transferVesting recalculates grantorVesting.releaseRate using total steps instead of remaining steps and
        │         │ unclaimed balance, and proposes the same fix.
   M-01 │ MISS    │ No finding identifies the inverted listing-type validation check (!= ListingType.SINGLE instead of == ListingType.PARTIAL) that bypasses minimum purchase amount enforcement
        │         │ in SecondSwap_Marketplace.sol.
   M-02 │ MISS    │ No finding identifies that discounted listings can revert during purchase due to baseAmount rounding down to zero (Finding [7] addresses buyer underpayment via partial-fill
        │         │ truncation instead).
   M-03 │ MISS    │ No finding identifies the lack of functionality to remove or deprecate supported payment tokens from isTokenSupport in SecondSwap_Marketplace.sol.
   M-04 │ EXACT   │ Matched by Finding [4], which identifies the exact defect where _tokenOwner allows multiple owners per token and deployer wrappers fail to verify that the caller is the
        │         │ specific plan's creator/issuer.
   M-05 │ MISS    │ No finding identifies the minimum price floor and granularity limit for low-value tokens imposed by 6-decimal payment currencies in SecondSwap_Marketplace.sol.
   M-06 │ EXACT   │ Matched by Finding [6], which identifies the exact defect where integer rounding in claimable allows currentStep and stepsClaimed to exceed numOfSteps, causing subsequent
        │         │ allocation and claim underflows.
   M-07 │ MISS    │ No finding identifies that marketplace platform fees (buyFee and sellFee) can be altered after listing creation without being snapshotted.
   M-08 │ MISS    │ No finding identifies that early-delisting penalties use the active setting rather than a fee snapshotted at listing time (Finding [10] addresses token decimal mismatch
        │         │ instead).
   M-09 │ MISS    │ No finding identifies that beneficiaries can evade token reallocation by listing their allocations on the marketplace.
   M-10 │ MISS    │ No finding identifies that transferVesting allows reallocating tokens that have already vested but remain unclaimed by the beneficiary.
   M-11 │ MISS    │ No finding identifies that maxSellPercent restrictions can be bypassed over time by reselling previously purchased allocations.
   M-12 │ MISS    │ No finding identifies that setSellable allows unauthorized increases to maxSellPercent after initial creation.
   M-13 │ MISS    │ No finding identifies that updating the marketplace address in VestingManager orphans active listings from the previous marketplace.
   M-14 │ MISS    │ No finding identifies the inverted mathematical formula used to calculate referralFeeCost in SecondSwap_Marketplace.sol (Finding [5] addresses missing on-chain ERC20
        │         │ transfers instead).
   M-15 │ MISS    │ No finding identifies the missing sellability check in completePurchase for previously listed vesting plans.
   M-16 │ MISS    │ No finding identifies that a beneficiary can frontrun an authority's transferVesting call by claiming tokens to trigger an insufficient balance revert.
   M-17 │ PARTIAL │ Matched by Finding [2], which identifies stepDuration rounding down to zero and causing division-by-zero reverts in claimable(), but offers a narrower fix (duration >=
        │         │ steps) that does not address non-exact divisibility.
   M-18 │ MISS    │ No finding identifies that unlisting after a seller has claimed additional steps disrupts the unlocking schedule and relocks claimable tokens.
   M-19 │ MISS    │ No finding identifies that large step counts relative to low-decimal token amounts cause releaseRate to round down to zero.
   M-20 │ MISS    │ No finding identifies that unlisting after claiming additional steps deducts the full original amount from sold, breaking maxSellPercent enforcement.