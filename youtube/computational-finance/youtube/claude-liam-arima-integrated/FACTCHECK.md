# FACTCHECK.md — claim | verdict | source | fix

Source: a third-party ARIMA tutorial transcript (supplied). Every math claim
below was independently verified against standard references — the transcript
is a teaching aid, not an authority.

| # | Claim in episode | Verdict | Source | Note |
|---|---|---|---|---|
| 1 | ARIMA = AutoRegressive Integrated Moving Average | HOLDS | IBM; Britannica | — |
| 2 | The "I" = Integrated = differencing (NOT integrals) | HOLDS | IBM ("integrated component involves differencing") | Body makes the "not calculus" point explicitly |
| 3 | ARMA/ARIMA require (approx.) stationarity: constant mean, constant variance, no seasonality | HOLDS | standard time-series theory; IBM ("made approximately stationary through transformations") | — |
| 4 | Differencing removes a trend → achieves stationarity | HOLDS | IBM | — |
| 5 | First difference Z_t = a_t − a_{t−1} | HOLDS | standard (∇a_t) | ⚠ Source transcript wrote a_{t+1} − a_t; both are "the first difference" (an index shift). Episode uses the standard backward form a_t − a_{t−1} |
| 6 | A linear trend has constant first differences | HOLDS | elementary (Δ of an arithmetic progression is constant) | The load-bearing intuition of Act II |
| 7 | ARIMA(p,d,q): p = AR order, d = degree of differencing, q = MA order | HOLDS | IBM (verbatim on all three) | — |
| 8 | ARIMA(1,1,1): Z_t = φ₁Z_{t−1} + θ₁ε_{t−1} + ε_t, on the differenced series | HOLDS | standard ARIMA form | Transcript's "V₁"/"theta₁" = φ₁/θ₁; the I is carried by Z_t being a difference |
| 9 | Higher d = difference again (d=2 → second difference); prefer the smallest d | HOLDS | standard (parsimony / over-differencing caution) | — |
| 10 | Recover a_t from differences by a cumulative sum (a_k = a_L + Σ Z); this is why it's "integrated" | HOLDS | standard (differencing and summation are inverse ops; discrete integration) | — |
| 11 | George Box & Gwilym Jenkins, 1970, proposed the Box–Jenkins method | HOLDS | IBM ("In 1970 … George Box and Gwilym Jenkins"); Box & Jenkins (1970), *Time Series Analysis: Forecasting and Control* | Anchors the B08 VOX context beat |

## Stripped as datable / out of scope

- No software/package names (statsmodels, R, etc.), no "as of" claims — none
  needed. The episode teaches the mechanism, timeless.
- The source's boat-anchor example is replaced by an original (e-bike sales)
  to avoid lifting another creator's signature example — see PLAN.md flag 1.

## Caveat (genre rule 5)

The transcript mixes correct math with casual phrasing ("V₁", a_{t+1}−a_t
shift). Every equation in the episode was re-derived to standard form, not
copied — see rows 5 and 8.
