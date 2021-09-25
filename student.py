#importing modules
import pandas as pd
import plotly.express as px

#read csv data using pd module
df = pd.read_csv("data.csv")

#selecting a particular student
student_df = df.loc[df["student_id"]=="TRL_zny"]

#finding the mean of student of attempts in each level
mean = student_df.groupby("level")["attempt"].mean()

#creating a graph
graph = px.scatter(mean, size=["attempt"], color=["attempt"])

graph.show()