# Chapter 8 — Fraud, Internal Controls, and Cash

## 8.1 Opening: The asset that walks out the door

Every asset on a company's balance sheet has some level of vulnerability to misappropriation. Inventory can be stolen, but inventory leaves a paper trail — bills of lading, receiving reports, physical counts. Equipment can be stolen, but equipment is heavy, registered, and noticeable when missing. Accounts receivable can be manipulated, but most fraud schemes against AR require collusion across multiple roles.

Cash is different. Cash is fungible, untraceable once it leaves the till, accepted everywhere, and present in volume in nearly every business. The Association of Certified Fraud Examiners has reported, year after year, that cash misappropriation is the most common single category of occupational fraud, even though cash represents a small fraction of any modern company's total assets. The fraudster's question is never *which asset is most valuable* but *which asset can I take without getting caught*. Cash, more than any other asset, answers that question.

This chapter is about the controls that protect cash specifically and the broader system of internal controls that protect every asset and every record. By the end of it, you should be able to:

- Define *fraud* in the accounting sense (intentional deception for financial gain), and identify the three legs of the *fraud triangle* (pressure, opportunity, rationalization).
- Explain the role of the Sarbanes-Oxley Act of 2002 and the COSO framework in setting the U.S. internal-control standard.
- Identify the five components of an internal control system: control environment, risk assessment, control activities, information and communication, monitoring.
- Apply the principles of internal control specifically to cash receipts and cash disbursements.
- Prepare a *bank reconciliation* — the period-end procedure that reconciles the company's cash records against the bank's records and surfaces errors and missing transactions.
- Set up and operate a *petty cash imprest fund* with appropriate journal entries.

You walk in with the AIS architecture from Chapter 7. You walk out knowing how the controls inside that architecture protect the asset most often targeted by fraud.

## 8.2 Fraud and the three pressures that produce it

Fraud, in the accounting context, is intentional deception for financial gain — distinct from honest error, which is unintentional. Auditors and fraud examiners use the *fraud triangle* model, popularized by criminologist Donald Cressey, to describe the conditions under which fraud occurs. Three legs:

*Pressure* — the financial or psychological motivation that pushes someone toward fraud. Personal debt. Gambling losses. A medical emergency. Living beyond means. A spouse's unemployment. The pressure is usually private and not visible to the employer.

*Opportunity* — the access and absence of oversight that lets the fraud actually happen. A bookkeeper who can both write checks and reconcile the bank statement has opportunity. A cashier who can void transactions without supervisor approval has opportunity. A manager who can approve their own expense reimbursements has opportunity. Internal controls are aimed at this leg of the triangle — pressure and rationalization are private and hard to see; opportunity is structural and *can* be removed.

*Rationalization* — the story the fraudster tells themselves to make the act feel acceptable. *I'm just borrowing it; I'll pay it back. The company owes me; they didn't give me the raise I deserved. Everyone does it. They'll never miss it.* The rationalizations are predictable but powerful — they let an otherwise honest person commit the crime.

The implication for a company designing controls: removing opportunity is the only one of the three legs the company can directly act on. Controls cannot reduce employees' personal financial pressure or change how they rationalize. Controls *can* remove the structural opportunity to commit fraud without detection.

## 8.3 Sarbanes-Oxley and the COSO framework

The Enron, WorldCom, and Tyco scandals of 2001-2002 made clear that public-company management could, in some cases, override the very internal controls their audited financial statements claimed were in place. Congress responded with the Sarbanes-Oxley Act of 2002 (SOX), which we met briefly in Chapter 1. Several SOX provisions directly affect internal controls:

*Section 302* requires the CEO and CFO of a public company to personally certify, in each periodic filing, that they have reviewed the report, that the financial statements fairly present the company's position, and that they have established and maintained internal controls. False certification carries criminal penalties.

*Section 404* requires public companies to include in their annual report a management assessment of the effectiveness of internal controls over financial reporting, plus an independent auditor's attestation of management's assessment. This was the most operationally consequential SOX provision — it forced public companies to document, test, and remediate their controls in a way that previously had been left to internal judgment.

*Section 906* extended criminal penalties for false certifications.

The Public Company Accounting Oversight Board (PCAOB) — also created by SOX — sets auditing standards for the firms that audit public companies and inspects their work.

The framework most U.S. companies use to structure their internal controls is the *COSO Internal Control — Integrated Framework*, originally published in 1992 by the Committee of Sponsoring Organizations of the Treadway Commission and substantially updated in 2013. COSO names five components of any internal control system:

