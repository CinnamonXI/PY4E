#files processing
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    newline = line.rstrip()
    print(newline.upper())
