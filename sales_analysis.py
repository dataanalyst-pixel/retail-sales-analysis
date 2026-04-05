# ============================================================
#  PROJECT 2: Retail Sales Performance Analysis
#  Author : [Your Name]
#  Tools  : Python | Pandas | Matplotlib | Seaborn | SQL
#  Dataset: 1,200 Orders | 2022–2023 | 5 Product Categories
# ============================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

import matplotlib
matplotlib.use('Agg')

# ── Style ─────────────────────────────────────────────────────
sns.set_theme(style="whitegrid")
PALETTE = ["#2C3E50","#E74C3C","#3498DB","#2ECC71","#F39C12"]
plt.rcParams.update({'figure.dpi': 150, 'font.family': 'DejaVu Sans'})

# ── 1. LOAD & CLEAN ───────────────────────────────────────────
print("=" * 60)
print("   RETAIL SALES PERFORMANCE ANALYSIS — 2022 to 2023")
print("=" * 60)

df = pd.read_csv("data/sales_data.csv", parse_dates=['OrderDate'])
print(f"\n✅ Loaded {df.shape[0]:,} orders × {df.shape[1]} columns")
print(f"   Date Range : {df['OrderDate'].min().date()} → {df['OrderDate'].max().date()}")
print(f"   Null Values: {df.isnull().sum().sum()}")

# ── 2. KEY METRICS ────────────────────────────────────────────
total_sales    = df['Sales'].sum()
total_profit   = df['Profit'].sum()
profit_margin  = (total_profit / total_sales) * 100
total_orders   = len(df)
avg_order_val  = df['Sales'].mean()
total_qty      = df['Quantity'].sum()

print(f"\n{'─'*45}")
print("📌 BUSINESS KPIs")
print(f"{'─'*45}")
print(f"  Total Revenue    : ₹{total_sales:>12,.2f}")
print(f"  Total Profit     : ₹{total_profit:>12,.2f}")
print(f"  Profit Margin    : {profit_margin:>11.1f}%")
print(f"  Total Orders     : {total_orders:>12,}")
print(f"  Avg Order Value  : ₹{avg_order_val:>12,.2f}")
print(f"  Units Sold       : {total_qty:>12,}")

# ── 3. ANALYSIS BREAKDOWNS ───────────────────────────────────
print(f"\n{'─'*45}")
print("📊 SALES BY REGION")
region_df = df.groupby('Region').agg(
    Sales=('Sales','sum'), Profit=('Profit','sum'), Orders=('OrderID','count')
).round(2).sort_values('Sales', ascending=False)
region_df['Margin%'] = (region_df['Profit']/region_df['Sales']*100).round(1)
print(region_df)

print(f"\n{'─'*45}")
print("📦 SALES BY CATEGORY")
cat_df = df.groupby('Category').agg(
    Sales=('Sales','sum'), Profit=('Profit','sum'), Orders=('OrderID','count')
).round(2).sort_values('Sales', ascending=False)
cat_df['Margin%'] = (cat_df['Profit']/cat_df['Sales']*100).round(1)
print(cat_df)

print(f"\n{'─'*45}")
print("🗓️  QUARTERLY PERFORMANCE")
q_df = df.groupby(['Year','Quarter']).agg(Sales=('Sales','sum'),Profit=('Profit','sum')).round(2)
print(q_df)

# ── 4. MONTHLY TREND ──────────────────────────────────────────
month_order = ['January','February','March','April','May','June',
               'July','August','September','October','November','December']
monthly = df.groupby(['Year','Month'])['Sales'].sum().reset_index()
monthly['Month'] = pd.Categorical(monthly['Month'], categories=month_order, ordered=True)
monthly = monthly.sort_values(['Year','Month'])

# ── 5. VISUALIZATIONS ─────────────────────────────────────────
print(f"\n{'─'*45}")
print("🎨 GENERATING VISUALIZATIONS...")

# Dashboard 1 — EDA Overview
fig, axes = plt.subplots(2, 3, figsize=(20, 12))
fig.suptitle("Retail Sales Performance Analysis — 2022–2023",
             fontsize=17, fontweight='bold', y=1.01)

# (a) Revenue by Category
ax = axes[0,0]
cat_sorted = cat_df.sort_values('Sales')
bars = ax.barh(cat_sorted.index, cat_sorted['Sales']/1e3,
               color=PALETTE[:len(cat_sorted)], edgecolor='white', height=0.6)
