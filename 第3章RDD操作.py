第三章 Spark program and shell session will work as follows：

A. Create some input RDDs from external data.
lines = sc.textFile("readme.md")
#使用textFile创建一个新的RDD
lines = sc.parallelize(["pandas", "i like pandas"])
#把程序中已有的集合传递给SparkContext的parallelize方法

B. Transform them to define new RDDs using transformations.
*Transforms: construct a new RDD from a previous one.
# -------针对各个元素 Element-wise transformations----------
1.  rdd1 = lines.filter(lambda line: "Python" in line)
    rdd2 = lines.filter(lambda word: word != '')
    rdd3 = rdd1.union(rdd2) # 打印出满足1或2的行数
2. map() #接收一个函数（用lambda)，把这个函数应用于RDD中每个元素
    #返回值不需要和输入类型一样
    nums = sc.parallelize([1,2,3,4])
    square = nums.map(lambda x: x * x)
3. flatMap() # 对每个输入元素生成多个输出元素
    #得到了由各列表中元素组成的RDD
    lines = sc.parallelize(["hello world","hi"])
    words = lines.flatMap(lambda line: line.split(" "))
    #flatMap must return a collect(e.g. list)
4. rdd1.distinct() #生成一个只包含不同元素的new RDD
# ------伪集合操作 Pseudo set operations---------
5. rdd1.union(rdd2) #包含两个RDD所有元素的RDD，包含重复数据
6. rdd1.intersection(rdd2) #只返回两个RDD中都有的元素，去掉所有重复元素
# 性能差，需要shuffle来发现共有元素
7. rdd1.subtract(rdd2) #只存在于RDD1，不存在于RDD2。需要suffle
8. rdd1.cartesian(rdd2) #所有可能的(a, b) pair
# a in rdd1, b in rdd2, 大规模cartesian product开销大

C. Ask Spark to persist()/cache() any intermediate RDDs
    that will need to be reused.
lines.persist() = lines.cache()
#多次action中重用此RDD，让spark把这个RDD存下来
lines.unpersist() #手动把persist的RDD从内存中移除

D. Launch actions to kick off触发 a parallel computation,
   which is then optimized and executed by Spark.
 #每调用一个新的action，整个RDD都会从头计算
*Action:  1. compute a result based on an RDD
          2. return it to the driver program
          or save it to an external storage system (e.g., HDFS).
1. sum = rdd.reduce(lambda x, y: x + y)
# 接受一个函数做参数，操作两个RDD的元素类型的数据，返回同类型新元素
   sum = rdd.fold(0)(lambda x, y: x + y)
# 接受一个函数做参数，需要初始值(期望的类型)，返回值类型与输入相同
2. lines.first() #返回RDD第一个元素
3. lines.count() #计数
4. lines.take(10) #收集RDD中少量元素，顺序可能不同
5. lines.collect() #获取整个RDD的数据
#只有整个数据集在单台机器内存中放得下才可以
6. saveAsTextFile()/ saveAsSequenceFile()
# 把RDD用自带的格式保存起来
7. countByValue # 各元素在RDD中出现的次数
8. top(10) #最前面的10个元素
9. takeOrdered(10)(ordering)
takeOrdered(20, key = lambda(x): -x) 降序
#从RDD中按照提供的顺序返回最前面的10个元素
takeOrdered(20, key = lambda(x,y): -y) 按照pair中value降序取前20个
10. takeSample(withReplacement, num, [seed])
# 从RDD中返回任意一些元素
rdd.takeSample(false, 1) #返回任意
sample(withReplacement, fraction, seed)
# withReplacement：是否放回，ture有放回，false无放回
# fraction: 抽取多少比例的数据
# seed：随即种子值为多少；e.g. 3:可能以1,2,3其中一个为起始值
11. aggregate!!! #通常返回不同类型的函数
e.g. 计算average
sc = sc.parallelize([1,2,3,4], 2)
seqOp = (lambda x, y: (x[0] + y, x[1] + 1))
# 对RDD里每个partition里要实施的操作
combOp = (lambda x, y: (x[0] + y[0], x[1] + y[1]))
# 对所有的partition汇总的操作
sumCount = sc.aggregate((0.0), seqOp, combOp)
>>>(10,4)
average = sumCount[0]/float(sumCount[1])
>>>2.5
12. foreach(func) #对RDD中每个元素使用给定的函数

E. lazy evaluation
Spark will not begin to execute until an action

F. Passing Functinos to Spark
1. word = rdd.filter(lambda s: "error" in s)
2. def containerror(s)
        return "error" in s
    word = rdd.filter(containerror)
