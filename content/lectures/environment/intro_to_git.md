# Intro to Git

Follow the tutorial
 [Version Control with Git](http://swcarpentry.github.io/git-novice/) on Software Carpentry website.

**Summary of useful Git commands**

Set up your username and email
~~~
git config --global user.name "Ryan Abernathey"
git config --global user.email "rpa@ldeo.columbia.edu"
~~~

Create a new repository:
~~~
cd my_project
git init      
~~~

Stage files for addition to the repository:
~~~
git add <filenames>  
~~~

Commit staged files:

~~~
git commit -m "your brief commit message goes here"
~~~

Other useful commands:

~~~
git status    # tells you what files are staged, which ones have been modified, are new,... )
git log       # view the commit log
git diff      # view file content differences
~~~

Working with a remote repository on GitHub:

~~~
git remote add ...
git push
git pull
~~~

Basic collaboration workflow:

* update your local repo with `git pull origin master`,
* make your changes and stage them with `git add`,
* commit your changes with `git commit -m`, and
* upload the changes to GitHub with` git push origin master`
