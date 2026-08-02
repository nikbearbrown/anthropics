# Chapter 14 — Corporation Accounting

## 14.1 Opening: The owner who is also a stranger

Mark Summers's Supreme Cleaners, the running example of Chapters 3-5, is a sole proprietorship. Mark *is* the business, in everything except formal accounting separation. He bears unlimited personal liability for its obligations. The business dissolves when Mark retires.

Now imagine Mark wants to open ten more locations. He doesn't have the capital. His brother and a few friends might invest, but they don't want to take on Mark's personal liability. Mark doesn't want to give up control to a fifty-fifty partner. The legal structure that solves all of these problems is the *corporation* — a legally distinct entity that owners can buy stakes in (called *stock*), with limited liability and separate legal personhood from its owners. Owners can be many or few, can be employees of the company or strangers who never set foot in it, and can buy or sell their stake without affecting the business's existence.

The accounting consequences are substantial. The equity section of a corporation's balance sheet is structurally different from a sole proprietorship's. *Capital* becomes *Common Stock* and *Additional Paid-in Capital* and *Retained Earnings*, with *Treasury Stock* and *Preferred Stock* as variants. Earnings retained from operations don't sit in the owner's capital account; they accumulate in Retained Earnings, distinct from the original investment. Distributions don't reduce capital directly; they go through Retained Earnings via dividends. Stock can be issued, repurchased, split, and converted, each with its own journal entry pattern.

By the end of this chapter, you should be able to:

- Explain the rights of common stockholders (voting, dividend participation, residual claim) and the special features of preferred stock (dividend preference, possible cumulative or convertible features).
- Journalize the issuance of common stock at par, above par, and (rarely) below par.
- Journalize the repurchase of stock as treasury stock and the reissuance of treasury stock.
- Journalize cash dividends, stock dividends, and stock splits.
- Distinguish authorized, issued, and outstanding shares.
- Compute and interpret *book value per share* and *earnings per share*.

## 14.2 Common stock and the basic rights of shareholders

*Common stock* is the basic ownership claim in a corporation. Each share carries (typically) one vote on shareholder matters — election of directors, major corporate actions like mergers or charter amendments, ratification of auditors. Each share also represents a fractional claim on the company's residual equity — what's left after liabilities and any preferred-stock claims are settled.

Three numbers describe a corporation's shares:

*Authorized shares* — the maximum number of shares the corporate charter permits the company to issue. Set by the charter, can be increased only by shareholder vote.

*Issued shares* — the number of shares the company has actually distributed to investors. Always ≤ authorized.

*Outstanding shares* — issued shares currently held by investors (i.e., not held by the company itself as treasury stock). Always ≤ issued.

Authorized − Issued = unissued shares; Issued − Outstanding = treasury shares.

*Par value* is a nominal accounting figure (often $0.01 or $1) printed on the stock certificate. It has limited economic meaning — par value is *not* market value, *not* book value, *not* purchase price. It's a legal floor below which shares typically cannot be issued. Most state laws require shares to be issued at or above par; below-par issuance is rare and typically problematic.

When stock is issued *at par*: Cash is debited for the issue price; Common Stock is credited for par value times shares issued.

When stock is issued *above par* (the common case): Cash is debited for full issue price; Common Stock is credited for par × shares; *Additional Paid-in Capital* (also called *Paid-in Capital in Excess of Par*) is credited for the difference.

For example: 1,000 shares of $1 par common stock issued at $25 per share.

| Account | Debit | Credit |
|---|---|---|
| Cash | $25,000 | |
| Common Stock | | $1,000 |
| Additional Paid-in Capital | | $24,000 |

Common Stock and Additional Paid-in Capital together represent the total *contributed capital* — what investors paid in. Plus *Retained Earnings* (accumulated retained net income) plus the various adjustments equals total *Stockholders' Equity*.

*No-par stock* exists in some states; the entire issue price is credited to Common Stock with no Additional Paid-in Capital. The accounting is simpler; the legal framework is different.

