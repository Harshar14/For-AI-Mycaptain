   
test_list = [1, 4, 5, 6, 7, 3] 
  
 
print ("The original list is : " + str(test_list)) 

var1, var2, var3 = [test_list[i] for i in (1, 3, 5)] 

print ("The variables are : " +  str(var1) + 
                           " " + str(var2) +
                            " " + str(var3))
