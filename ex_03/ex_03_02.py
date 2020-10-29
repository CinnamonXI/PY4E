#3.2 conditionals with try--except
hours = input("Enter worked hours:")
ipay = input("Enter pay per hour:")
try:
    fhour = float(hours)
    fpay = float(ipay)
except:
    print("Try again with a number")
    quit()

if fhour >= 40:
    extra = fhour - 40
    pay = 40 * fpay
    new_pay = extra * (fpay * 1.5)
    xp = new_pay + pay
else:
    xp = fhour * fpay
print("Pay:", xp)

