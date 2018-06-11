<p align="center">
    <img width=50% src="https://github.com/robertmartin8/PyGameofLife/blob/master/media/beacon.gif">
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

PyGameofLife is a simple implementation of Conway’s Game of Life in python, with an emphasis on a simple interface and intuitive code. I have recently added a command-line interface,
making it easy to generate high-quality gifs:

```bash
python life.py -seed r_pentomino -n 500 -interval 50


```

<p align="center">
    <img width=50% src="https://github.com/robertmartin8/PyGameofLife/blob/master/media/beacon.gif">
</p>


<center>
<img src="/rpentomino.gif" style="width:400px;"/>
</center>

## Getting started

Because this is just a small educational script, I have chosen not to distribute it on PyPI. To get started with it, clone/download
it, unzip it, then move the file somewhere convenient (either the desktop or your home directory).

Then, open up an instance of the command line / terminal, and `cd` to the correct directory. For example:

```bash
cd Users/your_username/PyGameofLife-master
```

Now that you are in the same directory, you should first install the requirements (if they aren't already on your system):

```
pip install -r requirements.txt
```

Then you can interface with it via the command line.

Example usage:

```bash
python life.py -seed beacon -interval 100
```


## User guide

If at any time you need a quick reference, just ask for help:

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
                        size of universe
  -seed SEED            seed for Life, see readme for list
  -n N                  number of universe iterations
  -quality QUALITY      image quality in DPI
  -cmap CMAP            colour scheme
  -interval INTERVAL    interval (in milliseconds) between iterations
  --seed-position SEED_POSITION
                        comma-separated coordinates of seed
```


### Size

If you want to change the size of size of the grid, you **must** also specify the starting coordinates
of the seed.


### Colours

Colours are amended with the `-cmap` flag. A list of all possible colourmaps can be found in the
[matplotlib documentation](https://matplotlib.org/examples/color/colormaps_reference.html). Note,
however, that you will only get the colours at each end of the spectrum, because in the cells in
Life are either dead (0) or alive (1).

Please note that the cmap names are case sensitive.

```bash

```

Command line interface

## Available seeds

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
