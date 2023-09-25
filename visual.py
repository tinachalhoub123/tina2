import streamlit as st
import pandas as pd
import plotly.express as px

# Load your data (replace 'your_data.csv' with your file path)
df = pd.read_csv('https://raw.githubusercontent.com/tinachalhoub123/tina2/main/Salary_Data.csv')

# Create the Streamlit app
st.title('Salary vs. Age Analysis')
st.write('Explore the relationship between salary, age, and work experience.')

# Add interactive controls
selected_experience_range = st.slider('Select Work Experience Range (in years)', min_value=0, max_value=11, value=(0, 5))

# Filter data based on work experience range
filtered_data = df[(df['YearsExperience'] >= selected_experience_range[0]) & (df['YearsExperience'] <= selected_experience_range[1])]

# Create a scatter plot
fig = px.scatter(
    filtered_data,
    
    x='Age',
    y='Salary',
    title='Salary vs. Age',
    labels={'Age': 'Age', 'Salary': 'Salary'},
    color='YearsExperience',
    size='YearsExperience'
)

# Customize the plot layout
fig.update_traces(marker=dict(opacity=0.7, line=dict(width=1, color='DarkSlateGrey')))

# Display the interactive plot
st.plotly_chart(fig)



df = pd.read_csv("https://raw.githubusercontent.com/tinachalhoub123/tina2/main/lebanon_mortality_2.csv")

# Create the Streamlit app
st.title('Lebanon Mortality Analysis (1960 - 2021)')
st.write('Explore Lebanon\'s mortality data over the years.')

# Add interactive controls
selected_range = st.slider('Select Year Range', min_value=1960, max_value=2021, value=(1960, 2021))

# Filter data based on the selected year range
filtered_data = df[(df['Year'] >= selected_range[0]) & (df['Year'] <= selected_range[1])]

# Create a Plotly Express line chart
fig = px.line(
    filtered_data,
    x="Year",
    y="Deaths",
    title="Lebanon Mortality",
    labels={"Year": "Year", "Deaths": "Number of Deaths"},
)

# Update the y-axis range
fig.update_yaxes(range=[0, 35])

# Display the interactive plot
st.plotly_chart(fig)

