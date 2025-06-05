#import libraries

import pandas as pd #for handling CSV files

#load the TF-IDF dataset which contains article pairs and similarity scores over 0.3
df = pd.read_csv("C:\\Users\\HP\\Downloads\\FASDH25-portfolio3\\data\\dataframes\\tfidf\\tfidf-over-0.3.csv")

#print the column names to ensure whether the loaded data is correct and see its structure.
print(df.columns)

#print first 10 rows for preview of the dataset
print(df.head(10))

#check whether there are any null values in the data
print(df.isnull().sum()) #prints the number of missing values

#create the edges list for plotting on Gephi by renaming the relavent columns
edges_df = df.rename(columns={"filename-1": "Source",
                              "filename-2": "Target",
                              "similarity": "Weight"})

#keep the columns which are required for Gephi edges
edges_df = edges_df[["Source", "Target", "Weight"]]
#print it to check
print(edges_df)
#save the edges list as a CSV file for visualization on Gephi
edges_df.to_csv("C:\\Users\\HP\\Downloads\\FASDH25-portfolio3\\data\\dataframes\\tfidf\\Gephi\\0.3_edges.csv", 
                index=False, encoding="utf-8-sig")

#create source node with filename, title, and month
source_nodes = df.rename(columns={"filename-1": "Id",
                                   "title-1": "Label",
                                   "month-1": "month"})
source_nodes = source_nodes[["Id", "Label", "month"]]

#create target nodes
target_nodes = df.rename(columns={"filename-2": "Id",
                                  "title-2": "Label",
                                  "month-2": "month"})

target_nodes = target_nodes[["Id", "Label", "month"]]

#combine source and target nodes 
nodes = pd.concat([source_nodes, target_nodes])
#remove duplicate values to avaoid repetition                                  
nodes = nodes.drop_duplicates()

#print nodes
print(nodes)

#save the nodes list as a CSV for network visualization in Gephi
nodes.to_csv("C:\\Users\\HP\\Downloads\\FASDH25-portfolio3\\data\\dataframes\\tfidf\\Gephi\\0.3_nodes.csv",index=False, encoding="utf-8-sig")
                              
