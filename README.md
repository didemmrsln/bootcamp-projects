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
│   ├── algebra-warmup/           Linear algebra warm-up (NumPy)
│   ├── learning-curves/          Bias/variance and learning-curve diagnostics
│   ├── linear-regression/        Linear regression, cross-validation, tuning
│   ├── olist-order-features/     Feature engineering on Olist orders
│   └── real-estate-estimator/    Matrix-solved price estimator
├── statistical-analysis/
│   ├── DAY_Olist.ipynb           Olist hypothesis testing (see below)
│   ├── Olist_Analysis_EN.pdf
│   ├── exploratory-analysis/     EDA exercises
│   └── olist-database-analysis/  SQL/PostgreSQL analysis of the Olist database
├── data-engineering-pipelines/
│   ├── context-and-setup/        Olist data model and environment setup
│   ├── data-preparation/         Cleaning and preparation exercises
│   ├── gwz-sales/                GreenWeez sales query (BigQuery)
│   ├── gz-dbt-project/           dbt Cloud project scaffold
│   ├── olist-package/            Reusable Python package for loading Olist data
│   └── reviews-translator/       Review translation and theme analysis (API)
└── python-fundamentals/
    ├── distances/                Refactoring notebook code into modules
    ├── farming-animals/          OOP: inheritance and polymorphism
    └── farming-crops/            OOP: abstract base classes
```

Each subfolder keeps the README from the standalone repository it came from.

## Statistical Analysis: Olist E-Commerce Analytics

**Files:** `statistical-analysis/DAY_Olist.ipynb`, `statistical-analysis/Olist_Analysis_EN.pdf`

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
