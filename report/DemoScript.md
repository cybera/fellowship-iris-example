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
if you want you could find out any fun things that have 
changed over the authoring of this as well. 




