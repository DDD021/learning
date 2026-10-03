PV = float(input("请输入本金："))
r = float(input("请输入年利率："))
n = int(input("请输入投资年数："))
FV = PV * (1 + r) ** n
print("最终金额为：", round(FV, 2))