*Control environment* — the tone at the top. Management's commitment to integrity, ethical values, board oversight, organizational structure, accountability. Without a control environment that takes integrity seriously, the rest of the components are paperwork.

*Risk assessment* — identifying and analyzing the risks that could affect the achievement of the organization's objectives. Different industries face different risks; controls should be calibrated to the actual risks the company faces.

*Control activities* — the policies and procedures that mitigate identified risks. Segregation of duties, authorizations, approvals, verifications, reconciliations, physical controls. The bulk of what most accountants think of as "internal controls" lives here.

*Information and communication* — the systems that capture and exchange the information needed to operate controls. The accounting information system from Chapter 7 sits here.

*Monitoring* — ongoing evaluation of whether the controls are operating as designed. Internal audit is a major mechanism. Without monitoring, controls degrade over time as the organization changes around them.

The five components are interdependent. A company with strong control activities but a weak control environment will see its activities undermined by management override. A company with strong monitoring but no risk assessment will be testing the wrong things.

## 8.4 The principles of internal control applied to cash

Seven principles of internal control, as commonly taught:

1. **Establishment of responsibility** — assign each task to a specific person, so accountability is clear.
2. **Segregation of duties** — no single person should both authorize a transaction, record it, and have custody of the related asset.
3. **Documentation procedures** — every transaction generates a paper trail that can be audited.
4. **Physical controls** — safes, locks, security cameras, controlled access to inventory and cash.
5. **Independent internal verification** — someone who didn't perform the transaction reviews it independently.
6. **Human resource controls** — bonding, background checks, vacation requirements, rotation of duties.
7. **Technology controls** — passwords, encryption, system logs, automated edit checks.

Applied specifically to cash:

*Cash receipts*. The principle of segregation says that the person who *receives* cash should not be the person who *records* the cash receipt or *reconciles* the bank statement. In a small business, this is hard — a single bookkeeper often does all three. The mitigations: external review (a CPA reviews the books quarterly), surprise audits (the owner pulls a sample of cash transactions monthly), bonding (the bookkeeper is insured for losses up to a stated amount), and mandatory vacations (a fraud that requires daily attention is exposed when the perpetrator is away). A medium-sized business should have separate cashiers, accounts-receivable clerks, and bank-reconciliation personnel.

*Cash disbursements*. Disbursements should be by pre-numbered check or electronic transfer, with supporting documentation (vendor invoice, purchase order, receiving report) verified before payment. The person authorizing the payment should not be the person preparing the check. The person preparing the check should not be the person reconciling the bank account. Voided checks should be retained, marked void, with the signature line cut out. Bank statements should be opened by someone independent of cash handling.

The structural rule in both directions: *the same person should never be in a position to commit a fraud and to conceal it from the records*. Removing that combination is the single highest-leverage control.

## 8.5 Bank reconciliation

The most important monthly control over cash is the *bank reconciliation* — the procedure that compares the company's records of cash to the bank's records and explains any difference. If the controls are working, the difference is small and explainable; if the controls are failing, the difference is large or unexplainable, and that's the early warning.

The two records typically don't match for innocent reasons:

- *Outstanding checks* — checks the company has issued and recorded, but the recipients haven't yet cashed.
- *Deposits in transit* — deposits the company has recorded but the bank hasn't yet processed.
- *Bank service charges* — fees the bank has charged but the company hasn't yet recorded.
- *NSF (non-sufficient funds) checks* — customer payments that bounced.
- *Bank-collected items* — notes the bank collected on the company's behalf and credited.
- *Errors* — by the bank, or by the company.

The reconciliation reconciles both sides toward a single corrected cash balance. The standard format:

```
Bank balance per statement                $X
+ Deposits in transit                     +
- Outstanding checks                      -
± Bank errors                             ±
                                         ---
Adjusted bank balance                     $Y

Book balance per company records          $A
+ Notes collected by bank                 +
- Bank service charges                    -
- NSF checks                              -
± Book errors                             ±
                                         ---
Adjusted book balance                     $Y
```

The two adjusted balances should equal each other. If they don't, an unreconciled item remains — usually a recording error. The book-side adjustments require *journal entries* to bring the company's books current; the bank-side adjustments are timing items that will resolve naturally as outstanding checks clear and deposits in transit get processed.

A worked example. Suppose at June 30 the company's books show a Cash balance of $4,250. The bank statement shows a balance of $4,860. Investigation reveals:

