# Intro to Unix

An introduction to basic Unix commands and the file system.

*The notes below are modified from the excellent [Unix Shell tutorial ](http://swcarpentry.github.io/shell-novice/) that is freely available on the Software Carpentry website. We highly recommend checking out the full version for further reading. The material is being used here under the terms of the [Creative Commons Attribution license](https://creativecommons.org/licenses/by/4.0/).*

---

## Navigating Files and Directories

Several commands are frequently used to create, inspect, rename, and delete files and directories.

To get started, open a terminal using the JupyterLab launcher. You will see
something like this.

~~~
jovyan@jupyter-rabernat:~$
~~~

The dollar sign is a **prompt**, which shows us that the shell is waiting for input.
`jovyan` is our **username** and `jupyter-rabernat` is the **hostname**.
Because we are using JupyterHub on the cloud, we all have the same username
("jovyan" = resident of the planet Jupyter). However, we each have a different
hostname (the name of the computer we are using), which corresponds to a
"virtual machine" running in the cloud. From now on, we will just use a `$`
to indicate the prompt.

To find out your username in general, you can use the command

~~~
$ whoami
jovyan
~~~

and to find out your hostname

~~~
$ hostname
jupyter-rabernat
~~~

Next,
let's find out where we are by running a command called `pwd`
(which stands for "print working directory").
At any moment,
our **current working directory**
is our current default directory,
i.e.,
the directory that the computer assumes we want to run commands in
unless we explicitly specify something else.
Here,
the computer's response is `/home/jovyan`,
which is the **home directory** of the user named `jovyan`.

~~~
$ pwd
~~~


~~~
/home/jovyan
~~~


To understand what a "home directory" is,
let's have a look at how the file system as a whole is organized.  For the
sake of this example, we'll be
illustrating the filesystem on our scientist Nelle's computer.  After this
illustration, you'll be learning commands to explore your own filesystem,
which will be constructed in a similar way, but not be exactly identical.  

On a Unix computer, the filesystem looks like something this:

![The File System](https://fsl.fmrib.ox.ac.uk/fslcourse/unix_intro/tree.gif)

At the top is the **root directory**
that holds everything else.
We refer to it using a slash character `/` on its own;
this is the leading slash in `/home/jovyan`.

Inside that directory are several other directories:
`bin` (which is where some built-in programs are stored),
`lib` (for the software "libraries" used by different programs),
`home` (where users' personal directories are located),
`etc` (system-wide configuration files),
and so on.  

Now let's learn the command that will let us see the contents of our
own filesystem.  We can see what's in our home directory by running `ls`,
which stands for "listing":

~~~
$ ls
~~~


~~~
config.yaml  examples  lost+found  work  worker-template.yaml
~~~

`ls` prints the names of the files and directories in the current directory in
alphabetical order,
arranged neatly into columns.
We can make its output more comprehensible by using the **flag** `-F`,
which tells `ls` to add a trailing `/` to the names of directories:

~~~
$ ls -F
~~~


~~~
config.yaml  examples/  lost+found/  work/  worker-template.yaml
~~~


`ls` has lots of other options. To find out what they are, we can type:

~~~
$ man ls
~~~

`man` is the Unix "manual" command:
it prints a description of a command and its options,
and (if you're lucky) provides a few examples of how to use it. To navigate through the `man` pages,
you may use the up and down arrow keys to move line-by-line,
or try the "b" and spacebar keys to skip up and down by full page.
Quit the `man` pages by typing "q".

Here,
we can see that our home directory contains mostly **sub-directories**.
Any names in your output that don't have trailing slashes,
are plain old **files**.

We can also use `ls` to see the contents of a different directory.  Let's take a
look at our `examples` directory by running `ls -F examples`,
i.e.,
the command `ls` with the **arguments** `-F` and `examples`.
The second argument --- the one *without* a leading dash --- tells `ls` that
we want a listing of something other than our current working directory:

~~~
$ ls -F examples
~~~

~~~
content/                                                LICENSE           publishconf.py
develop_server.sh*                                      Makefile          README.md
DONT_SAVE_ANYTHING_HERE.md                              pelicanconf.py    themes/
fabfile.py                                              pelican-plugins/
github_deploy_key_rabernat_research_computing_2018.enc  plugins/
~~~

The output is the list of all the files in the `examples` directory.
The examples directory on our JupyterHub is automatically populated with files
from the [Git Source Repository for the class](https://github.com/rabernat/research_computing_2018)

The command to change locations is `cd` followed by a
directory name to change our working directory.
`cd` stands for "change directory",
which is a bit misleading:
the command doesn't change the directory,
it changes the shell's idea of what directory we are in.

Let's say we want to move to the `content` directory we saw above.  We can
use the following series of commands to get there:

~~~
$ cd examples
$ cd content
~~~


These commands will move us from our home directory onto into
the `examples` directory, then into the `content` directory. `cd` doesn't print anything,
but if we run `pwd` after it, we can see that we are now
in `/home/jovyan/examples/content`.
If we run `ls` without arguments now,
it lists the contents of `/home/jovyan/examples/content`,
because that's where we now are.

We now know how to go down the directory tree, but
how do we go up?  
There is a shortcut in the shell to move up one directory level
that looks like this:

~~~
$ cd ..
~~~


`..` is a special directory name meaning
"the directory containing this one",
or more succinctly,
the **parent** of the current directory.
Sure enough,
if we run `pwd` after running `cd ..`, we're back in `/home/jovyan/examples`:

~~~
$ pwd
~~~

~~~
/home/jovyan/examples
~~~

e special directory `..` doesn't usually show up when we run `ls`.  If we want
to display it, we can give `ls` the `-a` flag:

~~~
$ ls -F -a
~~~


`-a` stands for "show all";
it forces `ls` to show us file and directory names that begin with `.`,
such as `..` (which, if we're in `/home/jovyan`, refers to the `/home` directory)
As you can see,
it also displays another special directory that's just called `.`,
which means "the current working directory".
It may seem redundant to have a name for it,
but we'll see some uses for it soon.

Note that in most command line tools, multiple parameters can be combined
with a single `-` and no spaces between the parameters: `ls -F -a` is
equivalent to `ls -Fa`.

These then, are the basic commands for navigating the filesystem on your computer:
`pwd`, `ls` and `cd`.  Let's explore some variations on those commands.  What happens
if you type `cd` on its own, without giving
a directory?  

~~~
$ cd
~~~


How can you check what happened?  `pwd` gives us the answer!  

~~~   
$ pwd
~~~


~~~
/home/jovyan
~~~

It turns out that `cd` without an argument will return you to your home directory,
which is great if you've gotten lost in your own filesystem.  

Let's try returning to the `content` directory from before.  Last time, we used
three commands, but we can actually string together the list of directories
to move to `data` in one step:

~~~
$ cd examples/content
~~~


Check that we've moved to the right place by running `pwd` and `ls -F`  

If we want to move up one level from the data directory, we could use `cd ..`.  But
there is another way to move to any directory, regardless of your
current location.  

So far, when specifying directory names, or even a directory path (as above),
we have been using **relative paths**.  When you use a relative path with a command
like `ls` or `cd`, it tries to find that location  from where we are,
rather than from the root of the file system.  

However, it is possible to specify the **absolute path** to a directory by
including its entire path from the root directory, which is indicated by a
leading slash.  The leading `/` tells the computer to follow the path from
the root of the file system, so it always refers to exactly one directory,
no matter where we are when we run the command.

This allows us to move to our `examples` directory from anywhere on
the filesystem.  To find the absolute path
we're looking for, we can use `pwd` and then extract the piece we need
to move to `examples`.  

~~~
$ pwd
~~~


~~~
/home/jovyan/examples/content
~~~


~~~
$ cd /home/jovyan/examples
~~~


Run `pwd` and `ls -F` to ensure that we're in the directory we expect.  

#### Two More Shortcuts

The shell interprets the character `~` (tilde) at the start of a path to
mean "the current user's home directory". For example, if Nelle's home
directory is `/home/jovyan`, then `~/examples` is equivalent to
`/home/jovyan/examples`. This only works if it is the first character in the
path.

Another shortcut is the `-` (dash) character.  `cd` will translate `-` into
*the previous directory I was in*, which is faster than having to remember,
then type, the full path.  This is a *very* efficient way of moving back
and forth between directories. The difference between `cd ..` and `cd -` is
that the former brings you *up*, while the latter brings you *back*. You can
think of it as the *Last Channel* button on a TV remote.

#### Tab Completion

Typing the full path to directories and files can be slow and annoying.
Fortunately, we have "tab completion" to help us. Try typing `cd ex` and then
press the `<tab>`. The system will try to "auto complete" your command.
Pressing tab twice brings up a list of all the files, and so on.
This is called **tab completion**,
and we will see it in many other tools as we go on.

#### Key Points:
- "The file system is responsible for managing information on the disk."
- "Information is stored in files, which are stored in directories (folders)."
- "Directories can also store other directories, which forms a directory tree."
- "`cd path` changes the current working directory."
- "`ls path` prints a listing of a specific file or directory; `ls` on its own lists the current working directory."
- `pwd` prints the user's current working directory.
- `whoami` shows the user's current identity.
- `/` on its own is the root directory of the whole file system.
- A relative path specifies a location starting from the current location.
- An absolute path specifies a location from the root of the file system.
- Directory names in a path are separated with '/' on Unix, but '\\\\' on Windows.
- '..' means 'the directory above the current one'; '.' on its own means 'the current directory'.
- Most files' names are `something.extension`. The extension isn't required, and doesn't guarantee anything, but is normally used to indicate the type of data in the file.
- Most commands take options (flags) which begin with a '-'.

## Working with Files and Directories

We now know how to explore files and directories,
but how do we create them in the first place?
Let's go back to our home directory
and use `ls -F` to see what it contains:

~~~
$ cd
$ pwd
~~~


~~~
/home/jovyan
~~~


~~~
$ ls -F
~~~


~~~
config.yaml  examples/  lost+found/  work/  worker-template.yaml
~~~


Let's create a new directory called `thesis` using the command `mkdir thesis`
(which has no output):

~~~
$ mkdir thesis
~~~


As you might guess from its name,
`mkdir` means "make directory".
Since `thesis` is a relative path
(i.e., doesn't have a leading slash),
the new directory is created in the current working directory:

~~~
$ ls -F
~~~


~~~
config.yaml  examples/  lost+found/  thesis/  work/  worker-template.yaml
~~~


## Good names for files and directories

 Complicated names of files and directories can make your life painful
 when working on the command line. Here we provide a few useful
 tips for the names of your files.

 1. Don't use whitespaces.

    Whitespaces can make a name more meaningful
   but since whitespace is used to break arguments on the command line
   is better to avoid them on name of files and directories.
    You can use `-` or `_` instead of whitespace.

 2. Don't begin the name with `-` (dash).

    Commands treat names starting with `-` as options.

 3. Stick with letters, numbers, `.` (period), `-` (dash) and `_` (underscore).

    Many other characters have special meanings on the command line.
    We will learn about some of these during this lesson.
    There are special characters that can cause your command to not work as
    expected and can even result in data loss.

 If you need to refer to names of files or directories that have whitespace
 or another non-alphanumeric character, you should surround the name in quotes (`""`).


Since we've just created the `thesis` directory, there's nothing in it yet:

~~~
$ ls -F thesis
~~~


Let's change our working directory to `thesis` using `cd`.
We then create a blank new file called `draft.txt` using the `touch command`:

~~~
$ cd thesis
$ touch draft.txt
~~~

Now we can edit the file in JupyterLab's text editor.
Let's type in a few lines of text.
Once we're happy with our text, we save the file, and
return to the shell.

`ls` now shows that we have created a file called `draft.txt`:

~~~
$ ls
draft.txt
~~~

Let's tidy up by running `rm draft.txt`:

~~~
$ rm draft.txt
~~~


This command removes files (`rm` is short for "remove").
If we run `ls` again,
its output is empty once more,
which tells us that our file is gone:

~~~
$ ls
~~~


#### Deleting Is Forever

The Unix shell doesn't have a trash bin that we can recover deleted
files from (though most graphical interfaces to Unix do).  Instead,
when we delete files, they are unhooked from the file system so that
their storage space on disk can be recycled. Tools for finding and
recovering deleted files do exist, but there's no guarantee they'll
work in any particular situation, since the computer may recycle the
file's disk space right away.


Let's re-create that file
and then move up one directory to `/home/jovyan` using `cd ..`:

~~~
$ touch draft.txt
$ cd ..
~~~


If we try to remove the entire `thesis` directory using `rm thesis`,
we get an error message:

~~~
$ rm thesis
~~~


~~~
rm: cannot remove `thesis`: Is a directory
~~~

This happens because `rm` by default only works on files, not directories.

To really get rid of `thesis` we must also delete the file `draft.txt`.
We can do this with the [recursive](https://en.wikipedia.org/wiki/Recursion) option for `rm`:

~~~
$ rm -r thesis
~~~


#### With Great Power Comes Great Responsibility

 Removing the files in a directory recursively can be very dangerous
 operation. If we're concerned about what we might be deleting we can
 add the "interactive" flag `-i` to `rm` which will ask us for confirmation
 before each step

~~~
 $ rm -r -i thesis
 rm: descend into directory ‘thesis’? y
 rm: remove regular file ‘thesis/draft.txt’? y
 rm: remove directory ‘thesis’? y
~~~


 This removes everything in the directory, then the directory itself, asking
 at each step for you to confirm the deletion.


Let's create that directory and file one more time.

~~~
$ mkdir thesis
$ touch thesis/draft.txt
$ ls thesis
~~~


~~~
draft.txt
~~~


`draft.txt` isn't a particularly informative name,
so let's change the file's name using `mv`,
which is short for "move":

~~~
$ mv thesis/draft.txt thesis/quotes.txt
~~~


The first parameter tells `mv` what we're "moving",
while the second is where it's to go.
In this case,
we're moving `thesis/draft.txt` to `thesis/quotes.txt`,
which has the same effect as renaming the file.
Sure enough,
`ls` shows us that `thesis` now contains one file called `quotes.txt`:

~~~
$ ls thesis
~~~


~~~
quotes.txt
~~~

One has to be careful when specifying the target file name, since `mv` will
silently overwrite any existing file with the same name, which could
lead to data loss. An additional flag, `mv -i` (or `mv --interactive`),
can be used to make `mv` ask you for confirmation before overwriting.

Just for the sake of consistency,
`mv` also works on directories

Let's move `quotes.txt` into the current working directory.
We use `mv` once again,
but this time we'll just use the name of a directory as the second parameter
to tell `mv` that we want to keep the filename,
but put the file somewhere new.
(This is why the command is called "move".)
In this case,
the directory name we use is the special directory name `.` that we mentioned earlier.

~~~
$ mv thesis/quotes.txt .
~~~


The effect is to move the file from the directory it was in to the current working directory.
`ls` now shows us that `thesis` is empty:

~~~
$ ls thesis
~~~


Further,
`ls` with a filename or directory name as a parameter only lists that file or directory.
We can use this to see that `quotes.txt` is still in our current directory:

~~~
$ ls quotes.txt
~~~


~~~
quotes.txt
~~~


The `cp` command works very much like `mv`,
except it copies a file instead of moving it.
We can check that it did the right thing using `ls`
with two paths as parameters --- like most Unix commands,
`ls` can be given multiple paths at once:

~~~
$ cp quotes.txt thesis/quotations.txt
$ ls quotes.txt thesis/quotations.txt
~~~


~~~
quotes.txt   thesis/quotations.txt
~~~


To prove that we made a copy,
let's delete the `quotes.txt` file in the current directory
and then run that same `ls` again.

~~~
$ rm quotes.txt
$ ls quotes.txt thesis/quotations.txt
~~~


~~~
ls: cannot access quotes.txt: No such file or directory
thesis/quotations.txt
~~~

This time it tells us that it can't find `quotes.txt` in the current directory,
but it does find the copy in `thesis` that we didn't delete.

### Key Points
- `cp old new` copies a file.
- `mkdir path` creates a new directory.
- `mv old new` moves (renames) a file or directory.
- `rm path` removes (deletes) a file.
- Use of the Control key may be described in many ways, including `Ctrl-X`, `Control-X`, and `^X`.
- The shell does not have a trash bin: once something is deleted, it's really gone.
- Depending on the type of work you do, you may need a more powerful text editor than Nano.

## Learning More

The goal of this lesson was to familiarize you with the basics of working
with files and directories.
There is a **lot more** to the unix shell and filexsystem than what we have  covered here!
To ge deeper with self study, we recommend the excellent
[Software Carpentry Unix Shell Lesson](https://swcarpentry.github.io/shell-novice/),
on which the above material was based.
