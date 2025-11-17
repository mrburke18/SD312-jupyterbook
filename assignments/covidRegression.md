# Predicting COVID-19 Cases and Deaths

The modeling and predicting of the spread of COVID-19 is a really hard
problem, which we have made harder by collecting only extremely noisy data.
What we're doing in this project is too rough-cut to be medically useful;
doing this without an epidemiologist in the room is a good and useful
exercise, but is not a professional solution.  Though they've stopped updating
the models, you can learn more about real COVID models for your own curiosity on [this page and its links](https://projects.fivethirtyeight.com/covid-forecasts/).

In this project, we'll be building a regularized linear regression model which
predicts the number of new cases and deaths that we should expect in a US
county two weeks from today.  A row of your dataset must contain a date, a
FIPS code, the number of smoothed cases that day (Day D), and the number of
smoothed cases two weeks from that day (Day D+14).  That last column is your
*target*, or what you're trying to predict.  You will decide what additional
features will be most useful for you in making your predictions more accurate
- I have some places for you to start here, though you are enthusiastically
encouraged to find your own data sources.

**[The New York Times County COVID
  counts](https://github.com/nytimes/covid-19-data)**.  Go ahead and clone this,
so you can update with new counts each if you want with a `git pull`.  At
minimum, you will need `covid-19-data/rolling-averages/us-counties-2021.csv`.  Within that is a column `cases_avg` - this is the
relevant statistic we'll be predicting.  There are some other potentially
interesting things in this repo like a survey on mask usage by county, and
reported statistics from colleges and prisons.  Definitely read all the
documentation and READMEs.  This data is quite noisy, in part because each
state is doing its own thing, and in part because of some communities' lack of
available health care or a reluctance to seek health care.  We don't need it
for this project, but for your own curiosity, the "excess deaths" file is
likely more meaningful in understanding the direct and indirect death toll of
the pandemic.

We're using `cases_avg`, not `cases`, because there are [oscillations in case
reportage](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7363007/) which mean
that some days of the week have higher reported cases than others, for reasons
that are independent of the actual pandemic.  `cases_avg` is a rolling average
of 7 days to smooth out some of these oscillations.

**[CDC County-level Historic Vaccination
Data](https://data.cdc.gov/Vaccinations/COVID-19-Vaccinations-in-the-United-States-County/8xkx-amqh)**.
If you want to include this, read about the data, then click `Export` in the
upper right, then `CSV`.

**[Adjacent
Counties](https://www.census.gov/geographies/reference-files/2010/geo/county-adjacency.html)**.
Of course, COVID behavior in adjacent counties is likely relevant.  This file
of which counties are adjacent to which, may be helpful in your data design.

**[County-level poverty
statistics](https://www.census.gov/data/datasets/2020/demo/saipe/2020-state-and-county.html)**.
Make sure to read the documentation.  I think the most useful file is in
`Additional File Formats`, `Archived Datasets`, `est20all.txt`.

**[County-level health
statistics](https://www.countyhealthrankings.org/explore-health-rankings/rankings-data-documentation)**.
Lots of useful stuff on this page.  I'll let you decide what, if anything, you
need.

**[Population
estimates](https://www.census.gov/data/tables/time-series/demo/popest/2010s-counties-detail.html)**.
The "United States" option in the bottom dataset seems useful, though there's
other demographic and population data elsewhere.

**[Google's Mobility Data](https://www.google.com/covid19/mobility/)**.
Google tracks people's movements. Here, they've keep track by day how the visits to Parks, Retail stores, Transit stations, Workplaces, etc. is changed from a pre-COVID baseline.

### Some steps to go through:

- Merging your data.  You want each row of your matrix to contain all the necessary information to predict on that datapoint.  This will mean duplicating demographic data (for example) for every datapoint from a given county.  Each county has a [FIPS Code](https://transition.fcc.gov/oet/info/maps/census/fips/fips.txt) which should help you merge much easier.
- Feature design.  For example, perhaps you think it would be helpful to know
  if on Day D cases had been increasing or decreasing compared to previous days.  Perhaps you want to augment with some nonlinear features.  Maybe some features strike you as distracting, and you want to remove them.  You don't get to use future information (if D-Day is May 14, you don't get to use the number of cases on May 21 as a feature).
- Feature normalization.
- Splitting the dataset into training and testing sets.
- Selecting a regularization parameter.
- Performing linear regression on your chosen features to predict smoothed
  D+14 cases ([of course, sklearn will be
helpful](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html)).
- Choose two counties with different characteristics (rural vs urban, red vs blue, whatever) and look at the specific errors of those counties. Are they equally accurate?  What do you think is going on?
- Explain all that.  Look at your linear coefficients, and give me some analysis as to what they mean.
