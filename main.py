import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

data = pd.read_csv("istherecorrelation.csv", sep=";")

# Convert commas to dots and ensure numeric types
data["WO [x1000]"] = data["WO [x1000]"].str.replace(",", ".").astype(float)
data["NL Beer consumption [x1000 hectoliter]"] = data["NL Beer consumption [x1000 hectoliter]"].astype(float)

wo = data["WO [x1000]"]
beer = data["NL Beer consumption [x1000 hectoliter]"]

corr_coef, p_value = pearsonr(wo, beer)
print(f"Pearson correlation coefficient: {corr_coef:.3f}")
print(f"P-value: {p_value:.3f}")

plt.figure(dpi=300)
plt.scatter(wo, beer, color="blue", label="Data points")
plt.xlabel("WO (x1000)")
plt.ylabel("NL Beer consumption (x1000 hectoliter)")
plt.title(f"WO vs Beer Consumption\nr={corr_coef:.3f}, p={p_value:.3f}")
plt.legend()
plt.grid(True)

plt.savefig("wo_vs_beer.png", dpi=300)
plt.show()
