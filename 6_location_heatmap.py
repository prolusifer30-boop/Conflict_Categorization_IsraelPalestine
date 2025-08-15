"""
Heatmap: Events by Location
Israel-Palestine Conflict Analysis
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create output folder if it doesn't exist
if not os.path.exists('visualizations'):
    os.makedirs('visualizations')

# Load data
print("Loading data...")
df = pd.read_excel('Cleaned_Israel_Palestine_Data.xlsx', sheet_name='in')
print(f"Loaded {len(df)} events")

# Count events by location
print("Creating heatmap...")
location_counts = df.groupby(['admin1']).size().reset_index(name='event_count')
location_counts = location_counts.sort_values('event_count', ascending=False).head(15)

# Calculate fatalities by location
location_fatalities = df.groupby(['admin1'])['fatalities'].sum().reset_index()
location_fatalities = location_fatalities.sort_values('fatalities', ascending=False).head(15)

# Merge the data
merged_data = pd.merge(
    location_counts,
    location_fatalities,
    on='admin1',
    how='outer'
).fillna(0)

# Sort by event count for consistent ordering
merged_data = merged_data.sort_values('event_count', ascending=False).head(15)

# Create pivot table-like structure for heatmap
heatmap_data = pd.DataFrame({
    'Administrative Area': merged_data['admin1'],
    'Event Count': merged_data['event_count'],
    'Fatalities': merged_data['fatalities']
}).set_index('Administrative Area')

# Create visualization
plt.figure(figsize=(12, 8))
ax = sns.heatmap(
    heatmap_data, 
    annot=True, 
    fmt='.0f', 
    cmap='YlOrRd',
    linewidths=0.5
)
plt.title('Top 15 Areas by Conflict Activity', fontsize=16)
plt.tight_layout()

# Save the visualization
plt.savefig('visualizations/6_location_heatmap.png', dpi=300, bbox_inches='tight')
print("Heatmap saved to visualizations/6_location_heatmap.png")

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
    <h1>Administrative Areas with Highest Conflict Activity</h1>
    
    <div class="chart-container">
        <img src="6_location_heatmap.png" alt="Location Heatmap" style="max-width: 100%;">
    </div>
    
    <div class="explanation">
        <h2>What This Shows:</h2>
        <p>This heatmap displays the top 15 administrative areas by conflict activity, showing both the number of events and fatalities in each area.</p>
        
        <h2>Business Analytics Concepts:</h2>
        <ul>
            <li><strong>Data Aggregation</strong>: Summarizing events by geographic region</li>
            <li><strong>Heat Mapping</strong>: Using color intensity to represent magnitude</li>
            <li><strong>Comparative Analysis</strong>: Contrasting event frequency with fatality counts</li>
        </ul>
    </div>
</body>
</html>
"""

# Save the HTML file
with open('visualizations/6_location_heatmap.html', 'w') as f:
    f.write(html_content)

print("HTML page created at visualizations/6_location_heatmap.html")
print("Done!") 