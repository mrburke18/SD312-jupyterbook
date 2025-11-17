# Linear Regression Assignment

We're going to be predicting how many young people move from the area they grew up to another in the United States.  [Our main dataset can be found here](https://migrationpatterns.org/).  For people born in the US from 1984-1992, it takes note of which [commuting zone](https://en.wikipedia.org/wiki/Commuting_zone) individuals lived in when they were 16, and which they lived in when they were 26.  For example, when I was 16, I lived in the St. Louis, Missouri commuting zone, and when I was 26, I lived in the Raleigh, NC commuting zone.  According to the dataset, I was one of 342 such people to make that move.  We are going to make the most accurate predictor we can which takes in two different commuting zones and predicts the number of people who moved from the first to the second.

Feel free to play with that website. Down at the bottom, next to "Want to know more?" is a link that says "download the data."  Do that, and unzip the file.

Inside there are a number of files, including `Data Dictionary.docx`, which
includes a description of the dataset.  Our "targets" will be pulled from
`od_pooled.csv`.

You'll have to build your own features.  What do you think is most important?
The distance away from each other?  Their economies?  Their populations?
Their political ideologies?  Their economic, ethnic, or cultural makeup? It's
up to you to build the feature set, and then build the best linear regressor
you can.

As an example, let's consider the first line of od_pooled.csv from the dataset:

```
6502,"Cleveland","Tennessee",100,"Johnson City","Tennessee",127,22148,56915,"pooled",.0057342,.0022314
```

For this line, you need to construct a row of $X$ and a value of $y$ in order to set up that datapoint in $Xw=y$ which is solved by linear regression.  The $y$ value is most straightforward: it's 127, or the number of people who have moved from Cleveland, TN to Johnson City, TN.  The row of $X$ is less straightforward.  Suppose you decide the only things you need to make this prediction is the population of the origin location and the population of the destination.  In this case, you'll construct two features, where the first feature is the population of Cleveland, and the second is the population of Johnson City. That's your row of $X$. (Of course, that's unlikely to be a sufficient feature set). (And of course, after a mention of Johnson City, TN, [I now have Old Crow Medicine Show in my head](https://www.youtube.com/watch?v=1gX1EP6mG-E&t=178s).)

Here are some potentially useful resources, though you are highly encouraged to find your own datasets:

- Many datasets are at the county level, which is different from commuting zones.  The file "2000 commuting zones" file [on this page](https://www.ers.usda.gov/data-products/commuting-zones-and-labor-market-areas/) will help you map FIPS codes (a number identifying counties) to 1990 Commuting Zone IDs.
- **[County-level poverty statistics](https://www.census.gov/data/datasets/2020/demo/saipe/2020-state-and-county.html)**. Make sure to read the documentation.  I think the most useful file is in `Additional File Formats`, `Archived Datasets`, `est20all.txt`.
- **[County-level health statistics](https://www.countyhealthrankings.org/explore-health-rankings/rankings-data-documentation)**. Lots of useful stuff on this page.
- **[Population estimates](https://www.census.gov/data/tables/time-series/demo/popest/2010s-counties-detail.html)**. The "United States" option in the bottom dataset seems useful, though there's other demographic and population data elsewhere.
- **[Ideological preferences](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/BQKU4M)** (click "Access Dataset" - you'll need to install the pyreadstat library to read these files)
- **[Economic distribution](https://www.minneapolisfed.org/institute/income-distributions-and-dynamics-in-america/data-center)** State-level economic distribution statistics.
- and **anything else you want**.

### Getting Location

One way I found to do this was with [Nominatim](https://nominatim.org/release-docs/develop/api/Search/), which is an API to OpenStreetMap.  For example, to get the latitude and longitude of Annapolis in Python, I can do this:

```python
import requests,json
r=requests.get('https://nominatim.openstreetmap.org/search?q=Annapolis+Maryland&format=json')
data=json.loads(r.content) #data is now a Python list of info
print(data)

'''
This prints:

[{'place_id': 3809116, 'licence': 'Data © OpenStreetMap contributors, ODbL 1.0. http://osm.org/copyright', 'osm_type': 'relation', 'osm_id': 133571, 'lat': '38.9786401', 'lon': '-76.492786', 'class': 'boundary', 'type': 'administrative', 'place_rank': 16, 'importance': 0.5722443958642912, 'addresstype': 'city', 'name': 'Annapolis', 'display_name': 'Annapolis, Anne Arundel County, Maryland, United States', 'boundingbox': ['38.9424993', '39.0025548', '-76.5395832', '-76.4686762']}]
'''

print(data[0]['lat'],data[0]['lon'])
# prints 38.9786401 -76.492786
```

Python's requests module breaks here on the yard due to ITSD's certificate
foolishness unless you first run [this script](../resources/fix-ssl.sh).

### Tips and Expectations

It's very important that we get the ML process right here. That means doing an
appropriate train/test split, and then working to understand your
hyperparameters in order to minimize testing error. The main hyperparameters
here are the feature set and the regularization parameter. Note that a
different feature set will mean a different optimal regularization parameter.

What you likely want is a function which takes in a training feature set, a
testing feature set, and the target, and which tries many regularization
parameters, returning the model that performs the best on the test set. This
automates much of the process, allowing you to focus on your feature set.

- You are expected to be curious and creative about building features that are useful and valuable. You should work quickly enough you have time to iterate on your feature set, not just live and die with the first set you can construct.
- You are expected to do the machine learning part (training/testing, regularization, etc.) right.
- Build a bad, skeleton system first with very few features, which creates a linear regressor.  Then add more complex features, and you should be able to just re-run this working code.
- Normalize your features.
- Make sure your project tells me what features you made and what worked and what didn't in terms of making your predictor better.  Make sure you're clear about how you set up your regression problem with a good regularization parameter.
- Choose two origin-destination pairs with different characteristics (for example, a red to a blue area, or a sparsely-populated area to a dense area), and look at the specific errors of those two cases.  Are they equally accurate?
- Look at your linear coefficients, and give me some analysis as to what they mean, and how your features relate to young adult migration.
