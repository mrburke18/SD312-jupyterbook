#So You Want to Use a Supercomputer

A Supercomputer isn't super because each core is faster.  A supercomputer is
super because there are more cores, which talk to each other really quickly.
So how can we take advantage of this (because so far, we're not)?

If this were an HPC class, we'd talk about how to parallelize your C or
Fortran code using MPI, OpenMP, or CUDA.  These are the canonical big three
for parallelizing your code - MPI (Message Passing Interface) is great for
communicating between processes, OpenMP is great for communicating between
threads, and CUDA is great for using the many small cores in a GPU.

[Due to the memory management model in
Python](https://wiki.python.org/moin/GlobalInterpreterLock), OpenMP and CUDA
are DOA - threads and Python just don't work very well.  So, let's look at
MPI, with a focus on the easy application of these concepts, without getting
too deep into MPI (because this just isn't that course).

Remember, each process has its own dedicated memory - they can't share arrays
or objects or anything else.  So, if you want them to communicated, that data
needs to be transmitted, either from one process's memory block to another's
(if both processes are running on the same physical machine), or over a
network (if they're on different physical machines).  MPI is a standard for
this kind of communication between programs written in C, C++, or Fortran.
There's also a very loose wrapper for Python called mpi4py.

###Just running multiple processes

Let's build this up.  First, here's a block of code:

```python
#!/usr/bin/env python3

from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
print(str(rank)+" "+str(size))
```

And here's what it looks like when run on Grace, in interactive mode:

```
(mypy3) taylor@grace00:/mnt/lustre/scratch/taylor> aprun -n 5 python3 mpiEx.py 
4 5
2 5
3 5
1 5
0 5
Application 142889 resources: utime ~0s, stime ~1s, Rss ~9496, inblocks ~11665, outblocks ~19014
```

The `-n 5` in there is telling Grace to run five processes of the exact same
command: `python3 mpiEx.py`.  Supercomputers and MPI are closely bound enough
that aprun is specifically set up to run MPI programs - what's happening it's
building a set of five processes, all of which can talk to each other, and all
of which are running exactly the same code.  After building the COMM_WORLD,
each process can see the size (the number of processes running), and its own
individual rank (each process has an integer assigned to it from 0-(size-1) ).
You can see from the output that all five processes ran the print command, but
the output differs only in that each has its own rank.  Of course, since these
are running in parallel, there's no guarantee in what order they'll get to
that print statement, and running it again would get the same output, but in a
different order.

Already, you can now do a lot of things you couldn't do before.  Given a
24-core node, you could only run one process before - now you can run lots.
And each can do a little different work.  For example, suppose you wanted to
run the same SGD code, but with a different learning rate.  The beginning of
your code might look like this:

```python
#!/usr/bin/env python3

from mpi4py import MPI
import sys

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

lr = sys.argv[rank+1]
print("My learning rate is "+lr)
```

And you might run it like this:

```
(mypy3) taylor@grace00:/mnt/lustre/scratch/taylor> aprun -n 5 python3 mpiEx.py .001 .01 .1 1 10
My learning rate is .1
My learning rate is 1
My learning rate is 10
My learning rate is .01
My learning rate is .001
Application 142893 resources: utime ~0s, stime ~1s, Rss ~9496, inblocks ~11670, outblocks ~19014
```

You would probably want output saved to a file, rather than printed, since
they're going to print all over each other.

The real power, of course, is the ability to do this with many, many
processes.  Suppose, for example, I have 70 processes to run.  Easy.  Reserve
3 nodes of 24 cores each, and run `aprun -n 70 python3 myProgram.py`, and
aprun will distribute them across all the cores you've reserved.

###Communication

Naturally, these processes can also use MPI to talk to each other.

```python
from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank!=0:
  data=np.random.random((3,))
  comm.Send(data,dest=0,tag=0)
else:
  for otherRank in range(1,size):
    r=np.zeros((3,))
    comm.Recv(r,source=otherRank,tag=0)
    print(r)
```

Here, everybody who isn't rank 0 is building a random 3-element numpy array,
and sending it to rank 0, with tag 0.  In turn, the rank 0 process receives
each of these messages, and prints them out.  Note it first had to build a
numpy array of the proper size.  This makes more sense when you think about
the underlying C.  Recv doesn't allocate memory, it just fills memory that's
already been allocated.  So here, we have to give it a pointer to the memory
address where there's sufficient room to put the message's contents.  Behind
the scenes, of course, np.zeros is allocating space in the heap, filling it
with zeros, and returning a pointer to it, so this makes some sense.

###Collective Communication

There are lots and lots of ways to efficiently communicate information between
many processes.  Here's some example code, and the results from running it.
Can you figure out what they do? (note, printing isn't atomic, and so printed
lines may appear out of order)

```python
from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

theArray=np.zeros((3,))
if rank==0:
  theArray[0]=10
  theArray[1]=11
  theArray[2]=12
theArray=comm.bcast(theArray,root=0)
print("Rank %d has array %s" % (rank,str(theArray)))

theArray=np.random.random((3,))
theArray=comm.gather(theArray,root=0)
print("Rank %d has array %s" % (rank,str(theArray)))

#Do a whole lot of work, get some accuracy
accuracy=np.random.random((1,))
print("Rank %d has accuracy %s" % (rank,str(accuracy)))
if rank==0:
  minAcc=np.zeros((1,))
  comm.Reduce(accuracy,minAcc,op=MPI.MAX,root=0)
  print("maximum accuracy is %s" % (str(minAcc)))
else:
  comm.Reduce(accuracy,None,op=MPI.MAX,root=0)
```

```
(mypy3) taylor@grace00:/mnt/lustre/scratch/taylor> aprun -n 3 python3 mpiEx.py 
Rank 2 has array [10. 11. 12.]
Rank 1 has array [10. 11. 12.]
Rank 0 has array [10. 11. 12.]
Rank 1 has array None
Rank 2 has array None
Rank 1 has accuracy [0.85215258]
Rank 2 has accuracy [0.60703246]
Rank 0 has array [array([0.55387189, 0.66794639, 0.87675483]), array([0.03789896, 0.98568601, 0.03072916]), array([0.64378999, 0.48931072, 0.07280644])]
Rank 0 has accuracy [0.19628018]
maximum accuracy is [0.85215258]
Application 143035 resources: utime ~1s, stime ~1s, Rss ~23624, inblocks ~27872, outblocks ~19014
```
