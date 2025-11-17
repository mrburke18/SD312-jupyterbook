#Using Neural Nets to Predict Covid-19 Cases in US Counties

**High-level view** - given health, demographic, historical Covid-19 infection data, and state official responses, you are going to build a neural network which predicts the number of Covid-19 cases and deaths two weeks from now for American counties.

For this, you will need several datasets.

- [NY Times county-level Covid-19 infection and death counts](https://github.com/nytimes/covid-19-data).  This dataset is updated daily, meaning your predictor can be, too.
- [US Census County Population Densities](somefile) from the 2010 Census.
- [State Stay-At-Home Orders](https://www.nytimes.com/interactive/2020/us/coronavirus-stay-at-home-order.html) as compiled by the NY Times.
- [County-level Health Data](https://www.countyhealthrankings.org/sites/default/files/media/document/2020%20County%20Health%20Rankings%20Data%20-%20v1.xlsx) (see the "Ranked Measure Data" tab) from [County Health Rankings & Roadmaps](https://www.countyhealthrankings.org/about-us).

As said, our goal will be to predict the number of Covid-19 cases and deaths two weeks from a given day.  So, your first set is to compile the above into a single, usable dataset.

##Step 1: Write a program that builds a dataset

Of the above four datasets, the last three don't change.  The first one, though, changes daily, and we'll want to be able to re-build our dataset and re-train our model to reflect all the most recent information.  So, your result for step 1 will be a program that builds a dataset, not just the dataset.

One datapoint in your dataset should consist of the following pieces of information about a county:

From the second dataset:

- The density of that county.
- The population of that county.

From the third dataset:

- The number of days from day D to D+14 that were under some stay-at-home order (you may have to make some generalizations, as the data is quite fine-grained and poorly formed).

From the fourth dataset:

- The bold columns (ex, Years of potential life lost rate, %Fair or Poor Health, Average Number of Physically Unhealthy Days, etc.)

And, from the first dataset:

- For a county, the *log* of the number of cases and deaths from some day D, the percent increase in cases and deaths from D-2, the percent increase from D-4, and day D+14 (this is 8 numbers for each day D).  If Day D is March 15, you are also likely able to make *another* datapoint with all the same data from the second-fourth datasets, but where Day D is March 16.  This makes your dataset pretty large.

Merging all these is actually not so hard, thanks to the FIPS codes, which are 5-digit numbers which uniquely identify counties and other census designated places.  For example, after some small manipulation of the formatting of the files, I've merged the health and density datasets like this:

```python
health=pd.read_csv('fixedHealth.csv')
density=pd.read_csv('DEC_10_SF1_GCTPH1.US05PR_with_ann.csv')
both=pd.merge(left=health,right=density,
       left_on='FIPS',right_on='Target Geo Id2') #merge on FIPS
both.drop(['Id', 'Id2', 'Geography',
       'Target Geo Id', 'Target Geo Id2', 'Geographic area',
       'Geographic area.1'],axis=1,inplace=True) #drop repeat info
```

...and you're done.

**Why the log of these counts?**  Because the numbers change exponentially, changes in the log of the counts are more easily predictable than the counts themselves.

##Step 2: Build and train a neural net

Build a feedforward network with depth/width/nonlinearities of your choice which takes in a datapoint (except for the D+14 counts) and outputs two things: the *log* of the D+14 of the number of cases, and the *log* of the D+14 of the number of deaths.  Minimize mean squared error.

Now we have a predictor which can be retrained every day with new data to predict the number of cases and deaths in two weeks.  Is it good?  You tell me, on a test set, does it perform well?  Should we trust it?
