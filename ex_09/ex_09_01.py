name = input("Enter file name:")
handle = open(name)
emails = []
counts = dict()
large_word = None
large_num = None
for line in handle:
    if line.startswith("From "):
        sline = line.split()
        emails.append(sline[1])
for email in emails:
    counts[email] = counts.get(email, 0) + 1
for k,v in counts.items():
    if large_num == None or v > large_num:
        large_num = v
        large_word = k 
print(large_word, large_num)

#alternative solution
name = input("Enter file name:")
handle = open(name)
emails = []
counts = dict()
for line in handle:
    if line.startswith("From "):
        sline = line.split()
        emails.append(sline[1])
for email in emails:
    if email in counts:
        counts[email] += 1
    else:
for k,v in counts.items():
    if large_num == None or v > large_num:
        large_num = v
        large_word = k 
print(large_word, large_num)