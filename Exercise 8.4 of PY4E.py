fname=input("Enter file name:")
fh=open(fname)
lst=list()                 #list for the output
for line in fh:          #to read every line in the file
    words=line.rstrip().strip() #to eliminate the white spaces
    for new in words:    #Check every element
       if new in lst:    #If element is repeated
         continue:       #Goto next loop
       else:             #If not in list
         lst.append(new)  #Add the element to the list
lst.sort()            #Sort the list in ascending order
print(lst)     #Print the list
#Code by Harsha R
