
user_name = input("what is your name?")

print("wow,what a unique name! Mine is chatbot")

place = input("where are you from?")

print("Oh my god! I wish I was from there")

number = input("whats your favorite number?")

my_number = float(number) * 5

print("cool! my number is five times as much as yours,", my_number)

dream_car = input("what is your dream car?")

cost_of_car= float(input("I'm sure that is a pricey car, how much does a " + dream_car + " cost?"))

interest_rate = input("wow! what is the yearly interest car for that?")

years_loan = input("And if you had to take a loan to buy the the car, how many years would you take the loan out for?" )

month_of_payment = float(years_loan) * 12

monthly_interest = float(interest_rate)/ 100 / 12

monthly_payment = (monthly_interest  * cost_of_car ) / (1 -( 1 + monthly_interest ) ** -month_of_payment)

print("If you bought the car you would have a monthly_payment of", monthly_payment ,"that totals to", cost_of_car)





































