title: "Computational Data Science"
date: 2017-09-23
semester: "Fall 2017"
code: "CMPT 318"

### What are the type of questions data science can answer?
We need well-formed questions.

How many students have GPA below 2.4 

Who are the students, CMPT majors? minors? etc. 
Do part time students count? 
GPA, is it cumulative, or upper divison only etc. 

### Data in Python Notes 

Numpy objects are faster than regular python objects because numpy obj are strongly typed, and are kept in C style arrays. 

`np.vectorize` applys np.ufunc into whole array . 

### Getting Data 
Data format include csv, json, xml. 

Could come from web api, databases. files. 

### Extract-Transform-Load 
`Extract` - take data from source, and load into your workspace 

`Transform` - fixing , cleaning,remove identification, etc.  
janitorial work.

`Load` - save for next pipeline. 

### Noise Filtering / Signal Processing
Part of cleaning, reality is our data can have noise covering up the truth. 

### Locally Weighted Scatterpot Smoothing (LOESS Smoothing)
1. Given a set of data 
2. Take a local fraction of the data 
3. Fit a line through this fraction data. Using least square regression techniques (or others)
4. use that line to be part of the curve for the middle of the neighbourhood
5. continue with the next set of fractions by sliding the window along , generating a curve

LOESS is computational heavy because of constantly recalculating per the sliding window. It gives accurate data if work with lots of data.

LOESS, smaller fraction means smaller set of neighbors, so more sensitive to noise in that region
 
larger fraction means won't respond to signal changes as well.


### What is a covariance matrix
Covariance measures how related item x is to y. Positive covariance means when x moves up, y moves up, Negative Convariance means when x moves up, y moves down. and 0 means they are not related at all

