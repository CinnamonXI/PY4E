fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    slines = line.rstrip()
    words = slines.split()
    for word in words:
        if word not in lst:
            lst.append(word)
print(sorted(lst))