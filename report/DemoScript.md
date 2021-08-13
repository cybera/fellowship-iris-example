# Demo Script

## Document Intro

The following is going to outline the changes made to 
the starting notebook to convert it from a single notebook 
which had a poor naming convention and function definition 
which was eventually refactored into a separate script. 

Additionally, some information on merging/comparing simultaneous
changes to a single notebook was demo'ed based on a branch
from a practice demo of the refactor changes. Some information on
that will also be presented. 

## Let's Get Started

To start with, a note on git. Since it is a version control
system there's lot's of good information on what exists in 
it's own history. For example, on github, 
there is a visual representation
of the branches or tree structure on repos that shows it's 
history and how branches have diverged or merged. In this repo,
you can take a look at the 
['network'](https://github.com/cybera/fellowship-iris-example/network)
where you can see the following branches: 

- a complex abandoned version of this demo, 
- a practice of this demo (with an open PR), and
- this live demo branch which has been merged to 'main'.

Below is an ASCII schematic of what that looks like:

```
** Simplified Git Tree Schematic **
↑ Future

o <- demo end
|
X    <-- Pull Request/Merge
| \ 
|  \ 
|   o several commits
|   |
|   o live demo
 \ /
  V 
  |
  |
  |   o practice demo
   \ /
    V
    |
    |   o complex abandonced branch 
     \ /
      V
      |
      o start branch
      |
      o older repo setup

↓ Past
```

You can also access this in other 3rd party tools (e.g. if you aren't using github), for example using the plugin 'Git Graph' in VS Code.


If you look at the above link or clone the repo and run git log 
there's also the commit SHA-1 hashes (long sequence of numbers and letters). We're going to reference 
those and (hopefully) you could do that on your own 
and figure out what happened, but below we'll explain what
was done, reference the SHA-1 hashes so you can see what was done 
and how that can be useful for going back or referencing 
any work you've done. If you ever want to go back 
and just look at the files you can do that on github
or in git on a cloned repo by using `git checkout <abc134>` 
where <abc134> would be replaced by the first few characters 
of the git commit hash you're interested in. 

Also, we'll be version controlling this document as well so 
if you want you could find out any fun or strange things that have 
changed over the authoring of this as well. 

## Actions


Below are the commit hashes (labels) of all the commits we did 
during the demo as well as their commit messages. Every commit 
creates a new snapshot of our files and moves us onto 
the next SHA-1 hash in the git graph. 

All git 
commands are run from github directory top level folder which
was ~/DS/fellowship-iris-example on my 
MAC (which corresponds equivalently /home/jovyan/ in the docker container).


----
### [c1b408](https://github.com/cybera/fellowship-iris-example/commit/c1b408): (Start, made branch from here)

**Git/Terminal:**
```
git switch main
git branch fellowship-demo
```
----
### [1bcd36](https://github.com/cybera/fellowship-iris-example/commit/1bcd36): renamed and moved notebook

**Git/Terminal:**
```
git mv zach-Iris_notebook.ipynb ./notebooks/IrisLoadAndDisplay.ipynb
git add ./notebooks/IrisLoadAndDisplay.ipynb
git commit -m 'renamed and moved notebook'
```

----
### [d756ce](https://github.com/cybera/fellowship-iris-example/commit/d756ce): Removed unnecessary cells, moved imports
**Text Editor:** 

- Deleted extra 'printing' cells (Esc + D + D),
- Copied imports to top of notebook.
```
git add ./notebooks/IrisLoadAndDisplay.ipynb
git commit -m 'Removed unnecessary cells, moved imports'
```

----
### [9943da](https://github.com/cybera/fellowship-iris-example/commit/9943da): refactored fucntion def 
_oh no a typo :(_ -- this could have been fixed with `git commit --ammend` before pushing.

**Text Editor:** 

Copied the function definition for `def scatterMatrix(dataFrame, labelColumn)` from the _IrisLoadAndDisplay.ipynb_ to a new 
python file _./scripts/visualization/graphs.py_

**Git/Terminal:**
```
git add ./scripts/visualization/graphs.py
git commit -m 'refactored fucntion def'
```
----
### [03ea64](https://github.com/cybera/fellowship-iris-example/commit/03ea64): Fixed matplotlib import

**Text Editor:** 

Add `import matplotlib` to _scripts/visualization/graphs.py_.

```
git add scripts/visualization/graphs.py
git commit -m 'Fixed matplotlib import'
```

----
### [78a46](https://github.com/cybera/fellowship-iris-example/commit/78a46c): Moved function def out to script

**Text Editor:** 

Deleted `def scatterMatrix(dataFrame, labelColumn)` cell.

Added external script import to top of notebook:
```python
import sys
sys.path.append('/home/jovyan/')
```

**Git/Terminal:**
```
git add ./notebooks/IrisLoadAndDisplay.ipynb
git commit -m 'Moved function def out to script'
```

----
### [d45abc](https://github.com/cybera/fellowship-iris-example/commit/d45abc): pre PR commit
**Text Editor:** 

Any last cleanup or other changes to the notebook were 
done (e.g. adding docstrings?). I don't remember, check the
actual commit at hyperlink.

**Git/Terminal:**
```
git add ./notebooks/IrisLoadAndDisplay.ipynb
git add ./scripts/visualization/graphs.py
git commit -m 'pre PR commit'
```

----
### [d45abc](https://github.com/cybera/fellowship-iris-example/commit/d45abc): Created branch for PR; 
_fellowship-demo still exists as an open branch in the repo_

Notice we're at the same hash 
because we haven't commited any changes.

**Git/Terminal:**
```
git branch fellowship-demo-PR
git switch fellowship-demo-PR
```

----
### [e0a1ed](https://github.com/cybera/fellowship-iris-example/commit/e0a1ed): Removed not PR ready notebooks

**Git/Terminal:**
```
git rm <some notebook that got added along the way>
git commit -m 'Removed not PR ready notebooks'
git push
```

----
### [Pull Request](https://github.com/cybera/fellowship-iris-example/pull/4): Opened on github.com
Before the next step we went to github.com/cybera/fellowship-iris-example/ and opened a PR on the newly made 
fellowship-demo-PR branch. 

We didn't have to do this, but I wanted to keep working in 
that branch but also didn't want to push some of the unfinished
committed work that was on my branch. (There's other ways 
you could go about this as well.)

[Here](https://github.com/cybera/fellowship-iris-example/pull/4) is that closed PR if you want to see what comments were made. 
Someone (rightfully) said that there should be axis labels in 
the PR comments. We're going to change that and push that.

----
### [ee6b7a](https://github.com/cybera/fellowship-iris-example/commit/ee6b7a): added axis labels (PR comment)

**Text Editor:** 

Add axis labels to function definition in _scripts/vizualization/graphs.py_.

**Git/Terminal:**
```
git add scripts/vizualization/graphs.py
git commit -m 'added axis labels (PR comment)'
git push
```

----
### [103c89](https://github.com/cybera/fellowship-iris-example/commit/103c89): Merge pull request #4 from cybera/fellowship-demo-PR
Now our data is in the main branch. 
Along the way we picked up [aee895](https://github.com/cybera/fellowship-iris-example/commit/aee895) as a commit 
because someone (me) updated the README.md file since the 
original branch for this demo was made. This will
show up in git log of all future branches from this merge 
to main. Since we weren't modifying the README we didn't 
need to worry about merging that file and it was merged 
automoatically. 
 
## Merging Jupyter Notebooks
Jupyter is a complex environment which works 
with a markup of python and its outputs. In other words, 
you're interacting with an application that 
writes the 'code' and creates syntactically valid 
json markup that it can save, read, and execute. 

Git, however, is designed primarily for version 
controlling more traditional line-by-line
programs and only knows how to work with lines of text. 
If you never collaborated on a notebook with someone 
you'd never have merge conflicts in a notebook and 
you might not notice this fact. If you ever 
have to merge changes from two people (say in a pull
request) you will discover that this is difficult. 

In the demo, I showed how to use a command line tool 
called nbdime which has git integration support 
to make this process a bit easier. To setup the demo 
I made two branches ahead of time where I had 
made concurrent changes in two branches that I wanted 
to later merge. 

These notebooks have changes on the same 
line -- one changed the figure size to 
(16,10) vs. (18,18) in the other -- 
which are a merge conflict for git. Additionally, 
there is a conflict in the output png genereated since one notebook
has increased the font size while the other has added 
a title to the figure.  

I called these two branches 
[notebookA](https://github.com/cybera/fellowship-iris-example/tree/notebookA) 
which is currently at hash b714a and 
[notebookB](https://github.com/cybera/fellowship-iris-example/tree/notebookB) 
which is at hash 495de. 
You can also look at the two notebooks here: 
[A](https://github.com/cybera/fellowship-iris-example/blob/notebookA/notebooks/IrisLoadAndDisplay.ipynb) and [B](https://github.com/cybera/fellowship-iris-example/blob/notebookB/notebooks/IrisLoadAndDisplay.ipynb)

To install the tool and connect it to git we run the following 
commands at the terminal (this has to be installed in the same place you're running git from, i.e. not in the requirements.txt).

If you were to switch to notebookB and run `git merge notebookA` you would be asking 
for git to take the changes in notebookA branch and merge them into 
nobetookB. This will result in a merge conflict. Git expects you to open that file,
look at the changes indicated with `<<<<, =====, >>>>` markup 
and fix the file in a text editor. Below is an example from 
this merge: 

```
    "import sklearn\n",
    "import sklearn.datasets\n",
    "\n",
    "import scripts.visualization.graphs as myGraphs\n",
    "\n",
    "import matplotlib.pyplot as plt\n",
<<<<<<< HEAD
    "plt.rcParams['figure.figsize'] = (18,18)"
=======
    "plt.rcParams['figure.figsize'] = (16,10)\n",
    "plt.rcParams['font.size'] = 14"
>>>>>>> notebookA
   ]
  },
  {
```

If you made the mistake of taking adjusting it as follows (accepting the 
18,18 figsize, accepting the font size line):

```
**Incorrect**
    "import scripts.visualization.graphs as myGraphs\n",
    "\n",
    "import matplotlib.pyplot as plt\n",
    "plt.rcParams['figure.figsize'] = (18,18)"
    "plt.rcParams['font.size'] = 14"
   ]
  },
  {
```

you would be missing the __\n"__ and __,__ required for the jupyter syntax and might break the notebook, 
preventing it from opening and you'd have to revert an old version. 
Even if you are using VS Code or other IDE to help, this may 
still not be easy or nice (there are some VS Code extensions 
that make this easier as well and 
seem to do something similar to nbdime as well).

Additionally, there is a merge conflict on the png output.
This might be easier to merge as it's an either/or selection, but it 
certainly is messier since you're dealing with binary data. 

If you had run the merge command 
and you don't want to continue 
we can undo our 'failed' merge 
with `git merge --abort` 
and try the following:

```terminal
## Install nbdime
> pip install nbdime
> nbdime config-git --enable

> git switch notebookB
> git merge notebookA
## Above results in a merge conflict

## After merge, opens browser
> nbdime mergetool
```

and resolve all the conflicts visually in a browswer window. 
The nbdime program also does a couple other 
nice things for you, like ignoring cell execution numberings, 
and other metadata that you probably weren't interested 
in version controlling anyway.  
