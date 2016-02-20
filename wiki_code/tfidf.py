from pyspark.mllib.feature import HashingTF,IDF
from pyspark import SparkConf,SparkContext
conf = SparkConf().setMaster("local").setAppName("big_data")
sc = SparkContext(conf=conf)
dirinput = "../bigdata/hw1/wikiset"
diroutput = "../bigdata/hw1/wikitfidf"
rdd = sc.wholeTextFiles(dirinput).map(lambda (name,text):text.split())
tf = HashingTF()
tfVectors = tf.transform(rdd).cache()
idf = IDF()
idfModel = idf.fit(tfVectors)
tfIdfVectors = idfModel.transform(tfVectors)
tfIdfVectors.saveAsTextFile(diroutput)