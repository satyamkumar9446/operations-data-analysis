import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Set style for better-looking charts
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

# Load the dataset
print("Loading support tickets dataset...")
df = pd.read_csv('data/support_tickets.csv')

print(f"Total records loaded: {len(df)}")
print(f"Columns: {df.columns.tolist()}")

# ==================== DATA CLEANING ====================
print("\n--- DATA CLEANING ---")

# Remove duplicates
initial_rows = len(df)
df = df.drop_duplicates()
print(f"Duplicates removed: {initial_rows - len(df)}")

# Handle missing values
print(f"Missing values before cleaning:\n{df.isnull().sum()}")
df = df.dropna()  # Remove rows with any null values
print(f"Rows after removing nulls: {len(df)}")

# Standardize text columns
df['Priority'] = df['Priority'].str.title()
df['Category'] = df['Category'].str.title()

# ==================== KPI CALCULATIONS ====================
print("\n--- KEY PERFORMANCE INDICATORS ---")

# 1. Average Resolution Time
avg_resolution_time = df['ResolutionTime'].astype(float).mean()
print(f"Average Resolution Time: {avg_resolution_time:.2f} hours")

# 2. Tickets by Priority
tickets_by_priority = df['Priority'].value_counts()
print(f"\nTickets by Priority:\n{tickets_by_priority}")

# 3. Ticket Distribution by Category
tickets_by_category = df['Category'].value_counts().head(10)
print(f"\nTop 10 Categories:\n{tickets_by_category}")

# 4. Average Customer Satisfaction by Priority
satisfaction_by_priority = df.groupby('Priority')['CustomerSatisfaction'].mean()
print(f"\nAverage Satisfaction by Priority:\n{satisfaction_by_priority}")

# 5. First Response Time Analysis (if column exists)
if 'FirstResponseTime' in df.columns:
    avg_first_response = df['FirstResponseTime'].astype(float).mean()
    print(f"Average First Response Time: {avg_first_response:.2f} hours")

# ==================== VISUALIZATIONS ====================
print("\n--- CREATING VISUALIZATIONS ---")

# Chart 1: Tickets by Priority (Pie Chart)
fig, ax = plt.subplots(figsize=(8, 6))
tickets_by_priority.plot(kind='pie', autopct='%1.1f%%', ax=ax, colors=['#ff6b6b', '#ffd93d', '#6bcf7f'])
ax.set_title('Support Tickets Distribution by Priority', fontsize=14, fontweight='bold')
ax.set_ylabel('')
plt.tight_layout()
plt.savefig('output/tickets_by_priority.png', dpi=300, bbox_inches='tight')
print("✅ Saved: tickets_by_priority.png")
plt.close()

# Chart 2: Resolution Time by Priority (Bar Chart)
fig, ax = plt.subplots(figsize=(10, 6))
resolution_by_priority = df.groupby('Priority')['ResolutionTime'].astype(float).mean().sort_values(ascending=False)
resolution_by_priority.plot(kind='bar', ax=ax, color=['#ff6b6b', '#ffd93d', '#6bcf7f'])
ax.set_title('Average Resolution Time by Priority', fontsize=14, fontweight='bold')
ax.set_xlabel('Priority Level')
ax.set_ylabel('Hours')
ax.set_xticklabels(ax.get_xticklabels(), rotation=0)
plt.tight_layout()
plt.savefig('output/resolution_time_by_priority.png', dpi=300, bbox_inches='tight')
print("✅ Saved: resolution_time_by_priority.png")
plt.close()

# Chart 3: Top Categories (Bar Chart)
fig, ax = plt.subplots(figsize=(12, 6))
tickets_by_category.plot(kind='barh', ax=ax, color='#4ecdc4')
ax.set_title('Top 10 Support Ticket Categories', fontsize=14, fontweight='bold')
ax.set_xlabel('Number of Tickets')
plt.tight_layout()
plt.savefig('output/top_categories.png', dpi=300, bbox_inches='tight')
print("✅ Saved: top_categories.png")
plt.close()

# Chart 4: Customer Satisfaction by Priority (Bar Chart)
fig, ax = plt.subplots(figsize=(10, 6))
satisfaction_by_priority.plot(kind='bar', ax=ax, color=['#ff6b6b', '#ffd93d', '#6bcf7f'])
ax.set_title('Average Customer Satisfaction by Priority', fontsize=14, fontweight='bold')
ax.set_xlabel('Priority Level')
ax.set_ylabel('
