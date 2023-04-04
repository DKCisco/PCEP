changeAmt = int(input("Enter the change due: "))

numQtrs = int(changeAmt // 25) #Figure out the number of quarters
changeAmt = int(changeAmt - (numQtrs * 25))

numDimes = int(changeAmt // 10) #Figure out the number of dimes
changeAmt -= (numDimes * 10)

numNickels = int(changeAmt //5) #Figure out number of nickels
changeAmt -= (numNickels * 5)

numPennies = int(changeAmt // 1) #Figure out number of pennies
changeAmt -= (numPennies * 1)

print("Quarters: ",numQtrs)
print("Dimes: %s" % numDimes)
print("Nickels: {}".format(numNickels))
print(f"Pennies: {numPennies}")
print(f"Final change amount: {changeAmt}")