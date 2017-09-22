title: Implicit Recommender System
date: 2017-09-21

I made a recommender system in my co-op term. I have the HTML copy of the jupyter notebook [here](/static/implicitALS.html)

A Flask app of the system in action [here](/recommender)

```python
import pandas as pd
import scipy.sparse as sparse
import numpy as np
from scipy.sparse.linalg import spsolve
```

# Implicit Recommender System

Like the title says, we are using implicit data to create a recommender system. The idea is that the more times a user have purchased something, the more confident we are that they like this item. We will use this as a metric.

## Cleaning the Data

The dataset is a spreadsheet of shopping history at a grocery store. 


```python
website_url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/00352/Online%20Retail.xlsx'
retail_data = pd.read_excel(website_url) # This may take a couple minutes
```


```python
retail_data.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>InvoiceNo</th>
      <th>StockCode</th>
      <th>Description</th>
      <th>Quantity</th>
      <th>InvoiceDate</th>
      <th>UnitPrice</th>
      <th>CustomerID</th>
      <th>Country</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>536365</td>
      <td>85123A</td>
      <td>WHITE HANGING HEART T-LIGHT HOLDER</td>
      <td>6</td>
      <td>2010-12-01 08:26:00</td>
      <td>2.55</td>
      <td>17850.0</td>
      <td>United Kingdom</td>
    </tr>
    <tr>
      <th>1</th>
      <td>536365</td>
      <td>71053</td>
      <td>WHITE METAL LANTERN</td>
      <td>6</td>
      <td>2010-12-01 08:26:00</td>
      <td>3.39</td>
      <td>17850.0</td>
      <td>United Kingdom</td>
    </tr>
    <tr>
      <th>2</th>
      <td>536365</td>
      <td>84406B</td>
      <td>CREAM CUPID HEARTS COAT HANGER</td>
      <td>8</td>
      <td>2010-12-01 08:26:00</td>
      <td>2.75</td>
      <td>17850.0</td>
      <td>United Kingdom</td>
    </tr>
    <tr>
      <th>3</th>
      <td>536365</td>
      <td>84029G</td>
      <td>KNITTED UNION FLAG HOT WATER BOTTLE</td>
      <td>6</td>
      <td>2010-12-01 08:26:00</td>
      <td>3.39</td>
      <td>17850.0</td>
      <td>United Kingdom</td>
    </tr>
    <tr>
      <th>4</th>
      <td>536365</td>
      <td>84029E</td>
      <td>RED WOOLLY HOTTIE WHITE HEART.</td>
      <td>6</td>
      <td>2010-12-01 08:26:00</td>
      <td>3.39</td>
      <td>17850.0</td>
      <td>United Kingdom</td>
    </tr>
  </tbody>
</table>
</div>



We take out the rows with empty customer IDs


```python
cleaned_retail = retail_data.loc[pd.isnull(retail_data.CustomerID) == False]
```


```python
cleaned_retail.info()
```

    <class 'pandas.core.frame.DataFrame'>
    Int64Index: 406829 entries, 0 to 541908
    Data columns (total 8 columns):
    InvoiceNo      406829 non-null object
    StockCode      406829 non-null object
    Description    406829 non-null object
    Quantity       406829 non-null int64
    InvoiceDate    406829 non-null datetime64[ns]
    UnitPrice      406829 non-null float64
    CustomerID     406829 non-null float64
    Country        406829 non-null object
    dtypes: datetime64[ns](1), float64(2), int64(1), object(4)
    memory usage: 27.9+ MB


Here we create a look up table for fast retrieval of descriptions


```python
item_lookup = cleaned_retail[['StockCode', 'Description']].drop_duplicates()
item_lookup['StockCode'] = item_lookup.StockCode.astype(str)

```


```python
item_lookup.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>StockCode</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>85123A</td>
      <td>WHITE HANGING HEART T-LIGHT HOLDER</td>
    </tr>
    <tr>
      <th>1</th>
      <td>71053</td>
      <td>WHITE METAL LANTERN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>84406B</td>
      <td>CREAM CUPID HEARTS COAT HANGER</td>
    </tr>
    <tr>
      <th>3</th>
      <td>84029G</td>
      <td>KNITTED UNION FLAG HOT WATER BOTTLE</td>
    </tr>
    <tr>
      <th>4</th>
      <td>84029E</td>
      <td>RED WOOLLY HOTTIE WHITE HEART.</td>
    </tr>
  </tbody>
</table>
</div>



