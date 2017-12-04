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

np.vectorize applys np.ufunc into whole array . 

### Getting Data 
Data format include csv, json, xml. 

Could come from web api, databases. files. 

### Extract-Transform-Load 
Extract - take data from source, and load into your workspace 
Transform - fixing , cleaning,remove identification, etc.  janitorial work.
Load - save for next pipeline. 

### Noise Filtering / Signal Processing
Part of cleaning, reality is our data can have noise covering up the truth. 

### Locally Weighted Scatterpot Smoothing (LOESS Smoothing)
1. Given a set of data 
2. Take a local fraction of the data 
3. Fit a line through this fraction data. Using least square regression techniques (or others)
4. use that line to be part of the curve for the middle of the neighbourhood
5. continue with the next set of fractions by sliding the window along , generating a curve

LOESS is computational heavy because of constantly recalculating per the sliding window. It gives accurate data if work with lots of data.

### What is a covariance matrix
Covariance measures how related item x is to y. Positive covariance means when x moves up, y moves up, Negative Convariance means when x moves up, y moves down. and 0 means they are not related at all

read up on covariance matrix [here](http://www.theanalysisfactor.com/covariance-matrices/)

This matrix just takes this idea, and extends it over multiple items. the matrix is *symmetric* that means when you transpose the table, it is the same values.

### Kalman Filtering 
read [article](http://www.bzarg.com/p/how-a-kalman-filter-works-in-pictures/) for explanation.

The filter works with two things, our observations, and our predictions of what we expect to happen (the prior). Both are assumed to be normal distribution. 

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

After ANOVA produces a result, if the result is significant, you can perform a Post Hoc Analysis such as Tukey HSD to further check the means difference. 

### Non Parametric Testing
#### Mann Whitney U Test vs Chi Square vs Regression
These tests are used to compare datasets that are not normally distributed. 

__Mann Whitney__ - test whether one group is larger / smaller than another. the values need to be ordinal, and indepedent observations. The idea is if we merge the two datasets together then sort. the output should be even shuffled. 
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

Large margin with many smaller bad points, or smaller margins with few bad points. 

#### Neural Net
The hottest thing in machine learning, 
It works with idea of Perceptron

- Take an input
- weight them 
- have an activation function to normalze the result
- also learn the weights from training data. 

we add extra layers of computation to do more complex decisions
using back propagation techniques. 

The models need initial weights assigned, then use training data to improve them until the NN converge to good values. 


#### Principal Component Analysis (PCA)

We do PCA to reduce number of dimensions. It does so by finding the vector along the which data has the maximum variance, and continously collapse the data long the vector until out of dimensions. 

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

    (X - X_min) / (X_max - X_min)

StandardScaling is 

    z = (x - mean) / SD

so it has mean of 0, and SD of 1.

### Feature Engineering
Machine learning and colour prediction needed feature engineering to get better results (we tested ML using RGB colouring and LAB colouring.)

### Supervised learning
we know the result and train the model for it

### Unsupervised learning
where there is no right answer known but the algorithm tries to find structure in data. Clustering is related to this category

