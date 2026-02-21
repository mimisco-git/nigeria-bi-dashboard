import pandas as pd
import sqlite3

conn = sqlite3.connect('../nigeria_business.db')

# Load GDP data
gdp = pd.read_csv('../outputs/gdp_growth_clean.csv')
gdp.to_sql('gdp_growth', conn, if_exists='replace', index=False)
print("GDP table loaded:", len(gdp), "rows")

# Load inflation data
inf = pd.read_csv('../outputs/inflation_clean.csv')
inf.to_sql('inflation', conn, if_exists='replace', index=False)
print("Inflation table loaded:", len(inf), "rows")

# SQL Query 1
print("\n=== SQL: Years with GDP Growth > 2% ===")
result = pd.read_sql("""
    SELECT year, ROUND(gdp_growth,2) as growth_pct 
    FROM gdp_growth 
    WHERE gdp_growth > 2 
    ORDER BY growth_pct DESC
""", conn)
print(result.to_string(index=False))

# SQL Query 2
print("\n=== SQL: Average inflation by period ===")
result2 = pd.read_sql("""
    SELECT 
        CASE WHEN year < 2020 THEN '2014-2019' ELSE '2020-2023' END as period,
        ROUND(AVG(inflation), 2) as avg_inflation
    FROM inflation
    GROUP BY period
""", conn)
print(result2.to_string(index=False))

# SQL Query 3
print("\n=== SQL: GDP contraction years ===")
result3 = pd.read_sql("""
    SELECT year, ROUND(gdp_growth,2) as growth_pct
    FROM gdp_growth
    WHERE gdp_growth < 0
    ORDER BY year
""", conn)
print(result3.to_string(index=False))

conn.close()
print("\nDatabase saved: nigeria_business.db")
