<p align="center">
    <img width=30% src="https://github.com/robertmartin8/PyGameofLife/blob/master/media/logo.gif">
</p>

<h1 align="center"> PyGameofLife </h1>

<!-- buttons -->
<p align="center">
    <a href="https://www.python.org/">
        <img src="https://img.shields.io/badge/python-v3-blue.svg?style=for-the-badge"
            alt="python"></a> &nbsp;
    <a href="https://opensource.org/licenses/MIT">
        <img src="https://img.shields.io/badge/license-MIT-blue.svg?style=for-the-badge"
            alt="MIT license"></a> &nbsp;
    <a href="https://github.com/robertmartin8/PyPortfolioOpt/graphs/commit-activity">
        <img src="https://img.shields.io/badge/Maintained%3F-yes-blue.svg?style=for-the-badge"
            alt="maintained"></a> &nbsp;
</p>

PyGameofLife is a simple implementation of Conway’s Game of Life in python, with a command-line interface that can generate pretty gifs. The source code emphasises simplicity and intuitive code rather than efficiency. A quick demo is shown here:

```bash
python life.py -seed r_pentomino -n 500 -interval 50
```

<p align="center">
    <img width=50% src="https://github.com/robertmartin8/PyGameofLife/blob/master/media/r_pentomino.gif">
</p>

# Contents

