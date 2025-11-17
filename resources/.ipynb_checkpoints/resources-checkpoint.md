# Mamba/Conda and Jupyter

## Installing Mamba and Python packages

The most common languages for processing data are Python and R.  We're going to be using Python.  Python has a lot of problems.  It's slow and it's undisciplined, making it poorly suited for large software projects.  However, it's fast for the programmer, and we can sidestep the "undisciplined" problem by noting that most data science projects don't require that much programming - it's just a little bit of programming applied to large data sets.

The fact that it's slow is still a problem when processing those large data sets.  The scientific computing community has gotten around this by writing a large number of very impressive libraries for data science that are written in C, but which provide an API for Python.  This lets the programmer direct what will happen in an easy-to-code language, while having all the computationally expensive parts happen in C.

This means that the "right" way to program for data science in Python is by using the libraries as much as possible, and doing as little as possible in pure Python - so we have to know how these libraries work (or at least, know how to look up how these libraries work - Google and Stack Overflow will be key throughout this course!).  The libraries we'll be using include:

- `pandas`: useful for loading and manipulating datasets
- `numpy`: used for linear algebra
- `scipy`: data structures and algorithms for scientific computing
- `matplotlib`: matlab-like plotting
- `sklearn`: machine learning algorithms
- `jupyter`: useful for making reports that include text, images, code, and graphs.
- `plotly`: useful for making plots (and interactive plots!) in a web environment (like a jupyter notebook)

Probably, we'll come up with some others, too.

### Installation
The first step is to install all this business.  Because all the libraries need to be compatible, it's common to use a package manager, which keeps track of all those compatibilities for you and installs the right versions of the right libraries.  The most common are Anaconda or Mamba.  Anaconda is more common, Mamba is a more recent, faster version which is meant to behave exactly like Anaconda.  I recommend Mamba, though either is fine.

You will want to install this on any machine you might want to work on, including and at least

- Your laptop
- ssh.cs.usna.edu 

On your laptop, you'll want to do this in a WSL prompt.

Start by installing mambaforge, by running `wget --no-check-certificate https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-Linux-x86_64.sh` (the `no-check-certificate` is bad practice made necessary by the monitoring software run by ITSD).

Run it by running `bash Mambaforge-Linux-x86_64.sh`.  Follow the prompts, and answer "yes" to all questions.

Close the terminal and reopen it.

Now, install libraries: `mamba install numpy scipy scikit-learn pandas plotly matplotlib jupyter`

## Using Jupyter

Once you have python installed, you can work with Jupyter notebooks either natively, or with VSCode.

To start Jupyter **if you're on a local machine**, run `jupyter lab`.  You'll notice your browser gets all excited and pops up a new window.  A Jupyter notebook allows for text in Markdown format, python code, images, etc.  It's a great format for telling a story that involves code/graphs, etc.  There are a whole bunch of Jupyter tutorials out there that are worth doing.  [I like this one, which also introduces pandas and some matplotlib](https://www.dataquest.io/blog/jupyter-notebook-tutorial/).

**If you're on a remote machine** (like ssh.cs.usna.edu), see the next section

### Working on a remote Jupyter notebook

When you run a Jupyter notebook, it sets up the Python kernel which is actually running your code, and a web server which serves the page you interact with it through.  You can access that server remotely, which lets you run code on that faster machine over there, and interact with it with a machine over here.

1. SSH onto the remote machine as normal, with no special flags.
2. Run `tmux` (or `screen`, whichever you prefer).  These programs allow you to run a command on a remote machine, "detatch" from that session, and they'll keep running even if you lose connection. (NOTE: `tmux` and `screen` can change your life)
3. On the remote machine, run `jupyter notebook --no-browser --ip=0.0.0.0 --port=2XXXX` where the `XXXX` is the last four numbers of your alpha.
4. It will output a URL that looks something like this: `http://ward-rweb-09:(your port)/?token=SOMELONGHASH`. Copy it, and paste it into your local browser. 
5. Detatch from the tmux or screen session (ctrl-b d on tmux, or ctrl-a d on screen). You can now log off the ssh terminal if you like.
6. When you log back in, you can rejoin that session with `tmux attach` or `screen -r`.


## Using VSCode

VSCode is a programming IDE with a lot of nice features, including:
- Jupyter notebook support
- Text editor keybindings
- LLM integration
- Remote code access

Of course, it has its own learning curve.

[VSCode can be installed on your laptop here](https://code.visualstudio.com/). There's a great deal of assistance online for how to do things. Here's a checklist for things you'll want to be able to do:

- Install extensions for (at least) Python, keybindings, and Jupyter
- Use your github account to set up Copilot
- Create notebooks, and export them as HTML files
- Change the python environment being used by your program
- SSH into a remote machine, and open and run code on that machine (note that this is a great answer when you have network access, and a really bad answer for when you don't)