# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 22:27:28 2022

@author: Prashanth K
"""

import PyPDF2
a=PyPDF2.PdfFileReader('split_by_page1.pdf')
b=PyPDF2.PdfFileReader('split_by_page2.pdf')
c=PyPDF2.PdfFileReader('split_by_page3.pdf')
l=a.getPage(0).extractText()
print(l)
m=b.getPage(0).extractText()
print(m)
n=c.getPage(0).extractText()
print(n)
with open("text1.txt","w") as f1:
    f1.write(l)
with open("text2.txt","w") as f2:
    f2.write(m)
with open("text3.txt","w") as f3:
    f3.write(n)
with open("text123.txt","w") as f123:
    f123.write(l+"\n"+m+"\n"+n)