We want to just focus on the interaction between customers, items, and number of items they bought. So we only keep those three columns. 

because of a quirk in the dataset, any sum that equals to zero signifies that the item was returned. We just set it to one for the sake of our experiment.

Finally, we keep the customers that have made a purchase by filtering by quantity > 0


```python
cleaned_retail['CustomerID'] = cleaned_retail.CustomerID.astype(int)
cleaned_retail = cleaned_retail[['StockCode', 'Quantity', 'CustomerID']]
grouped_cleaned = cleaned_retail.groupby(['CustomerID', 'StockCode']).sum().reset_index()
grouped_cleaned.Quantity.loc[grouped_cleaned.Quantity == 0] = 1
grouped_purchased = grouped_cleaned.query('Quantity > 0')
```

    /Users/jason/anaconda/envs/myEnv/lib/python2.7/site-packages/ipykernel_launcher.py:1: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      """Entry point for launching an IPython kernel.
    /Users/jason/anaconda/envs/myEnv/lib/python2.7/site-packages/pandas/core/indexing.py:179: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      self._setitem_with_indexer(indexer, value)



```python
grouped_purchased.head()

```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>CustomerID</th>
      <th>StockCode</th>
      <th>Quantity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>12346</td>
      <td>23166</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>12347</td>
      <td>16008</td>
      <td>24</td>
    </tr>
    <tr>
      <th>2</th>
      <td>12347</td>
      <td>17021</td>
      <td>36</td>
    </tr>
    <tr>
      <th>3</th>
      <td>12347</td>
      <td>20665</td>
      <td>6</td>
    </tr>
    <tr>
      <th>4</th>
      <td>12347</td>
      <td>20719</td>
      <td>40</td>
    </tr>
  </tbody>
</table>
</div>



We create a ${n}$ by ${m}$ table where ${n}$ is number of users and ${m}$ is number of items and each value in the table is how many items each person bought. 

We store this table into a sparse matrix for memory management


```python
customers = list(np.sort(grouped_purchased.CustomerID.unique())) # get unique customers
products = list(grouped_purchased.StockCode.unique()) # get unique products
quantity = list(grouped_purchased.Quantity) # all of our purchases

rows = grouped_purchased.CustomerID.astype('category', categories = customers).cat.codes
# get the associated row indices 
cols = grouped_purchased.StockCode.astype('category', categories = products).cat.codes
# get the associated column dices 
purchases_sparse = sparse.csr_matrix((quantity, (rows,cols)), shape=(len(customers), len(products)))
```


```python
purchases_sparse
```




    <4338x3664 sparse matrix of type '<type 'numpy.int64'>'
    	with 266723 stored elements in Compressed Sparse Row format>



## Creating a Training and Validation Set
 
Typically people use a percentage of the data as the training set, and a percentage as validation. but since we need all the reader / document interactions to find the proper matrix factorization, we would need a different method
 
To set up the training set, we will mask a certain percentage reader / document at random, then we will check how many of the items that were recommended the reader actually read.
 


```python
# This portion we will now figure out the training set and testing set
import random
def make_train(ratings, pct_test = 0.2):
    '''
    This function will take in the original user-item matrix and "mask" a percentage of the original ratings where a
    user-item interaction has taken place for use as a test set. The test set will contain all of the original ratings, 
    while the training set replaces the specified percentage of them with a zero in the original ratings matrix. 
    
    parameters: 
    
    ratings - the original ratings matrix from which you want to generate a train/test set. Test is just a complete
    copy of the original set. This is in the form of a sparse csr_matrix. 
    
    pct_test - The percentage of user-item interactions where an interaction took place that you want to mask in the 
    training set for later comparison to the test set, which contains all of the original ratings. 
    
    returns:
    
    training_set - The altered version of the original data with a certain percentage of the user-item pairs 
    that originally had interaction set back to zero.
    
    test_set - A copy of the original ratings matrix, unaltered, so it can be used to see how the rank order 
    compares with the actual interactions.
    
    user_inds - From the randomly selected user-item indices, which user rows were altered in the training data.
    This will be necessary later when evaluating the performance via AUC.
    '''
    test_set = ratings.copy() # Make a copy of the original set to be the test set. 
    test_set[test_set != 0] = 1 # Store the test set as a binary preference matrix
    training_set = ratings.copy() # Make a copy of the original data we can alter as our training set. 
    nonzero_inds = training_set.nonzero() # Find the indices in the ratings data where an interaction exists
    nonzero_pairs = list(zip(nonzero_inds[0], nonzero_inds[1])) # Zip these pairs together of user,item index into list
    random.seed(0) # Set the random seed to zero for reproducibility
    num_samples = int(np.ceil(pct_test*len(nonzero_pairs))) # Round the number of samples needed to the nearest integer
    samples = random.sample(nonzero_pairs, num_samples) # Sample a random number of user-item pairs without replacement
    user_inds = [index[0] for index in samples] # Get the user row indices
    item_inds = [index[1] for index in samples] # Get the item column indices
    training_set[user_inds, item_inds] = 0 # Assign all of the randomly chosen user-item pairs to zero
    training_set.eliminate_zeros() # Get rid of zeros in sparse array storage after update to save space
    return training_set, test_set, list(set(user_inds)) # Output the unique list of user rows that were altered  
```


```python
product_train, product_test, product_users_altered = make_train(purchases_sparse, pct_test= 0.2)
```

# Alternating Least Square (ALS)
 
ALS is an optimization technique through matrix factorization. It finds the latent factors between users, and items.
 
preferences are assumed to be the inner product $ p_{ui} = x^t_uy_i $ , where $ x_u $ is the user factor, and $ y_i $ is the item factor respectively. The vectors strive to map users and items into a common latent factor space where they can be compared directly.
 

 
[Link to the paper by Hu, Koren, and Volinksy](http://yifanhu.net/PUB/cf.pdf)
 
## Parameters
 
1. **alpha** - this is the rate of increasing our confidence in a $ r_{ui} $ pair
2. **factor** - the number of latent factors, default is 20
3. **regularization** - regularization scaling for both user and item factors to prevent overfit. Default is 0.1
4. **iterations** - number of iterations to run the ALS optimization. Default is 50


## Intuition

In collaborative filtering, there are two types of models, one is the nearst neigbhour model, where we use the ratings of "most similar" users to make decisions. 

The second is latent factor analysis (LFA), where we solve for the underlying factors that drives the rating. 

LFA is inspired by Principal Componet Analysis (PCA). PCA tries to explain what is the main driving force that explains all the patterns we see in the data set. 

If we can figure out the underlying factor determing that influences the rates. We can use it to predict any ratings for a product by a user. 

### How does LFA work? 

we decompose the user / item matrix to two matrices, one is $ U $ user describe by some underlying factors, and the other is product matrix , describe by the same factors. 

We solve for the two matrix using the ratings we already known. 

If we look at the two matrices, it looks alot like 
content base filtering, whereas factors are usually derived by experts, and each factors is usually a product attribute (for example, a book's factor might be genre, or author). Latent Factors are derived by machine learning techniques, the factors might not be associated with a product attribute, it may be abstract. 

where each user has a set of features they like, and each document has a set of features they are. 



```python
# using Ben Frederickson's algo. https://github.com/benfred/implicit
import implicit
alpha = 15
user_vecs, item_vecs = implicit.alternating_least_squares((product_train*alpha).astype('double'),
                                                           factors = 20,
                                                           regularization = 0.1,
                                                           iterations = 50)
```

    No handlers could be found for logger "implicit"



```python
user_vecs[0, :].dot(item_vecs).toarray()[0,:5]
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-16-f13ceb6904d3> in <module>()
    ----> 1 user_vecs[0, :].dot(item_vecs).toarray()[0,:5]
    

    ValueError: shapes (20,) and (3664,20) not aligned: 20 (dim 0) != 3664 (dim 0)


# Evaluating the Recommender System
 
 
We have to see if the order of recommendations given for each user matches the documents they have read. The way to calculate this is to use the [Receiver Operating Characteristics](https://en.wikipedia.org/wiki/Receiver_operating_characteristic) curve.
The greater the area under the curve, the higher the recommended item is on the list.
 
In order to do that, we need to write a function that can calculate a mean area under the curve (AUC) for any user that had at least one masked item. As a benchmark, we will also calculate what the mean AUC would have been if we had simply recommended the most popular items. Popularity tends to be hard to beat in most recommender system problems, so it makes a good comparison.
 


```python
from sklearn import metrics
def auc_score(predictions, test):
    '''
    This simple function will output the area under the curve using sklearn's metrics. 
    
    parameters:
    
    - predictions: your prediction output
    
    - test: the actual target result you are comparing to
    
    returns:
    
    - AUC (area under the Receiver Operating Characterisic curve)
    '''
    fpr, tpr, thresholds = metrics.roc_curve(test, predictions)
    return metrics.auc(fpr, tpr)   
```

We can now use this function to see how our recommender system is doing. To use this function, we will need to transform our output from the ALS function to csr_matrix format and transpose the item vectors. The original pure Python version output the user and item vectors into the correct format already.
 
The calc_mean_auc outputs two numbers, test and popularity benchmark. We want our test to be better than the popularity be


```python
def calc_mean_auc(training_set, altered_users, predictions, test_set):
    '''
    This function will calculate the mean AUC by user for any user that had their user-item matrix altered. 
    
    parameters:
    
    training_set - The training set resulting from make_train, where a certain percentage of the original
    user/item interactions are reset to zero to hide them from the model 
    
    predictions - The matrix of your predicted ratings for each user/item pair as output from the implicit MF.
    These should be stored in a list, with user vectors as item zero and item vectors as item one. 
    
    altered_users - The indices of the users where at least one user/item pair was altered from make_train function
    
    test_set - The test set constucted earlier from make_train function
    
    
    
    returns:
    
    The mean AUC (area under the Receiver Operator Characteristic curve) of the test set only on user-item interactions
    there were originally zero to test ranking ability in addition to the most popular items as a benchmark.
    '''
    
    
    store_auc = [] # An empty list to store the AUC for each user that had an item removed from the training set
    popularity_auc = [] # To store popular AUC scores
    pop_items = np.array(test_set.sum(axis = 0)).reshape(-1) # Get sum of item iteractions to find most popular
    item_vecs = predictions[1]
    for user in altered_users: # Iterate through each user that had an item altered
        training_row = training_set[user,:].toarray().reshape(-1) # Get the training set row
        zero_inds = np.where(training_row == 0) # Find where the interaction had not yet occurred
        # Get the predicted values based on our user/item vectors
        user_vec = predictions[0][user,:]
        pred = user_vec.dot(item_vecs).toarray()[0,zero_inds].reshape(-1)
        # Get only the items that were originally zero
        # Select all ratings from the MF prediction for this user that originally had no iteraction
        actual = test_set[user,:].toarray()[0,zero_inds].reshape(-1) 
        # Select the binarized yes/no interaction pairs from the original full data
        # that align with the same pairs in training 
        pop = pop_items[zero_inds] # Get the item popularity for our chosen items
        store_auc.append(auc_score(pred, actual)) # Calculate AUC for the given user and store
        popularity_auc.append(auc_score(pop, actual)) # Calculate AUC using most popular and score
    # End users iteration
    
    return float('%.3f'%np.mean(store_auc)), float('%.3f'%np.mean(popularity_auc))  
   # Return the mean AUC rounded to three decimal places for both test and popularity benchmark
```


```python
calc_mean_auc(product_train, product_users_altered, [sparse.csr_matrix(user_vecs), 
                                                     sparse.csr_matrix(item_vecs.T)],
                                                     product_test)
```




    (0.87, 0.812)




```python
customers_arr = np.array(customers)
products_arr = np.array(products)
```


```python
def get_items_purchased(customer_id, mf_train, customers_list, products_list, item_lookup):
    '''
    This just tells me which items have been already purchased by a specific user in the training set. 
    
    parameters: 
    
    customer_id - Input the customer's id number that you want to see prior purchases of at least once
    
    mf_train - The initial ratings training set used (without weights applied)
    
    customers_list - The array of customers used in the ratings matrix
    
    products_list - The array of products used in the ratings matrix
    
    item_lookup - A simple pandas dataframe of the unique product ID/product descriptions available
    
    returns:
    
    A list of item IDs and item descriptions for a particular customer that were already purchased in the training set
    '''
    cust_ind = np.where(customers_list == customer_id)[0][0] # Returns the index row of our customer id
    purchased_ind = mf_train[cust_ind,:].nonzero()[1] # Get column indices of purchased items
    prod_codes = products_list[purchased_ind] # Get the stock codes for our purchased items
    return item_lookup.loc[item_lookup.StockCode.isin(prod_codes)]
```


```python
customers_arr[:5]
```




    array([12346, 12347, 12348, 12349, 12350])




```python
customers_arr.shape
```




    (4338,)




```python
product_train.shape
```




    (4338, 3664)




```python
from sklearn.preprocessing import MinMaxScaler
def rec_items(customer_id, mf_train, user_vecs, item_vecs, customer_list, item_list, item_lookup, num_items = 10):
    '''
    This function will return the top recommended items to our users 
    
    parameters:
    
    customer_id - Input the customer's id number that you want to get recommendations for
    
    mf_train - The training matrix you used for matrix factorization fitting
    
    user_vecs - the user vectors from your fitted matrix factorization
    
    item_vecs - the item vectors from your fitted matrix factorization
    
    customer_list - an array of the customer's ID numbers that make up the rows of your ratings matrix 
                    (in order of matrix)
    
    item_list - an array of the products that make up the columns of your ratings matrix
                    (in order of matrix)
    
    item_lookup - A simple pandas dataframe of the unique product ID/product descriptions available
    
    num_items - The number of items you want to recommend in order of best recommendations. Default is 10. 
    
    returns:
    
    - The top n recommendations chosen based on the user/item vectors for items never interacted with/purchased
    '''
    
    cust_ind = np.where(customer_list == customer_id)[0][0] # Returns the index row of our customer id
    pref_vec = mf_train[cust_ind,:].toarray() # Get the ratings from the training set ratings matrix
    pref_vec = pref_vec.reshape(-1) + 1 # Add 1 to everything, so that items not purchased yet become equal to 1
    pref_vec[pref_vec > 1] = 0 # Make everything already purchased zero
    rec_vector = user_vecs[cust_ind,:].dot(item_vecs.T) # Get dot product of user vector and all item vectors
    # Scale this recommendation vector between 0 and 1
    min_max = MinMaxScaler()
    rec_vector_scaled = min_max.fit_transform(rec_vector.reshape(-1,1))[:,0] 
    recommend_vector = pref_vec*rec_vector_scaled 
    # Items already purchased have their recommendation multiplied by zero
    product_idx = np.argsort(recommend_vector)[::-1][:num_items] # Sort the indices of the items into order 
    # of best recommendations
    rec_list = [] # start empty list to store items
    for index in product_idx:
        code = item_list[index]
        rec_list.append([code, item_lookup.Description.loc[item_lookup.StockCode == code].iloc[0]]) 
        # Append our descriptions to the list
    codes = [item[0] for item in rec_list]
    descriptions = [item[1] for item in rec_list]
    final_frame = pd.DataFrame({'StockCode': codes, 'Description': descriptions}) # Create a dataframe 
    return final_frame[['StockCode', 'Description']] # Switch order of columns around
```

# Testing this out

We test this out, using customer #12390 as an example


```python
rec_items(12390, product_train, user_vecs, item_vecs, customers_arr, products_arr, item_lookup,
                       num_items = 10)
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>StockCode</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>22027</td>
      <td>TEA PARTY BIRTHDAY CARD</td>
    </tr>
    <tr>
      <th>1</th>
      <td>22138</td>
      <td>BAKING SET 9 PIECE RETROSPOT</td>
    </tr>
    <tr>
      <th>2</th>
      <td>22029</td>
      <td>SPACEBOY BIRTHDAY CARD</td>
    </tr>
    <tr>
      <th>3</th>
      <td>22716</td>
      <td>CARD CIRCUS PARADE</td>
    </tr>
    <tr>
      <th>4</th>
      <td>22714</td>
      <td>CARD BIRTHDAY COWBOY</td>
    </tr>
    <tr>
      <th>5</th>
      <td>22046</td>
      <td>TEA PARTY  WRAPPING PAPER</td>
    </tr>
    <tr>
      <th>6</th>
      <td>22617</td>
      <td>BAKING SET SPACEBOY DESIGN</td>
    </tr>
    <tr>
      <th>7</th>
      <td>22983</td>
      <td>CARD BILLBOARD FONT</td>
    </tr>
    <tr>
      <th>8</th>
      <td>22037</td>
      <td>ROBOT BIRTHDAY CARD</td>
    </tr>
    <tr>
      <th>9</th>
      <td>22899</td>
      <td>CHILDREN'S APRON DOLLY GIRL</td>
    </tr>
  </tbody>
</table>
</div>



and what items did customer #12390 actually purchase?


```python
get_items_purchased(12390, product_train, customers_arr, products_arr, item_lookup)
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>StockCode</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>10</th>
      <td>22745</td>
      <td>POPPY'S PLAYHOUSE BEDROOM</td>
    </tr>
    <tr>
      <th>34</th>
      <td>22326</td>
      <td>ROUND SNACK BOXES SET OF4 WOODLAND</td>
    </tr>
    <tr>
      <th>35</th>
      <td>22629</td>
      <td>SPACEBOY LUNCH BOX</td>
    </tr>
    <tr>
      <th>43</th>
      <td>22544</td>
      <td>MINI JIGSAW SPACEBOY</td>
    </tr>
    <tr>
      <th>44</th>
      <td>22492</td>
      <td>MINI PAINT SET VINTAGE</td>
    </tr>
    <tr>
      <th>92</th>
      <td>21094</td>
      <td>SET/6 RED SPOTTY PAPER PLATES</td>
    </tr>
    <tr>
      <th>96</th>
      <td>21212</td>
      <td>PACK OF 72 RETROSPOT CAKE CASES</td>
    </tr>
    <tr>
      <th>224</th>
      <td>21080</td>
      <td>SET/20 RED RETROSPOT PAPER NAPKINS</td>
    </tr>
    <tr>
      <th>226</th>
      <td>21086</td>
      <td>SET/6 RED SPOTTY PAPER CUPS</td>
    </tr>
    <tr>
      <th>547</th>
      <td>22328</td>
      <td>ROUND SNACK BOXES SET OF 4 FRUITS</td>
    </tr>
    <tr>
      <th>671</th>
      <td>22551</td>
      <td>PLASTERS IN TIN SPACEBOY</td>
    </tr>
    <tr>
      <th>779</th>
      <td>21121</td>
      <td>SET/10 RED POLKADOT PARTY CANDLES</td>
    </tr>
    <tr>
      <th>826</th>
      <td>22333</td>
      <td>RETROSPOT PARTY BAG + STICKER SET</td>
    </tr>
    <tr>
      <th>1177</th>
      <td>22635</td>
      <td>CHILDS BREAKFAST SET DOLLY GIRL</td>
    </tr>
    <tr>
      <th>1241</th>
      <td>22555</td>
      <td>PLASTERS IN TIN STRONGMAN</td>
    </tr>
    <tr>
      <th>1249</th>
      <td>22539</td>
      <td>MINI JIGSAW DOLLY GIRL</td>
    </tr>
    <tr>
      <th>4011</th>
      <td>22045</td>
      <td>SPACEBOY GIFT WRAP</td>
    </tr>
    <tr>
      <th>4015</th>
      <td>22746</td>
      <td>POPPY'S PLAYHOUSE LIVINGROOM</td>
    </tr>
    <tr>
      <th>9525</th>
      <td>16161U</td>
      <td>WRAP SUKI AND FRIENDS</td>
    </tr>
    <tr>
      <th>107430</th>
      <td>23126</td>
      <td>DOLLCRAFT GIRL AMELIE KIT</td>
    </tr>
    <tr>
      <th>107431</th>
      <td>23127</td>
      <td>DOLLCRAFT GIRL NICOLE</td>
    </tr>
    <tr>
      <th>108144</th>
      <td>23127</td>
      <td>FELTCRAFT GIRL NICOLE KIT</td>
    </tr>
    <tr>
      <th>108341</th>
      <td>23128</td>
      <td>FELTCRAFT BOY JEAN-PAUL KIT</td>
    </tr>
    <tr>
      <th>108342</th>
      <td>23126</td>
      <td>FELTCRAFT GIRL AMELIE KIT</td>
    </tr>
    <tr>
      <th>109882</th>
      <td>23128</td>
      <td>DOLLCRAFT BOY JEAN-PAUL</td>
    </tr>
    <tr>
      <th>113900</th>
      <td>23126</td>
      <td>DOLLCRAFT GIRL AMELIE</td>
    </tr>
    <tr>
      <th>115520</th>
      <td>23007</td>
      <td>SPACEBOY BABY GIFT SET</td>
    </tr>
    <tr>
      <th>115521</th>
      <td>23008</td>
      <td>DOLLY GIRL BABY GIFT SET</td>
    </tr>
    <tr>
      <th>148425</th>
      <td>23256</td>
      <td>CHILDRENS CUTLERY SPACEBOY</td>
    </tr>
    <tr>
      <th>153310</th>
      <td>23256</td>
      <td>KIDS CUTLERY SPACEBOY</td>
    </tr>
    <tr>
      <th>225914</th>
      <td>23229</td>
      <td>VINTAGE DONKEY TAIL GAME</td>
    </tr>
    <tr>
      <th>226497</th>
      <td>23229</td>
      <td>DONKEY TAIL GAME</td>
    </tr>
  </tbody>
</table>
</div>



### Further work on 
 
Latent Factor Analysis needs offline update, we have to decompose the rating matrix offline, and so new recommendations are based on matrices updated to a point. 


# Reference:
A Gentle Guide to Recommender System https://jessesw.com/Rec-System/

Ben Frederickson Implicit Library https://github.com/benfred/implicit

