"""
Bar Chart: Top 10 Event Types
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

# Get top 10 event types
top_events = df['event_type'].value_counts().nlargest(10)
top_events = top_events.sort_values()  # Sort for better visualization

# Create visualization
plt.figure(figsize=(10, 6))
ax = top_events.plot(kind='barh', color='navy')
plt.title('Top 10 Event Types', fontsize=16)
plt.xlabel('Number of Events')
plt.ylabel('Event Type')
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Add data labels
for i, v in enumerate(top_events):
    ax.text(v + 5, i, str(v), va='center')

# Save the visualization
plt.tight_layout()
plt.savefig('visualizations/1_event_types_bar.png', dpi=300, bbox_inches='tight')
print("Bar chart saved to visualizations/1_event_types_bar.png")

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
    <h1>Top 10 Event Types in the Israel-Palestine Conflict</h1>
    
    <div class="chart-container">
        <img src="1_event_types_bar.png" alt="Top 10 Event Types" style="max-width: 100%;">
    </div>
    
    <div class="explanation">
        <h2>What This Shows:</h2>
        <p>This horizontal bar chart displays the 10 most common types of events recorded in the dataset.</p>
        
        <h2>Business Analytics Concepts:</h2>
        <ul>
            <li><strong>Data Aggregation</strong>: Counting occurrences of each event type</li>
            <li><strong>Ranking Analysis</strong>: Ordering by frequency to identify most common events</li>
            <li><strong>Categorical Comparison</strong>: Horizontal format for easy comparison between categories</li>
        </ul>
    </div>
</body>
</html>
"""

# Save the HTML file
with open('visualizations/1_event_types_bar.html', 'w') as f:
    f.write(html_content)

print("HTML page created at visualizations/1_event_types_bar.html")
print("Done!") 