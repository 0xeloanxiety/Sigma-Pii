   ID   │ Verdict │ Justification
   --
   H-01 │ MISS    │ No finding identifies that the shared stepsClaimed state in VestingManager across listings alters claimable amounts depending on listing order.
   H-02 │ MISS    │ No finding identifies that transferVesting to VestingManager preserves a static stepsClaimed across sales, allowing subsequent buyers to claim
        │         │ tokens prematurely.
   H-03 │ EXACT   │ Matched Finding [1], as both identify that transferVesting resets releaseRate = totalAmount / numOfSteps without accounting for already-claimed
        │         │ amounts and steps, allowing grantors to overclaim, and both prescribe recalculating the rate using remaining amounts and remaining steps.
   M-01 │ MISS    │ No finding identifies the inverted != validation in listVesting that bypasses minimum purchase amount enforcement for partial listings.
   M-02 │ MISS    │ No finding identifies that rounding down baseAmount to zero when applying a discount prevents purchasing discounted listings.
   M-03 │ MISS    │ No finding identifies the missing administrative mechanism to remove depegged currencies from isTokenSupport.
   M-04 │ MISS    │ No finding identifies the token-owner mapping collision where multiple creators sharing a token can manipulate or fund each other's vesting
        │         │ plans.
   M-05 │ MISS    │ No finding identifies that 6-decimal payment token units enforce a minimum price floor that prevents pricing low-value tokens below 0.000001
        │         │ USDT.
   M-06 │ MISS    │ No finding identifies that stepsClaimed exceeding numOfSteps due to rounding causes an arithmetic underflow in claimable(), blocking token
        │         │ claims.
   M-07 │ MISS    │ No finding identifies that mutable buyFee and sellFee parameters can alter transaction costs unexpectedly after a listing is created.
   M-08 │ MISS    │ No finding identifies the lack of penalty fee caching at listing time; Finding [4] instead addresses the 18-decimal configuration mismatch for
        │         │ USDT.
   M-09 │ MISS    │ No finding identifies that users can front-run and block token reallocation by listing their vesting schedule on the marketplace.
   M-10 │ MISS    │ No finding identifies that transferVesting allows transferring already-vested but unclaimed tokens away from a beneficiary during reallocation.
   M-11 │ MISS    │ No finding identifies that maxSellPercent restrictions can be bypassed by selling previously purchased vesting allocations later.
   M-12 │ MISS    │ No finding identifies that uninitialized vesting settings allow unauthorized increases of maxSellPercent to 20% in setSellable.
   M-13 │ MISS    │ No finding identifies that updating the marketplace contract address in VestingManager permanently locks existing marketplace listings.
   M-14 │ MISS    │ No finding identifies the inverted mathematical formula calculating 90% instead of 10% for referralFeeCost; Finding [3] instead erroneously
        │         │ claims referral rewards are missing an on-chain transfer.
   M-15 │ MISS    │ No finding identifies the missing sellability check in completePurchase allowing purchases of tokens marked unsellable post-listing.
   M-16 │ MISS    │ No finding identifies the DoS vulnerability where beneficiaries can front-run an issuer's transferVesting reallocation by claiming tokens.
   M-17 │ PARTIAL │ Matched Finding [2], which correctly identifies that integer truncation in stepDuration = (_endTime - _startTime) / _numOfSteps yields zero
        │         │ when duration is less than steps and causes a division-by-zero DoS in claimable(), but suggests a narrower fix (requiring duration to be at
        │         │ least the number of steps) rather than ensuring exact divisibility.
   M-18 │ MISS    │ No finding identifies that unlisting after a seller claims additional steps disrupts the unlocking schedule and re-locks claimable tokens.
   M-19 │ MISS    │ No finding identifies that schedules with high step counts relative to token amounts round releaseRate to zero in _createVesting, causing
        │         │ beneficiaries to lose tokens.
   M-20 │ MISS    │ No finding identifies that delisting after claiming additional steps deducts the full listed amount from sold, breaking the maxSellPercent
        │         │ limit.