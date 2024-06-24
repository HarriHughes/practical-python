# mortgage.py
principal = 50000
rate = 0.02
payment = 1234
totalPaid = 0.0

while principal > 0:
    principal = principal * (1+rate/12) - payment
    totalPaid = totalPaid+ payment

    print('total Paid', totalPaid)
# Exercise 1.7
