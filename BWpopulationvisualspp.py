import pandas as pd
import plotly.express as px
import streamlit as st

st.title("Botswana 2022 Population census Analysis")
st.write("This app analyzes the Botswana population dataset and displays its visualization.")

import matplotlib.pyplot as plt
url = "https://raw.githubusercontent.com/edmondmadman/edmn/main/pdata.csv"
data = pd.read_csv(url)

st.dataframe(data)

groupby_column = st.selectbox('Population data from the biggest settlements in Botswana',
                               ('settlement','settlement','settlement'),
)

output_columns = ['total','males', 'females', 'Youth(18-35)']
data_grouped = data.groupby(by=[groupby_column], as_index=False)[output_columns].sum()

fig = px.bar(
    data_grouped,
    x = groupby_column,
    y = output_columns,
    color_continuous_scale=['red', 'yellow', 'green'],
    template='plotly_white',
    title= f'<b>Males, female and Youth Population by {groupby_column}<\b>'
)
st.plotly_chart(fig)