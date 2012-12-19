#! /usr/bin/python

import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
x = np.arange(5)#[ 0,1,2,3,4 ]
ax1 = fig.add_subplot( 111 )
print 'x is : ',x
y = x*2
#plt.xticks(['a','b','c','d','e'])
#locs, labels = plt.xticks()
labels = ('','','c','d','e')
#print 'locs is : ',locs
#new_labels = [ x.format( locs[i] ) for i,x in enumerate( labels ) ]
#print 'new_labels is : ',new_labels
plt.xticks(x,labels )
plt.plot(x,y)
plt.savefig('xticks.png')
