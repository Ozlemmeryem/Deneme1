# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 23:35:41 2019

@author: Administrator
"""

import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans

# Excel sheetlerinin isimlerini almak için
xls = pd.ExcelFile('CemData.xlsx')

# Her bir sheet dataframe olarak kaydedilir
kafe = pd.read_excel('CemData.xlsx','Kafe')
restoran = pd.read_excel('CemData.xlsx','Restoran',header=1)
bar = pd.read_excel('CemData.xlsx','Bar',header=1)
muze = pd.read_excel('CemData.xlsx','Muze',header=1)
galeri = pd.read_excel('CemData.xlsx','Galeri',header=1)
banka = pd.read_excel('CemData.xlsx','Banka',header=1)
durak = pd.read_excel('CemData.xlsx','OtobüsDurağı',header=1)
metro = pd.read_excel('CemData.xlsx','Metro',header=1)
otel = pd.read_excel('CemData.xlsx','Otel',header=1)
bim = pd.read_excel('CemData.xlsx','Bim',header=1)
a101 = pd.read_excel('CemData.xlsx','A101',header=1)
sok = pd.read_excel('CemData.xlsx','Şok',header=1)
migros = pd.read_excel('CemData.xlsx','Migros',header=1)
mcenter = pd.read_excel('CemData.xlsx','MacroCenter',header=1)
kuyumcu = pd.read_excel('CemData.xlsx','Kuyumcu',header=1)
tower = pd.read_excel('CemData.xlsx','Tower',header=1)
hastahane = pd.read_excel('CemData.xlsx','Hastahane',header=1)
okul = pd.read_excel('CemData.xlsx','Okul',header=1)

#legend font büyüklüğünü
fsize = 15;
merkezler = {}

# n değeri kaç adet cluster olacağını söyler
# aşağıda herbir sheet n_cluster parametresi değiştirilerek daha iyi sonuçlar elde edilebilir
# n=1 yaparak herbir sheet için merkez noktası belirlenir
n = 1

X = kafe[['Lat', 'Long']].values
kmeans = KMeans(n_clusters=n)
kmeans.fit(X)
y_kmeans = kmeans.predict(X)
centers = kmeans.cluster_centers_
merkezler[0] = centers

X = restoran[['Lat', 'Long']].values
kmeans = KMeans(n_clusters=n)
kmeans.fit(X)
y_kmeans = kmeans.predict(X)
centers = kmeans.cluster_centers_
merkezler[1] = centers

X = bar[['Lat', 'Long']].values
kmeans = KMeans(n_clusters=n)
kmeans.fit(X)
y_kmeans = kmeans.predict(X)
centers = kmeans.cluster_centers_
merkezler[2] = centers


X = muze[['Lat', 'Long']].values
kmeans = KMeans(n_clusters=n)
kmeans.fit(X)
y_kmeans = kmeans.predict(X)
centers = kmeans.cluster_centers_
merkezler[3] = centers


X = galeri[['Lat', 'Long']].values
kmeans = KMeans(n_clusters=n)
kmeans.fit(X)
y_kmeans = kmeans.predict(X)
centers = kmeans.cluster_centers_
merkezler[4] = centers

X = banka[['Lat', 'Long']].values
kmeans = KMeans(n_clusters=n)
kmeans.fit(X)
y_kmeans = kmeans.predict(X)
centers = kmeans.cluster_centers_
merkezler[5] = centers

X = durak[['Lat', 'Long']].values
kmeans = KMeans(n_clusters=n)
kmeans.fit(X)
y_kmeans = kmeans.predict(X)
centers = kmeans.cluster_centers_
merkezler[6] = centers

X = metro[['Lat', 'Long']].values
kmeans = KMeans(n_clusters=n)
kmeans.fit(X)
y_kmeans = kmeans.predict(X)
centers = kmeans.cluster_centers_
merkezler[7] = centers

X = otel[['Lat', 'Long']].values
kmeans = KMeans(n_clusters=n)
kmeans.fit(X)
y_kmeans = kmeans.predict(X)
centers = kmeans.cluster_centers_
merkezler[8] = centers

X = bim[['Lat', 'Long']].values
kmeans = KMeans(n_clusters=n)
kmeans.fit(X)
y_kmeans = kmeans.predict(X)
centers = kmeans.cluster_centers_
merkezler[9] = centers

X = a101[['Lat', 'Long']].values
kmeans = KMeans(n_clusters=n)
kmeans.fit(X)
y_kmeans = kmeans.predict(X)
centers = kmeans.cluster_centers_
merkezler[10] = centers

X = sok[['Lat', 'Long']].values
kmeans = KMeans(n_clusters=n)
kmeans.fit(X)
y_kmeans = kmeans.predict(X)
centers = kmeans.cluster_centers_
merkezler[11] = centers


X = migros[['Lat', 'Long']].values
kmeans = KMeans(n_clusters=n)
kmeans.fit(X)
y_kmeans = kmeans.predict(X)
centers = kmeans.cluster_centers_
merkezler[12] = centers


X = mcenter[['Lat', 'Long']].values
kmeans = KMeans(n_clusters=n)
kmeans.fit(X)
y_kmeans = kmeans.predict(X)
centers = kmeans.cluster_centers_
merkezler[13] = centers


X = kuyumcu[['Lat', 'Long']].values
kmeans = KMeans(n_clusters=n)
kmeans.fit(X)
y_kmeans = kmeans.predict(X)
centers = kmeans.cluster_centers_
merkezler[14] = centers


X = tower[['Lat', 'Long']].values
kmeans = KMeans(n_clusters=n)
kmeans.fit(X)
y_kmeans = kmeans.predict(X)
centers = kmeans.cluster_centers_
merkezler[15] = centers


X = hastahane[['Lat', 'Long']].values
kmeans = KMeans(n_clusters=n)
kmeans.fit(X)
y_kmeans = kmeans.predict(X)
centers = kmeans.cluster_centers_
merkezler[16] = centers


X = okul[['Lat', 'Long']].values
kmeans = KMeans(n_clusters=n)
kmeans.fit(X)
y_kmeans = kmeans.predict(X)
centers = kmeans.cluster_centers_
merkezler[17] = centers


# boş dataframe objesi
#yukarda elde edilen merkezler allArrays değişkeninde toplanır
# amaç tek bir dizide toplamak
allArrays = pd.DataFrame()

for x in range(0, 17):
    temp = pd.DataFrame(merkezler[x][:,0:2])
    allArrays = pd.concat([allArrays, temp],axis=0)

# allArrays dataframei ndarray'e dönüştürülür
last = allArrays.as_matrix()


# herbir sheetin merkez noktası ve bunların clustering merkezinin gösterilmesi
k_means = KMeans(n_clusters=1)
k_means.fit(last)
y_kmeans = k_means.predict(last)

plt.figure(figsize = (10, 6))
markers =['o', '.', ',', 'x','+', 'v', '^', '<', '>', 's', 'd','D','p','P','*','h']
for i in range(len(markers)):
    #print(markers[i])
    plt.scatter(merkezler[i][:,0], merkezler[i][:,1], marker=markers[i], s=50,label=xls.sheet_names[i])

karar_noktasi = k_means.cluster_centers_
plt.scatter(karar_noktasi[:, 0], karar_noktasi[:, 1], c='black', s=200, alpha=0.5,label='Karar Noktası')
plt.legend()