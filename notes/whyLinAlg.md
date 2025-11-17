# Why is Matrix Multiplication like this?

It seems super arbitrary, right?  Let's motivate it a little bit.

## Physics

Suppose we have a car rolling down a hill, as seen in the following
highly-professional picture of my whiteboard.

![](physicsSized.jpg)

This car is experiencing four forces, gravity (G), friction up the hill (F),
the normal force (N), some wind, which is blowing from the car's left rear
to right front (W), and some friction against the sideways portion of the
wind, which is coming directly out at the viewer (SF).  I've put some axes on
there - the Z axis is coming out of the board at you.  The directions of these
forces are, gravity (0,-1,0), friction (.87,.5,0), normal (-.5,.87,0), 
wind (-.37,0,-.93), and sideways friction (0,0,1).

Notice each of these vectors is of *unit length*, meaning they have a length
of 1.  This is commonly done when you want to indicate direction, without
indicating any magnitude.

So, given different magnitudes of G, F, N, and W, what's the total force on the
car?  Of course, we need to multiply each of our vectors by the force for that
vector, and add them all together.  Now, you should recognize this as a *linear
combination* of the vectors.  You've done this by hand many times.  How can we
do it using linear algebra, which specializes in linear combinations?

To start, we put our directional vectors into a matrix and then put our
magnitudes into a column vector, and multiply.  The first column is always
multiplied by $G$, the second by $F$, etc., giving us the linear combination
we're looking for.

$$
\left[
\begin{array}{ccccc}
0&.87&-.5&-.37&0\\
-1&.5&.87&0&0\\
0&0&0&-.93&1
\end{array}
\right]
\left[
\begin{array}{c}
G\\
F\\
N\\
W\\
SF
\end{array}
\right]
$$

The first matrix is 3x4, and the second is 4x1.  The result is a 3x1 vector
which is a vector representing the total force on the car.

## Restauranteur...ing?

Suppose you ran a chain of restaurants.  You sell hamburgers for 13 dollars, 
chicken for 10, and steak for 18.  Restaurant A sold 5 hamburgers, 8
chickens, and 3 steaks.  Restaurant B sold 10 hamburgers, 2 chickens, and 8
steaks.  How much money did each bring in?

For each restaurant, you'd make what we call *linear equations*, which look
like $T_r = 13H_r+10C_r+18S_r$, where $T_r$ is the total amount brought in by
restaurant $r$, $H_r$ is the number of hamburgers sold by restaurant $r$, etc.
This is a *linear* equation because no variables are being raised to a power.
Again, you should recognize this as being a linear combination of the number of
Hamburgers sold, chickens, and steaks.

Now, you want to calculate this for all your restaurants.  Unlike in our
physics example, we don't already have explicit vectors that need multiplying.
But, we can stack the number of hamburgers on top of each other to make a
single column vector, since they'll be multiplied by the same thing.  Now that
you know matrix multiplication, you can take your sales records (5 hamburgers,
8 chickens, 3 steaks), and put them into a single matrix, where the rows
correspond to restaurants, and the columns correspond to products sold.

$$
\left[
\begin{array}{ccc}
5&8&18\\
10&2&8
\end{array}
\right]
\left[
\begin{array}{c}
13\\
10\\
18
\end{array}
\right]
=
\left[
\begin{array}{c}
199\\
294
\end{array}
\right]
$$

Restaurant A made 199 dollars, and B made 294.  And, it'd be pretty easy to
scale all this up to an arbitrarily large number of restaurants by just adding
rows to the first matrix.  You could also add more products, and just add some
columns to the first matrix, and rows to the second.

Now, we might be interested in costs, as well.  Let's say a hamburger costs us
5 dollars, chickens cost us 3 dollars, and steak costs 12 dollars.  Can we
calculate costs for each restaurant just as easily?  All we have to do is add
a second column to that second matrix representing the costs of each of these
items.

$$
\left[
\begin{array}{ccc}
5&8&3\\
10&2&8
\end{array}
\right]
\left[
\begin{array}{cc}
13&5\\
10&3\\
18&12
\end{array}
\right]
=
\left[
\begin{array}{cc}
199&85\\
294&152
\end{array}
\right]
$$

