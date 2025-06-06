#import important libraries
import pandas as pd #for handling dataframes and CSV files.

#read the TF-IDF dataset containig article pairs of similarity over 0.3
df = pd.read_csv("C:\\Users\\HP\\Downloads\\FASDH25-portfolio3\\data\\dataframes\\tfidf\\tfidf-over-0.3.csv")

#filter out dataset for only similarity score (greater than equal to 0.7)
#help to focus analyze article pairs that have high similarity scores.
#helpful in comparing topics and clustering

high_similarity = df[df["similarity"] >= 0.7]

#save the filtered high_similarity rows to csv for future use

high_similarity.to_csv("C:\\Users\\HP\\Downloads\\FASDH25-portfolio3\\data\\dataframes\\tfidf\\tfidf-over-0.7.csv", index=False)

#print first few rows 
print(high_similarity.head())

#read the topic model dataset
topic_df = pd.read_csv("C:\\Users\\HP\\Downloads\\FASDH25-portfolio3\\data\\dataframes\\topic-model\\topic-model.csv")

#print first few rows of topic model data
print(topic_df.head())

# Merge filename-1 with topic words
#help from ChatGPT (Conversation 1)
merged_df = high_similarity.merge(topic_df, how='left', left_on='filename-1', right_on='file')#help from ChatGPT (conversation 1)
merged_df = merged_df.rename(columns={
    'topic': 'main_topic_file1',
    'topic_1': 'topic1_file1',
    'topic_2': 'topic2_file1',
    'topic_3': 'topic3_file1',
    'topic_4': 'topic4_file1'
})
#drop unnecessary metadata columns to avoid messy datasets 
merged_df = merged_df.drop(columns=['file', 'year', 'month', 'day'])

# Merge filename-2 with topic words
merged_df = merged_df.merge(topic_df, how='left', left_on='filename-2', right_on='file')
#rename colunms 
merged_df = merged_df.rename(columns={
    'topic':'main_topic_file2',
    'topic_1': 'topic1_file2',
    'topic_2': 'topic2_file2',
    'topic_3': 'topic3_file2',
    'topic_4': 'topic4_file2'
})
#drop unnecessary and duplicate columns 
merged_df = merged_df.drop(columns=['file', 'year', 'month', 'day','title_x','title_y'])

# Stacking/Concatenation of the partial rows of filename-2 under the rows of filename-1 
#create a new dataframe from the data of first articles
#rename columns to make this a standardized structure
#help from ChatGPT (Conversation 2)
df1=merged_df[[                                                                       
    'filename-1', 'title-1', 'year-1','month-1','day-1',
    'Topic_x', 'Count_x', 'topic1_file1', 'topic2_file1', 'topic3_file1','topic4_file1'
    ]].rename(columns={
        'filename-1':'filename',
        'title-1':'title',
        'year-1':'year',
        'month-1':'month',
        'day-1':'day',
        'Topic_x':'TopicNumber',
        'Count_x':'TopicCount',
        'topic1_file1':'topic1',
        'topic2_file1':'topic2',
        'topic3_file1':'topic3',
        'topic4_file1':'topic4'
        })

df2=merged_df[[
    'filename-2', 'title-2', 'year-2','month-2','day-2',
    'Topic_y', 'Count_y', 'topic1_file2', 'topic2_file2', 'topic3_file2','topic4_file2'
    ]].rename(columns={
        'filename-2':'filename',
        'title-2':'title',
        'year-2':'year',
        'month-2':'month',
        'day-2':'day',
        'Topic_y':'TopicNumber',
        'Count_y':'TopicCount',
        'topic1_file2':'topic1',
        'topic2_file2':'topic2',
        'topic3_file2':'topic3',
        'topic4_file2':'topic4'
        })
#combine both articles into one stacked dataframe
#helps to analyze every single article involved in high similarity

stacked_df=pd.concat([df1,df2],ignore_index=True)

#drop only entirely duplicate rows to make sure articles apearing in multiple similar pairs are not over-represented.
stacked_df = stacked_df.drop_duplicates()
#print first 10 rows 
print (stacked_df.head(10))    
#save the dataset containing high similarity articles with topics to a CSV to use in future for visualization and analysis.
stacked_df.to_csv("C:/Users/HP/Downloads/FASDH25-portfolio3/data/self_generated_data_from_tfidf/tfidf-over-0.7-with-topics.csv", index=False)
