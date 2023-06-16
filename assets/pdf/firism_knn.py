# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 17:55:38 2022

@author: firat ismailoglu
"""
import pandas as pd
import numpy as np
import statistics as st #mode fonksiyonu bu kutuphanenin icinde

#bir fonksiyonun disinda tanimlanan degisklenler fonkisyonun icinde de kullanilabilir

def train_val_test_split(full_data,egitim_rate,val_rate):
    #oncelikle tüm satirlar bir karalım
    global toplam_ornek #bu global bir degisken olsun diger fonksiyonlarda da kullaniriz/cagiririz
    toplam_ornek=full_data.shape[0]
    toplam_sinif_sayisi=len(np.unique(full_data[:,-1]))
    egitim_ornegi_sayisi=np.ceil(toplam_ornek*egitim_rate).astype(int)
    val_ornegi_sayisi=np.ceil(toplam_ornek*val_rate).astype(int)
    looptan_cikma=True
    while looptan_cikma:
        random_siralama=np.random.permutation(toplam_ornek)
        full_data=full_data[random_siralama,:]
        X_egitim=full_data[:egitim_ornegi_sayisi,:-1]
        y_egitim=full_data[:egitim_ornegi_sayisi,-1] #burada tüm siniflarin olmasini istiyoruz
        if len(np.unique(y_egitim))==toplam_sinif_sayisi:
            looptan_cikma=False
    
    X_val=full_data[egitim_ornegi_sayisi:egitim_ornegi_sayisi+val_ornegi_sayisi,:-1]
    y_val=full_data[egitim_ornegi_sayisi:egitim_ornegi_sayisi+val_ornegi_sayisi,-1]
    
    X_test=full_data[egitim_ornegi_sayisi+val_ornegi_sayisi:,:-1]
    y_test=full_data[egitim_ornegi_sayisi+val_ornegi_sayisi:,-1]
    return X_egitim,X_val,X_test,y_egitim,y_val,y_test

def oklid_uzaklik(x1,x2):
    #burada x1 ve x2 ayni boyutta iki vektör
    uzaklik=np.sqrt(np.sum(np.square(x1-x2)))
    return uzaklik

def min_max_normalizasyon(data):
    final_data=np.copy(data)
    #bunu kolon kolon ouşturacağız
    data_sayisi=final_data.shape[0]
    ozellik_sayisi=final_data.shape[1]
    for i in range(ozellik_sayisi):
        max_deger=np.max(final_data[:,i])
        min_deger=np.min(final_data[:,i])
        if max_deger==min_deger:
            final_data[:,i]=0
        else:
            for j in range(data_sayisi):
                final_data[j,i]=(final_data[j,i]-min_deger)/(max_deger-min_deger)
            
    return final_data

def skor(y_tahmin,y_gercek):
    t=0
    ornek_sayisi=len(y_tahmin)
    for i in range(ornek_sayisi):
        if y_tahmin[i]==y_gercek[i]:
            t+=1
    return (t/ornek_sayisi)*100

def knn_siniflandirma(x,X_data,y_data,k):
    ornek_sayisi=X_data.shape[0]
    uzakliklar=[]
    for i in range(ornek_sayisi):
        uzakliklar.append(oklid_uzaklik(x,X_data[i,:]))
    en_yakinlarin_indisleri=np.argsort(uzakliklar)[:k]
    return st.mode(y_data[en_yakinlarin_indisleri])
    
    
full_data=np.concatenate((temiz_veri_matrisi,yasamis_mi),axis=1)
X_egitim,X_val,X_test,y_egitim,y_val,y_test=train_val_test_split(full_data,0.5,0.2)
    
aday_k_degerler=[1,3,5,7,9,11] 

for k in aday_k_degerler:
    val_sayisi=X_val.shape[0]
    val_tahminler=np.zeros((val_sayisi,1)).astype(int)
    for i in range(val_sayisi):
        val_tahminler[i]=knn_siniflandirma(X_val[i,:],X_egitim,y_egitim,k)
    basari=skor(val_tahminler,y_val) 
    print("k:{} icin basari: {}".format(k,basari))
    
##### final siniflandirma ####
X_egitim_final=np.concatenate((X_egitim,X_val),axis=0)  #artik val sete ihtiyacimiz kalmadi, onu egitim setine ekleyelim  
y_egitim_final=np.concatenate((y_egitim,y_val),axis=0)    
    
test_ornegi_sayisi=X_test.shape[0]
final_tahminler=np.zeros((test_ornegi_sayisi,1))
for i in range(test_ornegi_sayisi):
    final_tahminler[i]=knn_siniflandirma(X_test[i,:],X_egitim_final,y_egitim_final,11)


final_skor=skor(final_tahminler,y_test) 
print("Final siniflandirma basarisi: {}".format(np.around(final_skor,3)))


