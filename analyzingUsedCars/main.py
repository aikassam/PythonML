#Project for learning data science in Python.
#Program intended to play around with data science techniques using dataset of used cars
#Data from Kaggle at https://www.kaggle.com/datasets/thedevastator/uncovering-factors-that-affect-used-car-prices
#Author of data: Data Society


#Data science libaries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Reading in data
used_cars = pd.read_csv('autos.csv')

#Condensing data to be more relevant

#If you're broke enough to be buying used cars, but spending more than $50k. please prioritize friend.
used_cars = used_cars[used_cars['price'] < 50000]


#Letting range of years of cars to include be 1980-2015.
used_cars = used_cars[used_cars['yearOfRegistration'] <= 2015]
used_cars = used_cars[used_cars['yearOfRegistration'] >= 1980]

#Removing columns with data unlikely to have a large impact on price.
used_cars = used_cars.drop(['dateCrawled', 'offerType', 'abtest', 'monthOfRegistration', 'nrOfPictures', 'postalCode', 'lastSeen', 'dateCreated', 'index'], axis=1)

#Plotting a graph of average price of used cars with respect to their year of registration.

#Initializing arrays for x and y values
xvalues = [None] * (2015-1980)
yvalues = [None] * (2015-1980)
x = 0


#Storing years in xvalues and mean of prices in yvalues
for i in range(1980, 2015):
    xvalues[x] = i
    yvalues[x] = used_cars[used_cars['yearOfRegistration']==i]['price'].mean()
    x = x + 1

#Plotting using matplotlib
plt.bar(xvalues, yvalues)
plt.show()