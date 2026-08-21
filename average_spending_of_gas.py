def average(*gas, kilometar):
    average = gas / (kilometar / 100)
    print(average)
    return round(average, 2)
     
kilometar = int(input("Please insert lenght of the route: "))
gas = int(input("Spend liters of gas: "))
average(gas,kilometar)
