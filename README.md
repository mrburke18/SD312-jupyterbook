# How to use and build this jupyter book for SD312-Machine Learning

**The setup of infoMaker.py**

The `infoMaker.py` script located in the `landing_scripts` directory generates the `courseInfo.json` file. This JSON file dictates the semester schedule used to generate the calendar.

To set up the calendar for a new semester, open `landing_scripts/infoMaker.py` and modify the values in the dictionary. You must update the `year`, `start` and `end` dates, `lectures` days, `holidays`, and any special schedule adjustments in the `weird` or `other` fields. Once the variables are accurate, execute the script to generate the updated `courseInfo.json` file:

```bash
python landing_scripts/infoMaker.py

```

**The creation of the book_312 virtual environment**

The required dependencies for building the Jupyter Book are specified in the provided `environment.yml` file. To create the isolated environment named `book_312`, navigate to the directory containing the file and execute the following command:

```bash
mamba env create -f environment.yml

```

**The setup of myst.yml**

The `myst.yml` file configures the metadata and structure of the Jupyter Book.

Open the file and update the `project` metadata, specifically the `title`, `copyright` year, and `github` repository URL. You must also maintain the `toc` (table of contents) section. Every Markdown (`.md`) and Jupyter Notebook (`.ipynb`) file that you intend to publish must be listed in this section in your desired hierarchical order. Files omitted from the `toc` will not be compiled into the final webpage.

**How to use the Makefile to make the webpage**

The `Makefile` automates the generation of the markdown calendar, the compilation of the Jupyter Book HTML files, and the remote deployment of the site. It is configured to execute the build step securely within the `book_312` virtual environment.

To fetch the latest schedule data, build the site, and deploy it, run the default target:

```bash
make all

```

This command runs `getCal.py` to download the schedule from a Google Sheet, runs `makeCal.py` to write `index.md`, builds the HTML via `jupyter-book`, and synchronizes the output directory to `ssh.cs.usna.edu` via `rsync`.

If you wish to compile and deploy the book using only the locally cached schedule data without querying the Google Sheet, use the following target:

```bash
make nogoogle

```

You must ensure you have the appropriate SSH keys and permissions configured on your system to allow `rsync` to write to the specified remote directory.