- [Getting started](#getting-started)
- [User guide](#user-guide)
  - [The seed](#the-seed)
  - [Size and position](#size-and-position)
  - [Colours](#colours)
  - [Animation paramaters](#animation-paramaters)
- [About](#about)

## Getting started

Because this is just a small educational script, I have chosen not to distribute it on PyPI. The only dependencies are `numpy` and `matplotlib`, which can be installed easily via `pip`:

```bash
pip install numpy matplotlib
```

To get started with PyGameofLife, navigate to a directory where you want to use the project, then clone it with:

```bash
git clone https://github.com/robertmartin8/PyGameofLife
```

Move into the directory that was just created (either through your filesystem or with `cd PyGameofLife`), and you are ready to go!

If you don't want to use `git clone` for whatever reason, you can manually download it, unzip it, and move the folder somewhere convenient (preferably either the desktop or your home directory). Then, open up your command line, and `cd` to the correct directory. For example:

```bash
cd Users/your_username/Desktop/PyGameofLife-master
```

That's all. You can interface with PyGameofLife via the command line. As an example, try running the following:

```bash
python life.py
```

After a brief moment, you should see `infinite.gif` appear. Open the file with any gif viewer (your  browser should work):

<p align="center">
    <img width=50% src="https://github.com/robertmartin8/PyGameofLife/blob/master/media/infinite.gif">
</p>

There are many many things you can customise.

## User guide

If at any time you need a quick reference, just run the `help` command:

```bash
python life.py --help
```

Which will give you the following

```bash
usage: life.py [-h] [--universe-size UNIVERSE_SIZE] [-seed SEED] [-n N]
               [-quality QUALITY] [-cmap CMAP] [-interval INTERVAL]
               [--seed-position SEED_POSITION]

PyGameofLife. By default, produces 50 generations of the 'infinite' seed

optional arguments:
  -h, --help            show this help message and exit
  --universe-size UNIVERSE_SIZE
                        comma-separated dimensions of universe (x by y)
  -seed SEED            seed for Life, see readme for list
  -n N                  number of universe iterations
  -quality QUALITY      image quality in DPI
  -cmap CMAP            colour scheme
  -interval INTERVAL    interval (in milliseconds) between iterations
  --seed-position SEED_POSITION
                        comma-separated coordinates of seed
```

However, I wll present some of the different options along with animations below.

### The seed

This is arguably where all of the magic of Life lies: simple seeds can produce exceedingly complex behaviour (it can be used to build a [Turing machine](http://rendell-attic.org/gol/tm.htm)), which is near-impossible to predict just by looking at the seed.

A seed is just a starting pattern that is placed somewhere in the universe. There are a number of seeds built in, and they should be referred to by the names below.

```bash
{
    "diehard": [[0, 0, 0, 0, 0, 0, 1, 0],
                [1, 1, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 1, 1, 1]],

    "boat": [[1, 1, 0],
            [1, 0, 1],
            [0, 1, 0]],

    "r_pentomino": [[0, 1, 1],
                    [1, 1, 0],
                    [0, 1, 0]],

    "pentadecathlon": [[1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 0, 1, 1, 1, 1, 0, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1]],

    "beacon": [[1, 1, 0, 0],
            [1, 1, 0, 0],
            [0, 0, 1, 1],
            [0, 0, 1, 1]],

    "acorn": [[0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0],
            [1, 1, 0, 0, 1, 1, 1]],

    "spaceship": [[0, 0, 1, 1, 0],
                [1, 1, 0, 1, 1],
                [1, 1, 1, 1, 0],
                [0, 1, 1, 0, 0]],

    "block_switch_engine": [[0, 0, 0, 0, 0, 0, 1, 0],
                            [0, 0, 0, 0, 1, 0, 1, 1],
                            [0, 0, 0, 0, 1, 0, 1, 0],
                            [0, 0, 0, 0, 1, 0, 0, 0],
                            [0, 0, 1, 0, 0, 0, 0, 0],
                            [1, 0, 1, 0, 0, 0, 0, 0]],

    "infinite": [[1, 1, 1, 0, 1],
                [1, 0, 0, 0, 0],
                [0, 0, 0, 1, 1],
                [0, 1, 1, 0, 1],
                [1, 0, 1, 0, 1]],
}
```

So you can do something like:

```bash
python life.py -seed diehard
```

<p align="center">
    <img width=50% src="https://github.com/robertmartin8/PyGameofLife/blob/master/media/infinite.gif">
</p>

If you'd like to add your own seed, the best way is to edit the source code and add it to the `seeds` dictionary at the top of `life.py`. By the way, if you try `boat` and it doesn't seem to be working, there's a [good reason](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life).

If you'd like to change the starting position of the seed, you can specify the coordinates (comma separated `x` and `y`) where the top-left of the seed will be placed.

```bash
python life.py -seed diehard --seed-position 20,20
```

### Size and position

By default, the size of the universe is 100x100. This is quite big relative to the size of most of the seeds, but is useful because many seeds in Life produce quite expansive results. But say you want a nice picture of the beacon, which we know is roughly the shape of a 4x4 square. We therefore probably want a 6x6 universe, with the top-left of the seed pegged at coordinates (1,1), because indexing starts from 0 in python.

```bash
python life.py -seed beacon --universe-size 6,6  --seed-position 1,1
```

<p align="center">
    <img width=50% src="https://github.com/robertmartin8/PyGameofLife/blob/master/media/beacon.gif">
</p>

As seen above, if you want to change the size of size of the grid, you **must** also specify the coordinates of the seed, otherwise you will probably get a nasty error.

### Colours

Colours are amended with the `-cmap` flag. A list of all possible colourmaps can be found in the
[matplotlib documentation](https://matplotlib.org/examples/color/colormaps_reference.html). Note,
however, that you will only get the colours at each end of the spectrum, because the cells in
Life are either dead (0) or alive (1). Colourmaps can be reversed by appending `_r` to the name of the original colourmap. Please note that the cmap names are case sensitive.

```bash
python life.py -seed beacon -cmap plasma_r --universe-size 6,6  --seed-position 1,1
```

<p align="center">
    <img width=50% src="https://github.com/robertmartin8/PyGameofLife/blob/master/media/beacon_plasma.gif">
</p>

### Animation paramaters

- The `-n` flag controls the number of iterations: the time taken to produce the animation grows linearly with the number of iterations.
- `-interval` is quite useful, and changes the rate at which Life iterates. In the simple example of the beacon, you could increase the flashing frequency by reducing the interval.
- Lastly, `-quality` dictates the image quality of the resulting animation. Be warned that higher DPI values greatly increase both the time taken to generate animations and the resulting fileszie.

## About

This is just a quick project to demonstrate the versatility of matplotlib's animation functions. PyGameofLife definitely doesn't present the most efficient solution, but the code is readable and intuitive (and arguably produces pretty output).

For a write-up explaining a little bit more about how the code works, check out the related [article](https://reasonabledeviations.com/2017/06/10/conway-python/) on my website.
