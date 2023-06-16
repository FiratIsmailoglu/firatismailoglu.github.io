# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 09:19:25 2022

@author: firat ismailoglu
"""

import numpy as np
import pandas as pd

data=pd.read_excel("kaggle_titanic.xlsx")
data=np.array(data)
random_siralama=np.random.permutation(1309)
data=data[random_siralama,:]

egitim=data[:1000,:]
test=data[1000:,:]

egitim_X=egitim[:,:-1]
egitim_y=egitim[:,-1]

test_X=test[:,:-1]
test_y=test[:,-1]
##############################################
################ NB ##########################
olenlerin_indisleri=np.where(egitim_y==0)[0]
egitim_X_olenler=egitim_X[olenlerin_indisleri,:]
global olme_olasiligi
olme_olasiligi=len(olenlerin_indisleri)/egitim_X.shape[0]

yasayanlarin_indisleri=np.where(egitim_y==1)[0]
#yasayanlarin_indisleri=np.setdiff1d(np.arange(1000),olenlerin_indisleri)
egitim_X_yasayanlar=egitim_X[yasayanlarin_indisleri,:]
global yasama_olasiligi
yasama_olasiligi=len(yasayanlarin_indisleri)/egitim_X.shape[0]

def NB_siniflandir(x,egitim_X_olenler,egitim_X_yasayanlar):
    p_olme=1
    olenler_sayisi=egitim_X_olenler.shape[0]
    p_yasama=1
    yasayanlarin_sayisi=egitim_X_yasayanlar.shape[0]
    for i in range(len(x)):
        p_olme=p_olme*((len(np.where(egitim_X_olenler[:,i]==x[i])[0])/olenler_sayisi)+0.000001)
        p_yasama=p_yasama*((len(np.where(egitim_X_yasayanlar[:,i]==x[i])[0])/yasayanlarin_sayisi)+0.000001)
    
    p_olme=p_olme*olme_olasiligi
    p_yasama=p_yasama*yasama_olasiligi
    if p_olme>p_yasama:
        return 0
    else:
        return 1
    
def skor(y_tahmin,y_gercek):
    toplam_ornek=len(y_tahmin)
    t=0
    for i in range(toplam_ornek):
        if y_tahmin[i]==y_gercek[i]:
            t+=1
    return (t/toplam_ornek)*100

##################Siniflandirma##########
test_ornegi_sayisi=test_X.shape[0]
tahminler=np.zeros((test_ornegi_sayisi,1))
for i in range(test_ornegi_sayisi):
    x=test_X[i,:]
    tahmin_edilen_sinif=NB_siniflandir(x,egitim_X_olenler,egitim_X_yasayanlar)
    tahminler[i]=tahmin_edilen_sinif
####################################33
from hafta4_knn import knn_siniflandirma

tahminler_knn=np.zeros((test_ornegi_sayisi,1))
for i in range(test_ornegi_sayisi):
    x=test_X[i,:]
    tahmin_edilen_sinif=knn_siniflandirma(x,egitim_X,egitim_y,5)
    tahminler_knn[i]=tahmin_edilen_sinif
    
    
    
    
    
    
    
    
    
    
    
    
    










