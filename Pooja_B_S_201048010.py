#!/usr/bin/env python
# coding: utf-8

# In[23]:


import pandas as pd
import numpy as np 


# In[14]:


readfile = pd.read_excel("data.xlsx")
readfile1 = pd.read_excel("data_1.xlsx")


# In[24]:


readfile2=pd.read_excel("detail.xlsx")
readfile3=pd.read_excel("detailVol.xlsx")
readfile4=pd.read_excel("detailTemp.xlsx")


# In[112]:


readfile2.to_csv("detail.csv",index=None,header=True)
df = pd.DataFrame(pd.read_csv("detail.csv"))


# In[113]:


readfile3.to_csv("detailVol.csv",index=None,header=True)
df1 = pd.DataFrame(pd.read_csv("detailVol.csv"))


# In[114]:


readfile4.to_csv("detailTemp.csv",index=None,header=True)
df2 = pd.DataFrame(pd.read_csv("detailTemp.csv"))


# In[115]:


import matplotlib.pyplot as plt


# In[116]:


np.random.seed(0)
rng = pd.date_range('2015-02-24', periods=10, freq='T')
df = pd.DataFrame({'Val' : np.random.randn(len(rng))}, index=rng)  
print (df)


# In[117]:


print (df.resample('1Min').sum())


# In[119]:


readfile5=pd.read_excel("detailDownsampled.xlsx")
readfile6=pd.read_excel("detailVolDownsampled.xlsx")
readfile7=pd.read_excel("detaliTempDownsampled.xlsx")


# In[120]:


readfile5.to_csv("detaliTempDownsampled.csv",index=None,header=True)
df3 = pd.DataFrame(pd.read_csv("detailTempDownsampled.csv"))


# In[121]:


readfile6.to_csv("detailVolDownsampled.csv",index=None,header=True)
df4 = pd.DataFrame(pd.read_csv("detailVolDownsampled.csv"))


# In[122]:


readfile7.to_csv("detailDownsampled.csv",index=None,header=True)
df5 = pd.DataFrame(pd.read_csv("detailDownsampled.csv"))


# In[133]:


df_t = pd.read_csv('detailTemp.csv',parse_dates=['Realtime'],index_col=['Realtime'])
df_t


# In[132]:


df_t.resample('1Min').sum()


# In[88]:


df_t.resample('1Min').agg(['min','max', 'sum'])


# In[89]:


df_t.resample('1Min', base=1).sum()


# In[94]:


df_d = pd.read_csv('detail.csv',parse_dates=['Absolute Time'],index_col=['Absolute Time'])
df_d


# In[95]:


df_d.resample('1Min').sum()


# In[96]:


df_d.resample('1Min').agg(['min','max', 'sum'])


# In[97]:


df_d.resample('1Min', base=1).sum()


# In[98]:


df_v = pd.read_csv('detailVolDownsampled.csv',parse_dates=['Realtime'],index_col=['Realtime'])
df_v


# In[99]:


df_v.resample('1Min').sum()


# In[100]:


df_t.resample('1Min').agg(['min','max', 'sum'])


# In[101]:


df_v.resample('1Min', base=1).sum()


# In[102]:


from scipy.signal import butter,filtfilt
# Filter requirements.
T = 5.0         # Sample Period
fs = 30.0       # sample rate, Hz
cutoff = 2      # desired cutoff frequency of the filter, Hz ,      slightly higher than actual 1.2 Hz
nyq = 0.5 * fs  # Nyquist Frequency
order = 2       # sin wave can be approx represented as quadratic
n = int(T * fs)


# In[134]:


# sin wave
sig = np.sin(1.2*2*np.pi*T)
# Lets add some noise
noise = 1.5*np.cos(9*2*np.pi*T) + 0.5*np.sin(12.0*2*np.pi*T)
data = sig + noise


# In[135]:


def butter_lowpass_filter(data, cutoff, fs, order):
    normal_cutoff = cutoff / nyq
    # Get the filter coefficients 
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    y = filtfilt(b, a, data)
    return y


# In[137]:


# importing unittest module
import unittest
# unittest will test all the methods whose name starts with 'test'
class SampleTest(unittest.TestCase):
   # return True or False
   def test(self):
      self.assertTrue(True)
# running the test
unittest.main()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




