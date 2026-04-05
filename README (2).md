# 📈 Retail Sales Performance Analysis

> An end-to-end business intelligence project analyzing **₹26.7 Lakh in sales** across 1,200 orders, 5 product categories, and 4 regions over 2 years — using Python, SQL, and professional data visualizations.

---

## 🚀 Project Overview

Every retail business needs to answer key questions:
- **Which region drives the most revenue?**
- **Which products are most profitable?**
- **Do discounts actually help or hurt profit?**
- **When is our peak sales season?**

This project answers all of these using real-world data analysis techniques.

---

## 🗂️ Project Structure

```
project2-sales-analysis/
│
├── data/
│   ├── sales_data.csv              ← 1,200 orders dataset
│   └── generate_data.py            ← Dataset generator
│
├── sql/
│   └── sales_queries.sql           ← 10 business SQL queries
│
├── visualizations/
│   ├── sales_dashboard.png         ← 6-panel KPI dashboard
│   └── quarterly_regional.png      ← Quarterly + heatmap charts
│
├── reports/
│   └── sales_executive_report.txt  ← Executive summary report
│
├── sales_analysis.py               ← Main Python script
├── requirements.txt
└── README.md
```

---

## 🛠️ Tools & Technologies

| Category | Tools |
|---|---|
| Language | Python 3.10+ |
| Data Analysis | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Database | SQL |
| Version Control | Git, GitHub |

---

## 📁 Dataset Description

| Column | Description |
|---|---|
| `OrderID` | Unique order identifier |
| `OrderDate` | Date of order (2022–2023) |
| `Region` | North / South / East / West |
| `Category` | Electronics / Clothing / Furniture / Food / Sports |
| `CustomerSegment` | Consumer / Corporate / Home Office |
| `ShipMode` | Shipping class |
| `Quantity` | Units ordered |
| `UnitPrice` | Price per unit |
| `Discount` | Discount applied (0–40%) |
| `Sales` | Final sale amount |
| `Profit` | Profit after costs |

---

## 📊 Key Business Findings

### 💰 Revenue KPIs
| Metric | Value |
|---|---|
| Total Revenue | ₹26,71,066 |
| Total Profit | ₹4,95,442 |
| Profit Margin | ~18.5% |
| Total Orders | 1,200 |
| Avg Order Value | ₹2,226 |

### 🔍 Top Insights
1. **Electronics** is the highest revenue category (30% of orders)
2. **North region** leads in total revenue
3. **Discounts above 20%** significantly reduce profitability
4. **Corporate segment** has the highest average order value
5. **Q4** is peak season — highest orders and revenue

### 💡 Business Recommendations
- Cap discounts at 20% — higher discounts hurt margins by 40%+
- Increase inventory and marketing budget before Q4
- Focus on Electronics + Corporate segment for maximum ROI
- Review Furniture pricing — lowest profit margin category

---

## ▶️ How to Run

```bash
git clone https://github.com/YOUR_USERNAME/project2-sales-analysis.git
cd project2-sales-analysis
pip install -r requirements.txt
python data/generate_data.py
python sales_analysis.py
```

---

## 🎯 Skills Demonstrated

- ✅ Business KPI Analysis
- ✅ Time Series / Trend Analysis
- ✅ Multi-dimensional Groupby Analysis
- ✅ SQL Business Queries
- ✅ Professional Dashboard Design
- ✅ Executive Reporting
- ✅ Discount Impact Analysis

---

## 👤 About Me

** Vanitha KP ** | Aspiring Data Analyst | Chennai, Tamil Nadu
- 📧vanithaperiyasamy13@gmail.com
- 💼 linkedin.com/in/vanitha-kp
- 🐙 [github.com/dataanalyst-pixel](https://github.com/dataanalyst-pixel)

⭐ **Star this repo if you found it useful!**
