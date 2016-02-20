from pyspark.mllib.feature import HashingTF,IDF
from pyspark import SparkConf,SparkContext
import math
conf = SparkConf().setMaster("local").setAppName("big_data")
sc = SparkContext(conf=conf)
dirinput = "../bigdata/hw1/stock/amazon.txt"

rdd = sc.textFile(dirinput).flatMap(lambda text:text.split()).map(lambda string: float(string))
stats = rdd.stats()
pstdev = stats.stdev()
pmean = stats.mean()
outliers = rdd.filter(lambda x: math.fabs(x-pmean)>2*pstdev)
print outliers.collect()