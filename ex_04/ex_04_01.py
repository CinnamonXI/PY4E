#a function that computes total pay
def computepay(h,r):
    try:
        fhour = float(h)
        fpay = float(r)
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
    return xp

hrs = input("Enter Hours:")
rate = input("Enter rate:")
p = computepay(hrs,rate)
print("Pay", p)