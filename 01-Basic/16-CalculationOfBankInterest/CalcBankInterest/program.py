# 1000$ - r = 0.2
# 1200$


# 1000 ?-> 1200$ => 1000 + (0.2 * 1000) = 1200$
# lastYearIncome *
def CalcBankInvestment(initialMoney, numberOfYears, rate):
    lastYearIncome = initialMoney
    if numberOfYears > 0:
        for i in range(numberOfYears):
            lastYearIncome *= 1 + rate

    return lastYearIncome

print(CalcBankInvestment(1000, 1, 0.02))
# Output:
    # 1020.0


