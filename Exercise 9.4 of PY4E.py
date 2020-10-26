name=input("Enter file name:")
if len(name)<1 : name="mbox-short.txt"
handle=open(name)
abc=list()
for line in handle:
   if not line.startswith("From"): continue
   line = line.split()
   abc.append(line[1])
count=dict()
for word in abc:
   count[word]=count.get(word,0)+1
bigcount=None
bigword=None
for word , count in count.items():
   if bigcount is None or count > bigcount:
      bigword=word
      bigcount=count
print(bigword ,  bigcount )