read up on covariance matrix [here](http://www.theanalysisfactor.com/covariance-matrices/)

This matrix just takes this idea, and extends it over multiple items. the matrix is *symmetric* that means when you transpose the table, it is the same values.

note unlike correlation, covariance is not standardized betwee -1 , 1, it's in the original unit.

### Kalman Filtering 
read [article](http://www.bzarg.com/p/how-a-kalman-filter-works-in-pictures/) for explanation.

The filter works with two things, our observations (given by the sensor AKA `Observation matrix`), and our predictions (given by our understanding , AKA `transition matrix`) of what we expect to happen (the prior). Both are assumed to be normal distribution. 

the `observational covariance, R` is how error prone we think about our observations. 

the lower the value, the less sensor errors are assumed, and observations have more effect on result,and more noise. 

the higher the values, the less the noise,

the `transitional covariance, Q` says what we think about our errors in our prediction. 

the lower the value - the less prediction errors are assumed, predictions have more effect on the result, -> less noise

the higher the value - more noise


Using the exercise on GPS data as an example. We know the person can walk at most 1 meter per second, we also know the GPS sensor records a data every 5 seconds. 

This means if the difference between two data point is more than 5 meters. then something is wrong with data. 

In this example, the sensor is the observation, and our knowledge of walking speed is the prediction. 

### Other filtering algorithms

Low-pass or high-pass:  keeps the low or high frequency and discard the opposite. 

Butterworth : not gone over in detail 

### Cleaning / Handling Outlier 
Outliers are tricky, need to be sane about whether the outlier point should kept in (because it is a valid data) or kept out (because it's invalid due to sensor precision)

#### Some actions you can do to "outliers"
* Leave it as is, because it's valid 
* Remove the record, because it's invalid 
* Remove the value and treat it as missing record 
* Impute (which is replace them by calculating a plausible value)

Common ways to impute 
* use nearby values 
* use average of known data 
* use linear regerssion 

may need to impute when you don't want to throw away the record just because of a low important variable. 

#### Regular Expression
python has built in regular expression Python re. 

* r'x' matches an x character
* r'.' matches any single character
* r'\.' matches a single . character
* r'x*' matches 0 or more x
* r'x+' matches 1 or more x
* r'x?' matches x but it's optional (0 or 1)
* r'^' matches start of string
* r'$' matches end of string
* r'[ab\.]+' matches 1+ a or b or .
* r'\d+' matches 1+ digits
* r'\s*' matches 0+ spaces ([ \t\n\r\f\v])
* r'\S*' matches 0+ non-spaces character

#### Hypothesis Testing
\\(H_o\\) is null hypothesis, \\(H_A\\) is the alternate hypothesis, these two cases should cover all scenarios. 

We assume \\(H_o\\) is true, and we test to see what's the probability, \\(p value\\), that it is true. If it is under an predetermined threshold \\(alpha\\) then we can reject \\(H_o\\) , otherwise we __fail__ to reject \\(H_o\\)

We need to make sure we are not running tests over and over until we reach a \\(p<0.05\\) This is a dishonest way to run experiments. (Remember 0.05 is 1/20 pure chance we will get \\(p<0.05\\)) 


#### Student T-Test 
\\(H_o\\) the two groups have similar means  

- Sample is a representative of the population
- Assumes the sample are independent and IID
- Population are normally distributed
- Population has the same variance

If the sample doesn't have these properties, then T-Test would not do any good for you. 

#### Normal Test
We can use the scipy.stats.normaltest to test for normality. 
the \\(H_o\\) is that sample is normally distributed

if data does not pass the normality test, we can transform the data by taking log, or square, or square root, to try for normality again

#### Levenes Test
test to see if two samples  have the same variance

#### Type 1 Error
This is when we incorrectly reject the null hypothesis 

#### Bonferroni Correction
This is used to account for when we are applying multiple hypothesis testings together. We increase our chance of Type 1 errors because we distort our alpha. 

For example, We have three tests with confidence interval of .95 each. that's .95^3 = .86 odds of no incorrect rejection. 
Bonferroni correct fixes this.

#### Tukey Honest Significant Different ( HSD) Test

THis is another way to compare multiple groups of data, instead of just using different T-Test pairs. But Tukey HSD takes in consideration of the number of groups being compared. 


#### Analaysis of Variance (ANOVA)
tests to see if any of the group have different means. 

Assumes group have equal variance, are normally distributed, and IID. 

After ANOVA produces a result, if the result is significant, you can perform a Post Hoc Analysis such as Tukey HSD to find out which group is different.
### Non Parametric Testing
#### Mann Whitney U Test vs Chi Square vs Regression
These tests are used to compare datasets that are not normally distributed. 

__Mann Whitney__ - test whether one group is larger / smaller than another. the values need to be ordinal, and indepedent observations. The idea is if we merge the two datasets together then sort. the output should be even shuffled.  works with data we can ordinal data best, 
__Chi Square__   - works in category of data, forms a contingency table, and sees how out of proportion your data is. whats the chance your variance in the data set is due to chance.  Degree of freedom is related to how many type of samples you got. 
__Regression__   - this is an inference test too, the null hypothesis is that the slope of the line is 0, ie, y does not depend on x. 



### Machine Learning Algorithm

#### Regression (Predict a number)

Taking an input and produce a quantity most relevant to the model. There is linear regression, then there is polynomial regression. Usually the higher degree the input allows closer fit to the data. 

but having too close a fit (overfit) is bad too, because it means the model is good at predicting the training set, but not much anything else.

#### Naive Baye:

Create predictions based on multiplying the likelihoods of various probabilities  together

Baye's Theorem \\(P(A|B) = P(B|A) * P(A)/P(B) \\)

Note, the input features have to be *independent* for this work, hence the name naive.

#### Nearest Neighbours

What k nearest training points are we closest to. 

smaller neighbours result in overfitting the data, and larger neighbours underfit reality. 

#### Support Vector Machines

Generate the best line that has the largest margin with no points inside. This line divides the classifiers. 

with SVM, we need to decide between large margin with many smaller bad points, or smaller margins with few bad points. (soft margin or hard margin respectively)

if the data is not linearly separatable, we can add polynomial features (through the polynomial kernel) for SVM.

the kernel in a SVM adds features to the model input. a kernel can be non-linear, RBF Kernel is another option
#### Neural Net

- Take an input (like pixels in an image)
- feed them into a layer of weights and biases, at each node, we can think of weights as the strength of the various inputs , and bias as how likely this node will be fired.

- have an activation function to normalize the result (squeezes the range of numbers into just 0,and 1)
- the network refers to how the data are arrange in layers, each layer influences the next layer to do stuff
- when we say learning, it refers to how to properly tune the weights and biases.


we add extra layers of computation to do more complex decisions
using back propagation techniques. 

The models need initial weights assigned, then use training data to improve them until the NN converge to good values. 


#### Principal Component Analysis (PCA)

We do PCA to reduce number of dimensions. It does so by finding the vector along the which data has the maximum variance, and continously collapse the data along the vector until out of dimensions. 

### Checking classifier accuracy
__Precision__ 
    how many selected were correct.
__Recall__
    how many correct were found. 
#### Preprocessing

SKLearn MinMax - organize data from 0 to 1, use when distribution is not gaussian or SD is very small
\\((x_i-min(x))/(max(x)-min(x))\\)

StandardScaler - scales your data so distribution is centred around 0, and standard deviation of 1.
\\((x_i-mean(x))/stdev(x)\\) 

### Feature Scaling

MinMaxScaling is 

\\((X - X_{min}) / (X_{max} - X_{min})\\)

StandardScaling is 

\\(z = (x - mean) / SD\\)

so it has mean of 0, and SD of 1.

### Feature Engineering
Machine learning and colour prediction needed feature engineering to get better results (we tested ML using RGB colouring and LAB colouring.)

### Supervised learning
we know the result and train the model for it

### Unsupervised learning
where there is no right answer known but the algorithm tries to find structure in data. Clustering is related to this category 

A few clustering algorithm include `KMeans(), AgglomerativeClustering, AffinityPropagation`

Anomaly Detection is another unsupervise technique, like spot the spam , or attacker on server, credit card charges, etc.



## Spark

Spark dataframes are implemented in Scala, which compiles in Java Virtual Machine. the python code are just for building execution plans.

pySpark and Pandas has some synergy, we can create a spark dataframe with pandas dataframe as a parameter, or python list, 

    :::python
    data = spark.createDataFrame(pd_DF)

and convert back to pandas with
    :::python
    pd_data = data.toPandas()s


Driver - program you are writing.
Executor - manages the data in spark dataframe

in a local spark, one driver and \\(n\\) executor threads.

on a cluster, driver runs on gateway and YARN starts executors on the cluster nodes, the hadoop distributed file system (HDFS) stores data on cluster nodes. the `spark-submit` keyword interacts with YARN

#### Partition
data in RDD are split in partitions, partitions are configurable, and each partition never span multiple machines.

we want partitions to be similar size, so that executors don't sit idle

in general we want between 100 and 10000 partitions

we can explicitly declare for number of partitions like so

    :::python
    x = spark.range(10000, numPartitions=6)

we can combine partitions together with `.coalesce(n)` 

because partitions can be stored on different machines, we need to be careful about __shuffle__ operations, which involves moving data across partitions across different machines. be careful of operations like `.repartition()` `.groupby()` 

operations that can be pipelined, such as `.select(), .filter(), .withColumn(), .drop(), .sample()` are ok 

#### Execution Plan and Lazy Evaluation
although `GroupBy` is a shuffling operation, it's less severe because the spark is optimized for per partition aggregation, we can see by the `spark.explain()` line.  

Spark uses lazy evaluation, which means only the relevant code are run. For example, since `.show()` only displays the top 20 rows, spark only calculates for 20 rows, not the whole dataframe.

we can `cache` intermediate results that we know we will use later on, the `cache` keyword lets spark know this.

**note** we can run SQL queries against spark dataframes by the `.createOrReplaceTempView(tableName)` then we can query against `spark.sql("SELECT foo FROM tableName")` 

with SQL we can't take advantage of caching.

its good to cache before multiple calls, like this

    :::python
    int_range = spark.range(..)
    values = int_range.select(..).cache()
    result1 = values.groupBy(..).agg(..)
    result2 = values.groupBy(..).agg(..)

#### Spark Joins
`join` is a shuffling operations, so we need to be careful, if we have a really small table joining a large table, we would broadcast the small table. 

    :::python
    small_tbl = functions.broadcast(small_tbl)
    joined_data = big_tbl.join(small_tbl, on='id')

#### Spark User Defined Functions
this is used when we want to run our own python functions (or python exclusive libraries such as RGB to LAB) against a column

    :::python
    def complicate_function(a,b):
        return a + 2*b 
    complicated_udf = functions.udf(complicate_function,
                                    returnType=types.IntegerType())

the UDF logic is sent out to the executor, and converted from JVM representation into python, called in python process, and result sent back into JVM

### Resilient Distributed Dataset RDD
the underlying data structure for Spark, is one-dimensional, and holds collection of whatever value we put in.

Dataframes are implemented as `Row` objects of RDD, to work with RDD in python, these are the key words

    :::python
    sc = spark.sparkContext
    rdd = sc.textFile('')
    pprint(rdd.take(6))

`rdd.take(n)` retrieves the first n elements as python list - similar to df.show(n)
`rdd.map(f)` applys a function f to each element - similar to d.select(..)
`rdd.filter(f)` applys a function f to each element, keeps row where returned True - similar to df.filter()

### Numpy / Pandas speed
pandas stores columns in contiguous column, so accessing columns is fast

    :::python
    df['col'].values
    # is faster than
    df.iloc[0] # a row object

    # using numpy libraries is much faster 
    # than using math libraries
    np.sin(df['a'])
    # rather than 
    def do_work(a):
        math.sin(a)
    df['a'].apply(do_work)

numexpr package has own expression syntax compiled internally, and allows for even faster running time

data are stored in columns in contiguous blocks, so accessing columns are fast, rows needs to be constructed so row operations are slow.

from fast to slow

1. numpexpr 
2. numpy expressions
3. vectorize
4. series.apply
5. dataframe.apply
6. python loop

##### Exercise 6
`stats.chi2_contingency()` takes in a pandas pivot table

`stats.mannWhitneyu()` takes in two series 

did anova analysis using `stats.f_oneway(lists of data)` 
 to do pairwise_tukey, we had to use 'melt' to transform wide data into long data

##### Exercise 7


##### Exercise 10
Part 1 

intro to pyspark, we learned spark dataframe, keyword is `spark.read.json` to take in a json file and turn into dataframe. 

`groupBy().mean().sort()` commands can be chained

##### Exercise 11
Part 1

We used spark dataframe to get reddit comment relative scores, the main point of the exercise was to practice placing caches at the right spot. we learn that caching before multiple operations is the best, predefine the schema is helpful too as it defines the data type of each column

broadcasting a small table to a big table is better than joining.

Part 2

here we practice using RDD to clean data. `spark.sparkContext.textFile` gets the RDD, then we can `map` and `filter` to clean the RDD dataset

we added columns to a spark dataframe with the `df.withColumn(newColumnName, col operations)` keyword


##### Exercise 12
we used pySpark to get a word count of the most common words in a few novels.
the key methods we used were 

`spark.df.explode` which transposes one row into multiple rows

`spark.df.split` which splits one row value base on a regex string