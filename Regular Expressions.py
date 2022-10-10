#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Find Spider-Man, Spiderman, SPIDER-MAN, etc.
import re
dailybugle = 'Spider-Man Menaces City!'
pattern = r'spider[- ]?man'
if re.match(pattern, dailybugle, re.IGNORECASE):
    print (dailybugle)


# In[3]:


#Match dates formatted like MM/DD/YYYY, MM-DD-YY,...
import re
date = '12/30/1969'
regex = re.compile(r'^(\d\d)[-/](\d\d)[-/](\d\d(?:\d\d)?)$')
match = regex.match(date)
if match:
    month = match.group(1) #12
    day = match.group(2) #30
    year = match.group(3) #1969


# In[4]:


#Convert <br> to <br /> for XHTML compliance
import re
text = 'Hello world. <br>'
regex = re.compile(r'<br>', re.IGNORECASE);
repl = r'<br />'
result = regex.sub(repl,text)


# In[5]:


pattern=re.compile('ab')
matcher=pattern.finditer("abaababa")
count=0
for match in matcher:
    count+=1
    print(f"{match.start()}...{match.end()}...{match.group()}")
    
print(f'The number of occurrences : {count}')


# In[6]:


count=0
matcher=re.finditer("ab","abaababa")
for match in matcher:
    print(match)


# In[7]:


matcher=re.finditer('[^abc]',"a7b@k9z")
for match in matcher:
    print(match.start(),"......",match.group())


# In[8]:


matcher=re.finditer('[0-9]',"a7b@k9z")
for match in matcher:
    print(match.start(),"......",match.group())


# In[9]:


matcher=re.finditer('[^a-zA-Z0-9]',"a7b@k9z")
for match in matcher:
    print(match.start(),"......",match.group())


# In[10]:


matcher=re.finditer("a","abaabaaab")
for match in matcher:
    print(match.start(),"......",match.group())


# In[11]:


matcher=re.finditer("a+","abaabaaab")
for match in matcher:
    print(match.start(),"......",match.group())


# In[12]:


n=input("Enter number:")
m=re.fullmatch("[7-9]\d{9}",n)
if m!= None:
    print("Valid Mobile Number")
else:
    print("Invalid Mobile Number")


# In[ ]:


import re,urllib
import urllib.request
u=urllib.request.urlopen("https://www.redbus.in/info/contactus")
text=u.read()
numbers=re.findall("[0-9-]{7}[0-9-]+",str(text),re.I)
for n in numbers:
    print(n)


# In[ ]:




