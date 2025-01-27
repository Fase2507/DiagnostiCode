import random

import keyboard
import pandas as pd
import numpy as np
import glob
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import style
from matplotlib.pyplot import ylabel, xlabel

##LINKS
#https://matplotlib.org/stable/gallery/index.html
#https://matplotlib.org/stable/gallery/index.html
#https://matplotlib.org/stable/plot_types/index

#PIE CHART!!
labels=["py","js","java","cpp"]

sizes=[50,79,122,21]

explode=[0.2,0,0,0.2]

plt.pie(sizes,labels=labels,autopct="%.2f%%",shadow=False,startangle=90,explode=explode)
plt.title("pie chart")
plt.show()

#HISTOGRAM
ages=np.random.normal(23,2,size=100)
plt.hist(ages.round(2),bins=20,cumulative=True,color="red",edgecolor="black",alpha=0.7)
plt.show()


#BAR PLOT
data=[10,2,35,40,5]
labels=["cpp","Bash","python","javascript","java"]
plt.bar(labels,data,color="red",edgecolor="black",width=.5,alpha=0.9,linewidth=3,tick_label=labels)
plt.show()


#PLOT & SCATTER together
# plt.title("Weights change over years")
# years=[2007 + x for x in range(18)]
# weights=[80,81,82,73,83,84,84,85,75,86,87,87,88,88,78,90,80,84]
# plt.xlabel("Years")
# plt.ylabel("Weights")
# plt.plot(years, weights,label='Weights over Years', color='red', marker='o', alpha=0.5,lw=2,linestyle="--")
# plt.scatter(years, weights)
# plt.legend()
# plt.show()

#SCATTER PLOT
# h=np.random.randn(100)*100
# v=np.random.randn(100)*100
# plt.scatter(h,v,color="red",s=120,marker="$\star$",alpha=0.5)
# plt.show()


# Generate data
# x = np.linspace(0, 10, 100)
# y = np.sin(x)
#
# # Create the plot
# plt.figure(figsize=(10, 5))
# plt.plot(x, y)
# plt.title('Simple Sine Wave')
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.grid(True)
# plt.show()
#
# # Example visualizations using seaborn u NEED TITANIC.CSV
# df=pd.read_csv("titanic.csv")
#
# # 1. Histogram
# plt.figure(figsize=(8, 6))
# sns.histplot(df['Age'], kde=True)
# plt.title('Distribution of Passenger Ages')
# plt.show()
#
# # 2. Box plot
# plt.figure(figsize=(8, 6))
# sns.boxplot(x='Pclass', y='Age', data=df)
# plt.title('Age Distribution by Passenger Class')
# plt.show()
#
# # 3. Count plot
# plt.figure(figsize=(8, 6))
# sns.countplot(x='Survived', hue='Sex', data=df)
# plt.title('Survival Count by Gender')
# plt.show()
#
# # 4. Scatter plot
# plt.figure(figsize=(8, 6))
# sns.scatterplot(x='Age', y='Fare', hue='Survived', data=df)
# plt.title('Age vs. Fare with Survival')
# plt.show()
#
# # 5. Heatmap of correlation
# plt.figure(figsize=(10, 8))
# sns.heatmap(df.select_dtypes(include=[np.number]).corr(), annot=True, cmap='coolwarm')
# plt.title('Correlation Matrix of Numerical Features')
# plt.show()
#
# # 6. Pairplot
# sns.pairplot(df, hue='Survived')  #This can be computationally expensive for large datasets
# plt.title("Kapsamlı Görüntüleme")
# plt.show()
#
# # 7. Violin plot
# plt.figure(figsize=(8, 6))
# sns.violinplot(x='Embarked', y='Fare', hue='Survived', data=df, split=True)
# plt.title('Fare Distribution by Embarkation Point')
# plt.show()


#SIN COS TAN LOG
# v=np.arange(0,10,0.1)
# fig,axs=plt.subplots(2,2,figsize=(10,10))
#
# axs[0,0].plot(v,np.sin(v))
# axs[0,0].set_title("Sine Wave")
#
# axs[0,1].plot(v,np.cos(v))
# axs[0,1].set_title("Cosine Wave")
#
# axs[1,0].plot(v,np.tan(v))
# axs[1,0].set_title("Tangent Wave")
#
# axs[1,1].plot(v,np.random.logistic(v))
# axs[1,1].set_title("logistic Wave")
# plt.suptitle("4Plots",fontsize=23,fontweight="bold",fontstyle="italic")
# plt.tight_layout()
# plt.savefig("Img/4plots2.png",dpi=300,bbox_inches="tight",pad_inches=5,transparent=False)#it will save the figure
# plt.show()

