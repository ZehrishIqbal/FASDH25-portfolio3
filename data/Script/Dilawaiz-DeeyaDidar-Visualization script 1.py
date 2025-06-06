import pandas as pd
import plotly.express as px

# Load the topic model CSV file
df = pd.read_csv("topic-model.csv")

# Remove unassigned topics (e.g., Topic = -1)
df = df[df["Topic"] != -1].copy()

# Create a datetime column using year, month, and day #help from chat Gpt
df["date"] = pd.to_datetime(dict(year=df["year"], month=df["month"], day=df["day"]))

# Round dates to the first of each month
df["month"] = df["date"].dt.to_period('M').dt.to_timestamp() #help from ChatGpt

# Get the top 5 most frequent topic numbers (excluding -1)
top_topics = df["Topic"].value_counts().nlargest(5).index.tolist() #help from chat gpt

# Filter dataset to only include rows with top 5 topics
df_top = df[df["Topic"].isin(top_topics)].copy()

# Group by month and topic (with keywords), and count article occurrences
monthly_counts = (
    df_top
    .groupby(["month", "Topic", "topic_1", "topic_2", "topic_3", "topic_4"])
    .size()
    .reset_index(name="Article Count")
)

# Create a readable topic label: combines ID and key terms # help from chat gpt
monthly_counts["Topic Label"] = (
    monthly_counts["Topic"].astype(str) + ": " +
    monthly_counts["topic_1"] + ", " + monthly_counts["topic_2"] + ", " +
    monthly_counts["topic_3"] + ", " + monthly_counts["topic_4"]
)

# Filter dates from May 2021 to April 2024
monthly_counts = monthly_counts[
    (monthly_counts["month"] >= "2021-05-01") & (monthly_counts["month"] <= "2024-04-30")
]

# Create a grouped bar chart using Plotly
fig = px.bar(
    monthly_counts,
    x="month",
    y="Article Count",
    color="Topic Label",
    barmode="group",
    title="Monthly Trends for Top 5 Topics (May 2021 - April 2024)",
    labels={"month": "Month", "Article Count": "Number of Articles"},
    template="plotly_white"
)

# Update layout for better visual clarity
fig.update_layout(
    xaxis_tickangle=45,
    title_font_size=20,
    xaxis_title_font_size=16,
    yaxis_title_font_size=16,
    legend_title_text="Topic",
    margin=dict(t=80, b=120)
)

fig.show()


fig.write_html("bargraph.html")
fig.show()
("../visualizations/dilawaiz_bargraph.html")
