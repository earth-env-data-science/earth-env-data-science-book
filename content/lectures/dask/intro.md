# Dask for Parallel Computing in Python

In past lectures, we learned how to use numpy, pandas, and xarray to analyze various types of geoscience data.
In this lecture, we address an incresingly common problem: what happens if the data we wish to analyze is "big data"

##  What is "Big Data"?

There is a lot of hype around the buzzword "big data" today.
Some people may associate "big data" with specific sortware platforms (e.g. "Hadoop", "spark"), while, for others, "big data" means specific machine learning techniques.
But I think [wikipedia's definition](https://en.wikipedia.org/wiki/Big_data) is the most useful

> Big data is data sets that are so voluminous and complex that traditional data processing application software are inadequate to deal with them.

By this definition, a great many datasets we regularly confront in Earth science are big data.

A good threshold for when data becomes difficult to deal with is when the volume of data exceeds your computer's RAM. Most modern laptops have between 2 and 16 GB of RAM. High-end workstations and servers can have 1 TB (1000 GB) or RAM or more. If the dataset you are trying to analyze can't fit in you computer's memory, some special care is required to carry out the analysis. Data that can't fit in RAM but can fit on your hard drive is sometimes called "medium data."

The next threshold of difficulty is when the data can't fit on your hard drive. Most modern laptops have between 100 GB and 4 TB of storage space on the hard drive. If you can't fit your dataset on your internal hard drive, you can buy an external hard drive. However, at that point you are better off using a high-end server, HPC system, or cloud-based storage for your dataset. Once you have many TB of data to analyze, you are definitely in the realm of "big data"

## What is Dask?

Dask is a tool that helps us easily extend our familiar python data analysis tools to medium and big data, i.e. dataset that can't fit in our computer's RAM. In many cases, dask also allows us to speed up our analysis by using mutiple CPU cores. Dask can help us work more efficiently on our laptop, and it can also help us scale up our analysis on HPC and cloud platforms. Most importantly, dask is almost invisible to the user, meaning that you can focus on your science, rather than the details of parallel computing.

Dask was created by the brilliant [Matt Rocklin](http://matthewrocklin.com/). You can learn more about it on

* [The Dask Documentation](http://dask.readthedocs.io/en/latest/)
* [The Dask Github Site](https://github.com/dask/dask)

Dask provides _collections for big data_ and _a scheduler for parallel computing_. It is probably easiest to illustrate what these mean through examples, so we will jump right in.