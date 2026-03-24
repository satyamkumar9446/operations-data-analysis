import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

# ==================== LOAD DATA ====================
print("Loading support tickets dataset...")
df = pd.read_csv('data/Support_tickets.csv')

print(f"Total records loaded: {len(df)}")
print(f"Columns: {df.columns.tolist()}")

# ==================== DATA CLEANING ====================
print("\n--- DATA CLEANING ---")

initial_rows = len(df)
df = df.drop_duplicates()
print(f"Duplicates removed: {initial_rows - len(df)}")

print(f"Missing values:\n{df.isnull().sum()}")
df = df.dropna()
print(f"Rows after cleaning: {len(df)}")

# Standardize text columns
df['priority'] = df['priority'].str.title()
df['industry'] = df['industry'].str.title()
df['region'] = df['region'].str.title()
df['customer_tier'] = df['customer_tier'].str.title()

# Save cleaned data
df.to_csv('output/cleaned_tickets.csv', index=False)
print("✅ Cleaned data saved.")

# ==================== KPI CALCULATIONS ====================
print("\n--- KEY PERFORMANCE INDICATORS ---")

print(f"Total Tickets: {len(df):,}")
print(f"Average Downtime (mins): {df['downtime_min'].mean():.2f}")
print(f"Average Customers Affected: {df['customers_affected'].mean():.2f}")
print(f"Average Error Rate (%): {df['error_rate_pct'].mean():.2f}")
print(f"Payment Impact Cases: {df['payment_impact_flag'].sum():,}")
print(f"Security Incidents: {df['security_incident_flag'].sum():,}")
print(f"Data Loss Cases: {df['data_loss_flag'].sum():,}")

tickets_by_priority = df['priority'].value_counts()
print(f"\nTickets by Priority:\n{tickets_by_priority}")

# ==================== VISUALIZATIONS ====================
print("\n--- CREATING VISUALIZATIONS ---")

# Chart 1: Tickets by Priority (Pie Chart)
fig, ax = plt.subplots(figsize=(8, 6))
tickets_by_priority.plot(
    kind='pie', autopct='%1.1f%%', ax=ax,
    colors=['#ff6b6b', '#ffd93d', '#6bcf7f', '#4ecdc4']
)
ax.set_title('Support Tickets by Priority', fontsize=14, fontweight='bold')
ax.set_ylabel('')
plt.tight_layout()
plt.savefig('output/tickets_by_priority.png', dpi=300, bbox_inches='tight')
print("✅ Saved: tickets_by_priority.png")
plt.close()

# Chart 2: Average Downtime by Priority (Bar Chart)
fig, ax = plt.subplots(figsize=(10, 6))
df.groupby('priority')['downtime_min'].mean().sort_values(ascending=False).plot(
    kind='bar', ax=ax, color=['#ff6b6b', '#ffd93d', '#6bcf7f', '#4ecdc4']
)
ax.set_title('Average Downtime by Priority (mins)', fontsize=14, fontweight='bold')
ax.set_xlabel('Priority')
ax.set_ylabel('Downtime (minutes)')
ax.set_xticklabels(ax.get_xticklabels(), rotation=0)
plt.tight_layout()
plt.savefig('output/downtime_by_priority.png', dpi=300, bbox_inches='tight')
print("✅ Saved: downtime_by_priority.png")
plt.close()

# Chart 3: Tickets by Industry (Horizontal Bar)
fig, ax = plt.subplots(figsize=(12, 6))
df['industry'].value_counts().head(10).plot(
    kind='barh', ax=ax, color='#4ecdc4'
)
ax.set_title('Top 10 Industries by Ticket Volume', fontsize=14, fontweight='bold')
ax.set_xlabel('Number of Tickets')
plt.tight_layout()
plt.savefig('output/tickets_by_industry.png', dpi=300, bbox_inches='tight')
print("✅ Saved: tickets_by_industry.png")
plt.close()

# Chart 4: Customer Sentiment by Priority (Bar Chart)
fig, ax = plt.subplots(figsize=(10, 6))
df.groupby('priority')['customer_sentiment'].mean().sort_values(ascending=False).plot(
    kind='bar', ax=ax, color=['#ff6b6b', '#ffd93d', '#6bcf7f', '#4ecdc4']
)
ax.set_title('Average Customer Sentiment by Priority', fontsize=14, fontweight='bold')
ax.set_xlabel('Priority')
ax.set_ylabel('Sentiment Score')
ax.set_xticklabels(ax.get_xticklabels(), rotation=0)
plt.tight_layout()
plt.savefig('output/sentiment_by_priority.png', dpi=300, bbox_inches='tight')
print("✅ Saved: sentiment_by_priority.png")
plt.close()

# Chart 5: Payment Impact & Security Incidents by Region
fig, ax = plt.subplots(figsize=(12, 6))
df.groupby('region')[['payment_impact_flag', 'security_incident_flag']].sum().plot(
    kind='bar', ax=ax, color=['#ff6b6b', '#4ecdc4']
)
ax.set_title('Payment Impact & Security Incidents by Region', fontsize=14, fontweight='bold')
ax.set_xlabel('Region')
ax.set_ylabel('Count')
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
ax.legend(['Payment Impact', 'Security Incident'])
plt.tight_layout()
plt.savefig('output/incidents_by_region.png', dpi=300, bbox_inches='tight')
print("✅ Saved: incidents_by_region.png")
plt.close()

# =============== SUMMARY ====================
print("\n" + "="*50)
print("📊 ANALYSIS SUMMARY")
print("="*50)
print(f"Total Tickets Analyzed : {len(df):,}")
print(f"Avg Downtime           : {df['downtime_min'].mean():.2f} mins")
print(f"Avg Customers Affected : {df['customers_affected'].mean():.2f}")
print(f"Avg Error Rate         : {df['error_rate_pct'].mean():.2f}%")
print(f"Payment Impact Cases   : {df['payment_impact_flag'].sum():,}")
print(f"Security Incidents     : {df['security_incident_flag'].sum():,}")
print(f"Data Loss Cases        : {df['data_loss_flag'].sum():,}")
print("="*50)
print("\n✅ All charts saved to /output/")
```

---
