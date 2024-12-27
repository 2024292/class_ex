import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('ireland_dairy_list.csv')

# Streamlit app
st.title('Ireland Dairy Exports Visualization')

# Display the data
st.write('## Data')
st.write(df)

# Plot the data
st.write('## Export Volume and Value Over the Years')
fig = px.line(df, x='Year', y=['Export Volume (tons)', 'Export Value (million €)'],
              labels={'value': 'Value', 'variable': 'Metric'}, title='Export Volume and Value Over the Years')
st.plotly_chart(fig)

# Assuming export_value is another DataFrame you have
# Sample data for export_value
export_value = pd.read_csv('exports_value.csv')

# Plot the time series of annual export value
st.write('## Annual Export Value Time Series')
fig = px.line(export_value, x='Year', y='Export Value (1000 USD)', markers=True, title='Annual Export Value Time Series')
st.plotly_chart(fig)

# Filter data for the latest year (2022)
latest_year = 2022
data = export_value[export_value['Year'] == latest_year]

# Aggregate export value by item for the year 2022
item_distribution = data.groupby('Item')['Export Value (1000 USD)'].sum()

# Calculate the percentage of each item
total_value = item_distribution.sum()
item_percentage = (item_distribution / total_value) * 100

# Filter out items with less than 3% of the total export value
filtered_items = item_percentage[item_percentage >= 3]
filtered_items['Others'] = item_percentage[item_percentage < 3].sum()

# Plot a pie chart for the item distribution
st.write(f"## Export Value Distribution by Item (Year {latest_year})")
fig = px.pie(filtered_items, values=filtered_items.values, names=filtered_items.index, title=f"Export Value Distribution by Item (Year {latest_year})")
st.plotly_chart(fig)

# Create an interactive barplot for the export quantity of each Item using Plotly
st.write('## Export Value (1000 USD) of each Item')
fig = px.bar(export_value, y='Item', x='Export Value (1000 USD)', color='Export Value (1000 USD)', title='Export Value (1000 USD) of each Item',
             color_continuous_scale=px.colors.sequential.Hot_r, animation_frame='Year', range_x=[0, export_value['Export Value (1000 USD)'].max()])
fig.update_yaxes(tickangle=0, tickfont_size=10)
fig.update_layout(width=1000)  
st.plotly_chart(fig)

# Area plot for export value by category
st.write('## Export Value by Category')
fig = px.area(export_value, x='Year', y='Export Value (1000 USD)', color='Item', title='Export Value by Category')
fig.update_layout(width=1000)  
st.plotly_chart(fig)
