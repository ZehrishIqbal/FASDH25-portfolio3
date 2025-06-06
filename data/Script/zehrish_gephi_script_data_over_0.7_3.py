#import libraries

import pandas as pd #for handling csv files or dataframes

#load the filtered high similarity csv 
df = pd.read_csv("C:\\Users\\HP\\Downloads\\FASDH25-portfolio3\\data\\self_generated_data_from_tfidf\\tfidf-over-0.7.csv")


#create the edges list for plotting on Gephi by remainig the relavent columns
edges_df = df.rename(columns={"filename-1": "Source",
                              "filename-2": "Target",
                              "similarity": "Weight"})
#keep the columns which are required for Gephi edges
edges_df = edges_df[["Source", "Target", "Weight"]]
#print it to check and confirm
print(edges_df)
#save the edges list as a CSV file for visualization in Gephi
edges_df.to_csv("C:\\Users\\HP\\Downloads\\FASDH25-portfolio3\\data\\self_generated_data_from_tfidf\\Gephi\\edges.csv", 
                index=False, encoding="utf-8-sig")

#create source node with filename, title, and month
source_nodes = df.rename(columns={"filename-1": "Id",
                                   "title-1": "Label",
                                   "month-1": "month"})
source_nodes = source_nodes[["Id", "Label", "month"]]
#create the target node
target_nodes = df.rename(columns={"filename-2": "Id",
                                  "title-2": "Label",
                                  "month-2": "month"})

target_nodes = target_nodes[["Id", "Label", "month"]]
#combine source and target nodes
nodes = pd.concat([source_nodes, target_nodes])
#drop duplicate values to avoid repetitions                                 
nodes = nodes.drop_duplicates()
#print the list of nodes to check and confirm
print(nodes)                                 
#save the nodes list as a CSV file for network visualization on gephi
nodes.to_csv("C:\\Users\\HP\\Downloads\\FASDH25-portfolio3\\data\\self_generated_data_from_tfidf\\Gephi\\nodes.csv", 
             index=False, encoding="utf-8-sig")
                              
