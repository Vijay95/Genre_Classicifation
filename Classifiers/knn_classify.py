# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 13:41:06 2016

@author: kbrahul
"""

import numpy as np
import sklearn
import pandas as pd
from sklearn import mixture
import os, glob
from sklearn.neighbors import KNeighborsClassifier
from scipy.stats import mode

#Concatenating the files
lis=[];
i=1;
path = 'training/'
for infile in sorted(glob.glob( os.path.join(path, '*.csv*'))):
    if i ==1:
        lis = np.array(pd.read_csv(infile))
        i=i+1;
    else:
        lis=np.vstack((lis,np.array(pd.read_csv(infile))))
#%%
temp_label=0;
labels=np.array([])
path = 'training/'
for infile in sorted(glob.glob( os.path.join(path, '*.csv*'))):
    temp_label+=1
    z=np.array(pd.read_csv(infile))
    length=z.shape[0];
    m=np.ones(length)
    m=m*temp_label
    labels=np.hstack((labels,m))

#%% KNN Fit
neigh = KNeighborsClassifier(n_neighbors=3)
neigh.fit(lis, labels)
#%%
c1=0
path = 'classical_cross/'
for infile in glob.glob( os.path.join(path, '*.csv*') ):
    test=pd.read_csv(infile)
    test=np.array(test)
    y_pred=neigh.predict(test)
    pred=mode(y_pred)
    pred=np.array(pred)
    prediction=pred[0]
    if prediction == 2:
        c1+=1
c1
#%%

c1
