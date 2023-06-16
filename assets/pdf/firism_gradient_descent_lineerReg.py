# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 17:27:59 2022

@author: firat ismailoglu
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def fonk(x):
    return np.square((x-2))+6

def fonk_turev(x):
    return 2*x-4

alfa=10
x=100
maxIter=10
fonk_degerleri=np.zeros((500,1))
fonk_degerleri[0]=fonk(x)

for i in range(1,maxIter):
    x=x-alfa*(fonk_turev(x))
    fonk_degerleri[i]=fonk(x)
    
plt.plot(np.arange(maxIter),fonk_degerleri) 
plt.xlabel("Iterasyon Sayisi",fontsize=20)  
plt.ylabel("Fonksiyon Degeri",fontsize=20)
plt.show()
#############################################

data=pd.read_excel("araba.xlsx")
data=np.array(data)

X=data[:,0]
y=data[:,1]
alfa=0.001
maxIter=50
w0,w1=np.random.rand(2)
for i in range(maxIter):
    t1=0
    t2=0
    for j in range(5):
        t1+=w0+w1*X[j]-y[j]
        t2=(w0+w1*X[j]-y[j])*X[j]
    w0=w0-alfa*(1/5)*t1
    w1=w1-alfa*(1/5)*t2
    
#################################
X=np.reshape(X,(5,1))
X=np.concatenate((np.ones((5,1)),X),axis=1)

w=np.dot(np.dot(np.linalg.inv(np.dot(X.T,X)),X.T),y)
w[0]+17.8*w[1]
    
    
    
        
        
        
        
    










    
    