The first column of our resulting matrix is the money brought in, and the
second column is the money spent.

Now, we of course want to calculate profit.  Of course, profit is (money
in-money out), or, first column of our result matrix minus the second.

$$
\left[
\begin{array}{ccc}
5&8&3\\
10&2&8
\end{array}
\right]
\left[
\begin{array}{cc}
13&5\\
10&3\\
18&12
\end{array}
\right]
\left[
\begin{array}{c}
1\\
-1
\end{array}
\right]
=
\left[
\begin{array}{cc}
199&85\\
294&152
\end{array}
\right]
\left[
\begin{array}{c}
1\\
-1
\end{array}
\right]
=
\left[
\begin{array}{c}
114\\
142
\end{array}
\right]
$$

Restaurant A made 114 dollars, and B made 142!  Of course, if we want a total,
we could just left-multiply again:

$$
\left[
\begin{array}{cc}
1&1
\end{array}
\right]
\left[
\begin{array}{c}
114\\
142
\end{array}
\right]
=256
$$


## Graph search

Suppose we have an adjacency matrix $A$ for a directed graph.

![](graph.jpg)

$$
A=\left[
\begin{array}{ccccccc}
0&1&0&1&0&1&0\\
0&0&1&0&0&1&1\\
0&0&0&1&0&0&0\\
1&0&0&0&1&0&0\\
1&0&0&0&0&0&0\\
0&1&0&0&0&0&0\\
0&0&1&0&0&0&0
\end{array}
\right]
$$

$A$, if course, tells us if it is possible to go from any vertex to any other
vertex in one hop.  But where can we get in two hops from (for example),
vertex D?  Well, if A[3,x] is 1, and A[x,y] is 1, then we can get from D to
vertex y in two hops.  Otherwise, we can't.  So, we can just multiply A by
itself:

$$
A^2=\left[
\begin{array}{ccccccc}
0&1&0&1&0&1&0\\
0&0&1&0&0&1&1\\
0&0&0&1&0&0&0\\
1&0&0&0&1&0&0\\
1&0&0&0&0&0&0\\
0&1&0&0&0&0&0\\
0&0&1&0&0&0&0
\end{array}
\right]
\left[
\begin{array}{ccccccc}
0&1&0&1&0&1&0\\
0&0&1&0&0&1&1\\
0&0&0&1&0&0&0\\
1&0&0&0&1&0&0\\
1&0&0&0&0&0&0\\
0&1&0&0&0&0&0\\
0&0&1&0&0&0&0
\end{array}
\right]
=
\left[
\begin{array}{ccccccc}
1& 1& 1& 0& 1& 1& 1\\
0& 1& 1& 1& 0& 0& 0\\
1& 0& 0& 0& 1& 0& 0\\
1& 1& 0& 1& 0& 1& 0\\
0& 1& 0& 1& 0& 1& 0\\
0& 0& 1& 0& 0& 1& 1\\
0& 0& 0& 1& 0& 0& 0
\end{array}
\right]
$$

To find out where you can get in $k$ hops, you can just compute $A^k$.

## Drawing lines

Suppose you want to write a program in Python to draw some arbitrary cubic
function $y=Ax^3+Bx^2+Cx+D$.  To use matplotlib to do this, you need an array
of $x$ values, and a list of corresponding $y$ values.  To make the line
smooth, you need a lot of them!  How can you do this computation?  The
following program does it.  Can you make sense of what is going on?

```python
#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

print("Displaying a cubic y=Ax^3+Bx^2+Cx+D")

coeffs=np.zeros((4,1))
coeffs[0]=float(input("A?"))
coeffs[1]=float(input("B?"))
coeffs[2]=float(input("C?"))
coeffs[3]=float(input("D?"))

xs=np.linspace(-10,10,100)#get 100 points, evenly spaced between -10 and 10

vals=np.ones((100,4))
vals[:,0]=xs*xs*xs  #x^3 for all values of x (remember, * is piecewise
                    #multiplication)
vals[:,1]=xs*xs #x^2
vals[:,2]=xs
#leave the 3th column as all ones

ys=vals@coeffs

plt.plot(xs,ys)
plt.show()
```

So, why is matrix multiplication organized this way?  Because, frequently,
it's *exactly what we need*!
