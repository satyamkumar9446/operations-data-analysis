# Operations Data Analysis — Support Ticket Analytics

## Overview
This project analyzes 50,000+ IT support tickets to identify operational KPIs, priority patterns, and customer satisfaction trends. The analysis directly supports decision-making in operations teams.

## Problem Statement
Operations teams manage thousands of support tickets daily but lack structured insights into:
- Which priority levels consume the most time?
- What are common ticket categories?
- How satisfied are customers with different priority levels?
- What is the actual resolution time across the organization?

## Approach

### 1. Data Cleaning
- Removed duplicate records
- Handled null values across all columns
- Standardized text formatting (Priority, Category)

### 2. KPI Calculations
Calculated key metrics:
- Average resolution time
- Ticket distribution by priority (High/Medium/Low)
- Top 10 ticket categories
- Customer satisfaction by priority level
- First response time analysis

### 3. Visualizations
Generated 4 actionable charts showing:
- Ticket distribution by priority (pie chart)
- Resolution time trends (bar chart)
- Top support categories (horizontal bar)
- Satisfaction scores by priority (comparative bar)

## Tools Used
- **Python 3.9+**
- **Pandas** — Data manipulation & cleaning
- **Matplotlib & Seaborn** — Data visualization
- **NumPy** — Numerical analysis

## Key Findings

| Metric | Value |
|--------|-------|
| Total Tickets | 47,659 |
| Avg Resolution Time | 24.3 hours |
| High Priority % | 18% |
| Avg Satisfaction | 4.2/5.0 |
| Top Category | Network Issues |

## How to Run

### Prerequisites
```
pip install -r requirements.txt
```

### Execution
```
python scripts/analysis.py
```

### Output
All cleaned data and visualizations are saved to `/output/`:
- `cleaned_tickets.csv` — Processed dataset
- `tickets_by_priority.png` — Priority distribution
- `resolution_time_by_priority.png` — Time analysis
- `top_categories.png` — Category breakdown
- `satisfaction_by_priority.png` — Satisfaction trends

## Dataset Source
- **Source:** Kaggle — Support Ticket Priority Dataset
- **Records:** 47,659 after cleaning
- **License:** Public Domain

## Skills Demonstrated
- Data cleaning & validation
- KPI calculation & tracking
- Statistical analysis
- Data visualization
- Python scripting
- Business insights generation

## Future Enhancements
- Add SQL query integration for real-time data
- Implement automated reporting dashboard
- Predictive modeling for resolution time estimation

## Author
Satyam Kumar Jha
[LinkedIn](https://linkedin.com/in/satyam-kumar-jha-447802243/)
