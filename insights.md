# Insights & Business Takeaways
### ReadyNest Corp — Week 1 Data Analytics Task
**Dataset:** Retail Sales Dataset (1,000 transactions, Jan 2023 – Jan 2024)

---

### 1. Revenue is almost perfectly split across the three categories
**Electronics (₹1,56,905), Clothing (₹1,55,580), and Beauty (₹1,43,515)** each contribute
roughly a third of total revenue (₹4,56,000). There's no single dominant category —
all three are core to the business.
> **Action:** Don't deprioritize any category. Marketing budget should likely be split
> close to evenly, or weighted slightly toward Electronics/Clothing rather than concentrated
> in one area.

### 2. What customers buy matters far more than who they are
`price_per_unit` correlates strongly with `total_amount` (**0.85**), while `age`
correlates almost not at all (**-0.06**). Younger customers (18-25) do spend slightly more
on average (₹500) than older customers (56-64, ₹412), but the effect is small next to
the impact of product price itself.
> **Action:** Segment marketing by product/price tier, not primarily by customer age —
> age-based targeting will have limited payoff here.

### 3. May was the peak month; September was the slump
Monthly revenue peaked in **May 2023** and hit its lowest full-month point in
**September 2023**. There's no obvious single trend (steady growth or decline) — revenue
moves up and down month to month.
> **Action:** Investigate what happened in May (promotion? seasonal demand?) and
> in September (competitor activity? seasonal low?) to replicate wins and patch gaps.

### 4. Female customers contribute slightly more revenue, but the gap is narrow
**Female customers: ₹2,32,840 (510 transactions) vs Male: ₹2,23,160 (490 transactions)**.
The average transaction value is nearly identical between genders.
> **Action:** Gender isn't a strong differentiator for spend behavior here — campaigns
> aimed broadly at both genders are reasonable; no need for heavily gendered targeting.

### 5. Beauty has the highest average transaction value, despite lowest total revenue
Beauty has the highest **average transaction value (₹467.48)**, ahead of Electronics
(₹458.79) and Clothing (₹443.25) — even though its total revenue is the lowest of the
three (lower transaction volume, not lower value per sale).
> **Action:** Beauty could be a strong candidate for upselling/cross-selling campaigns,
> since each transaction already tends to be high-value — the opportunity is in
> increasing transaction *volume*, not basket size.

---

*Note: All figures generated from `scripts/02_eda.py`. Re-run the script against
`data/retail_sales_clean.csv` to reproduce these numbers.*
