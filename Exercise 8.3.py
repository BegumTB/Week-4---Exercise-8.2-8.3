#!/usr/bin/env python
# coding: utf-8

# In[3]:


#previous code
# def is_palindrome(word):
#if len(word) <= 2 and word[0] == word[-1]:
#		print ("True")
#	elif first(word) == last(word):
#		print ("True")
#	else :
#		print ("False")

def is_palindrome(word):
    return word == word[::-1]


# In[2]:


print(is_palindrome('worw'))


# In[3]:


print(is_palindrome('begum'))


# In[4]:


print(is_palindrome('asddsa'))


# In[5]:


print(is_palindrome('1001'))


# In[4]:


print(is_palindrome('abcxcba'))


# In[5]:


print(is_palindrome('XYZ3ZYX'))


# In[ ]:




