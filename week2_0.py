principal = float(input("请输入本金"))       # 本金，单位：元
annual_rate = float(input("请输入年利率"))/100     # 年利率
years = int(input("请输入年份"))             # 年数

future_value = principal * (1 + annual_rate) ** years
profit = future_value - principal

print(round(future_value, 2))
print(round(profit, 2))