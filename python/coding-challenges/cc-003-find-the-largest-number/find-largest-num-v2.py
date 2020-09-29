list1 = [] 
  
num = int(input("Enter number of elements in list as 5: ")) 
  
for i in range(1, num + 1): 
    ele = int(input("Enter elements: ")) 
    list1.append(ele) 

list1.sort()  

print("Largest element is:", list1[-1]) 