# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 22:59:24 2016

@author: kbrahul
"""
import numpy as np
import sklearn
import pandas as pd
from sklearn import mixture
import os, glob
from sklearn.svm import NuSVC
from scipy.stats import mode
import numpy.matlib
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.tools.shortcuts import buildNetwork
from pybrain.structure import TanhLayer

#%% Functions :
#%%

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
i=1
temp_label=0;
labels=np.array([])
path = 'training/'
for infile in sorted(glob.glob( os.path.join(path, '*.csv*'))):
    a1=np.zeros(10)
    a1[temp_label]=1
    z=np.array(pd.read_csv(infile))
    length=z.shape[0]
    temp=np.matlib.repmat(a1,length,1)
    if i==1:
        labels=temp
        i+=1
    else:
        labels=np.vstack((labels,temp))
    temp_label+=1
    
#%% Preparation of data
ds = SupervisedDataSet(13, 10)
for i in range(lis.shape[0]):
    ds.addSample(lis[i],labels[i])

#%%Building Network :
net = buildNetwork(13,20,10, bias=True , hiddenclass=TanhLayer)
trainer = BackpropTrainer(net, ds)
trainer.train()
#%%
    
