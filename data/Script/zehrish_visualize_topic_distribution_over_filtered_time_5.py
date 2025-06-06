#import important libraries

import pandas as pd
import plotly.express as px


#Load the stacked dataframe
df = pd.read_csv("../dataframes/tfidf/tfidf-over-0.7-with-topics.csv")

#group the year, month, and day using pd.to_datetime
df["date"] = pd.to_datetime(df[["year", "month", "day"]])

#filter the date range
start_date = pd.to_datetime("2023-10-01")
end_date = pd.to_datetime("2024-10-31")
df = df[(df["date"] >= start_date) & (df["date"] <= end_date)]

# Remove unwanted TopicNumbers including -1 and low-quality topics
df = df[~df["TopicNumber"].isin([-1, 2, 56, 55, 62, 64, 26, 14, 12, 16,])]

#create a new column in year-month format
df["month_year"] = df["date"].dt.to_period("M").astype(str)

#count number of articles under each topic number per month
# Create a single label by joining topic columns with commas
df["Topic_Label"] = df[["topic1", "topic2", "topic3", "topic4"]].agg(", ".join, axis=1)

#grouping and counting
topic_counts = df.groupby(["month_year", "TopicNumber", "Topic_Label"]).size().reset_index(name="topic_counts")

#plot the bar graph
fig = px.bar(topic_counts,
    x="month_year",
    y="topic_counts",
    color="Topic_Label",
    barmode="group",
    color_discrete_sequence=px.colors.qualitative.Dark2,    #Chatgpt conversation 3     
    labels={
        "month_year": "Month-Year",
        "topic_counts": "Number of Articles",
        "TopicNumber": "Topic Number"
        },
    title="Article counts per Topic and per Month(Filtered date range)"
    )
#adjust axis, labels, 
fig.update_layout(
    xaxis_title="Month-Year",
    yaxis_title="Article Count",
    legend_title="Topic",
    barmode="group",
    )
#show the plot
fig.show()

#save the plot as html
fig.write_html("../visualizations/zehrish_bar_filtered_dates.html")
              
