# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 16:24:30 2022

@author: firat ismailoglu
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 09:25:34 2022

@author: firat ismailoglu

Titanic datasi hakkinda genel bilgiler:
*Her satir gemiye binen bir kisiye denk gelmektedir
*Toplamda 1309 kisi hakkinda bilgi vardir.
pclass: bilet sinifini veriyor, 1: en pahali biletler,3 en ucuzu alinabilecek degerler: 1,2,3
name: char tipinde, yolcunun ismi
gender: male yada female, cinsiyet
sibsp: kisinin gemideki toplam kardes ve eş sayisi
parch: kisinin gemideki toplam cocuk sayisi
ticket: bilet numarasi
fare: bilet ücreti (pound cinsinden)
cabin: kisinin gemide bulunduğu kabinin (odanin) numarasi
embarked: kisinin Titanic'e hangi limandan bindigini belirtir: S: Southhampton, Q: Queenstown, C:Cherbourg 
home.dest: kisinin ev adresi, ikametinin bulundugu yer
***survived*** SINIF bilgisi, asil tahmin etmek istedigimiz 1: kisi hayatta kalmistir, 0: kisi ölmüştür
"""
#oncelikle en gerekli iki kutuphaneyi cagiriyoruz
import pandas as pd
import numpy as np


#datanin okunmasi 
#onemli not: okunan bu data dataFrame tipindedir
data=pd.read_excel("titanic.xlsx") 

#data hakkinda genel bilgilere sahip olmak icin komutlar
data.info()
data.describe()
data.head(5)#datan'nin ilk 5 satirini getirir

toplam_kisi_sayisi=data.shape[0]

##############################
#datanin herhangi bir satirinin ve sutunun getirilmesi
#buna slicing'de denir yani dilimleme 
data.loc[43] #43. kisinin cagirilmasi
data.iloc[43,3] #43. kisinin 3. özelliginin yani yaşının cagirilmasi
#Python'da sayma 0'dan başlar!!
#Buradaki loc ve iloc methodlarina dikkat edin!!

yas=data['age'] #bu yalnizca yaş yani age kolunu getirir
#getirilen bu kolon Series tipinde olur
#kolonu indisi ile degil ismiyle çağırabilmek çok hoş bir seydir.
#simdi de pclass
bilet_sinifi=data['pclass']

############# value_counts() methodu ####
####bu method her bir unique degerin kac defa görüldüğünü sayar
# !!!! bu yalnizca bir Series objesinin methodur, başka tiplerde kullanamayiz!!!!
bilet_sinifi.value_counts()
############################
### for ve if yapilarinin kullanilmasi##
#bunlarin öğrenilmesi adina gemide pclass'i 1 olan, 
#yani lüks kabinde olan ve hayatta kalan kişileri sayalim:
t=0
for i in range(1309):
    if data.loc[i]['pclass']==1 and data.loc[i]['survived']==1:
        t+=1
print("Lüks kabindeki {} adet kisi hayatta kalmistir".format(t))     

######### veri tipleri arasinda dönüşüm###
#np.array ile numpy array'a dönüştürme
bilet_sinifi_np=np.array(bilet_sinifi)
## yada list komutu ile list tipine dönüştürürebiliriz:
bilet_sinifi_list=list(bilet_sinifi)
#yada 
bilet_sinifi_list=list(bilet_sinifi_np)
#list tipindeki .count() methodu aldigi degerin icinde kac adet oldugunu sayar
#Bu method yalnizca list tipine aittir!!!!
birinci_sinif=bilet_sinifi_list.count(1)
print("{} adet birinci sinif bilete (lüks) sahiptir".format(birinci_sinif))    


######################################################
######################################################
######### Simdi tek tek kolonlari önişlemeden geçirip 
######### sınıflandirmaya hazır hale getirelim####
#Burada isim gibi bazı özellikleri atacagiz, cunku bu özelliklerin 
#siniflandirmamiza yani kişinin hayatta kalip kalmayacagina bir etkisi yok.
bilet_sinifi=data['pclass'] #bu haliyle kalsin, tutarsiz, yada gürültülü bir veri yok içinde
bilet_sinifi=np.array(bilet_sinifi) #np array tipine cevirelim, çunku bu tipte veriyi saklamak, veri içinde gezmek daha kolaydir..
bilet_sinifi=bilet_sinifi.astype(int) #int tipinde kalsin, hafizada daha az yer tutar böylece
bilet_sinifi=np.reshape(bilet_sinifi,(toplam_kisi_sayisi,1)) #bunu kolon (dikine) haline getrirdik
#ilgilendigimiz tum özellikleri kolon (sütun) haline getirip daha sonra onlari birbirine bağlayacagiz. 

###### cinsiyete yani gender'a bakalim#####
### önce bakalim hic boş deger var mi, varsa bunlar kayip veridir
#bunu 2 sekilde kontrol edebiliriz:
#degerleri tek tek gezip kayip veri olup olmadigina bakalim:
kayip=False #olmadigini varsayarak başliyalim
for i in range(toplam_kisi_sayisi):
    if data['gender'][i] is None: 
        kayip=True
        break#kayip veriyi bulmussak tüm sütünu gezmemize gerek yok
print(kayip)
#görülüyor ki gender'da kayip  veri yok, devam edelim
#gender char tipinde bunu sayisayllastirmmamiz gerekir##
cinsiyet=np.zeros((toplam_kisi_sayisi,1)).astype(int) #bu 1309,1 boyutlarinda degerlerinin tamamı 0 olan bir sutun vektörü olusturur
#erkeklere 1 diyelim kadinlar 0 kalsin (tam tersini de yapabilirsiniz)
for i in range(toplam_kisi_sayisi):
    if data['gender'][i]=="male":
        cinsiyet[i]=1

##### simdi yaş'a bakalim ####
##önce yaş yani age kolonunda kayip veri olup olmadigina bakalim:
# !!!!! burda gender'da oldugu gibi is None 'i kullanmiyoruz.
# age sayisal tipte, o yüzden veride olmadiğinda yeri NaN oluyor yani Not a Number
# dolayisiyla yokluğunu np'ye ait isnan methodu ile test ediyoruz
kayip=False
for i in range(toplam_kisi_sayisi):
    if np.isnan(data['age'][i]):
        kayip=True
        break
print(kayip)
# Görüldüğü gibi age'de kayip veri vardir.
# Ayrica burda tutarsiz veri olup olmadigina da bakalim.
#genel olarak ortalamaninin 3 starndart sapma fazlaasindan buyuk olan
#yada uç standart sapma eksiginden küçük olan verileri tutarsiz veri olarak düşünürüz.
ortalama_yas=np.ceil(np.mean(data['age'])) #np'deki mean methodu bize ortalamayi verir -- ceil ile yukari yuvarliyoruz
standard_sapma_yas=np.std(data['age']) 
max_yas=ortalama_yas+3*standard_sapma_yas
min_yas=1
#ortalama'nin 3 standart sapmasi 0'in altinda cikiyor. Bu zaten yaş  için pek mumkun degil
#bu yüzden alt siniri 1 olarak belirleyelim
#once bos bir kolon olusturulaim.
yas=np.zeros((toplam_kisi_sayisi,1))
for i in range(toplam_kisi_sayisi):
    eldeki_yas=data['age'][i]
    if eldeki_yas<min_yas or eldeki_yas>max_yas or np.isnan(eldeki_yas): #problematik durumlar
        yas[i]=ortalama_yas #bu durumlarda ortalam yaşı atayalım
    else:
        yas[i]=eldeki_yas

#### simdi kardes sayisina bakalim###
kayip=False
for i in range(toplam_kisi_sayisi):
    if np.isnan(data['sibsp'][i]):
        kayip=True
        break
print(kayip)
## Görülüyorki kayıp veri yok
data['sibsp'].value_counts() #bu komut sonucunda görüyoruzki hiç olmayack veriler var -3 yada 71 gibi bu degerler kardes sayisi olamaz
#mantik olarak kardes sayisi en fazla 10 olabilir 
#eger kardes sayisi 0-10 arasinda degilse bunu tutarsiz veri olarak dusunelim
#bunun yerine en çok görülen deger olan 0'i yazalim
makul_kardes_sayisi=[0,1,2,3,4,5,6,7,8,9,10]
kardes=np.zeros((toplam_kisi_sayisi,1)).astype(int)
for i in range(toplam_kisi_sayisi):
    if not np.isin(data['sibsp'][i],makul_kardes_sayisi): #degilse anlamina gelmesi için basina not koyduk
        kardes[i]=0                                       #ayrica burdaki np.isin() bir seyin, bir seyin icinde olup olmadigini sorgular
    else:
        kardes[i]=data['sibsp'][i]
#istedigimiz seyin olup olmadigina bakmak icin kardes'teki degerlere bakalim
#hangi degerden kac tane oldugunu veren fonksiyon .value_counts() idi; fakat bu Series tipindeki bir objenin fonksiyonu idi
#o halde bunu kullanabilmek için Series'e cevirmek gerekir. Fakat Series'e cevirebilmek icin de vektörün tek boyutlu 
#olmasi gerekir. np.ravel() methodu vektörü tek boyuta indirir.        
pd.Series(np.ravel(kardes)).value_counts()
#Görüyoruz ki tüm yaş sayilari istedigimiz değerler içinde 

#parch bir öncekine benzer olarak çocuk sayisidir, yani gemideki birinin gemideki cocugu sayisi
#bunun icinde maklul degerler 0-10 arasi dusunebiliriz
#bu degerlerin dagilimina bakalim
data['parch'].value_counts()
#parch için tutarsiz veri olmadigi görülüyor, degistirmemiz gereken bir sey yok
cocuk=np.zeros((toplam_kisi_sayisi,1)).astype(int)
for i in range(toplam_kisi_sayisi):
    cocuk[i]=data['parch'][i]



#Fare yani bilet ucreti de bir sayisal degerdir. Bunun icinde ayni yaşta oldugu gibi
#kabul edebilecegimiz max deger, ortalamanin 3 standart sapma fazlasi
#en kucuk degeri de 0 olarak dusunebiliriz.
ortalama_fiyat=np.mean(data['fare'])
max_fiyat=ortalama_fiyat+3*np.std(data['fare'])
min_fiyat=0
fiyat=np.zeros((toplam_kisi_sayisi,1))

for i in range(toplam_kisi_sayisi):
    eldeki_fiyat=data['fare'][i]
    if eldeki_fiyat<min_fiyat or eldeki_fiyat>max_fiyat or np.isnan(eldeki_fiyat): #problematik durumlar
        fiyat[i]=ortalama_fiyat #bu durumlarda ortalam yaşı atayalım
    else:
        fiyat[i]=eldeki_fiyat

### Buraya kadarki tüm özellikleri birbirine bağlayarak bir X veri matrisi oluşturulim##
## Burda yapacagimiz sey kolon vektörü tipindeki özellikleri yanyana bağlamaktir.
#Bunun icin axis=1 diyecegiz, eger bu kolonlari alt alta yazmak isteseydik axis=0 olur.
temiz_veri_matrisi=np.concatenate((bilet_sinifi,cinsiyet,yas,kardes,cocuk,fiyat),axis=1)        

### Son olarak Survived yani yaşam-ölüm sinifinda bir kayip veri olup olmadigina bakalim#
kayip=False
for i in range(toplam_kisi_sayisi):
    if np.isnan(data['survived'][i]):
        kayip=True
        break
print(kayip)
### bunda da bir eksik veri bulunmamaktadir.
#O halde direkt kullanabiliriz.
yasamis_mi=np.zeros((toplam_kisi_sayisi,1)).astype(int)
for i in range(toplam_kisi_sayisi):
    if data['survived'][i]==1:
        yasamis_mi[i]=1 #else yazmamiza gerek yok, cunku zaten default olatak 0 var

full_data=np.concatenate((temiz_veri_matrisi,yasamis_mi),axis=1)