ax.set_title("Revenue by Product Category", fontsize=13, fontweight='bold')
ax.set_xlabel("Revenue (₹ Thousands)")
for bar, val in zip(bars, cat_sorted['Sales']/1e3):
    ax.text(bar.get_width()+5, bar.get_y()+bar.get_height()/2,
            f'₹{val:,.0f}K', va='center', fontsize=9)

# (b) Revenue by Region — Donut
ax = axes[0,1]
region_sorted = region_df.sort_values('Sales', ascending=False)
wedges, texts, autotexts = ax.pie(
    region_sorted['Sales'], labels=region_sorted.index,
    autopct='%1.1f%%', colors=PALETTE,
    wedgeprops={'edgecolor':'white','linewidth':2},
    pctdistance=0.82, startangle=90)
centre = plt.Circle((0,0), 0.60, fc='white')
ax.add_patch(centre)
ax.text(0, 0, f'₹{total_sales/1e6:.1f}M\nRevenue',
        ha='center', va='center', fontsize=11, fontweight='bold')
ax.set_title("Revenue Share by Region", fontsize=13, fontweight='bold')

# (c) Monthly Revenue Trend
ax = axes[0,2]
for yr, color in zip([2022,2023], ['#3498DB','#E74C3C']):
    sub = monthly[monthly['Year']==yr]
    ax.plot(sub['Month'].astype(str), sub['Sales']/1e3,
            marker='o', color=color, lw=2.5, ms=6, label=str(yr))
ax.set_title("Monthly Revenue Trend (2022 vs 2023)", fontsize=13, fontweight='bold')
ax.set_ylabel("Revenue (₹ Thousands)")
ax.tick_params(axis='x', rotation=45)
ax.legend()
ax.fill_between(range(len(sub)), 0, 1, alpha=0)  # invisible

# (d) Profit Margin by Category
ax = axes[1,0]
margin_sorted = cat_df.sort_values('Margin%', ascending=True)
colors_bar = ['#E74C3C' if m < 15 else '#2ECC71' for m in margin_sorted['Margin%']]
bars = ax.barh(margin_sorted.index, margin_sorted['Margin%'],
               color=colors_bar, edgecolor='white', height=0.6)
ax.axvline(15, color='orange', linestyle='--', lw=1.5, label='15% Threshold')
ax.set_title("Profit Margin % by Category", fontsize=13, fontweight='bold')
ax.set_xlabel("Profit Margin (%)")
ax.legend()
for bar, val in zip(bars, margin_sorted['Margin%']):
    ax.text(bar.get_width()+0.3, bar.get_y()+bar.get_height()/2,
            f'{val:.1f}%', va='center', fontsize=9)

# (e) Sales by Customer Segment
ax = axes[1,1]
seg_df = df.groupby('CustomerSegment')['Sales'].sum().sort_values(ascending=False)
ax.bar(seg_df.index, seg_df/1e3, color=PALETTE[:3], edgecolor='white', width=0.5)
ax.set_title("Revenue by Customer Segment", fontsize=13, fontweight='bold')
ax.set_ylabel("Revenue (₹ Thousands)")
for i, (seg, val) in enumerate(zip(seg_df.index, seg_df/1e3)):
    ax.text(i, val+5, f'₹{val:,.0f}K', ha='center', fontsize=10, fontweight='bold')

# (f) Discount vs Profit scatter
ax = axes[1,2]
scatter_df = df.groupby('Discount').agg(
    AvgProfit=('Profit','mean'), Count=('OrderID','count')).reset_index()
ax.scatter(scatter_df['Discount']*100, scatter_df['AvgProfit'],
           s=scatter_df['Count']*5, color='#E74C3C', alpha=0.7, edgecolors='white')
ax.axhline(0, color='black', lw=1, linestyle='--')
z = np.polyfit(scatter_df['Discount']*100, scatter_df['AvgProfit'], 1)
p = np.poly1d(z)
x_line = np.linspace(0, 40, 100)
ax.plot(x_line, p(x_line), color='#3498DB', lw=2, linestyle='--', label='Trend')
ax.set_title("Impact of Discount on Avg Profit", fontsize=13, fontweight='bold')
ax.set_xlabel("Discount (%)")
ax.set_ylabel("Average Profit (₹)")
ax.legend()