## 14.3 Preferred stock

*Preferred stock* is a hybrid — part equity, part debt-like. Holders typically receive a fixed dividend (e.g., 6% of par per year) before any common-stock dividend can be paid. They have preferential claims to assets in liquidation (after creditors but before common shareholders). They typically don't vote on company matters.

Several features distinguish preferred stock variants:

*Cumulative preferred* — if a dividend is missed in any year, it accumulates and must be paid before common stockholders can receive any dividend. Missed cumulative dividends are called *dividends in arrears*; they are not a liability (until declared) but must be disclosed.

*Convertible preferred* — can be converted into common stock at a stated ratio at the holder's option.

*Callable preferred* — can be repurchased by the company at a stated price.

*Participating preferred* — entitled to share in additional dividends beyond the fixed rate, after common stockholders receive a comparable dividend.

The journal entry for issuance parallels common stock: Cash debited, Preferred Stock (par × shares) credited, Additional Paid-in Capital — Preferred credited for any excess.

The trade-off in the preferred-stock structure: preferred buys *senior dividend and liquidation rights* at the cost of *no voting power and no participation in capital gains beyond the fixed dividend* (except for participating or convertible preferred). For investors seeking income with relatively predictable cash flows, preferred is attractive. For founders not wanting to dilute voting control, preferred is a way to raise capital without giving up votes.

## 14.4 Treasury stock

