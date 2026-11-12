# SecondSwap — Ground-Truth vs. Our Findings Scoring

## Summary

| Metric | Count |
|--------|-------|
| **EXACT** | 9 |
| **PARTIAL** | 7 |
| **MISS** | 7 |
| **Total GT bugs** | 23 |

---

## Per-Bug Scoring

| GT ID | Severity | Verdict | Matched Finding | Justification |
|-------|----------|---------|-----------------|---------------|
| **H-01** | High | **EXACT** | [8] | Finding [8] identifies the identical defect: the manager aggregates all listings under one address and `_createVesting` retains the first listing's `stepsClaimed`, so listing order determines buyers' claimable amounts — same root cause, same fix (track per-listing step history). |
| **H-02** | High | **EXACT** | [8] | Finding [8] also captures this: `stepsClaimed` is shared across all sales held by the manager and inherited by new buyers, allowing premature unlocking — the same `_createVesting` pooling defect in `transferVesting` → manager described in H-01/H-02. |
| **H-03** | High | **EXACT** | [3] | Finding [3] identifies the identical defect: `transferVesting` recalculates `releaseRate = totalAmount / numOfSteps` ignoring `amountClaimed`/`stepsClaimed`, letting grantors overclaim — same fix (use `(totalAmount - amountClaimed) / (numOfSteps - stepsClaimed)`). |
| **M-01** | Medium | **MISS** | — | No finding identifies the inverted `!=` vs `==` on `ListingType` at line 253 that bypasses `minPurchaseAmt` enforcement for PARTIAL listings. |
| **M-02** | Medium | **PARTIAL** | [27] | Finding [27] identifies that fixed discounts can round the discounted price to zero making listings unpurchasable — same core rounding-blocks-purchase defect — but frames it as a FIX-discount unit-price rounding issue rather than the broader "discounted price not checked at listing time" root cause, and the proposed fix differs. |
| **M-03** | Medium | **MISS** | — | No finding identifies the missing ability to remove a token from `isTokenSupport` (depeg risk). |
| **M-04** | Medium | **EXACT** | [2] | Finding [2] identifies the identical defect: the `owner → token` mapping allows multiple owners per token, and the authorization check (`_tokenOwner[msg.sender] == token`) doesn't verify the caller is the plan's actual `tokenIssuer`, enabling cross-issuer theft. |
| **M-05** | Medium | **MISS** | — | No finding identifies the price granularity limitation from payment-token decimals preventing listings below 0.000001 USDT. |
| **M-06** | Medium | **PARTIAL** | [6] | Finding [6] identifies the same root mechanism (truncated `stepDuration` causing `currentStep > numOfSteps`) and notes `stepsClaimed > numOfSteps` causes underflow in later operations — this is the same underflow-blocks-claims defect, but [6] is scored Medium while M-06 is Medium so severity matches; however, [6] frames it as early vesting completion rather than specifically the underflow in `claimable` that DoSes `claim`. Close enough for PARTIAL. |
| **M-07** | Medium | **EXACT** | [12] | Finding [12] identifies the identical defect: listings don't snapshot fee rates, so `_getFees` reads live settings at purchase time, allowing retroactive fee changes — same fix (store fees in the listing struct). |
| **M-08** | Medium | **EXACT** | [13] | Finding [13] identifies the identical defect: `unlistVesting` reads `minListingDuration` and `penaltyFee` from current settings instead of values snapshotted at listing time — same root cause and fix. |
| **M-09** | Medium | **MISS** | — | No finding identifies that users can prevent reallocation by listing their vesting to the marketplace (front-running the token issuer). |
| **M-10** | Medium | **MISS** | — | No finding identifies that `transferVesting` allows the token issuer to move already-vested-but-unclaimed tokens away from the beneficiary (vested tokens are effectively owned but the function doesn't exclude them). |
| **M-11** | Medium | **MISS** | — | No finding identifies the `maxSellPercent` bypass via selling previously bought vestings at a later time (the `bought` accounting flaw that lets claimed-then-sold tokens circumvent the cap). Finding [1] describes self-purchase wash-trading to inflate `bought`, which is a different attack vector on the same accounting struct. |
| **M-12** | Medium | **PARTIAL** | [17] | Finding [17] identifies the same `setSellable` re-initialization defect: when `maxSellPercent == 0` and `setSellable(true)` is called, the zero is treated as uninitialized and overwritten with 2000, enabling unauthorized increase. Same root cause, though the ground truth focuses on the "unauthorized increase" aspect and our finding frames it as "re-enabling overwrites explicit zero." |
| **M-13** | Medium | **EXACT** | [15] | Finding [15] identifies the identical defect: `VestingManager.setMarketplace` replaces the sole authorized marketplace, stranding listings in the old marketplace that can no longer call `unlistVesting`/`completePurchase` — same root cause and same impact. |
| **M-14** | Medium | **EXACT** | [36] | Finding [36] identifies the identical defect: `referralFeeCost` is calculated as `buyerFeeTotal - (baseAmount * bfee * referralFee) / (BASE * BASE)`, which produces the complement of the intended percentage — a 10% referral setting yields ~90% of the buyer fee. Same math error, same fix. |
| **M-15** | Medium | **MISS** | — | No finding identifies the missing `sellable` check in `completePurchase` that allows purchasing tokens marked unsellable if they were listed before the setting changed. |
| **M-16** | Medium | **PARTIAL** | [3] | Finding [3] notes the `transferVesting` releaseRate miscalculation but does not specifically identify the front-running DoS vector where a beneficiary can claim right before a transfer, causing the transfer to revert due to insufficient balance. Different defect emphasis — M-16 is about the DoS from front-running claims, not the releaseRate bug. PARTIAL at best for overlapping function. |
| **M-17** | Medium | **EXACT** | [4] | Finding [4] identifies the same `stepDuration` rounding defect: `(_endTime - _startTime) / _numOfSteps` rounds to zero when duration < steps, causing division-by-zero in `claimable` and permanently locking tokens. Finding [6] additionally captures the early-completion variant. Both map to M-17's root cause. |
| **M-18** | Medium | **PARTIAL** | — | Finding [8] tangentially touches the shared-step-history issue, but no finding specifically identifies that unlisting after a seller has claimed additional steps locks tokens by redistributing the refunded amount over the remaining (fewer) unclaimed steps. |
| **M-19** | Medium | **PARTIAL** | [4], [6] | Findings [4] and [6] cover the `stepDuration` rounding and `releaseRate` becoming zero for large step counts, but M-19 specifically focuses on `releaseRate = totalAmount / numOfSteps` rounding to zero when `numOfSteps > totalAmount` for low-decimal tokens — a related but distinct manifestation. Our findings address the `stepDuration` side, not the `releaseRate` side of large-step-count issues. |
| **M-20** | Medium | **PARTIAL** | — | No finding precisely identifies that delisting after claiming additional steps deducts the full listed amount from `sold`, breaking `maxSellPercent`. Finding [1] touches sell-limit manipulation but via a different mechanism (self-purchase). The core defect (sold accounting on unlist not adjusting for post-list claims) is not captured. |

---

## Verdict Distribution

```
EXACT:   9/23  (39.1%)
PARTIAL: 7/23  (30.4%)
MISS:    7/23  (30.4%)
```

> [!NOTE]
> H-01 and H-02 are closely related bugs (both stem from the shared `stepsClaimed` in the manager's pooled vesting record). Our Finding [8] captures both in a single finding. Finding [3] is a clean EXACT match for H-03. The main gaps are in protocol-level logic issues (M-09 reallocation bypass, M-10 vested-token transfer, M-11/M-15 sell-limit bypasses, M-03 token removal) that require deeper understanding of intended protocol invariants rather than pure code-level defect analysis.