plt.tight_layout()
plt.savefig("visualizations/sales_dashboard.png", bbox_inches='tight', dpi=150)
plt.close()
print("  ✅ Sales dashboard saved")

# Dashboard 2 — Quarterly + Region Deep Dive
fig, axes = plt.subplots(1, 2, figsize=(16, 6))
fig.suptitle("Quarterly & Regional Performance Deep Dive",
             fontsize=15, fontweight='bold')

# Quarterly grouped bar
ax = axes[0]
q_pivot = q_df['Sales'].unstack(level=0) / 1e3
x = np.arange(len(q_pivot))
w = 0.35
ax.bar(x - w/2, q_pivot[2022], w, label='2022', color='#3498DB', edgecolor='white')
ax.bar(x + w/2, q_pivot[2023], w, label='2023', color='#E74C3C', edgecolor='white')
ax.set_xticks(x)
ax.set_xticklabels(q_pivot.index)
ax.set_title("Quarterly Revenue: 2022 vs 2023", fontsize=13, fontweight='bold')
ax.set_ylabel("Revenue (₹ Thousands)")
ax.legend()

# Region × Category heatmap
ax = axes[1]
pivot = df.pivot_table(values='Sales', index='Region',
                       columns='Category', aggfunc='sum', fill_value=0) / 1e3
sns.heatmap(pivot.round(0), annot=True, fmt='.0f', cmap='YlOrRd',
            ax=ax, linewidths=0.5, cbar_kws={'label':'Sales (₹K)'})
ax.set_title("Region × Category Revenue Heatmap (₹K)", fontsize=13, fontweight='bold')
ax.set_xlabel("")
ax.set_ylabel("")

plt.tight_layout()
plt.savefig("visualizations/quarterly_regional.png", bbox_inches='tight', dpi=150)
plt.close()
print("  ✅ Quarterly & Regional chart saved")

# ── 6. INSIGHTS REPORT ────────────────────────────────────────
print(f"\n{'─'*45}")
print("💡 KEY INSIGHTS & RECOMMENDATIONS")
top_region   = region_df['Sales'].idxmax()
top_cat      = cat_df['Sales'].idxmax()
low_margin   = cat_df['Margin%'].idxmin()
high_disc    = df[df['Discount'] >= 0.3]['Profit'].mean()
no_disc      = df[df['Discount'] == 0]['Profit'].mean()

report = f"""
╔══════════════════════════════════════════════════════════╗
║       RETAIL SALES PERFORMANCE — EXECUTIVE REPORT        ║
╚══════════════════════════════════════════════════════════╝

DATASET   : 1,200 Orders | 2022–2023 | 5 Categories | 4 Regions

KEY PERFORMANCE INDICATORS
─────────────────────────────────────────────────────────
  Total Revenue      : ₹{total_sales:>12,.2f}
  Total Profit       : ₹{total_profit:>12,.2f}
  Profit Margin      : {profit_margin:>11.1f}%
  Total Orders       : {total_orders:>12,}
  Avg Order Value    : ₹{avg_order_val:>12,.2f}

TOP FINDINGS
─────────────────────────────────────────────────────────
  1. {top_region} is the highest revenue region
  2. {top_cat} is the best performing product category
  3. {low_margin} has the lowest profit margin — needs review
  4. Heavy discounts (30%+) reduce avg profit to ₹{high_disc:,.0f}
     vs ₹{no_disc:,.0f} with no discount — a {((no_disc-high_disc)/no_disc*100):.0f}% difference

RECOMMENDATIONS
─────────────────────────────────────────────────────────
  ✅ Cap discounts at 20% — higher discounts hurt profitability
  ✅ Invest more in {top_region} region — highest revenue potential
  ✅ Review pricing strategy for {low_margin} category
  ✅ Push Corporate segment — second highest revenue, high volume
  ✅ Q4 is peak season — increase inventory and marketing budget

═══════════════════════════════════════════════════════════
"""
print(report)
with open("reports/sales_executive_report.txt","w") as f:
    f.write(report)
print("✅ Report saved → reports/sales_executive_report.txt")
print("\n🎉 SALES ANALYSIS COMPLETE!\n")
