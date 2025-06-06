
import pandas as pd
import os

df = pd.read_csv("topic-model.csv")

# Check the structure
print(df.info())

# See the first few rows
print(df.head(10))

# Check all column names
print(df.columns.tolist())

# Column names and types
print(df.info())
print('\n1 ------\n')

# Missing values
print("Missing values in each column:")
print(df.isnull().sum())
print('\n2 ------\n')

# Create a datetime column
df["date"] = pd.to_datetime(dict(year=df["year"], month=df["month"], day=df["day"]))

# Check number of unique topics and count per topic
print(df[["Topic", "topic_1", "topic_2", "topic_3", "topic_4", "Count"]].drop_duplicates())
print('\n3 ------\n')

# Count articles by year
print(df["year"].value_counts().sort_index())
print('\n4 ------\n')

# Identify and display ambiguous keywords
ambiguous_keywords = ["bank", "hostages", "border", "court", "aid"]
print("\nNotable ambiguous keywords with dual meanings:", ambiguous_keywords)

keywords = pd.concat([df['topic_1'], df['topic_2'], df['topic_3'], df['topic_4']]).unique().tolist()
ambiguous = [word for word in keywords if word in ambiguous_keywords]
print("\n Notable ambiguous keywords with dual meanings:")
for word in ambiguous:
    print(f"- {word}") #help from ChatGPT 

print("\nInterpretation:") #help from ChatGpt
print("These keywords are semantically flexible. For example:")
print("'bank' may refer to the West Bank (geopolitical) or a financial institution.")
print("'court' could be a legal court or a sports court.")
print("'hostages' may indicate captured persons or be metaphorical in political contexts.")
print("'border' could refer to international boundaries or general edge areas.")
print("'aid' might mean humanitarian support or technical assistance.")

# Recreate the topic_label column
df["topic_label"] = df["topic_1"] + " (ID " + df["Topic"].astype(str) + ")"

# Count the number of articles per topic label and get top 5
top_topics = df["topic_label"].value_counts()
top_5_labels = top_topics.head(5).index

# Filter dataframe to only include rows with the top 5 topics
df_top = df[df["topic_label"].isin(top_5_labels)].copy()

# Create a year_month column
df_top['year_month'] = df_top['year'].astype(str) + "-" + df_top['month'].astype(str).str.zfill(2)

# Filter to timeframe: June 2023 – October 2024
df_top = df_top[(df_top['year_month'] >= '2023-06') & (df_top['year_month'] <= '2024-10')]

# Map human themes based on common keyword patterns #helo from ChatGpt 
theme_map = {
    "bank, west, israeli, palestinian": "Territorial Conflict & Diplomacy",
    "captives, hamas, release, hostages": "Hostage Crisis & Hamas Conflict",
    "my, her, she, we": "Civilian Stories & Personal Narratives",
    "hospital, patients, medical, hospitals": "Healthcare & War Casualties",
    "iran, iranian, syria, us": "International Political Responses"
}

# Apply theme mapping to topic_label column
df["topic_model"] = df["topic_label"].map(theme_map)

# Print theme-wise frequency
theme_counts = df["topic_model"].value_counts()
print("\nTop Themes:\n", theme_counts)

# Explore Monthly Article Counts by Theme #help from chat Gpt 
df["year_month"] = df["date"].dt.to_period("M").astype(str)
monthly_theme_counts = df.groupby(["year_month", "topic_model"]).size().reset_index(name="Article Count")
print("\nMonthly Article Counts for Top Themes:\n", monthly_theme_counts)

print("\nInsight:")
print("Most articles in 2023–2024 were focused on conflict regions like the West Bank, and humanitarian issues like hospital conditions.")
print("Themes like 'Civilian Stories' show personal experiences, while 'Hostage Crisis' reflects political-military tensions.")
