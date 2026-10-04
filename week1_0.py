principal = 8000       # 本金，单位：元
annual_rate = 0.04     # 年利率，8%写成0.08
years = 3             # 年数

future_value = principal * (1 + annual_rate) ** years
profit = future_value - principal

print(round(future_value, 2))
print(round(profit, 2))