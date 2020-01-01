
# coding: utf-8

# Data Types

# Numbers

# In[1]:


1 + 1


# In[2]:


1 * 3 


# In[3]:


1/2


# In[4]:


2**4


# In[5]:


4 % 2


# In[8]:


5 % 2


# In[9]:


(5+5) * (10+7)


# In[10]:


name_var = 2
x = 2
y = 3
z = x + y  


# In[12]:


name_var


# In[13]:


z


# In[14]:


'hello there'


# In[15]:


"This text is in double quotes"


# In[16]:


"There are many number's here"


# In[17]:


x = "Prasad"


# In[18]:


x


# In[19]:


print(x)


# Assignment

# In[20]:


age = 60
name = 'John'


# In[22]:


print("{} is {} years old".format(name,age))


# In[23]:


print("{one} is {two} years old".format(one = name, two = age))


# List

# In[24]:


['a','e','i','o','u']


# In[25]:


[10,11,12]


# In[26]:


['hello',1]


# In[27]:


[4,5,[3,'blah']]


# In[28]:


my_list = [9,8,7,6]


# In[29]:


my_list.append(8)


# In[30]:


my_list


# In[31]:


my_list.append('hi')


# In[32]:


my_list


# In[33]:


my_list[0]


# In[34]:


my_list[5]


# In[35]:


my_list[10]


# In[36]:


my_list[2:]


# In[39]:


my_list[2:4]


# In[40]:


my_list[:]


# In[41]:


my_list[:4]


# In[42]:


my_list[3:5]


# In[43]:


my_list


# In[44]:


my_list[0] = 56


# In[45]:


my_list


# In[46]:


listy = [1,2,[3,5,['blah','blah']]]


# In[47]:


listy[3]


# In[48]:


listy[2]


# In[49]:


listy[2][2]


# In[50]:


listy[2][2][0]


# In[51]:


listy[2][2][1]


# Dictionary

# In[54]:


d = {'key1' : 'value1','key2':5}


# In[55]:


d


# In[56]:


d['key2']


# Boolean

# In[57]:


True


# In[58]:


False


# In[59]:


d2 = {'key1':[1,2,3,4,5]}


# In[60]:


d2['key1'][3]


# In[61]:


d2['key1'][2:]


# Tuple

# In[62]:


t = (2,4,6,8,10)
t


# In[63]:


t[3]


# In[64]:


t[3] = 5


# Tuple is immutable

# In[65]:


s = {1,2,3,4,5,6,7,8}
s


# In[66]:


s1 = {1,1,1,2,2,2,3,3,3}
s1


# In[67]:


s.add(9)


# In[68]:


s


# Comparison Operators

# In[69]:


1 > 4


# In[70]:


3 > 1


# In[71]:


4 < 6


# In[72]:


2 >= 3


# In[73]:


4 <= 4


# In[74]:


4 == 5


# In[75]:


4 ==4


# In[77]:


'hi' == 'hello'


# In[78]:


4 != 7


# Logic Operators

# In[79]:


(3>2) and (2>1)


# In[80]:


(3<1) and (8>3)


# In[81]:


(4>7) or (6==6)


# In[82]:


(8>3) or (4<3) or (9<11) or ('r'=='r')


# if, if else, if elif else statements

# In[83]:


if 8>4:
    print("I win!!")


# In[84]:


if 3==4:
    print("This is equal")
else:
    print("Not equal")
        


# In[86]:


if 1>3:
    print("First")
elif 4<1:
    print("Middle")
elif 4>1:
    print("Second elif")
else:
    print("Last")


# for loop

# In[87]:


seq = [1,2,3,4,5]
seq


# In[88]:


for item in seq:
    print(item)


# In[89]:


for element in seq:
    print("Yep!")


# In[90]:


for num in seq:
    print(num + num)


# In[91]:


for iterator in seq:
    print('HaHaHa HoHoHo')


# while loop
# A while loop helps in running some condition or a piece of code while the condition holds true

# In[1]:


x = 1
while x < 10:
    print("The value of x is being printed as x")
    x = x + 1


# In[1]:


y = 1
while y < 5:
    print("The value of y is {}".format(y))
    y= y+1


# range

# In[2]:


range(5)


# In[3]:


range(10)


# In[7]:


for x in range(10):
    print(x)


# In[5]:


range(5)


# In[6]:


list(range(0,5))


# List Comprehension

# In[8]:


z = [1,2,3,4]


# In[9]:


z


# In[10]:


o = []
for item in z:
    o.append(item**2)
print(o)


# In[12]:


q = [item**2 for item in z]


# In[13]:


print(q)


# Functions in Python

# In[14]:


def func_name(param = "default"):
    '''doc string goes here'''
    print(param)


# In[15]:


func_name


# In[17]:


func_name()


# In[19]:


func_name("New Name")


# In[20]:


def find_sq(num):
    sq = num**2
    print("The square of the number you gave is {}".format(sq))


# In[21]:


find_sq(4)


# In[22]:


def find_sq2(num):
    return num**2


# In[23]:


find_sq2(9)


# Lambda Expressions

# In[25]:


def even_op(var):
    return var*2


# In[27]:


even_op(2)


# In[28]:


lambda var: var*2


# In[29]:


def find_cube(num):
    return num**3


# In[30]:


find_cube(4)


# In[31]:


lambda num: num**3


# maps and filter

# In[32]:


seq = [1,2,3,4,5]


# In[33]:


seq


# In[36]:


map(even_op,seq)


# In[37]:


list(map(even_op,seq))


# In[38]:


list(map(find_cube,seq))


# In[40]:


list(map(lambda var: var**3,seq))


# In[41]:


list(map(lambda var: var*2,seq))


# filter

# In[42]:


seq = [1,2,3,4,5]


# In[44]:


filter(lambda var: var%2==0,seq)


# In[45]:


list(filter(lambda var: var%2==0,seq))


# Methods

# In[46]:


st = "Hello, my name is Sam!"


# In[47]:


st.lower()


# In[48]:


st.upper()


# In[49]:


st.split()


# In[50]:


tweet = 'Go Sports! #Sports'


# In[51]:


tweet.split('#')


# In[52]:


tweet.split('#')[0]


# In[53]:


tweet.split('#')[1]


# In[54]:


d = {'key1': 'item1','key2':'item2'}


# In[55]:


d


# In[56]:


d.keys()


# In[57]:


d.items


# In[58]:


d.items()


# In[59]:


lst = [1,2,3]


# In[60]:


lst.pop()


# In[61]:


lst


# In[63]:


'x' in [1,2,3]


# In[64]:


'x' in ['x','y','z']

