import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import Perceptron
from math import sqrt

N=25

#Generate points
pts=np.random.rand(N,2)*2-1
t=(pts[:,0]*pts[:,0]+pts[:,1]*pts[:,1])>.75
plt.scatter(pts[:,0],pts[:,1],c=t)
plt.xlabel('x')
plt.ylabel('y')
plt.show()

#Transform to new space
transformed=np.zeros((N,2))
transformed[:,0]=pts[:,0]*pts[:,0]
transformed[:,1]=pts[:,1]*pts[:,1]

#See the values
for i in range(N):
  print(str(pts[i,:])+'\t'+str(transformed[i,:]))

#See the new points
plt.scatter(transformed[:,0],transformed[:,1],c=t)
plt.xlabel('$x^2$')
plt.ylabel('$y^2$')
plt.show()

percep=Perceptron()
percep.fit(transformed,t)
w=np.zeros(3)
print(percep.coef_)
w[:2]=percep.coef_
w[2]=percep.intercept_

#See the new points and classifier
plt.scatter(transformed[:,0],transformed[:,1],c=t)
wXs=np.linspace(0,1)
yXs=(-w[0]/w[1])*wXs-w[2]/w[1]
plt.plot(wXs,yXs,linewidth=2.0)
plt.xlabel('$x^2$')
plt.ylabel('$y^2$')
plt.show()

#Each pair from wXs,yXs is an (x^2,y^2) point on the line.  I can turn each of those into four points.
origClassifier=[]
for i in range(len(wXs)):
  xsq=wXs[i]
  ysq=yXs[i]
  if (ysq>=0):
    origClassifier.append([sqrt(xsq),sqrt(ysq)])
    origClassifier.append([-sqrt(xsq),sqrt(ysq)])
    origClassifier.append([sqrt(xsq),-sqrt(ysq)])
    origClassifier.append([-sqrt(xsq),-sqrt(ysq)])
origClassifier=np.array(origClassifier)

plt.scatter(pts[:,0],pts[:,1],c=t)
plt.scatter(origClassifier[:,0],origClassifier[:,1])
plt.show()
