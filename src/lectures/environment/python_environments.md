# Managing Python Environments

_Note: many elements in this guide 2343 adapted from
[Daniel Rothenberg](http://danielrothenberg.com/)'s excellent
[getting started guide](http://danielrothenberg.com/gcpy/getting_started.html)._

## Python

Python and nearly all of the software packages in the scientific python
ecosystem are [open-source](https://opensource.org/).
They are maintained and developed by a community of scientists and programmers,
some of whose work is supported by universities, non-profits, and for-profit
corporations.
This work mostly happens in the open, via [github](http://github.com/) and other
online collaboration platforms.

Because there is no single authority which controls all of these packages, it
can be intimidating for new users to figure out how to set up a functional
scientific python environment.
Coordinating the compatibility between these different packages and their
multiple versions used to be a nightmare!
Fortunately, the problem is solved completely by using a Python _distribution_
and / or a Python _package manager_ (described in detail below).

One important rule about scientific computing in Python is this:

**Do not use your system Python installation!**

The version of Python that ships with operating systems such as Red Hat Linux and
macOS is usually outdated and configured to support system functions. Although it
is entirely possible to install and use the necessary packages using the system
Python, it's much more practical on both
your local machine and any other computers you work with to use a specialized Python
installation.

```{note}
Everything in this course uses Python 3, the latest version of Python.
Python 2 is similar, but has some important differences that can make
Python 2 code incompatible with Python 3.
Python 2 was officially deprecated (declared obsolete) on
[Jan 1, 2020](https://www.python.org/doc/sunset-python-2/)
```

## Recommended Installation Method: Use Anaconda Python

The easiest way to set up a full-stack scientific Python deployment is to use a
Python distribution. This is an installation of Python with a set of curated
packages which are guaranteed to work together.
For this class, we recommend the
**[Anaconda Python Distribution](https://www.anaconda.com/download/)**.
Follow the link above to obtain a one-click installer for Linux, Mac, or
Windows.
(Make sure you select the Python 3 installer, not Python 2.7.)
In addition to the packages themselves, Anaconda includes a graphical
utility to help manage any packages you may want to install which are not
already included in the default inclusion list.

## Accessing the Command Line

These notes assume you have access to a Unix command line to type in shell commands.
For Linux and MacOS users, you can access the command line by opening the _terminal_ program.
It's more difficult for Windows users.
For Windows users, you should first install Anaconda (described above) or Miniconda (described below), which gives you access to the "Anaconda Prompt" desktop app.
(Instructions for this are given on the [Andaconda Website](https://docs.anaconda.com/anaconda/user-guide/getting-started/#write-a-python-program-using-anaconda-prompt-or-terminal).)
From the Anaconda Prompt, you should be able to run `conda` and other shell commands.

## Lightweight Alternative: Miniconda

If you are installing python on a remote machine via ssh, or you simply don't
want to download a huge file like the Anaconda Python Distribution, there is a
lightweight alternative installation method.

1. **Obtain a minimal Python installer**
  We recommend the [Miniconda](https://conda.io/miniconda.html) installer;
  this provides a Python install for your operating system, plus the **conda**
  package manager. This way, you can only install the packages you *want*.

2. **Run the installer**
  You'll probably need to do this from the command line, e.g.

        $ sh Miniconda3-latest-MacOSX-x86_64.sh

  Follow the instructions; you can choose where to place the installation (
  preferably somewhere you have write access without super-user/root access,
  like your home directory). At the end of this process, add this path to your
  \*rc configuration

        $ echo ". $HOME/miniconda3/etc/profile.d/conda.sh" > ~/.bashrc

  If you do this, your ``$PYTHONPATH`` will be implicitly configured correctly
  and you will never have to touch it.

3. **Create an environment and install packages.**
  This is described in the next section.

## Managing Environments with Conda

Python coupled with a package manager provides a way to make isolated,
reproducible *environments* where you have fine-tuned control over all packages
and configuration. **You should always work within an environment**, rather
than the "default" environment.

It is strongly recommended to read official
[Getting Started with Conda](https://conda.io/docs/user-guide/getting-started.html#)
guide.

To create a conda environment, you execute the following command:

    $ conda create --name my_environment python=3.9 numpy

This will create a special environment in ``$MINICONDA_HOME/envs/my_environment``
with only Python and numpy to begin with. Here, we've also told conda to install
Python version 3.9; you can specify exact versions or minima, and conda will
take care of figuring out all the compatibilities between versions for you. To use
this environment, simply "activate" it by executing:

    $ conda activate my_environment

Regardless of your shell, you should now see the string ``(my_environment)``
prepended to your prompt. Now, if you execute any Python-related tool from the
command line, it will first search in ``$MINICONDA_HOME/envs/my_environment/bin``
to find them.

You can deactivate your environment by typing:

    $ conda deactivate

To see all the environments on your system:

    $ conda info --envs

If you want to permanently remove an environment and delete all the data
associated with it:

    $ conda remove --name my_environment --all

For extensive documentation on using environments, please see
[the conda documentation](https://conda.io/docs/using/envs.html). The most
important feature to review here is the ability to *share and export* your
environment; this is the basis for reproducibility in the scientific Python stack.
At any time from the shell, you can execute

    $ conda list

to get a complete summary of all the packages installed in your environment, the
channel they were installed from, and their full version info. Using this info,
you can create an **environment file** in
[YAML syntax](http://docs.ansible.com/ansible/latest/YAMLSyntax.html)
which documents the exact
contents of your environment. With that file, a new environment with the exact
configuration can be installed by executing

    $ conda env create -f my_environment.yml

Below we will see an example of an environment file.

## Installing More Packages

Once you have a basic Python environment, you can easily add or remove packages
using conda.
Conda was created to help manage the complex dependencies and
pre-compiled binary libraries that are necessary in scientific python.

If you set up your python environment using the Anaconda Python Distribution or
with miniconda, you should already have the **conda** command available on
the command line.
With it, you can easily install packages from an official, curated set of packages which are
built and tested for a number of different system configurations on Linux,
Windows, and macOS

    $ conda install <package-name>

Additionally, there is a
community-maintained collection of packages/recipes called
[conda forge](https://conda-forge.github.io/>)
which is accessible through conda as a special "channel"

    $ conda install -c conda-forge <package-name>

While conda allows you to install almost any science-related package, there may
be other general-use python packages you wish to you that are not available in
via conda. For these, you can use an alternative installation method.

Outside of the scientific python community,
the most common way to install packages is to search for them on the official
[PyPI](https://pypi.python.org/pypi) index. Once you've found the package you
want to install (you may have also just found it on github or elsewhere), you
use the **pip** command from a the command line:

    $ pip install <package-name>

This will fetch the source code, build it, and install it to wherever your
``$PYTHONPATH`` is set. This works in the vast majority of cases, particularly
when the code you're installing doesn't have any compiled dependencies.

If you can't find a package on either PyPI or conda-forge, you can always install it
directly from the source code. If the package is on github, ``pip`` already has
an alias to do this for you:

    $ pip install git+https://github.com/<user>/<package-name>.git

## Channels and Conda Forge

Where do conda packages come from?
The packages are hosted on conda ["channels"](https://conda.io/projects/conda/en/latest/user-guide/concepts/channels.html). From the conda docs:

> Conda channels are the locations where packages are stored. They serve as the base for hosting and managing packages. Conda packages are downloaded from remote channels, which are URLs to directories containing conda packages. The conda command searches a set of channels. By default, packages are automatically downloaded and updated from the default channel https://repo.anaconda.com/pkgs/ which may require a paid license, as described in the repository [terms of service](https://www.anaconda.com/terms-of-service) a commercial license. The conda-forge channel is free for all to use. You can modify what remote channels are automatically searched. You might want to do this to maintain a private or internal channel. For details, see how to modify your channel lists.
>
> Conda-forge is a community channel made up of thousands of contributors. Conda-forge itself is analogous to PyPI but with a unified, automated build infrastructure and more peer review of recipes.

Don't be worried by the "commercial license part".
The Anaconda channel terms of service clearly excludes all educational activities
and all research activities at non-profit institutions from their definition of commercial usage.
Even companies with fewer than 200 employees are excluded.
The aim of the commercial paid license for Anaconda is to require large corporations
which use the repository heavily to contribute financially to its maintenance and development.
Without such contributions, Anaconda might not be able to sustain itself.

Despite this, we still recommend **always using the conda-forge channel for your python environments**.
The reason are as follows:
- Conda Forge is always free from commercial license restrictions
- Conda Forge generally has the largest volume of packages and the most up-to-date versions
- You can contribute your own packages to conda forge! This is not covered by this book,
  but you can read about it in the [Conda Forge docs](https://conda-forge.org/docs/maintainer/adding_pkgs.html).

A simple way to use the conda forge channel is to pass the `-c` option when you run conda:

    $ conda install -c conda-forge  {package_name}

As shown below, you can also add conda-forge to your `environment.yml` file.

## Speeding things up with Mamba

In order to put together an actual python environment from your package specifications,
conda has to solve a difficult puzzle.
Each package specified has certain dependencies on other packages.
For example, Xarray depends on Numpy, Pandas, and several others.
Moreoever, each version of Xarray requires certain minimum versions of other
packages (e.g. Xarray 0.19 requires Numpy >= 1.17 and Pandas >= 1.0).
Other packages in your environment may have different or incompatible versions.
Finding a combination of packages that are mutually compatible can be framed
mathematically as a [boolean satisfiability problem](https://en.wikipedia.org/wiki/Boolean_satisfiability_problem).

The default "solver" of this problem for conda can be [slow](https://www.anaconda.com/blog/understanding-and-improving-condas-performance)
It is not unheard of to spend 30 minutes or more solving large environments! 😱
Fortunately, a much faster alternative called [mamba](https://github.com/mamba-org/mamba)
has recently come out.
To install it, just run:

    conda install -n base -c conda-forge mamba

Now you can install environments and packages as before, but using the `mamba` command
instead of `conda`. Everything will be faster.


## Pangeo Python Environment

The environment on our cloud JupyterHub is a highly curated combination of packages
maintained by the [Pangeo Project](http://pangeo.io/).
Then environment lives at <https://github.com/pangeo-data/pangeo-docker-images/>.
In addition to just specifying a combination of packages, this repo automatically
builds [Docker containers](https://docs.docker.com/get-started/).

The latest Pangeo notebook environment lives at <https://github.com/pangeo-data/pangeo-docker-images/blob/master/pangeo-notebook/environment.yml>.
Below are the contents of that file as of 2021-11-04.
Copy and paste the following ``environment.yml`` file somewhere
on your local hard drive:

    name: pangeo
    channels:
     - conda-forge
    dependencies:
     - python=3.9*
     - pangeo-notebook=2021.09.30
     - pip=20
     - adlfs
     - awscli
     - boto3
     - bottleneck
     - cartopy >= 0.20.0
     - cfgrib
     - cmip6_preprocessing
     - ciso
     - dask-ml
     - datashader
     - descartes
     - earthdata
     - eofs
     - erddapy
     - esmpy
     - fastjmd95
     - fsspec
     - fsspec-reference-maker
     - gcsfs
     - gh
     - geocube
     - geopandas
     - geopy
     - geoviews-core
     - gsw
     - h5netcdf
     - h5py
     - holoviews
     - hvplot
     - intake
     - intake-esm
     - intake-geopandas
     - intake-stac
     - intake-xarray
     - ipyleaflet
     - ipytree
     - ipywidgets
     - jupyter-panel-proxy
     - jupyter-resource-usage
     - lz4
     - matplotlib-base
     - metpy
     - nb_conda_kernels
     - nbstripout
     - nc-time-axis
     - netcdf4
     - nomkl
     - numcodecs
     - numpy
     - pandas
     - panel
     - parcels
     - param!=1.11.0
     - prefect
     - pyarrow
     - pycamhd
     - pydap
     - pygeos
     - pystac
     - python-blosc
     - python-gist
     - python-graphviz
     - rasterio
     - rechunker
     - rio-cogeo
     - rioxarray
     - rise
     - s3fs>0.5
     - sat-search
     - sat-stac
     - satpy
     - scikit-image
     - scikit-learn
     - scipy
     - sparse
     - stackstac
     - tiledb-py
     - timezonefinder
     - xarray
     - xarrayutils
     - xarray_leaflet
     - xarray-spatial
     - xcape
     - xcube
     - xesmf
     - xgcm
     - xhistogram
     - xmitgcm
     - xpublish
     - xrft
     - xskillscore
     - zarr


Create this environment using mamba

    $ mamba env create -f environment.yml

Activate this environment

    $ conda activate pangeo

This environment should be sufficient for all of your work in this class.
