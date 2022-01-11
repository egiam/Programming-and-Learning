
import matplotlib.pyplot as plt

#Customization
year = [1940,1960,1980,2000,2020,2040,2060,2080,2100]
pop = [2.64,3.52,4.63,5.68,7.98,8.65,9.32,10.65,11.23]

plt.plot(year, pop)
plt.xlabel('year')
plt.ylabel('pop')
plt.title('world population projections')
plt.yticks([0,2,4,6,8,10])
plt.fill_between(year,pop,0,color='green')
plt.show()


#Histogram
help(plt.hist)
values = [0,0.6,1.4,1.6,2.2,2.5,2.6,3.2,3.5,3.9,4.2,6]
plt.hist(values, bins = 3)
plt.show()


##

year = [1950, 1970, 1990, 2010]
pop = [2.519, 3.692, 5.263, 6.972]

plt.plot(year, pop)

plt.show()

plt.scatter(year, pop)

plt.show()
