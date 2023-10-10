import streamlit as st
import pandas as pd
import plotly.express as px

# Load your data (replace 'your_data.csv' with your file path)
df = pd.read_csv(https://github.com/tinachalhoub123/tina2/blob/main/WC2023.csv)

# Create the Streamlit app
st.title('FIBA World Cup 2023 Teams Statistics')
st.info('This app shows the statistics of the teams in this year\'s Basketball World Cup - Fiba 2023, which Germany won after winning all the games played without losing a single one.')

# Add interactive controls
selected_stat = st.multiselect('Select a Statistic', df.columns[3:])

filtered_data = df[['POSITION', 'TEAM', selected_stat]]

# Create a scatter plot
fig = px.bar(filtered_data, x='TEAM', y=selected_stat, title=f'{selected_stat} by Country',  color=selected_stat)
fig.update_xaxes(title_text='Country')
fig.update_yaxes(title_text=selected_stat)


# Customize the appearance of the text labels
fig.update_traces(textposition='inside', textangle=0, textfont_size=10)
# Display the Plotly figure in Streamlit
st.plotly_chart(fig)


data = pd.read_csv("C:\\Users\\user\\Desktop\\lebanon_mortality_2.csv")

# Create the Streamlit app
st.title('Lebanon Mortality Analysis (1960 - 2021)')
st.write('Explore Lebanon\'s mortality data over the years.')
st.info('We can see that the mortality rate is extremely high in 1976 and lower but still high in 1982 and this is due to the Civil war, the assassination of president Bachir Gemayel and the Sabra and Shatila Massacre.')
# Add interactive controls
selected_range = st.slider('Select Year Range', min_value=1960, max_value=2021, value=(1960, 2021))

# Filter data based on the selected year range
filtered_data = data[(data['Year'] >= selected_range[0]) & (data['Year'] <= selected_range[1])]

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
