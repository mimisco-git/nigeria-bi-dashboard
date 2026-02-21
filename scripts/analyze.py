import pandas as pd

print("=== NIGERIA GDP ANALYSIS ===\n")

gdp = pd.read_csv('../outputs/gdp_growth_clean.csv')
print("GDP Growth Summary Statistics:")
print(gdp['gdp_growth'].describe().round(2))
print(f"\nBest growth year:  {gdp.loc[gdp['gdp_growth'].idxmax(), 'year']} → {gdp['gdp_growth'].max():.2f}%")
print(f"Worst growth year: {gdp.loc[gdp['gdp_growth'].idxmin(), 'year']} → {gdp['gdp_growth'].min():.2f}%")
print(f"Average growth (2014-2023): {gdp['gdp_growth'].mean():.2f}%")

print("\n=== INFLATION ANALYSIS ===\n")
inf = pd.read_csv('../outputs/inflation_clean.csv')
print("Inflation Summary Statistics:")
print(inf['inflation'].describe().round(2))
print(f"\nPeak inflation year: {inf.loc[inf['inflation'].idxmax(), 'year']} → {inf['inflation'].max():.2f}%")
print(f"Lowest inflation year: {inf.loc[inf['inflation'].idxmin(), 'year']} → {inf['inflation'].min():.2f}%")

print("\n=== NBS Q3 2024 KEY FIGURES ===")
nbs_data = {
    'Nominal GDP Q3 2024 (₦ Billion)': 71131.09,
    'Real GDP Growth Q3 2024 (%)': 3.46,
    'Services Contribution (%)': 53.58,
    'Agriculture Contribution (%)': 28.65,
    'Industries Contribution (%)': 17.77,
    'Oil GDP Share (%)': 5.57,
    'Non-Oil GDP Share (%)': 94.43,
    'Oil Production Q3 2024 (MBPD)': 1.47
}
for k, v in nbs_data.items():
    print(f"  {k}: {v}")

print("\n=== EXPORT BREAKDOWN Q1 2025 ===")
exports = {
    'Crude Petroleum': 62.89,
    'Natural Gas (LNG)': 9.38,
    'Other Petrol. Gases': 8.65,
    'Urea/Fertiliser': 4.15,
    'Cocoa Beans': 5.96,
    'Cashew & Sesame': 1.39,
}
for product, share in exports.items():
    bar = '█' * int(share / 2)
    print(f"  {product:<25} {share:>6.2f}%  {bar}")

summary = pd.DataFrame(list(nbs_data.items()), columns=['Indicator', 'Value'])
summary.to_csv('../outputs/analysis_summary.csv', index=False)
print("\nAnalysis summary saved to outputs/analysis_summary.csv")
