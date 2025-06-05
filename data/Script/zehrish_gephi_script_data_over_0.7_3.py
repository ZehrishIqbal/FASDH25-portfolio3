#import libraries

import pandas as pd

#load the csv file
df = pd.read_csv("C:\\Users\\HP\\Downloads\\FASDH25-portfolio3\\data\\dataframes\\tfidf\\tfidf-over-0.7.csv")


#create the edges list
edges_df = df.rename(columns={"filename-1": "Source",
                              "filename-2": "Target",
                              "similarity": "Weight"})

edges_df = edges_df[["Source", "Target", "Weight"]]
print(edges_df)
edges_df.to_csv("C:\\Users\\HP\\Downloads\\FASDH25-portfolio3\\data\\dataframes\\tfidf\\Gephi\\edges.csv", 
                index=False, encoding="utf-8-sig")


source_nodes = df.rename(columns={"filename-1": "Id",
                                   "title-1": "Label",
                                   "month-1": "month"})
source_nodes = source_nodes[["Id", "Label", "month"]]

target_nodes = df.rename(columns={"filename-2": "Id",
                                  "title-2": "Label",
                                  "month-2": "month"})

target_nodes = target_nodes[["Id", "Label", "month"]]
#combine and drop dublicates
nodes = pd.concat([source_nodes, target_nodes])
                                  
nodes = nodes.drop_duplicates()

print(nodes)                                 

nodes.to_csv("C:\\Users\\HP\\Downloads\\FASDH25-portfolio3\\data\\dataframes\\tfidf\\Gephi\\nodes.csv", 
             index=False, encoding="utf-8-sig")
                              
