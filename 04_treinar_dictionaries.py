name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"

handle = open(name)

counts = dict() 

bigemail = None 
bigcount = None

for line in handle: 
    if line.startswith("From "): 
        senders = line.split()
        email = senders[1]
        
        counts[email]=counts.get(email,0) + 1
        
        if bigcount is None or bigcount < counts[email]: 
            bigcount = counts[email]
            bigemail = email
            
print(bigemail, bigcount)
