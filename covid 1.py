import pandas as pd 
import matplotlib.pyplot as plt 
from pandas import DataFrame
import os

confirmed = pd.read_csv("time_series_covid19_confirmed_global.csv")
deaths = pd.read_csv("time_series_covid19_deaths_global.csv")
confirmed = confirmed.drop(['Province/State','Lat','Long'],axis=1) 
deaths = deaths.drop(['Province/State','Lat','Long'],axis=1)

confirmed_countries_list =  confirmed['Country/Region'].values.tolist()
confirmed_list =  confirmed.values.tolist()
deaths_list =  deaths.values.tolist()

# If any country has its data according to state wise then,these function will sum all state data in one country
confirmed = confirmed.groupby(confirmed['Country/Region']).aggregate('sum')
deaths = deaths.groupby(deaths['Country/Region']).aggregate('sum')

# Here we transpose the data file
confirmed = confirmed.T
deaths = deaths.T

Death_growing_rate = confirmed.copy()
for day in range(0,len(confirmed)):
    Death_growing_rate.iloc[day] = (deaths.iloc[day]/confirmed.iloc[day])*100

countries_list = []
confirmed_countries = confirmed_countries_list.copy()
Confirmed_Countries = list(dict.fromkeys(confirmed_countries))

#Making file for data on the desktop
os.chdir("C:\\Users\\HP\\Desktop")
A = open("Confirmed_countries.txt",'w')
for i in range (0,len(Confirmed_Countries)):
    A.write(Confirmed_Countries[i])
    A.write("\n")
n = int(input("\nEnter the number of countries you want to check the death growing rate : "))
print("Enter the name of countries by seeing in the Printed list for which you have to see death growing rate :\n")
for i in range(1,n+1):
    country_names = str(input())
    countries_list.append(country_names)
print("Entered countries list by user : ")    
print(countries_list)


# Plotting Graph of entered countries by user 
ax = plt.subplot()
ax.set_facecolor('black')
ax.tick_params(axis = 'x',color = 'white')
ax.tick_params(axis = 'y',color = 'white')
ax.set_title("Death rates of countries",color = 'red')
plt.xlabel(" Dates ")
plt.ylabel("Death growing rate")

for country in countries_list:
    Death_growing_rate[country].plot(label = country)    
plt.legend(loc = 'upper left')
plt.show() 

# Making list of High risk countries 
High_risk_Countries =[]
d = float(input("Enter the Death_growing_rate for which, you mark the country as the high risk country : "))
for i in range(1,len(confirmed_list)) :
    P = confirmed_list[i]
    D = deaths_list[i]
    C = confirmed_countries_list[i]
    for j in range(1,len(P)) :
        if (int(P[j])==0) or (int(D[j])==0):
            Dgr = 0
        else :
            Dgr = (int(D[j])/int(P[j]))* 100
            if Dgr > d :
                High_risk_Countries.append(C)
High_risk_Countries = list(dict.fromkeys(High_risk_Countries))
print("Total number of high risk countries : ", High_risk_Countries.__len__())
print("List of High risk countries :")
B = open("High_risk_countries.txt",'w')
for i in range (0,len(High_risk_Countries)):
    B.write(High_risk_Countries[i])
    B.write("\n")

# Plotting Graph of high risk countries  
ax = plt.subplot()
ax.set_facecolor('black')
ax.tick_params(axis = 'x',color = 'white')
ax.tick_params(axis = 'y',color = 'white')
ax.set_title("Death rates of high risk countries",color = 'red')
plt.xlabel(" Dates ")
plt.ylabel("Death growing rate")

for country in High_risk_Countries:
    Death_growing_rate[country].plot(label = country) 
plt.legend(loc = 'upper left')
plt.show() 
