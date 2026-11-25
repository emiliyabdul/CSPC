import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats 

df = pd.read_csv("heart.csv")

age = df["age"]
chol = df["chol"]
trestbps = df["trestbps"]
thalach = df["thalach"]

# Task 2
fig1, ([ageH, cholH], [trestbpsH, thalachH]) = plt.subplots(2, 2, figsize=(6, 6))

ageH.hist(age, bins=35, color="red", edgecolor="darkred", label="Age")
ageH.set(title="Age Distribution", xlabel="Age (years)", ylabel="Frequency")
ageH.legend()

cholH.hist(chol, bins=35, color="green", edgecolor="darkgreen", label="Cholesterol")
cholH.set(title="Serum Cholesterol Distribution", xlabel="Cholesterol (mg/dl)", ylabel="Frequency")
cholH.legend()

trestbpsH.hist(trestbps, bins=35, color="blue", edgecolor="darkblue", label="Resting BP")
trestbpsH.set(title="Resting Blood Pressure", xlabel="Blood Pressure (mm Hg)", ylabel="Frequency")
trestbpsH.legend()

thalachH.hist(thalach, bins=35, color="orange", edgecolor="darkorange", label="Max Heart Rate")
thalachH.set(title="Max Heart Rate Achieved", xlabel="Heart Rate (bpm)", ylabel="Frequency")
thalachH.legend()

fig1.tight_layout()
fig1.savefig("distrib.png")

# Task 3
fig2, ([ageN, cholN], [trestbpsN, thalachN]) = plt.subplots(2, 2, figsize=(6, 6))

rAge = stats.probplot(age, dist="norm", plot=ageN)[1][2]
ageN.set(title="Q-Q Plot: Age", xlabel="Theoretical Quantiles", ylabel="Age (years)")

rChol = stats.probplot(chol, dist="norm", plot=cholN)[1][2]
cholN.set(title="Q-Q Plot: Serum Cholesterol", xlabel="Theoretical Quantiles", ylabel="Cholesterol (mg/dl)")

rTrestbps = stats.probplot(trestbps, dist="norm", plot=trestbpsN)[1][2]
trestbpsN.set(title="Q-Q Plot: Resting BP", xlabel="Theoretical Quantiles", ylabel="Blood Pressure (mm Hg)")

rThalach = stats.probplot(thalach, dist="norm", plot=thalachN)[1][2]
thalachN.set(title="Q-Q Plot: Max Heart Rate", xlabel="Theoretical Quantiles", ylabel="Heart Rate (bpm)")

fig2.tight_layout()
fig2.savefig("Q-Qplot.png")
print(f"Correlation with each:\nAge: {rAge}\nChol: {rChol}\nTrestbps:{rTrestbps}\nThalach: {rThalach}")