import sys
from pyspark import SparkContext

if __name__ == "__main__":
    lines = sc.textFile("graph")

    graph_rdd = lines.map(eval) \
                    .groupByKey() \
                    .mapValues(list) \
                    .partitionBy(10) \
                    .cache()

    nodes = graph_rdd.flatMap(lambda (i, edgelist):edgelist+[i]) \
                    .distinct() \
                    .cache()

    size = nodes.count()
    scores = nodes.map(lambda i: (i, 1.0/size)) \
                .partitionBy(10) \
                .cache()

    i = 0
    eps = 0.001
    max_iterations = 100
    err = eps + 1.0
    while i<max_iterations and err>eps:
        i +=1
        old_scores = old_scores
        joined = graph_rdd.join(scores)
        scores = joined.values() \
                    .flatMap(lambda (neighborlist, score): [(x, 1.0*score/)])
