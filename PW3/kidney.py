import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats 

df = pd.read_csv("heart.csv")

#Task 1
# print(df.shape)
# print(df.head())
# print(df.columns)

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
# print(f"Correlation with each:\nAge: {rAge}\nChol: {rChol}\nTrestbps:{rTrestbps}\nThalach: {rThalach}")

Wage, page = stats.shapiro(age)
Wchol, pchol = stats.shapiro(chol)
Wtrestbps, ptrestbps = stats.shapiro(trestbps)
Wthalach, pthalach = stats.shapiro(thalach)

results = [
    ("Age", Wage, page),
    ("Cholesterol", Wchol, pchol),
    ("Resting BP", Wtrestbps, ptrestbps),
    ("Max Heart Rate", Wthalach, pthalach),
]

for name, W, p in results:
    status = "Normality REJECTED (not normal)" if p < 0.05 else "Normality NOT rejected (normal OK)"
    # print(f"{name:<15} | W = {W:.4f} | p = {p:.4e} | {status}")
    
#Task 4
healthyThalach = thalach[df["target"]==1]
# healthyThalach = df.loc(df["target"]==1,thalach)
illThalach = thalach[df["target"]==0]

u_stat, p = stats.mannwhitneyu(healthyThalach,illThalach)
# if(p<0.05): print("Means differ")
# else: print("Means are close")

groups = ["Healthy", "Disease"]
data = [healthyThalach, illThalach]

means = [g.mean() for g in data]
sems = [stats.sem(g) for g in data]                 # s / sqrt(N)
ci95 = [1.96 * stats.sem(g) for g in data]          # 95% CI half-width

# for name, mean, sem, ci in zip(groups, means, sems, ci95):
    # print(f"{name:<8} | Mean = {mean:.2f} bpm | SEM = ±{sem:.2f} | 95% CI = [{mean - ci:.2f}, {mean + ci:.2f}]")

fig3, ax = plt.subplots(figsize=(5, 4))

ax.errorbar(groups, means, yerr=ci95, fmt="o", markersize=8, capsize=6, linewidth=2, color="green")

ax.set(title="Mean Max Heart Rate (thalach) with 95% CI",label="Max Heart Rate (bpm)")
ax.grid(True, axis="y", linestyle="--", alpha=0.5)

fig3.tight_layout()
fig3.savefig("thalach_means.png")

#Task 5
correlation,p = stats.pearsonr(age,thalach)
# print(f"The correlation between age and max heart rate is {correlation:.2f}")

fig4, corr = plt.subplots(1,1,figsize=(5,5))
corr.scatter(age,thalach)
corr.set(title="Correlation between age and max heart rate", xlabel="age", ylabel="heart rate")
fig4.tight_layout()
fig4.savefig("correlation.png")

#Task 6
df1 = pd.read_csv("chemicals_cancer.csv")
# print(df1.shape)
# print(df1.head())
# print(df1.columns)
benzene = df1["benzene"]
cadmium = df1["cadmium"]
malignancy = df1["malignancy"]

corB, p = stats.pearsonr(benzene,malignancy)
corC, p = stats.pearsonr(cadmium,malignancy)

print(f"Correlation between benzene and malignancy {corB:.2f}")
print(f"Correlation between cadmium and malignancy {corC:.2f}")
print()


fig5, (corrB,corrC )= plt.subplots(1,2,figsize=(10,5))

corrB.scatter(benzene,malignancy)
corrB.set(title="Correlation between benzene and malignancy", xlabel="benzene", ylabel="malignancy")

corrC.scatter(cadmium,malignancy)
corrC.set(title="Correlation between cadmium and malignancy", xlabel="cadmium", ylabel="malignancy")

fig5.tight_layout()
fig5.savefig("BenCadMal.png")

#Task 7
# lowPolutionB = benzene[df1["pollution_index"] < 60]
# lowPolutionC = cadmium[df1["pollution_index"] < 60]
# lowPolutionMalign = malignancy[df1["pollution_index"] < 60]

# lpcorB, p = stats.pearsonr(lowPolutionB,lowPolutionMalign)
# lpcorC, p = stats.pearsonr(lowPolutionC,lowPolutionMalign)

# print(f"Correlation between benzene and malignancy with low pollution index: {lpcorB:.2f}")
# print(f"Correlation between cadmium and malignancy with low pollution index: {lpcorC:.2f}")
# print()


# highPolutionB = benzene[df1["pollution_index"] > 60]
# highPolutionC = cadmium[df1["pollution_index"] > 60]
# highPolutionMalign = malignancy[df1["pollution_index"] > 60]

# hpcorB, p = stats.pearsonr(highPolutionB,highPolutionMalign)
# hpcorC, p = stats.pearsonr(highPolutionC,highPolutionMalign)

# print(f"Correlation between benzene and malignancy with high pollution index: {hpcorB:.2f}")
# print(f"Correlation between cadmium and malignancy with high pollution index: {hpcorC:.2f}")
# print()

midPolutionB = benzene[(df1["pollution_index"] > 40) & (df1["pollution_index"] < 60)]
midPolutionC = cadmium[(df1["pollution_index"] > 40) & (df1["pollution_index"] < 60)]
midPolutionMalign = malignancy[(df1["pollution_index"] > 40) & (df1["pollution_index"] < 60)]

midpcorB, p = stats.pearsonr(midPolutionB,midPolutionMalign)
midpcorC, p = stats.pearsonr(midPolutionC,midPolutionMalign)

print(f"Correlation between benzene and malignancy with mid index: {midpcorB:.2f}")
print(f"Correlation between cadmium and malignancy with mid index: {midpcorC:.2f}")
print()

#Bonus
probs = df["target"].value_counts(normalize=True)
H = stats.entropy(probs, base=2)
print(probs)
print(f"\nShannon Entropy: {H:.4f} bits (max possible = {np.log2(len(probs)):.4f} bits)")