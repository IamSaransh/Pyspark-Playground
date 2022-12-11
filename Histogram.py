from pyspark.sql import SparkSession
import collections

spark = SparkSession.builder.appName("hehe").getOrCreate()

lines = spark.read.text("ml-100k/u.data")
lines.show()

# write.text("WorkSpace/PySpark/ml-100k/output.txt")
