import numpy as np
import pandas as pd
import matplotlib as plt

df = pd.read_csv("heart.csv")

print(df.shape)
print(df.head())
# print(df.columns)

age = df["age"]
chol = df["chol"]
trestbps = df["trestbps"]
thalac = df["thalac"]
