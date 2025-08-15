"""
Geographic Scatter Plot: Event Locations
Israel-Palestine Conflict Analysis
"""
import pandas as pd
import matplotlib.pyplot as plt
import os

# Create output folder if it doesn't exist
if not os.path.exists('visualizations'):
    os.makedirs('visualizations')

# Load data
print("Loading data...")
df = pd.read_excel('Cleaned_Israel_Palestine_Data.xlsx', sheet_name='in')
print(f"Loaded {len(df)} events")

# Filter for events with valid coordinates
df_geo = df.dropna(subset=['latitude', 'longitude'])
print(f"Creating geographic scatter plot with {len(df_geo)} events with valid coordinates")

# Create visualization
plt.figure(figsize=(10, 12))
scatter = plt.scatter(
    df_geo['longitude'], 
    df_geo['latitude'], 
    c=df_geo['fatalities'].clip(0, 20),  # Clip for better color distribution
    cmap='YlOrRd', 
    alpha=0.6,
    s=30,
    edgecolor='k',
    linewidth=0.5
)

plt.grid(True, linestyle='--', alpha=0.7)
plt.colorbar(scatter, label='Fatalities (capped at 20)')
plt.title('Geographic Distribution of Conflict Events', fontsize=16)
plt.xlabel('Longitude')
plt.ylabel('Latitude')

# Mark key cities (approximate coordinates)
key_locations = {
    'Tel Aviv': (34.78, 32.08),
    'Jerusalem': (35.21, 31.77),
    'Gaza City': (34.45, 31.50),
    'Ramallah': (35.20, 31.90),
    'Hebron': (35.10, 31.53)
}

for city, (lon, lat) in key_locations.items():
    plt.plot(lon, lat, 'b*', markersize=10)
    plt.annotate(city, (lon, lat), xytext=(5, 5), textcoords='offset points')

# Save the visualization
plt.tight_layout()
plt.savefig('visualizations/5_geographic_scatter.png', dpi=300, bbox_inches='tight')
print("Geographic scatter plot saved to visualizations/5_geographic_scatter.png")

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
    <h1>Geographic Distribution of Conflict Events</h1>
    
    <div class="chart-container">
        <img src="5_geographic_scatter.png" alt="Geographic Distribution" style="max-width: 100%;">
    </div>
    
    <div class="explanation">
        <h2>What This Shows:</h2>
        <p>This scatter plot displays the geographic distribution of conflict events, with color intensity indicating the number of fatalities. Key cities are marked with stars.</p>
        
        <h2>Business Analytics Concepts:</h2>
        <ul>
            <li><strong>Geospatial Analysis</strong>: Visualizing data in geographic space</li>
            <li><strong>Hotspot Identification</strong>: Locating areas with high conflict intensity</li>
            <li><strong>Multi-variable Visualization</strong>: Showing both location and fatality count</li>
        </ul>
    </div>
</body>
</html>
"""

# Save the HTML file
with open('visualizations/5_geographic_scatter.html', 'w') as f:
    f.write(html_content)

print("HTML page created at visualizations/5_geographic_scatter.html")
print("Done!") 