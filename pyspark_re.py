from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession 
spark = SparkSession.builder.appName("Python Spark DataFrames basic example").config("spark.some.config.option", "some-value").getOrCreate()

df = spark.read.option('header', True).csv('GL_return.csv', )
print(df)