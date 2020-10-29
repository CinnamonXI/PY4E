#3.1 conditionals
hours = input("Enter worked hours:")
fhour = float(hours)
ipay = input("Enter pay per hour:")
fpay = float(ipay)

if fhour >= 40:
    extra = fhour - 40
    pay = 40 * fpay
    new_pay = extra * (fpay * 1.5)
    print("Pay:", new_pay + pay)
else:
    print("Pay:", fhour * fpay)

