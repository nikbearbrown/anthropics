# Source Details — financial-services--claude-liam-dcf-model

Generated: 2026-09-05T11:09:00

## Reel
- Question: Claude, Dcf Model.
- Family: financial-services
- Source sheet: /Users/nik/Documents/books/anthropics/financial-services/youtube/claude-liam-dcf-model/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/financial-services/plugins/agent-plugins/model-builder/skills/dcf-model/SKILL.md
- Name: dcf-model
- Description: Real DCF (Discounted Cash Flow) model creation for equity valuation. Retrieves financial data from SEC filings and analyst reports, builds comprehensive cash flow projections with proper WACC calculations, performs sensitivity analysis, and outputs professional Excel models with executive summaries. Use when users need to value a company using DCF methodology, request intrinsic value analysis, or ask for detailed financial modeling with growth projections and terminal value calculations.

## Capabilities To Name On Screen
- Default to using all of the information provided by the user and MCP servers available for data sourcing.

## Constraints / Failure Modes
- If running inside Excel (Office Add-in / Office JS environment): Use Office JS directly — do NOT use Python/openpyxl. Write formulas via range.formulas =…
- ⚠️ Office JS merged cell pitfall: When building section headers with merged cells, do NOT call .merge() then set .values on the merged range — Office JS still reports…
- Every projection, margin, discount factor, PV, and sensitivity cell MUST be a live Excel formula — never a value computed in Python and written as a number
- The only hardcoded numbers permitted are: (1) raw historical inputs, (2) assumption drivers (growth rates, WACC inputs, terminal g), (3) current market data (share…
- If you catch yourself computing something in Python and writing the result — STOP. The model must flex when the user changes an assumption
- Verify Step-by-Step With the User (DO NOT build end-to-end):
- Center cell = base case. Build the axis values so the middle row header and middle column header exactly equal the model's actual assumptions (e.g., if base WACC = 9.0%…
- NO placeholder text, NO linear approximations, NO manual steps required

## Procedure / Sequence
- Data Retrieval and Validation: Fetch data from MCP servers, user provided data, and the web. Data Sources Priority: 1. MCP Servers (if configured)…
- Historical Analysis (3-5 years): Analyze and document: - Revenue growth trends: Calculate CAGR, identify drivers - Margin progression: Track gross…
- Build Revenue Projections: Methodology: 1. Start with latest actual revenue (LTM or most recent fiscal year) 2. Apply growth rates for each…
- Operating Expense Modeling: Fixed/Variable Cost Analysis: Operating expenses should model realistic operating leverage: - Sales & Marketing…
- Free Cash Flow Calculation: Build FCF in proper sequence: Working Capital Modeling: - Calculate as % of revenue change (delta revenue) - Typical…
- Cost of Capital (WACC) Research: CAPM Methodology for Cost of Equity: Cost of Debt Calculation: Capital Structure Weights: Special Cases: - Net Cash…
- Discount Rate Application (5-10 Year Forecast): Mid-Year Convention: - Cash flows assumed to occur mid-year - Discount Period: 0.5, 1.5, 2.5, 3.5, 4.5, etc. - Discount…
- Terminal Value Calculation: Perpetuity Growth Method (Preferred): Terminal Growth Rate Selection: - Conservative: 2.0-2.5% (GDP growth rate)…

## Supporting Files And Signals
- Referenced: range.formulas = [["=D19*(1+$B$8)"]]
- Referenced: range.format.*
- Referenced: .formulas
- Referenced: .values
- Referenced: recalc.py
- Referenced: .merge()
- Referenced: ws["D20"] = "=D19*(1+$B$8)"
- Referenced: ws["D20"] = calculated_revenue
- Referenced: python recalc.py model.xlsx 30
- Referenced: =IF($B$6=1,[Bear cell],IF($B$6=2,[Base cell],[Bull cell]))
- Signal: code block: js
- Signal: code block: csv
- Signal: code block: python
- Signal: code block: bash
- Signal: code block: json

## Source Sections
- Overview
- Tools
- Critical Constraints - Read These First
- DCF Process Workflow
- Step 1: Data Retrieval and Validation
- Step 2: Historical Analysis (3-5 years)
- Step 3: Build Revenue Projections
- Step 4: Operating Expense Modeling
- Step 5: Free Cash Flow Calculation
- Step 6: Cost of Capital (WACC) Research

## Batch Log Match
- Row: 190
- Canonical path: anthropics/financial-services/plugins/agent-plugins/model-builder/skills/dcf-model/SKILL.md
- MP4 path: anthropics/financial-services/youtube/claude-liam-dcf-model/mp4/claude-liam-dcf-model.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.
