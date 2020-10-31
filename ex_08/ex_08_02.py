fname = input("Enter file name: ")
if len(fname) < 1 : 
    fname = "mbox-short.txt"

fh = open(fname)
count = 0
for line in fh:
    nline = line.rstrip()
    if nline.startswith("From") and nline.endswith("2008"):
        sline = line.split()
        email = sline[1]
        print(email)
        count += 1

print("There were", count, "lines in the file with From as the first word")
