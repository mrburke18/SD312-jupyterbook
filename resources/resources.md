# Mamba/Conda and Jupyter

## Installing Mamba and Python packages

In this course, we will be using `mamba` to manage our Python packages.

You will want to install this on any machine you might want to work on,
including and at least `ssh.cs.usna.edu`.

I don't trust anything you've done before. We'll start by **destroying your
current installation**. SSH into `ssh.cs.usna.edu`, and run:

```bash
rm -rf ~/anaconda3 \
       ~/miniconda3 \
       ~/opt/anaconda3 \
       ~/mambaforge \
       ~/miniforge3 \
       ~/.conda \
       ~/.mamba \
       ~/.continuum \
       ~/.jupyter \
       ~/.ipython \
       ~/.cache/pip \
       ~/.cache/conda \
       ~/.cache/mamba \
       ~/.pyenv \
       ~/.poetry \
       ~/.local/share/jupyter
```

Then edit your `~/.bashrc`. Locate the blocks bounded by `# >>> conda
initialize >>>` and `# <<< conda initialize <<<`. Delete those blocks.

Now you'll **reinstall** mamba.

```bash
curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-x86_64.sh"
bash Miniforge3-Linux-x86_64.sh
```

Accept everything.

Restart your terminal. Install useful packages: `mamba install numpy scipy
pandas scikit-learn plotly matplotlib jupyter`

## Using Jupyter

Once you have python installed, you can work with Jupyter notebooks either
natively, or with VSCode. You are welcome to use VSCode. The rest of the
instructions are for if you prefer to work natively.

To start Jupyter **if you're on a local machine**, run `jupyter lab`.  You'll notice your browser gets all excited and pops up a new window.  

**If you're on a remote machine** (like ssh.cs.usna.edu), see the next section

### Working on a remote Jupyter notebook

When you run a Jupyter notebook, it sets up the Python kernel which is actually running your code, and a web server which serves the page you interact with it through.  You can access that server remotely, which lets you run code on that faster machine over there, and interact with it with a machine over here.

1. SSH onto the remote machine as normal, with no special flags.
2. Run `tmux` (or `screen`, whichever you prefer).  These programs allow you to run a command on a remote machine, "detatch" from that session, and they'll keep running even if you lose connection. (NOTE: `tmux` and `screen` can change your life)
3. On the remote machine, run `jupyter notebook --no-browser --ip=0.0.0.0 --port=2XXXX` where the `XXXX` is the last four numbers of your alpha.
4. It will output a URL that looks something like this: `http://ward-rweb-09:(your port)/?token=SOMELONGHASH`. Copy it, and paste it into your local browser. 
5. Detatch from the tmux or screen session (ctrl-b d on tmux, or ctrl-a d on screen). You can now log off the ssh terminal if you like.
6. When you log back in, you can rejoin that session with `tmux attach` or `screen -r`.

