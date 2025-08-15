"""
Pie Chart: Top 5 Actors
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

# Get top 5 actors
top_actors = df['actor1'].value_counts().nlargest(5)

# Create visualization
plt.figure(figsize=(10, 8))
wedges, texts, autotexts = plt.pie(
    top_actors.values, 
    labels=top_actors.index,
    autopct='%1.1f%%',
    startangle=90,
    wedgeprops=dict(width=0.4), # For donut chart
    pctdistance=0.85,
    explode=[0.05] * len(top_actors) # Slight explode for all slices
)
plt.setp(autotexts, size=12, weight="bold")
plt.setp(texts, size=10)
plt.title('Top 5 Actors Involved in Conflict', fontsize=16)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle

# Add a center circle for donut chart
centre_circle = plt.Circle((0,0),0.25,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Save the visualization
plt.tight_layout()
plt.savefig('visualizations/2_actors_pie.png', dpi=300, bbox_inches='tight')
print("Pie chart saved to visualizations/2_actors_pie.png")

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
    <h1>Main Actors in the Israel-Palestine Conflict</h1>
    
    <div class="chart-container">
        <img src="2_actors_pie.png" alt="Top 5 Actors" style="max-width: 100%;">
    </div>
    
    <div class="explanation">
        <h2>What This Shows:</h2>
        <p>This pie chart displays the 5 most active parties involved in events recorded in the dataset.</p>
        
        <h2>Business Analytics Concepts:</h2>
        <ul>
            <li><strong>Proportional Analysis</strong>: Showing the relative contribution of each actor</li>
            <li><strong>Stakeholder Identification</strong>: Revealing key parties in the conflict</li>
            <li><strong>Part-to-Whole Relationship</strong>: Understanding how each actor contributes to overall events</li>
        </ul>
    </div>
</body>
</html>
"""

# Save the HTML file
with open('visualizations/2_actors_pie.html', 'w') as f:
    f.write(html_content)

print("HTML page created at visualizations/2_actors_pie.html")
print("Done!") 