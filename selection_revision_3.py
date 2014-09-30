#Amin Hagos
#30-09-2014
#Development Exercises Task 3

hours_worked = int(input("please enter the amount of hours you have worked this week:" ))
hour_pay = int(input("please enter the amount of money you earn per hour: "))

if hours_worked <= 40:
    money_earned = hour_pay * hours_worked
    print("you will recieve £{0} this week!".format(money_earned))

elif 40 < hours_worked < 60:
    extra_hours = hours_worked - 40
    extra_rate = hour_pay * 1.5
    extra_cash = extra_hours * hour_pay
    money_earned2 = (40 * hour_pay) + extra_cash
    print("you will recieve £{0} this week!".format(money_earned2))
else:
    print("the working hours you have entered is invalid.")
