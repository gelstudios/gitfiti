[![Build Status](https://travis-ci.org/gelstudios/gitfiti.svg?branch=master)](https://travis-ci.org/gelstudios/gitfiti)

gitfiti _noun_ : Carefully crafted graffiti in a github commit history calendar.  

An example of gitfiti in the wild:  
![alt text](https://raw.github.com/gelstudios/gitfiti/master/gitfiti-screenshot.png "screenshot")

`gitfiti.py` is a tool I wrote to decorate your github account's commit history calendar by (blatantly) abusing git's ability to accept commits _in the past_.

How?  `gitfiti.py` generates a bash script: `gitfiti.sh` that makes commits with the GIT_AUTHOR_DATE and GIT_COMMITTER_DATE environment variables set for each targeted pixel.

Since this is likely to clobber repo's history, I highly recommend that you create a _new_ github repo when using gitfiti. Also, the generated bash script assumes you are using public-key authentication with git.


### Pixel Art:
![alt text](https://raw.github.com/gelstudios/gitfiti/master/pixels-large.png "pixel art")  
Included "art" from left to right: kitty, oneup, oneup2, hackerschool, octocat, octocat2

### Usage:
1. Create a new github repo to store your handiwork.
2. Run `gitfiti.py` and follow the prompts for username, art selection, offset, and repo name.
3. Run the generated `gitfiti.sh` from your home directory (or any non-git tracked dir) and watch it go to work.
4. Wait... Seriously, you'll probably need to wait a day or two for the gitfiti to show in your commit graph.

### User Templates
The file format for personal templates is the following:

1. Each template starts off with a ":" and then a name (eg. ":foo")
2. Each line after that is part of a json-recognizable array.
3. The array contain values 0-4, 0 being blank and 4 being dark green.
4. To add multiple templates, just add another name tag as described in 1.

For example:

```
:center-blank
[[1,1,1,1,1,1,1],
[1,1,1,1,1,1,1],
[1,1,1,1,1,1,1],
[1,1,1,0,1,1,1],
[1,1,1,1,1,1,1],
[1,1,1,1,1,1,1],
[1,1,1,1,1,1,1]]
```

This would output a 7 x 7 light green square with a single blank center square.

Once you have a file with templates, enter its name when prompted and the templates will be added to the list of options.

### Removal:
Fortunately if you regret your gitfiti in the morning, removing it is fairly easy: delete the repo you created for your gitfiti (and wait).

### License:
gitfiti is released under [The MIT license (MIT)](http://opensource.org/licenses/MIT)

---
#### Todo:
- ~~Remove 'requests' dependency~~ [_thanks empathetic-alligator_](https://github.com/empathetic-alligator)
- ~~Web interface~~ See several web-based things below
- ~~Load "art" from a file~~ [_thanks empathetic-alligator_](https://github.com/empathetic-alligator)
- Load commit content from a file
- Text/alphabet option
- ...
- Profit?

#### Notable derivatives or mentions:
- [Pikesley's](https://github.com/pikesley) Pokrovsky, which offers Github History Vandalism [as a Service!](http://pokrovsky.herokuapp.com/)
- [github-board](https://github.com/bayandin/github-board) commits gitfiti from easy templates
- [ghdecoy](https://github.com/tickelton/ghdecoy) fills the contribution graph with random data (sneaky!)
- [Gitfiti Painter](http://codepen.io/cbas/pen/vOXeKV) visual drawing tool for artists to easily create templates
- [git-draw](https://github.com/ben174/git-draw) a Chrome extension which will allow you to freely draw on your commit map(!)
- [github-jack](https://github.com/tardypad/github-jack) a pure bash version with space invaders and shining creepypasta
- Seen something else? Submit a pull request or open an issue!


  
  
![alt text](http://f.cl.ly/items/0J463J0K1N020S1Q3E3l/er-small.png "tiny logo")
