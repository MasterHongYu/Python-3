#不要用跟模組名稱一樣的檔案名!!!
import random as rand
dataRandom = rand.uniform(0.0,1.0)
print(round(dataRandom,3))
dataRandom = round(rand.normalvariate(100,10),2)
print(dataRandom)
import statistics as stat
listRandom = [1,3,7,4,9,24,58,89,137,245,289]
dataRandomMean = stat.mean(listRandom)
dataRandomMedian = stat.median(listRandom)
dataRandomStdev = stat.stdev(listRandom)
print(round(dataRandomMean),dataRandomMedian,round(dataRandomStdev))

'''
import numpy as np
data = np.array([1,2,3,4])
print(data)
print(data.size)'''