from pyspark.mllib.feature import HashingTF, IDF
from pyspark import SparkConf, SparkContext
import json
import re
#from pprint import pprint


conf = SparkConf().setMaster("local").setAppName("HW12")
sc = SparkContext(conf = conf)

keyword_list = ['ibm','google','amazon','facebook','bloomberg']


folder_name = '/Users/yibeihuang/Desktop/Se2-Resources/BigData/HW/tweefile'
# Read a set of text files as TF vector
rdd = sc.wholeTextFiles(folder_name).map(lambda (name, text): text.split())
tf = HashingTF()
tfVectors = tf.transform(rdd).cache()
# Compute the IDF, then the TF-IDF vectors
idf = IDF()
idfModel = idf.fit(tfVectors)
tfIdfVectors = idfModel.transform(tfVectors)

#################
result = tfVectors.collect()
result = str(result)
resultFile = '/Users/yibeihuang/Desktop/Se2-Resources/BigData/HW/tweersultfile/result.txt'
with open(resultFile, 'w') as f2:
	f2.write(result)
