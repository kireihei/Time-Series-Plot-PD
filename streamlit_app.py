from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

st.title("Time Series Plot of Probability of Default")  # set the title for the app

"""
## Welcome to Streamlit!
`/streamlit_app.py` 

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).
"""


# load data file
def load_data():
    data = pd.read_csv("PDdata.csv")
    data.loc[:, "DataDate"] = pd.to_datetime(data.loc[:, "DataDate"])
    return data


# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load data into the dataframe.
df = load_data()
# Notify the reader that the data was successfully loaded.
data_load_state.text('Loading data...done!')

company_ID = st.select_slider('Select a Company ID',
                              options=list(df.loc[:, "CompanyID"].unique()))
st.write('The selected company is', company_ID)


with st.echo(code_location='below'):
    total_points = st.slider("Number of points in spiral", 1, 5000, 2000)
    num_turns = st.slider("Number of turns in spiral", 1, 100, 9)

    Point = namedtuple('Point', 'x y')
    data = []

    points_per_turn = total_points / num_turns

    for curr_point_num in range(total_points):
        curr_turn, i = divmod(curr_point_num, points_per_turn)
        angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
        radius = curr_point_num / total_points
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        data.append(Point(x, y))

    st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
        .mark_circle(color='#0068c9', opacity=0.5)
        .encode(x='x:Q', y='y:Q'))
