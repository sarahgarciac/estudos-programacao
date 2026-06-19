fname = input("Enter file name: ")
fh = open(fname, "r")
count = 0 
n = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    if line.startswith("X-DSPAM-Confidence:"): 
       count = count + 1
       x = line.find(":")
       splic = line [x + 1 :]
       fsplic = float(splic)
       n = n + fsplic
       

fcount = float(count)
av = n / fcount

print("Average spam confidence:", av)
