#----FOR LOOP----------------

for var in range (100):
    print("upflairs",var)
    
    
company = "upflairs"
stu_name = ['manshi','abhishek','mohit','sachin']
stu_marks = (85,41,63,96,14,25)
##dict
dict = {'A':10,'B':20,'C':30}

for char in company:
    print(char)
for char in stu_name:
    print(char)
    
for i in dict:
      print(i)  
      
numbers= [323,51,122,3,45,123,5,1,11,56,4,54,51,]

count=0
for i in numbers:
    if i == 45:
        print(count)
    
    else:
        count = count+1    
no=0
for char in numbers:
    if char <=50:
        print(no)
        no += 1
    

##=============WHILE LOOP========================
"""initialize
   while condition:
   
   increment"""
   
i=0
while i<= 10:
    print("upflairs",i)
    i += 1


#Break keyword used to stop loop 
for i in range(11):
    print(i)
    if i ==5:
        break

#continue ignore or skips the condition
for i in range(11):
    print(i)
    if i==5:
        continue

cont=0
for i in range(10):
    cont +=1
    continue

print(cont)

cont=0
for i in range(10):
    continue
    cont +=1
    

print(cont)

##=============FUNCTIONS============

#creating a function

age =[12,20,30,40,50,60,70,80,90]
age2=[1,2,3,4,5]


def my_len(ls): #here  ls is a parameter
    count = 0
    for i in ls:
        count += 1
    return count   #return acts as a break statemenet
                    

print(my_len(age))  
print(my_len(ls=age))#here is argument when we call a funtion and use parameter
print(my_len(age2))

noo=[2,3,-4,65,3,4,3]
print(min(noo))

def find_minimum(numbers):
    if not numbers:
         return None  # Return None if the list is empty
    min_num = numbers[0]  # Initialize min_num with the first element
    for num in numbers:
        if num < min_num:
            min_num = num  # Update min_num if a smaller number is found
    return min_num

# Example usage:
my_list = [5, 2, 8, 1, 10]
result = find_minimum(my_list)
print(f"The minimum number in the list is: {result}")

# def my_min(numbers):
#     min_no = numbers[0]
#     for num in numbers:
#         if num<mn:
#             min_no= num
#     return min_no        
        
    
# print(my_min(noo))       



