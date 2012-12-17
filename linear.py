#! /usr/bin/python

"""
linear operation in score distribution 
affects the FAR
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import  Line2D

x = np.arange( 0,20,0.01 )
thresh = [ 8,8,8 ]
line = [ 0.0,0.6,1.0 ]
y0 = x*0
y1 = np.exp( -(x-6)**2/5. )
y2 = np.exp( -(x-7)**2/5. )


plt.figure(1)
plt.subplot(211)
plt.axis( [0,20,0,1.3] )
#plt.fill_between( x,0,y1,color='r',alpha=0.6 )
plt.fill_between( x,0,y1, where=y1>=y0, color='g',alpha=0.6 )
#plt.plot(x,y1,x,y2)

idx_intsec = 800
plt.fill_between( x[idx_intsec:],0,y1[idx_intsec:], color='y' )
plt.annotate( 'threshold',xy=(9,0.9),xytext=(12,1.0), arrowprops=dict(facecolor='black',shrink=0.05), )
plt.annotate( 'FAR',xy=(8,0.1),xytext=(12,0.4), arrowprops=dict(facecolor='black',shrink=0.05), )
plt.plot( x,y1,thresh,line )
#plt.show()


plt.subplot(212)
plt.axis( [0,20,0,1.3] )
plt.fill_between( x,0,y2, where=y2>=y0, color='g',alpha=0.6 )
idx_intsec = 800
plt.fill_between( x[idx_intsec:],0,y2[idx_intsec:], color='y' )
plt.annotate( 'threshold',xy=(9,0.9),xytext=(12,1.0), arrowprops=dict(facecolor='black',shrink=0.05), )
plt.annotate( 'new FAR',xy=(8,0.1),xytext=(12,0.4), arrowprops=dict(facecolor='black',shrink=0.05), )
plt.plot(x,y2,thresh,line )

plt.show()

