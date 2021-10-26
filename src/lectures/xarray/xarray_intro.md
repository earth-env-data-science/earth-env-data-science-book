# Xarray for multidimensional gridded data

In the previous set of lectures, we saw how Pandas provided a way to keep track of additional "metadata" surrounding tabular datasets, including "indexes" for each row and labels for each column. These features, together with Pandas' many useful routines for all kinds of data munging and analysis, have made Pandas one of the most popular python packages in the world.

However, not all Earth science datasets easily fit into the "tabular" model (i.e. rows and columns) imposed by Pandas. In particular, we often deal with _multidimensional data_. By _multidimensional data_ (also often called _N-dimensional_), I mean data with many independent dimensions or axes. For example, we might represent Earth's surface temperature $T$ as a three dimensional variable

$$ T(x, y, t) $$

where $x$ is longitude, $y$ is latitude, and $t$ is time.

The point of xarray is to provide pandas-level convenience for working with this type of data.

![xarray data model](http://xarray.pydata.org/en/stable/_images/dataset-diagram.png)

## Learning Goals for Xarray

Because of the importance of xarray for data analysis in geoscience, we are going to spend a long time on it.
The goals of this section include the following.

### Lesson 1: Xarray Fundamentals

#### Dataset Creation

1. Describe the core xarray data structures, the `DataArray` and the `Dataset`, and the components that make them up, including: Data Variables, Dimensions, Coordinates, Indexes, and Attributes
1. Create xarray `DataArrays` and `DataSets` out of raw numpy arrays
1. Create xarray objects with and without indexes
1. Load xarray datasets from netCDF files and openDAP servers
1. View and set attributes

#### Basic Indexing and Interpolation

1. Select data by position using `.isel` with values or slices
1. Select data by label using `.sel` with values or slices
1. Select timeseries data by date/time with values or slices
1. Use nearest-neighbor lookups with `.sel`
1. Mask data with `.where`
1. Interpolate data in one and several dimensions

#### Basic Computation

1. Do basic arithmetic with DataArrays and Datasets
1. Use numpy universal function on DataArrays and Datasets, or use corresponding built-in xarray methods
1. Combine multiple xarray objects in arithmetic operations and understand how they are broadcasted / aligned
1. Perform aggregation (reduction) along one or multiple dimensions of a DataArray or Dataset

#### Basic Plotting

1. Use built-in xarray plotting for 1D and 2D DataArrays
1. Customize plots with options

### Lesson 2: Advanced Usage


#### Xarray's groupby, resample, and rolling

1. Split xarray objects into groups using `groupby`
1. Apply reduction operations to groups (e.g. mean)
1. Apply non-reducing functions to groups (e.g. standardize)
1. Use `groupby` with time coordinates (e.g. to create climatologies)
1. Use artimetic between `GroupBy` objects and regular DataArrays / Datasets
1. Use `groupby_bins` to aggregate data in bins
1. Use `resample` on time dimensions
1. Use `rolling` to apply rolling aggregations

#### Merging Combining Datasets

1. Concatentate DataArrays and Datasets along a new or existing dimension
1. Merge multiple datasets with different variables
1. Add a new data variable to an existing Dataset

#### Reshaping Data

1. Transpose dimension order
1. Swap coordinates
1. Expand and squeeze dimensions
1. Convert between DataArray and Dataset
1. Use `stack` and `unstack` to transform data

#### Advanced Computations

1. Use `differentiate` to take derivatives of data
1. Use `apply_ufunc` to apply custom or specialized operations to data


#### Plotting

1. Show multiple line plots over a dimension using the `hue` keyword
1. Create multiple 2D plots using faceting
