"""
Line Chart: Fatalities Over Time
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

# Convert fatalities to numeric
df['fatalities'] = pd.to_numeric(df['fatalities'], errors='coerce').fillna(0).astype(int)

# Calculate monthly fatalities
print("Creating line chart...")
monthly_fatalities = df.groupby('month')['fatalities'].sum().reset_index()
monthly_fatalities = monthly_fatalities.sort_values('month')

# Create visualization
plt.figure(figsize=(12, 7))
plt.plot(
    monthly_fatalities['month'], 
    monthly_fatalities['fatalities'],
    marker='o',
    linestyle='-',
    linewidth=2,
    markersize=6,
    color='darkred'
)

plt.title('Fatalities Over Time (Monthly)', fontsize=16)
plt.xlabel('Month')
plt.ylabel('Number of Fatalities')
plt.grid(True, linestyle='--', alpha=0.7)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha='right')

# Show only some x-tick labels to avoid overcrowding
x_ticks = np.arange(0, len(monthly_fatalities), max(1, len(monthly_fatalities)//10))
plt.xticks(x_ticks, [monthly_fatalities['month'].iloc[i] for i in x_ticks])

# Highlight peaks with annotations
if len(monthly_fatalities) > 0:
    # Find the top 3 peaks
    peaks = monthly_fatalities.nlargest(3, 'fatalities')
    
    for _, peak in peaks.iterrows():
        plt.annotate(
            f"{int(peak['fatalities'])}",
            xy=(peak['month'], peak['fatalities']),
            xytext=(0, 15),
            textcoords='offset points',
            ha='center',
            arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0.2')
        )

# Save the visualization
plt.tight_layout()
plt.savefig('visualizations/4_fatalities_line.png', dpi=300, bbox_inches='tight')
print("Line chart saved to visualizations/4_fatalities_line.png")

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
    <h1>Fatalities Over Time in the Israel-Palestine Conflict</h1>
    
    <div class="chart-container">
        <img src="4_fatalities_line.png" alt="Fatalities Over Time" style="max-width: 100%;">
    </div>
    
    <div class="explanation">
        <h2>What This Shows:</h2>
        <p>This line chart tracks the total fatalities reported each month throughout the period covered by the dataset.</p>
        
        <h2>Business Analytics Concepts:</h2>
        <ul>
            <li><strong>Trend Analysis</strong>: Tracking changes in conflict intensity over time</li>
            <li><strong>Peak Detection</strong>: Identifying periods of heightened conflict</li>
            <li><strong>Impact Measurement</strong>: Quantifying the human cost of conflict</li>
        </ul>
    </div>
</body>
</html>
"""

# Save the HTML file
with open('visualizations/4_fatalities_line.html', 'w') as f:
    f.write(html_content)

print("HTML page created at visualizations/4_fatalities_line.html")
print("Done!") 