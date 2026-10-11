# Spread Locator: Statistical Distribution Analysis Model

## Project overview
A mathematics and advanced-statistics project that studies e-commerce transaction amounts using probability distributions, Q-Q plots, transformations, z-scores, PDF and CDF.

## Files
- `Spread_Locator_Maths_Project.docx` — college-style project report with theory, methodology, results and conclusion.
- `Spread_Locator_Theory_Report.pdf` — theory and report PDF.
- `Spread_Locator_Dataset_and_Analysis.xlsx` — synthetic sample transaction dataset and analysis sheets.
- `spread_locator_analysis.py` — Python analysis script.
- `README_Spread_Locator.md` — this guide.

## Important data note
The included 500-row dataset is synthetic and is intended for demonstration because the assignment brief describes the schema but does not include a downloadable data file. Replace it with the actual course dataset before submitting if one is provided.

## Run
Install dependencies:
```bash
pip install numpy pandas scipy statsmodels matplotlib seaborn openpyxl
```
Keep the Python file and workbook in the same folder, then run:
```bash
python spread_locator_analysis.py
```

## Main questions answered
- Bernoulli and Binomial: transaction success indicator and grouped outcomes.
- Poisson: transactions per day.
- Log-normal and power-law: transaction amount modeling.
- Q-Q plot: visual check of normality.
- Box-Cox: transformation for positive skewed amounts.
- Z-scores and threshold: unusual amounts and amounts above ₹5,000.
- PDF/CDF: fitted density and cumulative probability.

## Interpretation caution
Model fit should be compared using suitable goodness-of-fit diagnostics and preferably AIC/BIC or out-of-sample validation. The fitted power-law family in SciPy is not by itself proof that the data follow a true power-law tail.
# Spread-Locator
