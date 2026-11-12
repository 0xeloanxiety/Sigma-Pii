   ID   │ Verdict │ Justification
  ──────┼─────────┼─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
   H-01 │ PARTIAL │ Matched Finding [8], which correctly identifies that listing order causes vestings pooled under the manager to inherit the first seller's
        │         │ stepsClaimed (delaying claims for earlier-stage allocations), but does not provide an explicit fix.
   H-02 │ PARTIAL │ Matched Finding [8], which identifies that manager-held listings retain a static stepsClaimed allowing new buyers to unlock tokens prematurely,
        │         │ but lacks an explicit fix.
   H-03 │  EXACT  │ Matched Finding [2], identifying the exact same defect where transferVesting recalculates releaseRate without deducting claimed amounts and
        │         │ steps, and proposing the exact same fix.
   M-01 │  MISS   │ No finding identifies the inverted != operator check in SecondSwap_Marketplace.sol that bypasses minimum purchase amount enforcement for
        │         │ partial listings.
   M-02 │  MISS   │ No finding identifies the rounding down of baseAmount to zero when calculating discounted purchase prices in spotPurchase.
   M-03 │  MISS   │ No finding identifies the missing administrative mechanism to remove depegged tokens from isTokenSupport.
   M-04 │  MISS   │ No finding identifies the _tokenOwner mapping collision in SecondSwap_VestingDeployer.sol where multiple owners can share a single token and
        │         │ manipulate each other's vesting plans.
   M-05 │  MISS   │ No finding identifies the price granularity limitation imposed by payment token decimals preventing listings cheaper than 0.000001 USDT.
   M-06 │ PARTIAL │ Matched Finding [6], which identifies that stepDuration truncation causes currentStep to exceed numOfSteps and leaves stepsClaimed >
        │         │ numOfSteps, but targets capping currentStep rather than handling the subtraction underflow in claimable.
   M-07 │  MISS   │ No finding identifies that marketplace platform fees can be modified after listing creation, disrupting pricing predictability.
   M-08 │  MISS   │ No finding identifies that early delisting penalty fee calculations read mutable protocol fee parameters instead of caching the fee rate at
        │         │ listing time.
   M-09 │  MISS   │ No finding identifies that users can prevent administrator reallocation by listing their vestings on the marketplace.
   M-10 │  MISS   │ No finding identifies that transferVesting fails to protect already vested but unclaimed tokens from being transferred away during
        │         │ reallocation.
   M-11 │  MISS   │ No finding identifies that maxSellPercent restrictions can be bypassed by selling previously bought secondary vestings at a later time.
   M-12 │  MISS   │ No finding identifies the missing initialization check in setSellable that allows unauthorized increases of maxSellPercent to 20%.
   M-13 │  MISS   │ No finding identifies that updating the marketplace address in SecondSwap_VestingManager permanently locks existing listings created under the
        │         │ prior marketplace.
   M-14 │ PARTIAL │ Matched Finding [5], which explicitly notes the flawed subtraction math in referralFeeCost (buyerFeeTotal - ... instead of a percentage
        │         │ calculation), but primarily focused on referral rewards never being disbursed on-chain and omitted the standalone fix formula.
   M-15 │  MISS   │ No finding identifies the missing sellability check in completePurchase that permits purchases of listings after a token has been marked
        │         │ unsellable.
   M-16 │  MISS   │ No finding identifies that transferVesting can be front-run and DoS'd by the beneficiary claiming tokens before reallocation.
   M-17 │ PARTIAL │ Matched Finding [3], which identifies that stepDuration = (endTime - startTime) / numOfSteps can truncate to zero and cause a division-by-zero
        │         │ DoS in claimable, but only addresses the zero-value case rather than the broader divisibility rounding issue.
   M-18 │  MISS   │ No finding identifies that delisting a vesting after the seller has claimed intermediate steps locks tokens that should have remained
        │         │ immediately claimable.
   M-19 │  MISS   │ No finding identifies that large step counts can cause releaseRate to round down to zero and freeze funds when token amounts are smaller than
        │         │ the step count.
   M-20 │  MISS   │ No finding identifies that deducting the full listed amount from sold when delisting after claiming steps breaks the maxSellPercent cap.