- Outstanding checks: $700 (issued and recorded by the company; not yet cleared the bank)
- Deposits in transit: $200 (received and recorded by the company; not yet credited by the bank)
- Bank service charge: $15 (debited by bank; not yet recorded by company)
- NSF check from a customer: $125 (returned by the bank; not yet adjusted on company's books)
- Note collected by bank for the company: $250 (credited by bank; not yet recorded by company)

```
Bank balance                              $4,860
+ Deposits in transit                       +200
- Outstanding checks                        -700
                                          ------
Adjusted bank balance                     $4,360

Book balance                              $4,250
+ Note collected                            +250
- Service charge                             -15
- NSF check                                 -125
                                          ------
Adjusted book balance                     $4,360
```

Both sides agree at $4,360. Two journal entries bring the books to that figure:

| Account | Debit | Credit |
|---|---|---|
| Cash | $250 | |
| Notes Receivable (or Interest Revenue) | | $250 |

| Account | Debit | Credit |
|---|---|---|
| Bank Service Expense | $15 | |
| Accounts Receivable | $125 | |
| Cash | | $140 |

After posting these, Cash on the company's books equals $4,360, matching the reconciled bank balance.

## 8.6 Petty cash imprest funds

Some legitimate cash payments are too small to justify a check (a $4 stamp, a $12 office snack, a $20 cab fare for an out-of-town vendor). The standard control mechanism is a *petty cash imprest fund* — a small fund of cash, kept locked, with a designated custodian, replenished only by check.

Setup: write a check for, say, $200, made payable to "Petty Cash" or to the custodian. Cash the check, put the $200 in the locked box.

| Account | Debit | Credit |
|---|---|---|
| Petty Cash | $200 | |
| Cash | | $200 |

Operation: when an employee needs petty cash, the custodian disburses against a signed petty-cash voucher that records the date, amount, purpose, and recipient. The voucher goes in the box as a substitute for the cash. At all times, the cash plus the vouchers should total $200.

Replenishment: when the cash gets low (say down to $40), the custodian gathers the vouchers ($160 worth, in this case) and submits them for reimbursement. A check is written for $160 to bring the cash back to $200. The journal entry distributes the expenses across the appropriate accounts:

| Account | Debit | Credit |
|---|---|---|
| Office Supplies Expense | $50 | |
| Postage Expense | $30 | |
| Travel Expense | $80 | |
| Cash | | $160 |

The Petty Cash account itself doesn't move during replenishment — it stays at $200, the *imprest* (Latin: "advance, loan") amount. Only when the fund's authorized total is changed (raising it to $300 or shrinking it to $100) does the Petty Cash account itself adjust.

The control logic: at any moment, an auditor can count the cash in the box, sum the vouchers, and verify the imprest amount. The custodian cannot conceal misappropriation by simply taking cash, because the cash + vouchers equation must hold. Replenishment requires submitting all vouchers to a different person, who reviews them before issuing the replenishment check. Segregation of duties is enforced through the imprest mechanism.

## 8.7 Exercises

### Warm-up

1. **Name the three legs of the fraud triangle** and identify which leg internal controls primarily target.

2. **Name the five components of the COSO Internal Control — Integrated Framework.**

3. **Why is segregation of duties more important for cash than for, say, vehicles or buildings?**

### Application

4. **A small business has one bookkeeper who opens incoming mail (including customer payments), records cash receipts, and reconciles the bank statement.** Identify the segregation-of-duties violation and propose at least three mitigations the owner could implement.

5. **A company's June 30 bank statement shows $12,200; the company's books show $11,400. Outstanding checks total $1,150; deposits in transit total $400; bank charged $25 service fee not yet recorded; bank collected a $75 note for the company.** Prepare the bank reconciliation and the journal entries to update the books.

6. **A petty cash fund of $300 has $42 cash remaining and vouchers for $80 supplies, $60 postage, $115 travel, and $5 in unaccountable shortage.** Prepare the replenishment journal entry.

### Synthesis

7. **A new CFO at a mid-sized company discovers that the company has documented internal controls but the documentation hasn't been updated in three years. Several of the people named in the documentation have left the company.** Walk through what's wrong with this situation in COSO-framework terms, and propose what the CFO should do first.

8. **The Madoff scheme operated for decades while clients received apparently routine account statements.** Explain, drawing on this chapter and Chapter 1, what specific internal controls Madoff's clients (and the SEC) lacked that allowed the fraud to persist.

### Challenge

9. **A grocery store chain's cashiers are required to take their two-week vacation as a single block.** Why might this seemingly trivial HR policy be one of the most effective internal controls a cash-intensive business can implement?

10. **Sarbanes-Oxley imposed substantial compliance costs on public companies.** Discuss whether the costs are justified by the benefit. This question has no clean answer — the value is in the analysis. Reference at least two specific SOX provisions and what gap each was designed to close.

## 8.8 Chapter summary

You walked into this chapter knowing that internal controls existed. You walk out knowing what they look like in practice and why cash is the asset that demands the most protection.

Fraud requires pressure, opportunity, and rationalization. Internal controls remove opportunity, the only leg the company can directly act on. The Sarbanes-Oxley Act of 2002 codified internal-control documentation, testing, and management certification for public companies after the Enron/WorldCom/Tyco scandals; the COSO framework defines the five-component structure most U.S. organizations use.

Seven principles — establishment of responsibility, segregation of duties, documentation, physical controls, independent verification, HR controls, technology controls — apply to every asset class but apply most rigorously to cash. The bank reconciliation is the monthly procedure that compares the company's cash records to the bank's and surfaces errors. The petty cash imprest fund is the mechanism that handles small cash disbursements without circumventing controls.

The single most important idea: the same person should never be in a position to commit a fraud *and* conceal it from the records. Every other control follows from this principle.

The common mistake to watch for: assuming controls are about catching fraudsters. The deeper purpose is making fraud structurally impossible for honest people to commit even under personal pressure. Most occupational fraud is committed by employees who would not have stolen from a former employer with stricter controls.

## 8.9 The cash equivalents line and what counts

A practical detail that surprises students: on a balance sheet, "Cash" is rarely just the currency in the till. The line is usually labeled *Cash and cash equivalents*, and its definition matters for both reporting and analysis.

Cash, narrowly, includes coin and currency on hand, demand deposits at banks (checking accounts), and savings accounts immediately accessible. *Cash equivalents* are short-term, highly liquid investments that are readily convertible to known amounts of cash and are so near maturity that they present insignificant risk of changes in value due to interest-rate movements. The standard threshold is investments with original maturities of three months or less when the company acquired them — Treasury bills, commercial paper, money-market instruments. A six-month CD purchased six weeks ago is *not* a cash equivalent (the original maturity was six months); a three-month T-bill purchased two weeks ago *is*.

The classification matters because cash and cash equivalents drive every short-term liquidity ratio (current ratio, quick ratio) and the cash flow statement's beginning and ending balances. Stretching the definition to include longer-dated investments inflates apparent liquidity and is one of the things auditors check carefully.

Restricted cash — cash that the company holds but is contractually required to use for a specific purpose (a sinking fund for bond repayment, a deposit held against a lease, escrowed cash awaiting a closing) — is *not* cash and cash equivalents in the analytical sense. Restricted cash is typically reported separately on the balance sheet and is not available for general operating use. Including restricted cash in the unrestricted cash line is misleading and is one of the common manipulations regulators flag.

These distinctions matter for the bank reconciliation as well — the procedure reconciles only the unrestricted operating cash accounts. Restricted accounts are reconciled separately, often less frequently, with their own controls.

## 8.10 A note on bonding, vacations, and small-business reality

The principles in §8.4 read clean in textbook form. In a five-person business, applying them straight is impossible. The bookkeeper *is* the entire accounting function. Segregation of duties cannot be enforced by giving the same person three different roles. The owner is often too busy running the business to provide independent verification at the level the principles ask for.

Three real-world mitigations make small-business cash controls workable.

*Bonding* — purchasing fidelity insurance that covers losses from employee dishonesty. The bonding company underwrites the employees, in effect — they run a background check, set a coverage level, and reimburse the company for documented theft up to the policy limit. A bonded bookkeeper is statistically less likely to commit fraud (bonding companies decline applications they consider risky) and the company is financially protected if fraud occurs anyway.

*Mandatory vacations* — requiring every employee in a sensitive cash role to take their full annual leave as a continuous block, during which someone else handles the duties. This is one of the most underrated controls for small organizations. Many fraud schemes require continuous attention from the perpetrator (intercepting bank statements, modifying records before they're reviewed, rolling over a kiting scheme). A two-week absence breaks the loop. Several large frauds in the historical record have unraveled the moment the perpetrator was forced to take time off; the temporary replacement noticed the inconsistencies.

*External review* — engaging an outside CPA quarterly or annually to perform agreed-upon procedures: pulling a sample of transactions, reviewing bank reconciliations, reviewing the petty cash log, comparing year-over-year ratios for unexpected shifts. This is not an audit (which is more comprehensive and more expensive) but a periodic external set of eyes that the in-house bookkeeper knows is coming. The deterrent effect is substantial.

For small businesses, the realistic control architecture is bonding, mandatory vacations, and external review — applied in combination, they substitute for the segregation of duties that a small headcount cannot support directly.

## 8.11 Connections forward

Chapter 9 turns to *accounting for receivables* — the asset class that captures money customers owe the company. You'll see how accounts receivable get recorded, how the company estimates uncollectible accounts, and how notes receivable (more formal IOUs with interest) differ from ordinary trade receivables. The cash control disciplines from this chapter remain in the background; receivables are essentially future cash that hasn't arrived yet, and they need their own protections.
---

## LLM Exercise — Chapter 8: Fraud, Internal Controls, and Cash (AI Bookkeeping Tool Project)

**Project:** AI Bookkeeping Tool.
**What you're building this chapter:** internal-control features (audit log, role-based actions, segregation-of-duties flags), bank reconciliation, petty-cash imprest fund management.
**Tool:** **Claude Code.**

---

**The Prompt:**

```
I'm in Chapter 8 of building my AI Bookkeeping Tool. The tool now
has special journals and subsidiary ledgers. This chapter taught:
the fraud triangle (pressure + opportunity + rationalization);
Sarbanes-Oxley and the COSO framework for internal controls;
the five internal-control principles (control environment, risk
assessment, control activities, information/communication,
monitoring); the principles of internal control applied to cash
(segregation of duties, authorization, documentation, physical
controls, independent verification); bank reconciliation (book
balance + deposits in transit - outstanding checks +/- bank
errors and adjustments = adjusted balance); petty cash imprest
funds (fund maintained at fixed amount; replenished by recording
expenses, not by debit to petty cash).

Extend the tool. Produce four outputs.

1. **An audit log.** Every transaction posting gets a log entry
   containing:
   - Timestamp.
   - User identifier.
   - Action (post, edit, void).
   - Affected accounts.
   - Before-and-after values for edits.
   The log is append-only; entries cannot be edited or deleted
   from within the application.

2. **Role-based actions and segregation flags.** Add minimal
   role support:
   - "Recorder" can post journal entries.
   - "Reviewer" can approve entries but not post.
   - "Manager" can post AND approve, but the audit log flags
     this as a segregation-of-duties violation that should be
     reviewed.
   Edge case: in a one-person shop, segregation is impossible;
   the tool should flag this honestly rather than pretend.

3. **A bank-reconciliation module.** Given:
   - The book balance from the cash account on a date.
   - The bank statement balance on the same date.
   - A list of deposits in transit, outstanding checks, bank
     errors, NSF checks, service charges, interest.
   The module produces an adjusted-balance reconciliation that:
   - Computes the adjusted book balance.
   - Computes the adjusted bank balance.
   - Asserts they match (raise error if not).
   - Generates the journal entries needed to bring the book
     balance to the adjusted balance.

4. **A petty-cash module.** Functions to:
   - Establish a petty cash fund (debit Petty Cash, credit Cash).
   - Replenish the fund (debit appropriate expense accounts,
     credit Cash — does NOT touch Petty Cash, which stays at its
     imprest level).
   - Adjust the fund size up or down (debit or credit Petty Cash,
     opposite Cash).

Tests for each. Update spec.
```

---

**What this produces:** Internal-control features that elevate the tool from "calculator" toward "production-ready." Bank reconciliation is the most operationally consequential addition — it's the routine that catches almost all cash errors.

**How to adapt this prompt:**

- *For your own project:* The role-based actions are aspirational for a single-user tool. Build them anyway — they document the segregation-of-duties principle and serve as a reminder of which functions should NOT be combined.
- *For ChatGPT / Gemini:* Works as written.
- *For Claude Code:* The right tool. The bank-reconciliation module benefits from concrete test data (a real or realistic bank statement and check register).
- *For a Claude Project:* Update spec.

**Connection to previous chapters:** Ch 3 built the journal-entry engine; Ch 8 hardens it against errors and fraud.

**Preview of next chapter:** Chapter 9 adds the receivables module — allowance-for-doubtful-accounts, two methods of estimating uncollectibles, notes receivable with interest, factoring.


---

## AI Wayback Machine

**Harry Markopolos** was forensic accountant who warned the SEC about Bernie Madoff for years before the Ponzi scheme collapsed.

**Run this:**

```
Who is Harry Markopolos, and how does their work connect to fraud and controls we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Harry Markopolos"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to apply Harry Markopolos's ideas to a specific accounting question.
- Add a constraint: "Answer including criticisms or limits of Harry Markopolos's framework."

What changes? What gets better? What gets worse?
