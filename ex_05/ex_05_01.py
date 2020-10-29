#print the total, count, and average
total = 0
count = 0
while True:
    ques = input("Enter a number:")
    count += 1 
    if ques == "done":
        break
    else:
        try:
            iques = int(ques)
            total += iques
        except:
            print("Not a number")
            continue
       
print(total, count, total/count)

    
