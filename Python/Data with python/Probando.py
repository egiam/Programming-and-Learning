
import numpy as np

#np.mean(xx[:,0])       out: 1.7472
#np.median(xx[:,0])     out: 1.75
#np.corroef(xx[:,0], xx[:,1])
#np.std(xx[:,0])
#height = np.round(np.random.normal(x,xx,x))
#weight = np.round(np.random.normal(x,xx,x))
#np_city = np.column_stack((heaight, weight))

np_2d = np.array([[1.73, 1.68, 1.71],
                [65.4, 59.2, 63.6]])

print(np_2d)
print(np_2d.shape)


height = [1.73, 1.68, 1.71]
weight = [65.4, 59.2, 63.6]

np_height = np.array(height)
np_weight = np.array(weight)

print(np_height, np_weight, sep='/')

bmi = np_weight / np_height ** 2

print(bmi)


print (np.array([0,1,2,3,4,5,6,7,8,9]))
