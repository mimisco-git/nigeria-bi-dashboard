import pandas as pd

print("=== CLEANING WORLD BANK DATA ===")
wb = pd.read_csv('../data/API_NGA_DS2_en_csv_v2_8585.csv', skiprows=4)

# Extract GDP growth
gdp = wb[wb['Indicator Name'] == 'GDP growth (annual %)'].copy()
years = [str(y) for y in range(2014, 2024)]
gdp_clean = gdp[['Country Name'] + years].melt(
    id_vars='Country Name', var_name='year', value_name='gdp_growth'
)
gdp_clean.columns = ['country', 'year', 'gdp_growth']
gdp_clean['year'] = gdp_clean['year'].astype(int)
gdp_clean.dropna(inplace=True)
gdp_clean.to_csv('../outputs/gdp_growth_clean.csv', index=False)
print("GDP growth data saved.")
print(gdp_clean.to_string())

print("\n=== CLEANING INFLATION DATA ===")
inf = wb[wb['Indicator Name'] == 'Inflation, consumer prices (annual %)'].copy()
inf_clean = inf[['Country Name'] + years].melt(
    id_vars='Country Name', var_name='year', value_name='inflation'
)
inf_clean.columns = ['country', 'year', 'inflation']
inf_clean['year'] = inf_clean['year'].astype(int)
inf_clean.dropna(inplace=True)
inf_clean.to_csv('../outputs/inflation_clean.csv', index=False)
print("Inflation data saved.")
print(inf_clean.to_string())

print("\n=== CLEANING NBS GDP EXCEL DATA ===")
xl = pd.ExcelFile('../data/Q3_GDP_2024.xlsx')
print("Available sheets:", xl.sheet_names)

# Read the real GDP growth sheet
real_growth = xl.parse('real gdp growth rate %', header=None)
print("\nReal GDP growth sheet preview:")
print(real_growth.head(15).to_string())
real_growth.to_csv('../outputs/nbs_real_gdp_growth_raw.csv', index=False)
print("NBS real GDP growth saved.")

print("\n=== CLEANING TRADE DATA ===")
trade_xl = pd.ExcelFile('../data/Q1_2025_Foreign_Trade_Statistics_Tables.xlsx')
products = trade_xl.parse('PRODUCT RANKING')
print("\nTrade product ranking preview:")
print(products.iloc[1:16].to_string())
products.to_csv('../outputs/trade_products_raw.csv', index=False)
print("Trade data saved.")

print("\n=== ALL CLEANING COMPLETE ===")
print("Output files in ../outputs/")
