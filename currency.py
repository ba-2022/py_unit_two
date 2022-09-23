value = input("How much money would you like to withdraw today? Please enter a value in dollars and cents: ")

decimized_value = float(value)

hundred = int(decimized_value/100)

remainder = decimized_value % 100

tens = int(hundred/2)

dollar= int(5)

quarter= int(dollar*.25)


print(hundred, "hundreds")
print(remainder, "remainder")
print(tens, "tens")
print(dollar, "dollar bills")
print(quarter, "quarter")









#pennies = int(decimized_value*100)




