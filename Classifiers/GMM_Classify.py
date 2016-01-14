# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 22:24:05 2015

@author: kbrahul
"""

import numpy as np
import sklearn
import pandas as pd
from sklearn import mixture
import os, glob

#Reading the files
lis=[];
path = 'training/'
for infile in sorted(glob.glob( os.path.join(path, '*.csv*'))):
    print infile
    lis.append(pd.read_csv(infile))

#Converting them to np.array

#%%
#Defining gmms
g_model=[mixture.GMM(n_components=1,covariance_type='full',thresh=0.001,min_covar=0.001,n_iter=100) for x in range(len(lis))]
#%%
#Fitting gmm
for i in range(len(lis)):
    g_model[i].fit(lis[i])
    

#%%
#Checking the log likelihood with each song



c1=0
path = 'classical_cross/'
for infile in glob.glob( os.path.join(path, '*.csv*') ):
    sumg=[]
    test=pd.read_csv(infile)
    test=np.array(test)
    for i in range(len(lis)):
        sumg.append(np.sum(g_model[i].score(test)))
    if max(sumg) == sumg[1]:
        c1=c1+1

c1
#%%
""" Yet to be edited from here on"""

c2=0
path = 'classical_cross/'
for infile in glob.glob( os.path.join(path, '*.csv*') ):
    test=pd.read_csv(infile)
    test=np.array(test)
    logg1=g_model[0].score(test)
    logg2=g_model[1].score(test)
    logg3=g_model[2].score(test)
    logg4=g_model[3].score(test)
    logg5=g_model[4].score(test)
    logg6=g_model[5].score(test)
    logg7=g_model[6].score(test)
    logg8=g_model[7].score(test)
    sumg1=np.sum(logg1)
    sumg2=np.sum(logg2)
    sumg3=np.sum(logg3)
    sumg4=np.sum(logg4)
    sumg5=np.sum(logg5)
    sumg6=np.sum(logg6)
    sumg7=np.sum(logg7)
    sumg8=np.sum(logg8)
    sum=[sumg1,sumg2,sumg3,sumg4,sumg5,sumg6,sumg7,sumg8]
    if max(sum)==sumg2:
     c2=c2+1

#%%
c3=0
path = 'country_cross/'
for infile in glob.glob( os.path.join(path, '*.csv*') ):
    test=pd.read_csv(infile)
    test=np.array(test)
    logg1=g1.score(test)
    logg2=g2.score(test)
    logg3=g3.score(test)
    logg4=g4.score(test)
    logg5=g5.score(test)
    logg6=g6.score(test)
    logg7=g7.score(test)
    logg8=g8.score(test)
    sumg1=np.sum(logg1)
    sumg2=np.sum(logg2)
    sumg3=np.sum(logg3)
    sumg4=np.sum(logg4)
    sumg5=np.sum(logg5)
    sumg6=np.sum(logg6)
    sumg7=np.sum(logg7)
    sumg8=np.sum(logg8)
    sum=[sumg1,sumg2,sumg3,sumg4,sumg5,sumg6,sumg7,sumg8]
    if max(sum)==sumg3:
     c3=c3+1


c4=0
path = 'disco_cross/'
for infile in glob.glob( os.path.join(path, '*.csv*') ):
    test=pd.read_csv(infile)
    test=np.array(test)
    logg1=g1.score(test)
    logg2=g2.score(test)
    logg3=g3.score(test)
    logg4=g4.score(test)
    logg5=g5.score(test)
    logg6=g6.score(test)
    logg7=g7.score(test)
    logg8=g8.score(test)
    sumg1=np.sum(logg1)
    sumg2=np.sum(logg2)
    sumg3=np.sum(logg3)
    sumg4=np.sum(logg4)
    sumg5=np.sum(logg5)
    sumg6=np.sum(logg6)
    sumg7=np.sum(logg7)
    sumg8=np.sum(logg8)
    sum=[sumg1,sumg2,sumg3,sumg4,sumg5,sumg6,sumg7,sumg8]
    if max(sum)==sumg4:
     c4=c4+1


c5=0
path = 'hiphop_cross/'
for infile in glob.glob( os.path.join(path, '*.csv*') ):
    test=pd.read_csv(infile)
    test=np.array(test)
    logg1=g1.score(test)
    logg2=g2.score(test)
    logg3=g3.score(test)
    logg4=g4.score(test)
    logg5=g5.score(test)
    logg6=g6.score(test)
    logg7=g7.score(test)
    logg8=g8.score(test)
    sumg1=np.sum(logg1)
    sumg2=np.sum(logg2)
    sumg3=np.sum(logg3)
    sumg4=np.sum(logg4)
    sumg5=np.sum(logg5)
    sumg6=np.sum(logg6)
    sumg7=np.sum(logg7)
    sumg8=np.sum(logg8)
    sum=[sumg1,sumg2,sumg3,sumg4,sumg5,sumg6,sumg7,sumg8]
    if max(sum)==sumg5:
     c5=c5+1


c6=0
path = 'jazz_cross/'
for infile in glob.glob( os.path.join(path, '*.csv*') ):
    test=pd.read_csv(infile)
    test=np.array(test)
    logg1=g1.score(test)
    logg2=g2.score(test)
    logg3=g3.score(test)
    logg4=g4.score(test)
    logg5=g5.score(test)
    logg6=g6.score(test)
    logg7=g7.score(test)
    logg8=g8.score(test)
    sumg1=np.sum(logg1)
    sumg2=np.sum(logg2)
    sumg3=np.sum(logg3)
    sumg4=np.sum(logg4)
    sumg5=np.sum(logg5)
    sumg6=np.sum(logg6)
    sumg7=np.sum(logg7)
    sumg8=np.sum(logg8)
    sum=[sumg1,sumg2,sumg3,sumg4,sumg5,sumg6,sumg7,sumg8]
    if max(sum)==sumg6:
     c6=c6+1



c7=0
path = 'metal_cross/'
for infile in glob.glob( os.path.join(path, '*.csv*') ):
    test=pd.read_csv(infile)
    test=np.array(test)
    logg1=g1.score(test)
    logg2=g2.score(test)
    logg3=g3.score(test)
    logg4=g4.score(test)
    logg5=g5.score(test)
    logg6=g6.score(test)
    logg7=g7.score(test)
    logg8=g8.score(test)
    sumg1=np.sum(logg1)
    sumg2=np.sum(logg2)
    sumg3=np.sum(logg3)
    sumg4=np.sum(logg4)
    sumg5=np.sum(logg5)
    sumg6=np.sum(logg6)
    sumg7=np.sum(logg7)
    sumg8=np.sum(logg8)
    sum=[sumg1,sumg2,sumg3,sumg4,sumg5,sumg6,sumg7,sumg8]
    if max(sum)==sumg7:
     c7=c7+1


c8=0
path = 'pop_cross/'
for infile in glob.glob( os.path.join(path, '*.csv*') ):
    test=pd.read_csv(infile)
    test=np.array(test)
    logg1=g1.score(test)
    logg2=g2.score(test)
    logg3=g3.score(test)
    logg4=g4.score(test)
    logg5=g5.score(test)
    logg6=g6.score(test)
    logg7=g7.score(test)
    logg8=g8.score(test)
    sumg1=np.sum(logg1)
    sumg2=np.sum(logg2)
    sumg3=np.sum(logg3)
    sumg4=np.sum(logg4)
    sumg5=np.sum(logg5)
    sumg6=np.sum(logg6)
    sumg7=np.sum(logg7)
    sumg8=np.sum(logg8)
    sum=[sumg1,sumg2,sumg3,sumg4,sumg5,sumg6,sumg7,sumg8]
    if max(sum)==sumg8:
     c8=c8+1
  



c=c1+c2+c3+c4+c5+c6+c7+c8
c

#%%
