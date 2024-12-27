import streamlit as st
import pandas as pd

df = pd.read_csv('ireland_dairy_list.csv')

# Streamlit app
st.title('Ireland Dairy Exports Visualization')

# Display the data
st.write('## Data')
st.write(df)

# Plot the data
st.write('## Export Volume and Value Over the Years')
st.line_chart(df.set_index('Year')[['Export Volume (tons)', 'Export Value (million €)']])

# Assuming export_value is another DataFrame you have
# Sample data for export_value
export_value = pd.read_csv('exports_value.csv')

# Plot the time series of annual export value
st.write('## Annual Export Value Time Series')
st.line_chart(export_value.set_index('Year')['Export Value (1000 USD)'])

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
st.write(filtered_items)

# Create an interactive barplot for the export quantity of each Item using Streamlit
st.write('## Export Value (1000 USD) of each Item')
st.bar_chart(export_value.set_index('Item')['Export Value (1000 USD)'])

# Area plot for export value by category
st.write('## Export Value by Category')
st.area_chart(export_value.pivot(index='Year', columns='Item', values='Export Value (1000 USD)'))