When a corporation buys back its own previously-issued shares, the repurchased shares become *treasury stock*. They are not retired (the corporate charter still authorizes them, and they're still issued in the legal sense), but they are no longer outstanding — they don't vote, don't receive dividends, and don't count in earnings-per-share calculations.

Companies repurchase stock for several reasons: to return cash to shareholders (when the company has excess cash and prefers buybacks to dividends), to support the share price, to reissue shares for stock options or compensation plans, to acquire another company in a stock transaction.

The standard accounting under U.S. GAAP is the *cost method*: treasury stock is recorded at the cash cost of repurchase, and held as a contra-equity account.

A company repurchases 100 shares of its own common stock at $40 per share:

| Account | Debit | Credit |
|---|---|---|
| Treasury Stock | $4,000 | |
| Cash | | $4,000 |

Treasury Stock is a *contra-equity* account — it reduces total stockholders' equity. On the balance sheet, it appears as a deduction at the bottom of the equity section.

Reissuance of treasury stock at the same price:

| Account | Debit | Credit |
|---|---|---|
| Cash | $4,000 | |
| Treasury Stock | | $4,000 |

Reissuance *above* original cost (say, reissued at $45):

| Account | Debit | Credit |
|---|---|---|
| Cash | $4,500 | |
| Treasury Stock | | $4,000 |
| Paid-in Capital from Treasury Stock | | $500 |

Reissuance *below* original cost (say, $35) reduces Paid-in Capital from Treasury Stock first; if the balance is exhausted, the remaining loss reduces Retained Earnings. *Treasury stock transactions never produce gains or losses on the income statement.* This is a structural rule — a corporation cannot earn income by trading its own shares.

## 14.5 Cash dividends, stock dividends, stock splits

*Cash dividends* — declared by the board, paid in cash to shareholders. Three dates matter:

- *Declaration date*: the board votes; legal liability arises. Journal entry: Debit Retained Earnings (or Dividends), Credit Dividends Payable.
- *Date of record*: shareholders as of this date receive the dividend. No journal entry.
- *Payment date*: cash goes out. Journal entry: Debit Dividends Payable, Credit Cash.

*Stock dividends* — distribution of additional shares to existing shareholders proportionally. No cash leaves the company; the equity composition shifts. A 10% stock dividend on 1,000,000 outstanding shares means 100,000 new shares are issued pro-rata to existing holders.

For *small* stock dividends (below 20-25%), the entry capitalizes the *fair market value* of the issued shares from Retained Earnings to Common Stock and Additional Paid-in Capital. For 100,000 new $1 par shares with market value $20:

| Account | Debit | Credit |
|---|---|---|
| Retained Earnings | $2,000,000 | |
| Common Stock | | $100,000 |
| Additional Paid-in Capital | | $1,900,000 |

For *large* stock dividends (above 25%), only par value is capitalized: Debit Retained Earnings $100,000, Credit Common Stock $100,000.

Total stockholders' equity is unchanged — the entry shuffles balances among components without affecting the sum.

*Stock splits* — distribution of additional shares accompanied by a reduction in par value, so the total par-value-times-shares stays constant. A 2-for-1 split on $1 par stock: every existing share becomes two shares, each at $0.50 par. No journal entry is required (just a memorandum); only the par value and share count change. Stock splits are typically used to lower per-share market price into a range investors find attractive; they have no effect on total equity or on each shareholder's percentage ownership.

The trade-off across these distribution methods: cash dividends transfer real value out of the company; stock dividends and stock splits don't, but they signal something about board confidence and reach a different segment of investor preferences. Companies use the methods in combination.

## 14.6 Retained Earnings and the income flow

*Retained Earnings* is the accumulated net income (or net loss) the company has retained — earned but not paid out as dividends — since inception. The closing entries from Chapter 5 close net income (or loss) into Retained Earnings each year; dividends declared close out as deductions.

The balance in Retained Earnings is *not* cash. It's the cumulative net contribution to equity from operations. The company may have retained $500 million of earnings over twenty years and have only $30 million of cash — the rest may have been used to buy equipment, build buildings, acquire other companies, repay debt, repurchase stock. Retained Earnings is an equity claim; the cash that backed it has long since been deployed elsewhere.

A subtle but important point: dividends can only be paid to the extent of retained earnings (and within state-law constraints on capital impairment). A company that has accumulated losses and has zero retained earnings cannot legally pay dividends until it has rebuilt retained earnings through future profits. This is the *legal capital* doctrine — paid-in capital is generally protected from being distributed to shareholders.

## 14.7 Earnings per share and book value per share

Two per-share metrics are central to corporate equity analysis.

*Earnings per share (EPS)* = Net Income (less preferred dividends) / Weighted Average Common Shares Outstanding.

EPS measures profit attributable to each share of common stock. It's the most-watched single financial-statement metric for public companies — earnings releases lead with it, analysts forecast it, stock prices respond to it. *Diluted EPS* — which incorporates the effect of stock options, convertible securities, and other dilutive instruments — is reported alongside *basic EPS* and is typically the figure most analysts focus on.

*Book value per share* = (Total Stockholders' Equity − Preferred Equity) / Shares Outstanding.

Book value per share is the accounting-claim of each common share against the company's net assets. It's typically much less than the share's market price (because market reflects future earnings expectations, while book reflects historical-cost values). The ratio of market price to book value (the *price-to-book ratio*) is one of the standard valuation metrics.

For a company with $480 million stockholders' equity (no preferred) and 60 million shares outstanding, book value per share = $8. If the market price is $24 per share, the price-to-book ratio is 3.0 — investors are pricing the company at three times its net book value, reflecting their expectation of future earnings and growth.

## 14.8 Exercises

### Warm-up

1. **Distinguish authorized, issued, and outstanding shares.**

2. **Explain in two sentences how a sole proprietorship's equity section differs structurally from a corporation's.**

3. **State the formulas for EPS (basic) and book value per share.**

### Application

4. **A corporation issues 5,000 shares of $5 par common stock at $30 per share.** Journalize the issuance.

5. **A corporation buys back 1,000 of its own shares at $42 each, then later reissues 400 of them at $50.** Journalize both transactions.

6. **The board of directors of a corporation with 2,000,000 shares outstanding (each $1 par, market $25) declares a 5% stock dividend.** Journalize the dividend.

### Synthesis

7. **A company has cumulative preferred stock that has missed two years of dividends, totaling $500,000 in arrears.** Discuss what financial-statement disclosure is required and why these arrearages are not (yet) a liability.

8. **A 2-for-1 stock split doubles the share count without changing total equity.** Discuss what economic signal management is sending by approving the split, and what (if anything) actually changes for the shareholder.

### Challenge

9. **A company with $50 million of retained earnings and $5 million of cash declares a $10 million dividend.** Walk through what happens. What does this transaction tell a careful reader about the company's financial flexibility?

10. **Treasury stock transactions can never produce a gain or loss on the income statement.** Explain why this rule exists structurally — what would go wrong if companies could record gains and losses from trading their own shares?

## 14.9 Chapter summary

You walked into this chapter with sole-proprietorship equity. You walk out with corporate equity in its full range.

Common stock represents the basic ownership claim, voting rights, and residual claim. Preferred stock provides senior dividend and liquidation rights at the cost of voting power. Authorized, issued, and outstanding shares are three distinct counts that any reader of an equity section must track.

Stock issuance journal entries split the proceeds between the par-value account (Common Stock or Preferred Stock) and Additional Paid-in Capital. Treasury stock — repurchased shares — is a contra-equity account; treasury transactions never affect the income statement.

Cash dividends transfer cash out of the company and reduce retained earnings. Stock dividends shuffle equity components without transferring any value out. Stock splits change share counts and par values without affecting total equity. Each method has its own journal entry pattern.

Retained Earnings is the cumulative net income retained by the company. Earnings per share and book value per share are the two standard per-share metrics for corporate equity analysis.

The single most important idea: a corporation's equity section reports the cumulative *legal* and *accounting* claims of owners, not the *market value* of those claims. Market value lives outside the financial statements and is shaped by future expectations the historical-cost system doesn't capture.

The common mistake to watch for: treating Retained Earnings as a pile of cash. It's not. It's an accumulated equity figure; the cash that backed each year's retained earnings has typically been deployed into operating assets long ago.

## 14.10 Stock-based compensation: a brief introduction

A category that has grown enormous at modern public companies and deserves at least a flag: *stock-based compensation*. Companies — particularly in technology — pay employees substantial portions of their compensation in equity rather than cash. Stock options, restricted stock units (RSUs), and employee stock purchase plans (ESPPs) all transfer ownership claims from existing shareholders to employees over time, in exchange for service.

The accounting principle (ASC 718): the *fair value* of the equity award at grant date is recognized as compensation expense over the *vesting period*. Stock options vesting over four years require one-quarter of the grant-date fair value to be expensed each year, regardless of whether the option is ever exercised. The expense reduces net income; the offsetting credit goes to Additional Paid-in Capital. When options are eventually exercised, additional accounting entries record the cash received and the share issuance.

The fair value of a stock option at grant date is typically computed using the *Black-Scholes* model or a binomial pricing model. Inputs include the current stock price, the option's strike price, the time to expiration, expected stock-price volatility, the risk-free interest rate, and the expected dividend yield. The mechanics are beyond an introductory chapter; the conceptual point is that options have economic value at grant — they are not free even though no cash changes hands at grant — and the standard captures that value as compensation expense.

For technology companies, stock-based compensation is often the largest non-cash expense on the income statement and the largest reconciling item between net income and operating cash flow. A reader analyzing a tech company's profitability who ignores stock-based compensation is missing a substantial real cost that current shareholders bear in the form of dilution.

## 14.11 The statement of stockholders' equity

A formal statement that ties everything in this chapter together: the *Statement of Stockholders' Equity* (or Statement of Changes in Stockholders' Equity). This statement shows how each component of equity changed during the period — opening balances, plus issuances, plus net income, less dividends, plus or minus other changes (treasury stock movements, stock dividends, accumulated other comprehensive income), to closing balances.

The format is typically a multi-column matrix:

| | Common Stock | APIC | Retained Earnings | Treasury Stock | Total |
|---|---|---|---|---|---|
| Beginning balance | $X | $X | $X | $(X) | $X |
| Net income | | | $X | | $X |
| Dividends declared | | | $(X) | | $(X) |
| Stock issued | $X | $X | | | $X |
| Treasury stock purchased | | | | $(X) | $(X) |
| Ending balance | $X | $X | $X | $(X) | $X |

For a sole proprietorship, the analogous statement is the Statement of Owner's Equity from Chapter 2. For a corporation, the additional columns reflect the more complex equity structure.

The statement is the bridge between the income statement (which produces net income) and the balance sheet (which reports the resulting equity). It is the fourth-most-prominent of the standard four statements (after income statement, balance sheet, and cash flow statement) but is often the most informative for an analyst trying to understand changes in ownership claims, dilution from option exercises, and the timing of repurchases and dividends.

## 14.12 A note on disclosure for public companies

Public companies must disclose substantial detail about their equity structure in the notes to the financial statements: the number of shares authorized, issued, and outstanding for each class of stock; the par value; voting rights and other terms; details of any preferred-stock features; treasury stock activity; stock-based compensation expense; option-grant activity and outstanding option positions; share-repurchase programs.

The disclosure requirements have grown over the decades as the variety and sophistication of equity instruments has expanded. A modern 10-K's equity-section footnote is often dozens of pages — and reading it carefully is essential for any serious analysis of a company's capital structure and the dilution risk to current shareholders.

## 14.13 Why the corporate form dominates

A reflection. The corporate form, with all its accounting complexity, has become the dominant business structure for any business of meaningful size. The reasons are structural: limited liability, separability of ownership from management, transferability of ownership without disrupting operations, ability to raise capital from many anonymous investors, and indefinite life. None of these features exist for sole proprietorships or general partnerships in the same form.

The cost is the accounting and legal apparatus this chapter described. Stock issuance, treasury stock tracking, dividend mechanics, EPS computation, footnote disclosure, regulatory filings — all are overhead the corporate form imposes. For a small business, the overhead can outweigh the benefits; for a business above a certain size, the benefits dominate. Most U.S. businesses start as sole proprietorships or LLCs and convert to corporations when they grow past a threshold where the structural benefits become worth the accounting overhead.

The C corporation taxation regime — double taxation of corporate income at the entity level and again at the shareholder level when dividends are paid — is the major cost. The S corporation and LLC structures provide pass-through taxation while preserving most of the limited-liability benefit, and have become widely used for small and mid-sized businesses. The accounting at the entity level is similar to corporate accounting; the tax mechanics differ.

A quick comparison. A C corporation pays corporate income tax (at the federal rate of 21% as of 2024 plus state corporate tax) on its earnings, then shareholders pay individual income tax (or capital gains tax) on dividends received and on gains from selling shares. An S corporation passes income through to its shareholders directly; the entity itself pays no federal income tax. An LLC is tax-elected — by default a single-member LLC is taxed as a sole proprietorship, a multi-member LLC as a partnership, but either can elect corporate taxation if it makes sense.

## 14.15 Connections forward

Chapter 15 covers *partnership accounting* — the equity structure for businesses with multiple non-corporate owners. The mechanics differ from corporate equity in interesting ways: partner capital accounts, profit-and-loss-sharing agreements, partner admission and withdrawal, partnership liquidation. Chapter 16 then closes the book with the *Statement of Cash Flows* — pulling together everything from the previous fifteen chapters into the fourth and final core financial statement.
---

## LLM Exercise — Chapter 14: Corporation Accounting (AI Bookkeeping Tool Project)

**Project:** AI Bookkeeping Tool.
**What you're building this chapter:** the corporate-equity module — common stock, preferred stock, treasury stock, dividends (cash + stock + splits), retained earnings flow, EPS and book-value-per-share.
**Tool:** **Claude Code.**

---

**The Prompt:**

```
I'm in Chapter 14 of building my AI Bookkeeping Tool. This chapter
taught: corporations (separate legal entity, limited liability, can
issue stock); common stock (basic shareholder rights — vote, dividends
if declared, residual claim); preferred stock (cumulative or non-
cumulative dividends, often non-voting, ahead of common in
liquidation); treasury stock (the corporation's own stock repurchased
— contra-equity account; cost method most common); cash dividends
(declaration creates Dividends Payable; payment removes both);
stock dividends (small <25% at fair value, large >25% at par;
either way they redistribute equity, not reduce it); stock splits
(no journal entry, just memorandum); retained earnings (closes
income summary in; closes dividends out); EPS = (net income -
preferred dividends) / weighted average shares outstanding; BVPS =
common equity / common shares outstanding.

Extend the tool. Produce four outputs.

1. **A stock-issuance module.** Functions for:
   - `issue_common_stock(shares, par_value, issue_price, date)` —
     records Cash debit, Common Stock credit at par, Additional
     Paid-in Capital credit for excess.
   - `issue_preferred_stock(shares, par_value, issue_price, dividend_
     rate, cumulative_yn, date)` — similar.
   - Handle no-par stock (no APIC; all credited to Common Stock).
   - Handle stock issued for non-cash consideration (fair value of
     stock or the asset, whichever more reliable).

2. **A treasury-stock module.** Functions for:
   - `repurchase_treasury_stock(shares, price_per_share, date)` —
     records Treasury Stock debit (contra-equity), Cash credit.
   - `reissue_treasury_stock(shares, reissue_price, date)` — handles
     three cases: reissue at cost (no gain/loss); reissue above cost
     (credit APIC-Treasury); reissue below cost (debit APIC-Treasury
     to extent available, then Retained Earnings).
   - `retire_treasury_stock(shares, date)` — removes the shares
     permanently.

3. **A dividend module.** Functions for:
   - `declare_cash_dividend(amount_per_share, record_date, payment_
     date)` — debits Retained Earnings, credits Dividends Payable.
   - `pay_cash_dividend(payment_date)` — debits Dividends Payable,
     credits Cash.
   - `declare_stock_dividend(percentage, fair_value, date)` — small
     vs. large stock dividend handling.
   - `record_stock_split(ratio, date)` — memorandum entry only,
     updates outstanding share count.

4. **An EPS/BVPS calculator.** Functions for:
   - `compute_basic_eps(period)` — (net income - preferred dividends)
     / weighted average common shares.
   - `compute_book_value_per_share()` — common equity / common
     shares outstanding.

Tests for each — issuance at premium, treasury repurchase + reissue
above cost, cash + stock dividend, EPS with preferred outstanding.

Update spec.
```

---

**What this produces:** A corporate-equity module that handles stock, treasury, dividends, and the EPS/BVPS calculations.

**How to adapt this prompt:**

- *For your own project:* If your fictional business is a sole proprietorship or partnership, the corporate-equity module is forward-compatible — you can still build it for the case the business incorporates.
- *For ChatGPT / Gemini:* Works as written.
- *For Claude Code:* The right tool. Treasury-stock reissue is the most error-prone single feature (the three-case handling for reissue price); rigorous tests matter.
- *For a Claude Project:* Update spec.

**Connection to previous chapters:** Ch 5's closing entries are now extended — corporations close dividends to retained earnings, not to capital. The tool's close-period function should detect entity type and adjust.

**Preview of next chapter:** Chapter 15 adds the partnership module — partner capital accounts, profit-sharing, admission/withdrawal, liquidation. The other major entity form.


---

## AI Wayback Machine

**Catherine Schrand** was Wharton accounting researcher whose work on earnings management and corporate financial reporting shaped the field.

**Run this:**

```
Who is Catherine Schrand, and how does their work connect to corporation accounting we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Catherine Schrand"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to apply Catherine Schrand's ideas to a specific accounting question.
- Add a constraint: "Answer including criticisms or limits of Catherine Schrand's framework."

What changes? What gets better? What gets worse?
