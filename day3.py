##Dictionary

dict={'A':23,'B':324,'C':45,'D':56}
print(dict,type(dict))

dt2={0:10,1:20,3:40}
print(dt2)

dct2={0:[10],1:(20),3:{34}}
print(dct2)

print(dict['C'])
print(dt2[0])

#insert an pair
dict['D']=400
dict['e']=50
print(dict)

#remove
dict.pop('C')
print(dict)

print(dict.keys())#print keys

print(dict.values())# print values

stu_marks={"name":['manshi','ram','krishna','harsh'],
           "marks":[25,41,52,34],
           "subject":'Science'}
print(stu_marks)
print(type(stu_marks))

#remove specific values
stu_marks['name'].pop()
stu_marks['marks'].pop()
print(stu_marks)

#insert any element to specific place
stu_marks['name'].insert(1,'abhishek')
stu_marks['marks'].insert(1,55)
print(stu_marks)

#update value
stu_marks['name'][1]='abhishek'

#update string values name
stu_marks['subject']=("data sciencess","sciences")
print(stu_marks)

#no. of values 
print(len(stu_marks['name']))


##=========Conditional statements=========

age= 21
if age > 21:
    print('you can vote')
else:   
    print('you cannot vote')
    

#=========ATM SIMULATION PROGRAM=======
name = input('Enter your name:')
print('hello', name) 
message="""
How may i help you

Please select ant of them options
type 1 >>> CHECK BALANCE
type 2 >>> DEPOSIT
type 3 >>> WITHDRAWL
"""
print(message) 
task=int(input('plz choose any option: '))#type casted to int by default string
available_amt=5000

if task>=1 and task<=3:
    print("welcome")
    
    if task==1:#check balance
        print("you're available balance is :",available_amt)
    
    elif task==2:#deposit amt
        #three dots replacement of pass
        deposit_amt=int(input("enter your deposit amount: "))
        if deposit_amt>=500:
            available_amt += deposit_amt
            print("your amt has been deposited")
            print("available balance:", available_amt )
        else:
            print("pls deposit atleast 500 or more")
               
    else:#withdrawl
        withdrawl_amt= int(input("enter the amount you want:"))
        if withdrawl_amt>=500:
            available_amt -= withdrawl_amt
            print("processing")
            print("successfully withdrawed ",withdrawl_amt)
            print("available balence",available_amt)
else:
    print("enter a valid input ")
    


    




