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

## Setting Up GitHub SSH Keys inside JupyterHub

```{warning}
As of August 12, 2021, GitHub [no longer supports username / password authentication](https://github.blog/changelog/2021-08-12-git-password-authentication-is-shutting-down/).
Users must switch to personal access tokens or SSH-keys for authentication.
```

This is a very quick guide to getting your GitHub authentication set up,
adopted from the [Carpentries GitHub Remotes lesson](https://swcarpentry.github.io/git-novice/07-github/index.html#ssh-background-and-setup).

1. Open a terminal in JupyterHub
1. Type the command
   ```
   ssh-keygen -t ed25519 -C "YOUR EMAIL ADDRESS GOES HERE"`
   ```
   (Don't just copy this text; you have to put in tour actual email address in between the quotes.) This command will create an ssh public / private key pair.
1. Enter a password for your new SSH key and record it in a safe place.
   This password is used to "lock" the SSH key. It can't be used without the password.
1. Type the command
   ```
   cat ~/.ssh/id_ed25519.pub
   ```
   and copy the result. It should look something like `ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIJOMg813PWuWX/ilyexj2k/di1lBHwQHCHbRB6l4dV9K rpa@ldeo.columbia.edu`. (Note that this is my _real_ public key, but it is completely
   safe to share. Without the corresponding private key it is useless.)
1. Go to <https://github.com/settings/keys>. Click the green  button that says "New SSH Key".
   Give your key the title "JupyterHub SSH Key for Research Computing" and paste the
   public key from the previous step into the "Key" box.
1. Verify that your key works by typing
   ```
   ssh -T git@github.com
   ```
   on the command like of the JupyterHub. (Note you will have to enter your SSH key password from step 3.)

You should now be able to push to GitHub.

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
