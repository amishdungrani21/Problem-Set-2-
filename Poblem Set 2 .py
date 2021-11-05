#!/usr/bin/env python
# coding: utf-8

# # Question 1 

# In[1]:


a = 0
def b():
    global a
    a = c(a)
def c(a):
    return a + 2


# In[2]:


b()
b()
b()
a


# # Question 2

# In[3]:


def file_length(file_name):
    file = open(file_name)
    contents = file.read()
    file.close()
    print(len(contents))


# In[4]:


file_length('Filetext.txt')


# # Question 3

# In[5]:





# In[6]:





# #     Question 4    

# In[16]:


def collatz(b):
    l=[b]
    if b==1:
        return [1]                  
    elif b%2==0:
        l.extend(collatz(b/2))      
    else:
        l.extend(collatz(b*3+1))    
    return l

print(collatz(22))


# # Question 5

# In[17]:


def binary( decimal_number ):
    if decimal_number == 0:
        return 0
    else:
        return (decimal_number % 2 + 10 * binary(int(decimal_number // 2)))


# In[18]:


binary(9)


# # Question 8

# a) SELECT Temperature(C),FROM Weather;
# b) SELECT DISTINCT City FROM Weather;
# c) SELECT * FROM Weather WHERE Country='India';
# d) SELECT * FROM Weather WHERE Season='Fall';
# e) SELECT City,Country,Season FROM Weather WHERE Rainfall(mm) BETWEEN 200 AND 400;
# f) SELECT City, Country FROM Weather HAVING min(Temperatutr(C)) > 20;
# g) SELECT AVG(Rainfall(mm)) FROM Weather;
# h) 

# # Question 9

# a)

# In[28]:


words = ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 
'the', 'lazy', 'dog']
newwords = []
for words in words:
    newwords.append(words.upper())
print(newwords)


# b)

# In[29]:


words = ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 
'the', 'lazy', 'dog']
newwords = []
for words in words:
    newwords.append(words.lower())
print(newwords)


# c)

# In[30]:


number = [3, 5, 5, 3, 5, 4, 3, 4, 3]
print (number)


# In[ ]:




