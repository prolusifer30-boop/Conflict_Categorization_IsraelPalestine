"""
Area Chart: Event Types Over Time
Israel-Palestine Conflict Analysis
"""
import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np

# Create output folder if it doesn't exist
if not os.path.exists('visualizations'):
    os.makedirs('visualizations')

# Load data
print("Loading data...")
df = pd.read_excel('Cleaned_Israel_Palestine_Data.xlsx', sheet_name='in')
print(f"Loaded {len(df)} events")

# Convert dates and create month column
df['event_date'] = pd.to_datetime(df['event_date'])
df['month'] = df['event_date'].dt.strftime('%Y-%m')

# Get top 5 event types (for cleaner visualization)
top_5_types = df['event_type'].value_counts().nlargest(5).index.tolist()

# Create monthly pivot table
print("Creating area chart...")
monthly_pivot = pd.pivot_table(
    df[df['event_type'].isin(top_5_types)],
    index='month', 
    columns='event_type',
    values='event_date',
    aggfunc='count'
).fillna(0)

# Sort by date
monthly_pivot = monthly_pivot.sort_index()

# Convert to percentage
monthly_pivot_pct = monthly_pivot.div(monthly_pivot.sum(axis=1), axis=0) * 100

# Create visualization
plt.figure(figsize=(12, 7))
ax = monthly_pivot_pct.plot.area(stacked=True, alpha=0.7, figsize=(12, 7))

plt.title('Event Types Over Time (Monthly)', fontsize=16)
plt.xlabel('Month')
plt.ylabel('Percentage of Events')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.legend(title='Event Type', loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=3)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha='right')

# Show only some x-tick labels to avoid overcrowding
x_ticks = np.arange(0, len(monthly_pivot.index), max(1, len(monthly_pivot.index)//10))
plt.xticks(x_ticks, [monthly_pivot.index[i] for i in x_ticks])

# Save the visualization
plt.tight_layout()
plt.savefig('visualizations/3_events_over_time.png', dpi=300, bbox_inches='tight')
print("Area chart saved to visualizations/3_events_over_time.png")

# Create simple HTML to display the chart
html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Israel-Palestine Conflict Analysis</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 20px; }}
        h1 {{ color: #333366; }}
        .chart-container {{ margin: 20px 0; }}
        .explanation {{ margin: 20px 0; line-height: 1.5; }}
    </style>
</head>
<body>
    <h1>Event Types Over Time in the Israel-Palestine Conflict</h1>
    
    <div class="chart-container">
        <img src="3_events_over_time.png" alt="Event Types Over Time" style="max-width: 100%;">
    </div>
    
    <div class="explanation">
        <h2>What This Shows:</h2>
        <p>This stacked area chart displays how the composition of different event types changed over time on a monthly basis.</p>
        
        <h2>Business Analytics Concepts:</h2>
        <ul>
            <li><strong>Time Series Analysis</strong>: Tracking changes in patterns over time</li>
            <li><strong>Compositional Analysis</strong>: Showing how the mix of events evolved</li>
            <li><strong>Trend Identification</strong>: Revealing shifts in event types that might indicate changing conflict dynamics</li>
        </ul>
    </div>
</body>
</html>
"""

# Save the HTML file
with open('visualizations/3_events_over_time.html', 'w') as f:
    f.write(html_content)

print("HTML page created at visualizations/3_events_over_time.html")
print("Done!") 