#PIE CHART for election results
# style.use("dark_background") #u have to import style from matplotlib
# votes=[10,5,24,18]
# party=["X","Y","Z","H"]
#
# plt.pie(votes,labels=None,autopct="%.2f%%",shadow=False,startangle=90)
# plt.title("pie chart")
# plt.legend(labels=party,loc="upper left")
# plt.show()

#SHOWING STOCK GRAPH BY PLOT
# stock_a=[23,27,35,67,71]
# stock_b=[21,22,23,24,25]
# stock_c=[285,293,301,330,354]
#
# stock_ticks=list(range(20,400,20))
# day_ticks=list(range(1,6,1))
# plt.plot(stock_a,label="company A",color="red",marker="*",alpha=0.8,lw=3,linestyle="-")
# plt.plot(stock_b,label="company B",color="green",marker="o",alpha=0.8,lw=3,linestyle="--")
# plt.plot(stock_c,label="company C",color="blue",marker="x",alpha=0.8,lw=3,linestyle="-.")
# plt.title("Stocks",fontsize=20,fontweight="bold",fontstyle="italic")
# plt.xlabel("Days",fontsize=15,fontweight="bold",fontstyle="italic")
# plt.ylabel("Price")
# plt.legend(loc="best")
# plt.yticks(stock_ticks,[f"{x} TL " for x in stock_ticks])
# plt.xticks(day_ticks,[f"{i}. day" for i in day_ticks])
# plt.show()

#Showing Income Graph by PLOT
# years=[2014,2015,2016,2017,2018,2019,2020]
# income=[10000,20000,5000,40000,10050,60000,23170]
# income_ticks=list(range(10000,60000,5000))
# plt.plot(years,income,color="red",marker="o",alpha=0.5,lw=2,linestyle="--")
# plt.title("Income",fontsize=20,fontweight="bold",fontstyle="italic")
# plt.xlabel("Years")
# plt.ylabel("Income")
# plt.yticks(income_ticks,[f"{x} $ " for x in income_ticks])
# plt.show()

#BOX PLOT
# height=np.random.randint(10,100,size=100)
# print(height.mean())
# plt.boxplot(height,vert=True,patch_artist=True,boxprops=dict(facecolor="white",color="black",alpha=0.5))
# plt.show()

#BOX PLOT2
# first=np.linspace(0,10,25)
# second=np.linspace(10,200,25)
# third=np.linspace(200,210,25)
# fourth=np.linspace(210,230,25)
#
# datav=np.concatenate((first,second,third,fourth),axis=0)
# plt.boxplot(datav,vert=True,patch_artist=True,boxprops=dict(facecolor="white",color="black",alpha=0.5))
# plt.show()

#3D PLOT
# ax=plt.axes(projection="3d")

# x=np.random.randint(0,10,size=100)
# y=np.random.randint(0,10,size=100)
# z=np.random.randint(0,10,size=100)
#
# x=np.arange(0,np.pi,0.1)
# y=np.sin(x)
# z=np.cos(x)
#
# ax.scatter(x,y,z,c="red",s=100,linewidths=.7,edgecolors="black")
# plt.suptitle("3D Plot",fontsize=20,fontweight="bold",fontstyle="italic")
# ax.set_xlabel("X")
# ax.set_ylabel("Y")
# ax.set_zlabel("Z")
# plt.show()

#3D2 PLOT_SURFACE
# ax=plt.axes(projection="3d")
#
# a=np.arange(-5,5,0.1)
# b=np.arange(-5,5,0.1)
#
# x,y=np.meshgrid(a,b)
# z=np.sin(x)*np.cos(y)
#
# ax.plot_surface(x,y,z,cmap="plasma",alpha=0.9)
# ax.set_xlabel("Test")
# ax.set_title("3D PLOT")
# ax.set_ylabel("Y")
# ax.view_init(0,90)
# plt.show()

#ANIMATION
# heads_tails=[0,0]
#
# for _ in range(1000):
#     heads_tails[random.randint(0,1)]+=1
#     plt.bar(["Heads","Tails"],heads_tails,color=["green","black"])
#     plt.tick_params(axis='x', colors='red', labelsize=15)
#
#     ylabel("Values",fontsize=20,fontweight="bold",fontstyle="italic")
#     plt.pause(0.001)
#     if keyboard.is_pressed('q'):
#         break
#
# plt.show()

##DOC LINKS
#https://matplotlib.org/stable/gallery/index.html
#https://matplotlib.org/stable/gallery/index.html
#https://matplotlib.org/stable/plot_types/index
##VIDEO LINKS
#https://www.youtube.com/watch?v=OZOOLe2imFo&t=2614s
#https://www.youtube.com/watch?v=TA8C8EBLIxI