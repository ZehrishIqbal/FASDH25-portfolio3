#import important libraries

import pandas as pd #for handlilng dataframes
import plotly.express as px # for visualizations

#Load the stacked dataframe containing data from TF-IDF and also topic numbers and topic words from Topic model dataset
df = pd.read_csv("../self_generated_data_from_tfidf/tfidf-over-0.7-with-topics.csv")

#group the year, month, and day into proper datatime format for eaisier time-based analysis
df["date"] = pd.to_datetime(df[["year", "month", "day"]])

# Remove rows with -1 TopicNumber which are unnecessary
df = df[~df["TopicNumber"].isin([-1, 56, 55, 62, 64, 26, 12, 16])] #Chatgpt (Conversation 0)

#create a new column in year-month format to group articles by month
df["month_year"] = df["date"].dt.to_period("M").astype(str)


# Create a single label by joining the four topic labels with commas for easy grouping and visualization.
df["Topic_Label"] = df[["topic1", "topic2", "topic3", "topic4"]].agg(", ".join, axis=1)

#group the dataset by month, topic number, and count articles in each group
topic_counts = df.groupby(["month_year", "TopicNumber", "Topic_Label"]).size().reset_index(name="topic_counts")

#plot the bar graph to show topic frequency over time
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
    title="Article counts per Topic and per Month"
    )
#adjust axis, labels, for better readability
fig.update_layout(
    xaxis_title="Month-Year",
    yaxis_title="Article Count",
    barmode="group",
    )
#show the plot in browser
fig.show()

#save the plot as html
fig.write_html("../visualizations/zehrish_bar_all_years.html")
              
