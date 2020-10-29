#3.3 grade computing
score = input("Enter your score:")
fscore = float(score)

if fscore > 1 or fscore < 0:
    print("Out of Range") 
elif fscore >= 0.9:
    print("A")
elif fscore >= 0.8:
    print("B")
elif fscore >= 0.7:
    print("C")
elif fscore >= 0.6:
    print("D")
else:
    print("F")