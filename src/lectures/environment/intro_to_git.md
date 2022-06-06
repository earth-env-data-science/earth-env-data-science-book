# Intro to Git for Version Control

## Overview

[_Version control_](https://en.wikipedia.org/wiki/Version_control) is a powerful way to organize, back up, and share with collaborators your research computing code.
A Verson control system keeps track of a set of files and saves snapshots (i.e. _versions_, _commits_) of the files at any point in time.
Using version control allows you to confidently make changes to your code (any any other files), with the ability to roll back to any previous state. This help avoid filling our directories up with files that look like this:

    my_code.py
    my_code_version2.py
    my_code_version2B-RPA-edit.py
    my_code_FINAL_VERSION.py
    my_code_THIS_IS_ACTUALLY_THE FINAL VERSION.py

Version control also allows you to share code with collaborators, make simultaneous edits, and merge your changes in a systematic, controlled way.

Version control has been used for a long time in software development.
More recently, it has become an essential part of modern data and computational science.
Our strong recommendation is that _all of your research code be stored in a version control system_.

The tool we will be using for version control is called [Git](https://git-scm.com).
Git is incredibly powerful--it also has a somewhat steep learning curve.
Fortunately, in this class, we will only be using a small subset of what git can do, avoiding the more complex aspects.

For a full-length tutorial, we recommend the article [Version Control with Git](http://swcarpentry.github.io/git-novice/) on Software Carpentry website.
Here we simply enumerate the most common git commands.


## Summary of useful Git commands

Set up your username and email

    git config --global user.name "Ryan Abernathey"
    git config --global user.email "rpa@ldeo.columbia.edu"


Create a new repository:

    cd my_project
    git init      

Stage files for addition to the repository:

    git add <filenames>  

Commit staged files:


    git commit -m "your brief commit message goes here"

Get information about your repository:

    git status    # tells you what files are staged, which ones have been modified, are new,... )
    git log       # view the commit log
    git diff      # view file content differences


Revert a file to an earlier version:

    git checkout <commit tag> <filenames>

## Using Git / GitHub from remote JupyterHub

The recommended way to move code in and out of a remote hub is via git / GitHub.
You should clone your project repo from the terminal and use git pull / git push to update and push changes.
In order to push data to GitHub from the hub, you will need to set up GitHub authentication.
[gh-scoped-creds](https://github.com/yuvipanda/gh-scoped-creds/) should be already setup
on your 2i2c managed JupyterHub, and we shall use that to authenticate to GitHub for
push / pull access.

Open a terminal in JupyterHub, run `gh-scoped-creds` and follow the prompts.

Alternatively, in a notebook, run the following code and follow the prompts:

```
import gh_scoped_creds
%ghscopedcreds
```

You should now be able to push to GitHub from the hub! These credentials will expire after
8 hours (or whenever your JupyterHub server stops), and you'll have to repeat these steps
to fetch a fresh set of credentials. Once you authenticate, you'll be provided with a link
to a [GitHub App](https://docs.github.com/en/developers/apps/getting-started-with-apps/about-apps)
that you have to [install](https://docs.github.com/en/developers/apps/managing-github-apps/installing-github-apps)
on the repositories you want to be able to push to from this particular JupyterHub. You only
need to do this once per JupyterHub, and can revoke access any time. You can always provide
access to your own personal repositories, but might need approval from admins of GitHub
organizations if you want to push to repos in that organization.


## Collaborating with Git and Github

* Create a new repository on GitHub
* Follow the instructions and run `git remote add origin <repo url>` on your local repo
  ````{warning}
  In order to authenticate with your SSH key from the previous section, you need use SSH-style GitHub urls.
  When setting up a new repo, underneath where it says "Quick setup — if you’ve done this kind of thing before",
  make sure you click the SSH box. The repo URL should look something like `git@github.com:rabernat/planets.git`
  (NOT `https://github.com/rabernat/planets.git`).

  If you already added a remote with `http://`, you can remove it by typing
  ```
  git remote rm origin
  ```
  (assuming the name of your remote is indeed `origin`.)
  ````
* make your changes and stage them with `git add`,
* commit your changes with `git commit -m`, and
* upload the changes to GitHub with` git push origin main`
* update your local repo with `git pull origin main`

All of the above commands are available from our course's cloud-based JupyterHub.
This is an excellent way to move code in and out of your cloud-based environment
(while simultaneously backing it up.)
