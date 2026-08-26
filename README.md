# Workintech Data Science Bootcamp — Projects

A collection of exercises and mini-projects completed during the
[Workintech Data Science & Analytics Bootcamp](https://www.workintech.com.tr),
organized by skill area rather than by week. Each folder represents one
category from my [portfolio site](#) (link once live) — click into a
category to see the full notebook/deck behind the summary shown there.


## Structure

```
bootcamp-projects/
├── machine-learning/
│   └── Classification (PyCaret) and clustering (KMeans/DBSCAN) exercises
├── statistical-analysis/
│   └── Hypothesis testing and exploratory analysis
├── data-engineering-pipelines/
│   └── dbt, BigQuery, Fivetran, and REST API exercises
├── bi-visualization/
│   └── Power BI and Looker Studio dashboards
└── automation-version-control/
    └── Git/GitHub workflow and Zapier automation exercises
```

## Statistical Analysis: Olist E-Commerce Analytics

**Files:** `DAY_Olist.ipynb`, `Olist_Analysis_EN.pptx`

A hypothesis-driven analysis of the Olist Brazilian e-commerce dataset
(~99,000 orders, 2016–2018), covering four axes: product segmentation,
delivery time, payment behavior, and seller performance.

**Methods:** Pearson correlation, one-way ANOVA (α = 0.05)

**Key findings:**
- Delivery time has the strongest relationship with customer
  satisfaction (r = −0.30, p < 0.001)
- Installment count is moderately correlated with payment amount
  (r = 0.27, p < 0.001)
- Payment method shows statistical but not practical significance on
  satisfaction (ANOVA)
- Best-selling categories (by volume) and highest-revenue categories
  (by value) are largely disjoint — a segmentation insight with
  inventory/marketing implications

Full write-up, methodology notes, and all charts are in the notebook and
accompanying slide deck.

---

*Didem Arslan Yenihayat · Workintech Data Science & Analytics Bootcamp, 2026*
