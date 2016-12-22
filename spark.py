from __future__ import print_function, division

__author__ = 'amrit'

import sys
from pyspark.ml import Pipeline
from pyspark.sql import Row, SQLContext
from pyspark.sql.types import *
from pyspark.ml.feature import RegexTokenizer,StopWordsRemover
from pyspark import SparkContext
from pyspark import SparkConf

sys.dont_write_bytecode = True

def preprocess(sc, path=''):
    row = Row("docs")
    df = sc.textFile(path).map(row).toDF()
    tokenizer = RegexTokenizer(inputCol="docs", outputCol="rawTokens")
    stopwordsremover = StopWordsRemover(inputCol="rawTokens", outputCol="words")

    pipeline = Pipeline(stages=[tokenizer, stopwordsremover])
    model = pipeline.fit(df)
    return model

if __name__ == '__main__':
    sconf = SparkConf()
    sconf.setAppName("yewno")
    sconf.setMaster("localhost")
    sconf.set("spark.executor.memory", "6g")
    sconf.set("spark.driver.memory", "6g")
    sc = SparkContext(conf=sconf)
    dataset = "dataset/file"
    model = preprocess(sc, path=dataset)
