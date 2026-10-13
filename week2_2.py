pay=float(input("买入单价"))
sale=float(input("卖出单价"))
amount=int(input("数量"))
tax=int(input("手续费"))
profit=(sale-pay)*amount-tax
profit_rate=profit/(pay*amount)
print(profit)
print(round(profit_rate*100,2),"%")