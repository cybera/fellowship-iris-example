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
- this branch which has been merged to 'main'

Below is an ASCII schematic of what that looks like:

```
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
      o start
```

You can also access this in other 3rd party tools (e.g. if you aren't using github), for example using the plugin 'Git Graph' in VS Code.


If you look at the above link or clone the repo and run git log 
there's also the commit SHA-1 hashes. We're going to reference 
those and (hopefully) you could do that on your own 
and figure out what happened, but below we'll explain what
was done, reference the SHA-1 hashes so you can see what was done 
and how that can be useful for going back or referencing 
any work you've done. 

Also, we'll be version controlling this document as well so 
if you want you could find out any fun or strange things that have 
changed over the authoring of this as well. 

## Outline

c1b408 Start (Delete GetData.ipynb)
aee895 Update README.md (on main)
1bcd36 renamed and moved notebook
d756ce Removed unnecessary cells, moved imports
9943da refactored fucntion def
03ea64 Fixed matplotlib import
78a46c Moved function def out to script
d45abc pre PR commit
\<this is where we branched\> _fellowship-demo exists as a branch here still_
e0a1ed Removed not PR ready notebooks
ee6b7a added axis labels (PR comment)
103c89 Merge pull request #4 from cybera/fellowship-demo-PR
    
    

```gitlog
commit d5b747176137e793058ca17a40702c58407f57f9 (HEAD -> script)
Author: Zachary Shand <zachary.shand@cybera.ca>
Date:   Mon Aug 9 16:40:22 2021 -0600

    Wrote intro to Script file

commit 103c89e50ea3331c6602bfc7ebc1412e5ddab415 (origin/main, origin/HEAD, main)
Merge: aee8952 ee6b7a0
Author: Zach <81401558+ZachAttacksProblems@users.noreply.github.com>
Date:   Wed Aug 4 13:45:23 2021 -0600

    Merge pull request #4 from cybera/fellowship-demo-PR
    
    Fellowship demo pr

commit ee6b7a08d09a87f2816071cedca2135235adddc9 (origin/fellowship-demo-PR)
Author: Zachary Shand <zachary.shand@cybera.ca>
:...skipping...
commit d5b747176137e793058ca17a40702c58407f57f9 (HEAD -> script)
Author: Zachary Shand <zachary.shand@cybera.ca>
Date:   Mon Aug 9 16:40:22 2021 -0600

    Wrote intro to Script file

commit 103c89e50ea3331c6602bfc7ebc1412e5ddab415 (origin/main, origin/HEAD, main)
Merge: aee8952 ee6b7a0
Author: Zach <81401558+ZachAttacksProblems@users.noreply.github.com>
Date:   Wed Aug 4 13:45:23 2021 -0600

    Merge pull request #4 from cybera/fellowship-demo-PR
    
    Fellowship demo pr

commit ee6b7a08d09a87f2816071cedca2135235adddc9 (origin/fellowship-demo-PR)
Author: Zachary Shand <zachary.shand@cybera.ca>
Date:   Wed Aug 4 13:44:39 2021 -0600

    added axis labels

commit e0a1ede1924dda708bef89475688897517551985
Author: Zachary Shand <zachary.shand@cybera.ca>
Date:   Wed Aug 4 13:34:41 2021 -0600

    Removed not PR ready notebooks

commit d45abc16baa1b0ceefac404f37c061ac8845e545 (origin/fellowship-demo, fellowship-demo)
Author: Zachary Shand <zachary.shand@cybera.ca>
Date:   Wed Aug 4 13:31:36 2021 -0600

    pre PR commit

commit 78a46c63ef73f902d3e5e4b48f6d36392c691c5b
Author: Zachary Shand <zachary.shand@cybera.ca>
Date:   Wed Aug 4 13:28:26 2021 -0600

    Moved function def out to script

commit 03ea6496173a2df22ba707ffac896df1c7cc2ccc
Author: Zachary Shand <zachary.shand@cybera.ca>
Date:   Wed Aug 4 13:28:13 2021 -0600

    Fixed matplotlib import

commit 9943da35ea1882111915fcdc77cdcfab4d76a868
Author: Zachary Shand <zachary.shand@cybera.ca>
Date:   Wed Aug 4 13:24:21 2021 -0600

    refactored fucntion def

commit d756ceba3f2cb9e40b060bdcabf872d53a4259c5
Author: Zachary Shand <zachary.shand@cybera.ca>
Date:   Wed Aug 4 13:20:00 2021 -0600

    Removed unnecessary cells, moved imports
commit 1bcd366928d4e3d7b337b65c946ce52ea7ef9cd6
Author: Zachary Shand <zachary.shand@cybera.ca>
Date:   Wed Aug 4 13:16:42 2021 -0600

    renamed and moved notebook

commit aee895242ca9dd97e709614d985f1a4c98914c3b
Author: Zach <81401558+ZachAttacksProblems@users.noreply.github.com>
Date:   Wed Aug 4 12:37:10 2021 -0600

    Update README.md

commit c1b408d6c4ca7924a9b71d2aaa62c91267b4a807
Author: Zach <81401558+ZachAttacksProblems@users.noreply.github.com>
Date:   Wed Aug 4 10:58:54 2021 -0600

    Delete GetData.ipynb
```

