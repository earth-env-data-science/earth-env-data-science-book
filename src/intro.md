# An Introduction to Earth and Environmental Data Science

## History

This book grew out of a course developed at Columbia University called _Research Computing in Earth Science_.
It was written mostly by [Ryan Abernathey](https://rabernat.github.io), with significant contributions from
[Kerry Key](https://emlab.ldeo.columbia.edu/index.php/team/kerry-key/) and
[Tim Crone](https://github.com/tjcrone).
By separating the book from the class, we hope to create an open-source community resource for Python education
in the Earth and Environmental Sciences.

## Motivation and Scope

Computing has become an indispensable tool for nearly all Earth and Environmental Scientists, but it doesn't often appear in our curriculums.
This book focuses on _data analysis_, a subset of computing in which the data already exist, e.g.from observations or from the output of a simulation, but have to be transformed into understanding.
There are many different ways to gain understanding, but most workflows often boil down to:

- read data files
- perform some analysis operations, from very simple (e.g. take the mean) to very complex (e.g. train a deep neural network)
- visualize the output in a plot

This book doesn't attempt to teach deep learning; its goal is to teach the basic foundations of Earth and Environmental Data Science which are often overlooked.
The material is designed to be accessible for Earth Science graduate students in any discipline, with no prerequisites.

This book is intended to introduce new graduate students to modern computing software, programming tools and best practices that are broadly applicable to the analysis and visualization of Earth and Environmental data.
This includes an introduction to Unix, version control, and basic programming in the open-source Python language.
The bulk of the content is devoted to in-depth exploration of the numerical analysis and visualization packages which comprise the modern Scientific Python ecosystem, including Numpy, Scipy, Matplotlib, Pandas, Xarray, using real Earth and Environmental datasets.

## Learning Goals

After completing all of the material, students should have the ability to:

- Use unix commands to work with files and directories
- Navigate the JupyterHub Environment effectively
- Identify common geoscience data formats and the python packages which can load them
- Perform basic exploratory data analysis on Earth and Environmental data, distinguishing between
  - _Tabular data_: rows and columns
  - _Gridded data_: multidimensional numerical arrays
- Use visualization to enhance interpretation of data, including maps and interactive visualizations
- Construct complete, well-structured programs in Python
- Practice reproducible research through version control and binder

## Recommended Course Structure

This course material can be used however you want.
However, it was developed for a full-credit, semester-long course that meets twice a week.
The idea is to complete one lecture and one homework assignment per week.
One of the weekly meetings consists of a lecture in which the instructor presents the week's lecture, with students typing along.
The other should be used as "collaborative time," during which the students work on their assignments, ask questions, and interact with their peers.
A final project is an important capstone experience for a semester-long course.
