import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


##Task-1
#
# matris = np.random.randint(0,15,(3,3))
# print("matris \n",matris)
# print("transpoze \n",np.matrix_transpose(matris))
# print("determinant \n",np.linalg.det(matris))
# print("2 ile carpim \n",matris*2)

##Task-2
# array=np.array([1,6,11,16,21,26,31,36,41,46])
# print(array)
# print("ortalama \n",array.mean())
# print("standart sapma \n",array.mean()- array.std())
# print("karesi \n", array**2)
# print("25'ten buyuk \n", array[array>25])

##task-3
# x=np.linspace(0,2*np.pi,100)
# y_sin=np.sin(x)
# y_cos=np.cos(x)
# plt.plot(x,y_sin,label='sin(x)')
# plt.plot(x,y_cos,label='cos(x)')
# plt.title('Sin-Cos grafiği')
# plt.legend()
# plt.show()

##Task-4
# data={
#    'isim':['Veli','Ayşe','Betül','Mehmet'],
#    'yaş':[25,30,22,27],
#    'gelir':[4500,6000,6000,5200]
# }
#
# df=pd.DataFrame(data)
#
# print("ortalama gelir: ",df['gelir'].mean())
# print("ortalama yas:\n ",df['yaş'].mean())
# print("5000'den büyük olanlar=\n", df[df['gelir']>5000])
# print("yaşa göre sırala,Küçükten buyuğe: \n",df.sort_values(by=['yaş'],ascending=True))

# Task5 Tıntanic
# df=pd.read_csv("titanic.csv")
# print(df.columns)
# print(df.head(10))
# print(df.tail(5))
# print(df['Age'].isnull().fillna(df['Age'].mean()))
#__________________________________________________
# print("Hayatta kalan kisi sayısı Erkek Kadın \n",df.groupby('Sex')['Survived'].sum())
# print("Toplam kisi sayısı Kadın Erkek \n",df.groupby('Sex')['PassengerId'].count())
# sonuc=df.groupby('Sex')['Survived'].sum()/df.groupby('Sex')['PassengerId'].count()
# print("Oranlar \n",sonuc)