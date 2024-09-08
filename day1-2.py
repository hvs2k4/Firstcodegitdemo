print("hello world")

#string
st="upflairs pvt.ltd @ 12345"
print(st)

print(st[5])
print(st[-5])
print(st[5:-3])
print(st[:3])
print(st[::])
print(st[::2])  ##jump

st.upper() #builtin functions
print(st.upper())

st.lower()#builtinlower fn
print(st.lower())

ST="UPflairs fuck of "
print(ST.title())

st="upFLAIRSSSS FUCK OF"
print(st.capitalize())

sT="upflairs pvt. ltd  jaipur @12345"
print(sT.count('a'))

print(len(sT))# gives the length

print(st.find('p')) #gives the first index

print(sT.split())#divides words by spaces

print(sT.split('a'))#divides by given name

print(sT.replace('a','r'))#replaces the given value

print(sT.replace('upflairs','flipkart'))

print(sT.endswith('i')) #gives ture false
print(sT.startswith('u'))

##boolean data type
var1=True
var2=False
print(var1,var2)
print(type(var1),type(var2))

#list
## Array=similar data type collection of data items
#List is an alternative of array
lst=[10,20,30,40,50.25,2.3,'upflairs',True]
print(type(lst),lst)

#indexing in list
print(lst[3])
print(lst[-4])
print(lst[::])
print(lst[-1:])

appnd=lst.append('manshi') #add in list
print(lst)

pops=lst.pop() #remove
print(lst.pop())#to print the removed elment
lst.append('krish')
lst.pop(3)
print(lst)

lst[-1]='harsh' #update or replaces specified element
print(lst)

#add to specified place
lst.insert(2,'krish')
print(lst)

ls=[1,2,5,6,3,75,34,63]
ls.sort()
print(ls)

lstt=['krish','harsh','manish','rohit']
lstt.sort()#sorts the list
print(lstt)

ls.reverse()#reverses the elements
print(ls)

print(ls.index(34))#gives the index of specified elemenet

##list under list
lst1=[10,20,30,40,50,60,[True,85,41,54,63,'upflairs'],25]
print(lst1)
print(lst1[6])
print(lst1[5])
print(lst1[7])
lst1[6][5]='flipkart'
print(lst1[6])
lst1[6].insert(4,'flip')
print(lst1[6])


##----------Tuplee--------------
#tuples are immutable(cannot be changed once created)

tpl=()
print(type(tpl),tpl)

tple=(1,2,3,4,'krish','harsh')
#tpl.append('manish')#this cannot be done
print(tpl)

#with single item
tplee=(10,)
print(tplee)

tuppl= 10,20,30,40,50#this is also a tuple

#access=yes
#remove=no
#insert=no
#update=no


##-------SETS------------
st={}
print(st,type(st))
#doesnt allow duplicate values
#doesnt maintain order
#immutable
stt={25,41,54,21,16,84,1,2,5,49,54}
print(stt,type(stt))
#print(stt{3})#this cant be accesed
#stt.remove(16)#gives error
stt.discard(16)#no error
print(stt)

#stt{4}=353 @@invalid
print(stt)








