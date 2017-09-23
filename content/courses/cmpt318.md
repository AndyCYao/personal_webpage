title: "Computational Data Science"
date: 2017-09-23
semester: "Fall 2017"
code: "CMPT 318"

# Noise Filtering / Signal Processing

## Locally Weighted Scatterpot Smoothing (LOESS Smoothing)
1. Given a set of data 
2. Take a local fraction of the data 
3. Fit a line through this fraction data. Using least square regression techniques (or others)
4. use that line to be part of the curve for the middle of the neighbourhood
5. continue with the next set of fractions by sliding the window along , generating a curve

LOESS is computational heavy, it works best with lots of data.

## What is a covariance matrix
Covariance measures how related item x is to y. Positive covariance means when x moves up, y moves up, Negative Convariance means when x moves up, y moves down. and 0 means they are not related at all

read up on covariance matrix [here](http://www.theanalysisfactor.com/covariance-matrices/)

This matrix just takes this idea, and extends it over multiple items. the matrix is *symmetric* that means when you transpose the table, it is the same values.

## Kalman Filtering 
read [article](http://www.bzarg.com/p/how-a-kalman-filter-works-in-pictures/) for explanation.

The filter works with two things, our observations, and our predictions of what we expect to happen (the prior). Both are assumed to be normal distribution. 