# Low-rank approximation of faces

We have recently learned that it is possible to replace the full, explicit
representation of data with a smaller, low-rank approximation, by using the
only most important vectors in the SVD.

We're going to play with this idea with a dataset of faces. [Here is a
directory full of faces from official midshipman
portraits](cropped_faces.tgz) (they've been
automatically extracted, so there may be the occasional weird picture in
there). Faces are particularly interesting to approximate because our minds
are particularly attuned to changes in faces.

The first step is to read in all the pictures (each of which is 127x127), and
flatten each 2D image to a single 1D row (of size $127^2=16129$), and combine
them into a single matrix, where each row corresponds to an image. I'll call
this matrix $A$.

Write a function that takes in a single row vector, reconstitutes it into an
image, and displays that image. Sanity check your matrix that you've assembled
it correctly.

Calculate and plot the singular values of this matrix. What is the rank of
$A$? Looking at the plot, are some singular values very small compared to the
others, therefore possibly representing noise rather than signal?

Now we're going to do a low-rank approximation of $A$ to check your theory.
Calculate the SVD of $A$. Write a function that takes in $U, s,$ and $V$, and a
proposed rank $k$. Crop $U$ to contain only the first $k$ columns (call it
$U'$, it should be $n \times k$), crop $s$ to contain only the first $k$
singular values, and crop $V$ to contain only the first $k$ columns ($m \times
k$). Assemble $\Sigma'$ from $s'$, and remultiply your cropped matrices to get
a low-rank approximation of $A$ ($A'=U'\Sigma'V'^T$). $A'$ should be the same
size as $A$.

Now reassemble rows of $A'$ to be images, and look at the reconstructions. How
good are they? How large of a $k$ is necessary for the reconstructions to look
like faces? To be *recognizable* faces?

Use a variety of different faces in your exploration, covering a diversity of
directions faced, glasses, ethnicities, smilyness, etc., so you're sure that
your answers are correct for many different appearances. Are some variations
more poorly approximated than others? Why might that be?
