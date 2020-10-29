numbers=[]
while True:
    ques = input("Enter a number: ")
    if ques == "done":
        break
    else:
        try:
            iques = int(ques)
            numbers.append(iques)
        except:
            print("Invalid input")
            continue
        numbers.sort(reverse=False)
print("Maximum is", numbers[-1])
print("Minimum is", numbers[0])