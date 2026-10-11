"""
Spread Locator: Statistical Distribution Analysis Model
Run: pip install numpy pandas scipy statsmodels matplotlib seaborn openpyxl
Dataset: Reads the included workbook's Transactions sheet. Dataset is synthetic/demo data.
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

FILE = "Spread_Locator_Dataset_and_Analysis.xlsx"
df = pd.read_excel(FILE, sheet_name="Transactions")
x = df["transaction_amount"].dropna().to_numpy()

print("Rows:", len(x))
print("Mean:", x.mean())
print("Median:", np.median(x))
print("Sample standard deviation:", x.std(ddof=1))
print("Skewness:", stats.skew(x, bias=False))
print("Observed P(amount > ₹5000):", (x > 5000).mean())

# Bernoulli: transaction success indicator
success = (df["transaction_status"] == "Success").astype(int)
p_success = success.mean()
print("Bernoulli p(success):", p_success)

# Binomial: number of successes in groups of n trials; illustration using groups of 10 rows
group_size = 10
groups = [success.iloc[i:i+group_size].sum()
          for i in range(0, len(success), group_size) if len(success.iloc[i:i+group_size]) == group_size]
print("Binomial estimate p:", p_success, "group size:", group_size)
print("Grouped successes:", groups[:10])

# Poisson: transactions per calendar day
daily = df.groupby(pd.to_datetime(df["transaction_date"]).dt.date).size()
lam = daily.mean()
print("Poisson lambda (mean daily count):", lam)

# Log-normal fit, location fixed to 0
shape, loc, scale = stats.lognorm.fit(x, floc=0)
print("Log-normal parameters (shape, loc, scale):", shape, loc, scale)
print("Fitted log-normal P(X > 5000):", stats.lognorm.sf(5000, shape, loc=loc, scale=scale))

# Power-law fit as a bounded power distribution on normalized data.
# For rigorous Pareto/power-law tail analysis, choose a tail threshold and compare models.
x_scaled = x / x.max()
pl_a, pl_loc, pl_scale = stats.powerlaw.fit(x_scaled, floc=0, fscale=1)
print("SciPy powerlaw fit (shape, loc, scale) on normalized amounts:", pl_a, pl_loc, pl_scale)

# Normal Q-Q plot
stats.probplot(x, dist="norm", plot=plt)
plt.title("Normal Q-Q Plot")
plt.tight_layout()
plt.show()

# Box-Cox requires strictly positive values
x_bc, lam_bc = stats.boxcox(x)
print("Box-Cox lambda:", lam_bc)
plt.figure()
plt.hist(x_bc, bins=30, density=True)
plt.title(f"Box-Cox transformed values (lambda={lam_bc:.3f})")
plt.show()

# Z-scores, PDF and CDF
z = (x - x.mean()) / x.std(ddof=1)
print("Z-score sample:", z[:10])
grid = np.linspace(x.min(), x.max(), 300)
plt.figure()
plt.plot(grid, stats.lognorm.pdf(grid, shape, loc=loc, scale=scale))
plt.title("Fitted Log-normal PDF")
plt.show()
plt.figure()
plt.plot(grid, stats.lognorm.cdf(grid, shape, loc=loc, scale=scale))
plt.title("Fitted Log-normal CDF")
plt.show()

# Empirical normal-model probability (normality is questionable for skewed amounts)
normal_prob = stats.norm.sf(5000, loc=x.mean(), scale=x.std(ddof=1))
print("Normal-model P(X > 5000) (use cautiously):", normal_prob)
