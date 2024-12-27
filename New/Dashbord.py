import streamlit as st
import pandas as pd

df = pd.read_csv('Ireland_dairy_list.csv')

# Streamlit app
st.title('Ireland Dairy Exports Visualization')

# Display the data
st.write('## Data')
st.write(df)


# st.write('## Export Volume and Value Over the Years')
# st.line_chart(df.set_index('Year')[['Export Volume (tons)', 'Export Value (million €)']])
