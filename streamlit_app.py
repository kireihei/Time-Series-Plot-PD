from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
If you have any questions, please refer to [documentation](https://docs.streamlit.io/).
"""

# load data file
def load_data():
    data = pd.read_csv("PDdata.csv")
    data.loc[:, "DataDate"] = pd.to_datetime(data.loc[:, "DataDate"])
    return data


# set the title for the app
st.title("Time Series Plot of Probability of Default")  

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load data into the dataframe.
df = load_data()
# Notify the reader that the data was successfully loaded.
data_load_state.text('Loading data...done!')

with st.echo(code_location='below'):
    # select box
    company_ID = st.selectbox('Select a Company ID',
                              options=list(df.loc[:, "CompanyID"].unique()))
    st.write('The selected company is', company_ID)

    # line chart
    selected_df = df[df.loc[:, "CompanyID"] == company_ID]
    st.line_chart(selected_df, x="DataDate", y="PD")
