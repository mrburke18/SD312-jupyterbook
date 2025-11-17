# Recommender Systems

You're familiar with recommender systems already.  In no small part, this is
because recommender systems are what drive the free internet - based on your
interests and activities, advertising companies would like to produce ads
for products that are interesting to you, specifically.  The more interested
you likely are, the higher chance you click on the ad, and the advertising
company can get paid.

These systems exist much more transparently in contexts like Amazon and
Netflix, where your product ratings and purchase history allow them to
suggest other products you might want (for example, at the moment, my Amazon
recommendations are full of unicorn stuff, because my 5-year-old niece just
had a birthday, and that's what I shopped for recently).

Recommender systems are a fairly rough field of Machine Learning -
techniques tend to be tightly bound to the particular kinds of data
available in a particular problem (for example, website visits collected by
Google Chrome might be used very differently from purchase history on
Amazon, might be used very differently from 1-5 star movie rankings on
Netflix).  Except for on very large scales, measuring success can also be
pretty difficult, and tends to look like, "eh, sure, these make sense as
recommendations."

Roughly, recommender approaches fit into two main types.  The first is
*content-based filtering*.  In these, each item which might be recommended
is given a description ("is a book", "is targeted at children", "is about
unicorns").  Each user then is given a fingerprint, or a list of which
features he/she has demonstrated an interest in.  The system can then find
other items with the same set of features.  The main challenge is in
building the correct sort of features, so that items with the same features
are actually liked by the same people (for example, there's a lot of
unicorn-based stuff that I really don't want to see).

A great example of content-based filtering is online radio, where you give
it a seed song or artist, and it provides other songs that feature the same
properties as the seed song you fed it.

The other approach is *collaborative filtering*.  In collaborative
filtering, we work off of purchase counts, or ratings, or some other
information from the user, rather than from features of the object itself.
The main point of leverage is that people can be similar, and products can
be similar, and if similar people like similar products, well, you might
like those products, too.

The main benefit of collaborative filtering is that you don't need a
description of the item itself, which can be difficult to keep up with if
you have a large set of often-changing.  The main benefit of content-based
filtering is that you often need much less data to produce a useful
recommendation, because you can start with meaningful, human-designed
features.

Of course, we could also imagine deploying systems that use both
content-based and collaborative approaches.

We're going to focus on two pretty straightforward collaborative filtering
techniques, because they build nicely off our knowledge of clustering and
lower-dimensional subspaces.  Content-based approaches will fit in better
once we learn about some other predictive techniques.

## K-Nearest Neighbor

Suppose we have a bunch of ratings for movies.  Given that somebody just
watched some given movie, and presumably enjoyed it, what can we recommend
for them to watch next that would be similar?  This might be difficult to
answer, given that we only have ratings, and don't know anything about the
movie itself.  However, we can suggest that two similar movies will be liked
the same way by the same people, and so the vectors formed by the columns of
the ratings matrix should be similar.

One problem is that ratings matrices tend to be highly sparse, because most
people have not interacted with (much less taken the time to rate) most
products.  Our next approach will explicitly attempt to fill these blank
spaces in with expected ratings; for now, though, we'll have to decide what
to do with those blank spaces.  Here's the choices: one choice is to only
keep the dimensions that are non-zero in both.  Another is to keep the
dimensions that are non-zero in at least one of the vectors, and leave the
information that this movie wasn't watched by one of the users by leaving it
as a 0, and treating it like any other rating.  This is a little bit
uncomfortable, perhaps, because a 0 seems like it's "even worse" than a
1-star rating, and that may be a bad way to think of it.  However, at least
it allows us to consider whether a movie was watched or not as itself useful
information.  Really, this boils down to your data, and what you discover
works better.

So, if we take the column vector of the movie the viewer just watched, and
compare its distance from all other column vectors, we can recommend the
movies that are closest.

As with clustering, your choice of "distance" is an important consideration.
Here, I list three common ways to measure distance, and the differences
between them.

- **Euclidean distance**: You know this one.  Each of our vectors is a point in $n$-dimensional space, and we can find the length of the line between two of those points.  The trouble is that $n$ is usually quite large (lots
of users!), and even with small differences, Euclidean distance gets really big really fast for large numbers of dimensions.  Maybe doing PCA and projecting into fewer dimensions first makes sense.
- **Cosine distance**: One minus the cosine of the angle between two vectors (so two vectors pointing in the same direction have a cosine distance of 0).  This is interesting because it is invariant to the magnitude of the vectors.  This can be good if you think that *what* people choose to watch is more important than *how much they liked it*.  Naturally, the rating still matters, but just having non-zeros in the same places goes a long way towards making vectors similar in this way.  When using cosine distance, it is common to *normalize* data by subtracting from each ranking the average ranking of that movie, so vectors can point in opposite direction of each other, if two users disagree.
- **Jaccard distance**: If the ONLY thing that matters to you is "watched or not", you can use the Jaccard distance to measure the distance between the sets of people who watched a movie. To calculate the Jaccard distance between two sets A and B, you calculate $1-\frac{|A\cap B|}{|A\cup B|}$.  If you like the idea of Jaccard distance, but you have non-binary data, you might round it, by saying, for example, 1s and 2s are rounded down to 0, and 3,4,5s are rounded up to 1.

## Other tweaks

If you have really sparse data, you might choose to **cluster first**.  By
clustering movies, you might be able to discover different types of movies.
Suppose you discover $k$ clusters.  You can take your $n\times m$ matrix and
replace it with an $n\times k$ matrix, where each entry is that user's
average rating of movies in that cluster.  This is likely much less sparse.
You can then recommend whole genres (like, for example, an online radio
playlists), rather than a single song or movie.

Also, you might first choose to **perform PCA**.  If your data actually lies
in a lower dimension, you might as well do your measures of distance in that
lower dimension, making it cheaper to compute.

So which is best?  It's not really like that.  You can find lots of arguing
online about that.  Try them all!  Which one seems to work better for your
dataset?  Why?

![](https://www.smbc-comics.com/comics/1549556091-20190207.png)
