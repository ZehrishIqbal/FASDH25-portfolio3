import pandas as pd
import plotly.express as px

# Load dataset
df = pd.read_csv("topic-model.csv")

# Filter out outliers
df = df[df["Topic"] != -1].copy()

# Create topic labels from keywords #help from ChatGpt
df["Topic_Label"] = df[["topic_1", "topic_2", "topic_3", "topic_4"]].agg(", ".join, axis=1)

# Group by Topic_Label and Year to get article count
grouped = df.groupby(["Topic_Label", "year"]).size().reset_index(name="Article_Count")

# Get top 10 topics based on total article count #help from ChatGpt
top_ten_topics = grouped.groupby("Topic_Label")["Article_Count"].sum().nlargest(10).index

# Filter to only include top 10 topics
grouped = grouped[grouped["Topic_Label"].isin(top_ten_topics)]

# Create grouped bar chart
fig = px.bar(
    grouped,
    x="year",
    y="Article_Count",
    color="Topic_Label",
    barmode="group",
    title="Article Counts by Topic and Year",
    labels={
        "year": "Year",
        "Article_Count": "Number of Articles",
        "Topic_Label": "Topic"
    },
    height=500
)

# Show chart
fig.write_html("bargraph.html")
fig.show()
("../visualizations/dilawaiz_bargraph.html")
