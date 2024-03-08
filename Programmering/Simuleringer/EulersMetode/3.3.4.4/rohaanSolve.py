fund = 0
time = 0
maxTime = 40
growthFactor = 0
growthFactorIncecrement = 0.000001
periodicIncrease = 1000
targetFundValue = 47900

while fund < targetFundValue:
    time = 0
    fund = 0
    growthFactor += growthFactorIncecrement
    while time < maxTime:
        fund *= 1 + growthFactor
        fund += periodicIncrease
        time += 1
print(f"Growthfactor: {round(growthFactor, 6)}\tFund: {round(fund, 6)}")