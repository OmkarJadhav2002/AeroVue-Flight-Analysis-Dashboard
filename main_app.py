import streamlit as st
from dbhelper import DB
import plotly.graph_objects as go
import plotly.express as ex
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

db = DB()

home_intro = """
# Welcome to the Flight Dashboard!

This dashboard provides you with real-time insights and visualizations of flight data. Whether you're a traveler, 
aviation enthusiast, or just curious about flight statistics, this is the place to explore various aspects of flights 
around the world.

Navigate through the different sections to discover information about flight routes, airlines, airports, and more. 
Interact with the interactive charts and maps to gain a deeper understanding of the global aviation landscape.

Start your journey by selecting a section from the sidebar menu and enjoy your exploration!

Tech Stack Used: Python, MySQL, Streamlit 

Developer😎: Omkar Jadhav  
"""

st.sidebar.title("Flights Analysis")

user_option = st.sidebar.selectbox("Menu", ["Select One", "Check Flights", "Analysis"])

if user_option == "Check Flights":
    st.title("Check Flights")

    city = db.fetch_cities()
    col1, col2 = st.columns(2)
    with col1:
        source = st.selectbox("Source", sorted(city))
    with col2:
        destination = st.selectbox("Destination", sorted(city))

    # showing the results on dashboard (getting data from dbhelper file)
    if st.button("Search"):
        results = db.fetch_all_flights(source, destination)
        # st.dataframe(results)
        df = pd.DataFrame(results, columns=["Airline", "Route", "Dep_time", "Passengers", "Price"])
        # st.dataframe(df)
        if df.empty:
            st.write("No flights available.")
        else:
            st.dataframe(df)

elif user_option == "Analysis":
    st.title("Flights Analysis")
    airline, frequency = db.fetch_airline_count()

    # plotting the pie chart (flights)
    fig = go.Figure(
        go.Pie(
            labels=airline,
            values=frequency,
            hoverinfo="label+percent",
            textinfo="value"
        )
    )
    st.header("Pie Chart")
    st.plotly_chart(fig)

    # display busiest cities
    st.title("Busiest Cities")
    city, frequency1 = db.fetch_busy_airport_cities()
    fig = ex.bar(
        x=city,
        y=frequency1
    )
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)

    # display daily number of flights(line chart)
    st.title("Daily Number of Flights")
    date, frequency2 = db.fetch_daily_flights()
    fig = ex.line(
        x=date,
        y=frequency2
    )
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)

    # display price distribution
    st.title("Price Distribution")
    flights_data = db.fetch_price()
    df = pd.DataFrame(flights_data, columns=['Price'])
    fig = px.histogram(df, x='Price', nbins=20)
    st.plotly_chart(fig)

else:
    # st.title("About the projects.(Technology used, Motivation, etc.😁)")
    st.markdown(home_intro)

