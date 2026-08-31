# ⚡ Load-Shedding Business Cost Index 🇿🇦

> **A data analytics project investigating South Africa's load-shedding trends, seasonality, and estimated business impact from 2022–2025.**

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-SQLite-003B57?style=for-the-badge\&logo=sqlite\&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge\&logo=pandas\&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge\&logo=jupyter\&logoColor=white)
![Status](https://img.shields.io/badge/Status-Portfolio%20Project-2ea44f?style=for-the-badge)

**Author:** Diya Lakha
**Focus:** Data Analytics · SQL · Python · Business Intelligence

---

## 📊 Project Overview

Load-shedding has been one of South Africa's most persistent economic challenges, affecting households, employees, and businesses across the country.

This project explores the problem from a **data and business perspective**, asking three core questions:

1. **How has load-shedding severity changed from 2022 to 2025?**
2. **Is load-shedding actually worse during winter than summer?**
3. **What could this mean financially for a small business experiencing lost operating hours?**

The project builds a complete analytics pipeline:

**Raw Data → Python → SQLite → SQL Analysis → Pandas → Visualisation → Business Insights**

The result is a reproducible portfolio project demonstrating how technical data analysis can be translated into a business-focused narrative.

---

# 🔎 Key Findings

### Annual severity

| Year     | Average Stage | Hours Without Power | Estimated Business Cost |
| -------- | ------------: | ------------------: | ----------------------: |
| **2022** |          4.01 |           2,928 hrs |              R2,488,800 |
| **2023** |          4.81 |           3,508 hrs |              R2,981,800 |
| **2024** |          1.87 |           1,366 hrs |              R1,161,100 |
| **2025** |          1.28 |             932 hrs |                R792,200 |

### 📈 What the analysis shows

* **2023 was the most severe year** in the sample, with an average stage of **4.81** and approximately **3,508 hours without power**.
* Load-shedding severity **fell substantially from 2024 onward**, with average stage dropping to **1.87 in 2024** and **1.28 in 2025**.
* **Winter appears measurably worse than summer**, with an average stage of **3.77 during winter compared with 2.59 during summer** across the four-year period.
* Across the full sample, businesses could experience approximately **8,734 hours without power**.
* Using the project's adjustable cost assumption of **R850 per hour**, this represents an estimated **R7.4 million in cumulative lost revenue**.

> ⚠️ **Important:** These figures are generated from an **illustrative synthetic dataset**. They demonstrate the analytical pipeline and should not be interpreted as official Eskom statistics or measured business losses.

---

## 📉 Visual Insights

### Average Load-Shedding Stage by Year

![Average stage by year](outputs_avg_stage_by_year.png)

The yearly trend highlights the sharp increase in severity through 2023 followed by a substantial decline during 2024 and 2025.

### ☀️ Summer vs ❄️ Winter

![Seasonality](outputs_seasonality.png)

The seasonal analysis investigates whether the commonly held assumption that **winter load-shedding is worse** is supported by the data.

### 📈 Load-Shedding Trend

![Trend over time](outputs_trend.png)

The trend visualisation provides a more granular view of how load-shedding severity changed throughout the analysis period.

---

# 🧠 Business Question

The technical analysis is built around a simple business problem:

> **What does unreliable electricity mean for a small South African business?**

When electricity is unavailable, businesses can potentially experience:

* Payment and point-of-sale systems becoming unavailable
* Reduced customer traffic
* Interrupted productivity
* Equipment downtime
* Stock or food spoilage
* Employees being unable to perform normal tasks
* Reduced operating hours
* Additional costs associated with backup power

Rather than claiming these costs are directly observed, this project uses an **explicit modelling assumption** to estimate potential lost revenue.

### 💰 Cost Assumption

The model currently assumes:

```text
R850 lost revenue per hour without electricity
```

This value is intentionally configurable.

The calculation is:

```text
Estimated Business Cost =
Hours Without Power × Cost Per Hour
```

The assumption can be changed in:

```text
scripts/build_database.py
```

This makes it possible to model different business sizes or industries without changing the rest of the pipeline.

---

# 🗂️ About the Data

The current dataset is located at:

```text
data/eskom_stages.csv
```

### Synthetic dataset

The dataset used in this repository is **illustrative sample data** generated by:

```text
scripts/generate_sample_data.py
```

It is designed to approximate publicly reported national patterns, including:

* Higher severity during 2022–2023
* Particularly severe conditions during 2023
* Significant improvement during 2024–2025
* Higher severity during winter months

However, the **individual daily observations are synthetic**.

This distinction is important because the purpose of the project is to demonstrate the complete analytics workflow without depending on an external API from day one.

### 🔄 Moving to real data

The project includes an optional script for collecting live data:

```text
scripts/fetch_live_data.py
```

Real data can be collected through the **EskomSePush API**.

Once sufficient real-world historical data has been accumulated, the same database schema, SQL queries, and analysis notebook can be reused with minimal changes.

This separation between **data collection and analysis** is intentional and makes the project easier to extend.

---

# 🏗️ Project Architecture

```text
                         LOAD-SHEDDING ANALYTICS PIPELINE
                                      │
                                      ▼
                         ┌──────────────────────┐
                         │   Data Collection    │
                         │                      │
                         │ Synthetic / API Data │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │ Python + Pandas      │
                         │ Cleaning / Processing│
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │      SQLite          │
                         │    Data Storage      │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │         SQL          │
                         │ Analysis / Metrics   │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │ Python Visualisation │
                         │ Matplotlib / Seaborn │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │ Business Insights    │
                         │ & Cost Estimation    │
                         └──────────────────────┘
```

---

# 📁 Project Structure

```text
load-shedding-analytics/
│
├── data/
│   └── eskom_stages.csv
│       # Generated sample dataset
│
├── sql/
│   ├── schema.sql
│   │   # SQLite database schema
│   │
│   └── queries.sql
│       # Analytical SQL queries
│
├── scripts/
│   ├── generate_sample_data.py
│   │   # Generates the synthetic dataset
│   │
│   ├── fetch_live_data.py
│   │   # Optional EskomSePush API integration
│   │
│   └── build_database.py
│       # Loads data into SQLite and calculates
│       # estimated business costs
│
├── notebooks/
│   └── analysis.ipynb
│       # Main analysis, visualisations and narrative
│
├── requirements.txt
│   # Python dependencies
│
└── README.md
    # Project documentation
```

---

# 🛠️ Tech Stack

| Technology           | Purpose                                     |
| -------------------- | ------------------------------------------- |
| **Python**           | Data processing, analysis and visualisation |
| **Pandas**           | Data cleaning, transformation and analysis  |
| **Matplotlib**       | Data visualisation                          |
| **Seaborn**          | Statistical and analytical visualisation    |
| **SQLite**           | Lightweight relational database             |
| **SQL**              | Aggregation and analytical queries          |
| **Jupyter Notebook** | Exploratory analysis and storytelling       |
| **EskomSePush API**  | Optional real-world data source             |

---

# ⚙️ Getting Started

## 1. Clone the repository

```bash
git clone <your-repository-url>
cd load-shedding-analytics
```

## 2. Create a virtual environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### macOS / Linux

```bash
python -m venv venv
source venv/bin/activate
```

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 4. Generate the sample dataset

```bash
python scripts/generate_sample_data.py
```

This creates:

```text
data/eskom_stages.csv
```

## 5. Build the SQLite database

```bash
python scripts/build_database.py
```

This loads the dataset into SQLite and applies the business-cost calculation.

## 6. Run the analysis

Open:

```text
notebooks/analysis.ipynb
```

using either **Jupyter Notebook** or **VS Code**.

Run the notebook cells from top to bottom to reproduce the analysis and visualisations.

---

# 🧮 SQL Analysis

The project uses SQL to answer specific analytical questions rather than using SQL purely for data storage.

Examples include:

### Annual severity

```sql
SELECT
    year,
    AVG(stage) AS average_stage,
    SUM(hours_without_power) AS total_hours
FROM load_shedding
GROUP BY year
ORDER BY year;
```

### Seasonal comparison

The analysis categorises observations into **summer** and **winter** and compares average load-shedding severity between the two periods.

### Rolling trend

A SQL window function is used to calculate a **90-day rolling average**, helping smooth daily fluctuations and expose the underlying trend.

See:

```text
sql/queries.sql
```

for the complete analytical query set.

---

# 📊 Analytics Workflow

The project demonstrates a complete data analytics workflow:

### 1. Data Generation

Python creates a structured dataset representing daily load-shedding conditions.

### 2. Data Preparation

Pandas is used for cleaning, transforming and preparing the data for analysis.

### 3. Database Construction

The cleaned data is loaded into a SQLite database.

### 4. SQL Analysis

SQL is used to calculate:

* Annual averages
* Total hours without electricity
* Seasonal averages
* Business cost estimates
* Rolling averages
* Trend metrics

### 5. Visualisation

The SQL outputs are brought back into Python for visual analysis using Matplotlib and Seaborn.

### 6. Data Storytelling

The final notebook turns the analytical results into a business-focused narrative.

---

# 🎯 Skills Demonstrated

## SQL

* `SELECT` and filtering
* Aggregation
* `GROUP BY`
* `CASE` expressions
* Date-based analysis
* Window functions
* 90-day rolling averages
* Business metric calculations

## Python

* Pandas
* Data cleaning
* Data transformation
* Data generation
* Data reshaping
* Joining analytical results
* Reproducible analysis

## Data Visualisation

* Matplotlib
* Seaborn
* Trend analysis
* Seasonal comparisons
* Business-focused charts
* Visual storytelling

## Data Analytics

* Exploratory data analysis
* KPI development
* Time-series analysis
* Seasonality analysis
* Business impact modelling
* Assumption-driven analysis

## Data Ethics & Quality

A major focus of the project is **transparency around data quality**.

The repository clearly distinguishes between:

```text
Synthetic Data
      ↓
Demonstration / Development
```

and:

```text
Real Data
      ↓
Production-quality Analysis
```

This prevents synthetic observations from being presented as official measurements.

---

# 🚀 Future Improvements

The project is designed to grow beyond the initial analysis.

### 🔌 Real historical data

Replace the synthetic dataset with accumulated real-world EskomSePush data.

### 📊 Interactive dashboard

Build a Power BI or Tableau dashboard on top of the SQLite dataset.

Potential dashboard filters could include:

* Year
* Month
* Season
* Load-shedding stage
* Estimated business cost

### 🗺️ Geographic analysis

Expand the dataset from national-level analysis to:

* Provinces
* Municipalities
* Metropolitan areas

This could reveal whether certain regions experience disproportionately high impacts.

### 📐 Statistical testing

Add statistical tests to determine whether the observed winter/summer difference is statistically significant.

For example:

```text
Winter vs Summer
        ↓
Hypothesis Test
        ↓
Statistical Significance
```

### 💼 Industry-specific cost modelling

Instead of a single R850/hour assumption, create configurable models for different business types such as:

* Retail
* Restaurants
* Small offices
* Professional services
* Hospitality

This would provide a more realistic estimate of economic impact.

---

# 💡 Why This Project Matters

This project demonstrates that data analytics is not simply about producing charts.

The goal is to move from:

> **"Load-shedding is bad."**

to:

> **"How severe has it actually been, when is it worst, how has it changed over time, and what could that mean financially for a business?"**

That shift from **raw data → measurable evidence → business insight** is the core purpose of this project.

---

# ⚠️ Data & Methodology Disclaimer

This repository is a **portfolio analytics project** and should not be interpreted as an official economic assessment of South African load-shedding.

In particular:

* The current daily dataset is synthetic.
* The annual and seasonal figures are therefore illustrative.
* The R850/hour business cost is an adjustable modelling assumption.
* Estimated lost revenue does not represent independently measured business losses.
* Real-world analysis should use validated historical load-shedding data and sector-specific financial assumptions.

The project is intentionally transparent about these limitations so that the analytical methodology can be evaluated independently from the current data source.

---

# 📌 Possible Research Questions

The pipeline can also be extended to investigate questions such as:

* Was 2023 statistically different from 2022?
* How much did load-shedding improve between 2023 and 2025?
* Is winter consistently worse every year?
* Which months contribute the highest estimated business losses?
* How sensitive are cost estimates to the R850/hour assumption?
* Which industries would be most vulnerable to prolonged outages?
* Does load-shedding severity show long-term seasonal patterns?

---

# 👩‍💻 Author

**Diya Lakha**

Computer Science student interested in:

**Data Analytics · Software Development · SQL · Python · Business Intelligence**

This project was developed as part of a personal portfolio to demonstrate practical data analytics skills, from data preparation and SQL querying through to visualisation and business storytelling.

---


