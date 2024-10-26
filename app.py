import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.figure_factory as ff
import time

# Set the title and a relevant data science image
st.title("Total Data Science App")
image_url = 'https://images.unsplash.com/photo-1517841905240-472988d191e4'  # Example data science image
st.image(image_url, use_column_width=True)

st.write("Explore a complete Streamlit app with various components and an open-source dataset.")

# Load and display the dataset
@st.cache
def load_data():
    data = sns.load_dataset('iris')  # loads sample Iris dataset
    return data

df = load_data()
st.subheader("Iris Dataset Preview")
st.write(df.head())

# Data Overview
st.write("### Data Overview")
st.write("Shape of dataset:", df.shape)
st.write("Columns in the dataset:", df.columns.tolist())
st.write("Data types:", df.dtypes)

# Display basic stats
st.write("### Basic Statistics")
st.write(df.describe())

# Add data visuals
st.write("### Visualizations")

# Pairplot using seaborn
st.write("#### Pairplot of Iris Dataset")
sns.pairplot(df, hue="species")
st.pyplot()

# Interactive scatter plot with Plotly
st.write("#### Scatter Plot: Sepal Length vs Sepal Width")
fig = px.scatter(df, x="sepal_length", y="sepal_width", color="species", size="petal_length")
st.plotly_chart(fig, use_container_width=True)

# Boxplot
st.write("#### Boxplot by Species")
fig = px.box(df, x="species", y="sepal_length", points="all")
st.plotly_chart(fig)

# Distribution plots
st.write("#### Distribution Plot for Petal Length")
hist_data = [df[df["species"] == species]["petal_length"] for species in df["species"].unique()]
group_labels = df["species"].unique().tolist()
fig = ff.create_distplot(hist_data, group_labels, bin_size=.2)
st.plotly_chart(fig)

# Sidebar widgets and user inputs
st.sidebar.header("User Inputs")
species = st.sidebar.selectbox("Select Species", df["species"].unique())
sepal_length = st.sidebar.slider("Sepal Length", float(df["sepal_length"].min()), float(df["sepal_length"].max()))
sepal_width = st.sidebar.slider("Sepal Width", float(df["sepal_width"].min()), float(df["sepal_width"].max()))

filtered_df = df[(df["species"] == species) &
                 (df["sepal_length"] <= sepal_length) &
                 (df["sepal_width"] <= sepal_width)]
st.write("### Filtered Data")
st.write(filtered_df)

# Map visualization (example for geolocation data)
st.write("### Map Display (Randomly Generated Data)")
map_data = pd.DataFrame(np.random.randn(100, 2) / [50, 50] + [37.76, -122.4], columns=['lat', 'lon'])
st.map(map_data)

# Interactive widgets
st.write("### Interactive Widgets")
if st.button("Say Hello"):
    st.write("Hello!")
else:
    st.write("Goodbye")

genre = st.radio("Favorite Genre", ('Comedy', 'Drama', 'Documentary'))
if genre == 'Comedy':
    st.write("You like Comedy!")

age = st.slider("Select Age", 0, 100, 25)
st.write("Selected Age:", age)

contact = st.selectbox("Preferred Contact Method", ["Email", "Phone", "Mail"])
st.write("Contact method selected:", contact)

# Show progress bar
st.write("### Progress Bar")
progress_bar = st.progress(0)
for percent_complete in range(100):
    time.sleep(0.05)
    progress_bar.progress(percent_complete + 1)
st.success("Completed!")

st.write("### Success Animation")
st.balloons()

# User Feedback
st.write("### User Feedback")
title = st.text_input("Enter Title")
rating = st.slider("Rate this app", 1, 5)
st.write("You rated this app:", rating)
