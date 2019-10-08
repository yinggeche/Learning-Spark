allFiles = sc.wholeTextFiles('dir')
# loads all files in directory 'dir' in a PairRDD, with file names as keys end file contents as values

1. 创建pairRDD
pairs = lines.map(lambda x: (x.split(" ")[0], x))
2. transformations
# pairRDD的转化操作
reduceByKey((x,y):x+y) #合并具有相同键的值 !!!shuffle
返回 所有key和用key规约出来的结果值
groupByKey() #对具有相同键的值进行分组
combineBy()
mapValues(func) #对值改变
mapKeys(func)
flatMapValues(func)
keys() #返回keysRDD
values() #返回valuesRDD
sortByKey() #返回根据key排序的RDD
foldByKey()
combineByKey(createCombiner, mergeValue, mergeCombiners)
#类似于aggregat
求平均值
keyAvg = words.combineByKey((lambda x: (x,1)), #ture a V into C
    (lambda x,y:(x[0]+y, x[1]+1)), # merge a V into a C
    (lambda x, y: (x[0] + y[0]), (x[1] + y[1]))) # combines 2 C into a single one
    .mapValues(lambda (val, count): 1.*val/count)

# 对两个pairRDD的转化操作
rdd1.subtractByKey(rdd2) #删掉与rdd2的key相同的元素
rdd1.join(rdd2) #内连接，key相同，把values放在一起(key,(values1, values2))
# !!!shuffle
rdd1.rightOuterJoin(rdd2) #保留rdd2必须存在
rdd1.leftOuterJoin(rdd2) #保留rdd1必须存在
rdd1.cogroup(rdd2) #把相同键的分组到一起
{(1,(2,[])), (3, ([4, 6], [9]))}
# 对第二个元素进行筛选
result = pairs.filter(lambda keyValue: len(keyValue[1]) > 20)
3. actions
count = rdd.countByKey() 每个键计数 = {(1, 1), (3, 2)}
collectAsMap() #返回一个方便查询的映射表
lookup(key) #返回键key对应的所有值 [4, 6]

4. 数据分区
m workers with k processors each
"ideal" #partitions = m k
