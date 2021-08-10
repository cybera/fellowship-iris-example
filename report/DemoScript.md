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
- this branch which has been merged to 'main'.

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
any work you've done. 

Also, we'll be version controlling this document as well so 
if you want you could find out any fun or strange things that have 
changed over the authoring of this as well. 

## Actions


Below are the commit hashes (labels) of all the commits we did 
during the demo as well as their commit messages.

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
_fellowship-demo exists as a branch here still_

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
 
    


