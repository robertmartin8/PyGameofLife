import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


seeds = {'diehard': [[0, 0, 0, 0, 0, 0, 1, 0],
                     [1, 1, 0, 0, 0, 0, 0, 0],
                     [0, 1, 0, 0, 0, 1, 1, 1]],
         'boat': [[1, 1, 0],
                  [1, 0, 1],
                  [0, 1, 0]],
         'r_pentomino': [[0, 1, 1],
                         [1, 1, 0],
                         [0, 1, 0]],
         'pentadecathlon': [[1, 1, 1, 1, 1, 1, 1, 1],
                            [1, 0, 1, 1, 1, 1, 0, 1],
                            [1, 1, 1, 1, 1, 1, 1, 1]],
         'beacon': [[1, 1, 0, 0],
                    [1, 1, 0, 0],
                    [0, 0, 1, 1],
                    [0, 0, 1, 1]],
         'acorn': [[0, 1, 0, 0, 0, 0, 0],
                   [0, 0, 0, 1, 0, 0, 0],
                   [1, 1, 0, 0, 1, 1, 1]],
         'spaceship': [[0, 0, 1, 1, 0],
                       [1, 1, 0, 1, 1],
                       [1, 1, 1, 1, 0],
                       [0, 1, 1, 0, 0]],
         'block_switch_engine': [[0, 0, 0, 0, 0, 0, 1, 0],
                                 [0, 0, 0, 0, 1, 0, 1, 1],
                                 [0, 0, 0, 0, 1, 0, 1, 0],
                                 [0, 0, 0, 0, 1, 0, 0, 0],
                                 [0, 0, 1, 0, 0, 0, 0, 0],
                                 [1, 0, 1, 0, 0, 0, 0, 0]],
         'infinite': [[1, 1, 1, 0, 1],
                      [1, 0, 0, 0, 0],
                      [0, 0, 0, 1, 1],
                      [0, 1, 1, 0, 1],
                      [1, 0, 1, 0, 1]]}


def survival(x, y, universe):
    """
    :param x: x coordinate of cell
    :param y: y coordinate of cell
    """
    num_neighbours = np.sum(universe[x-1:x+2, y-1:y+2]) - universe[x, y]

    # The rules of Life
    if universe[x, y] and not 2 <= num_neighbours <= 3:
        return 0
    elif num_neighbours == 3:
        return 1

    return universe[x, y]


def generation(universe):

    new_universe = np.copy(universe)

    # Apply the survival function to every cell in the universe
    for i in range(universe.shape[0]):
        for j in range(universe.shape[1]):
            new_universe[i, j] = survival(i, j, universe)

    return new_universe


def animate_life(universe_size, seed, seed_position, n_generations=30, interval=300, save=False):
    # Initialise the universe and seed
    universe = np.zeros(universe_size)
    x_start, y_start = seed_position[0], seed_position[1]
    seed_array = np.array(seeds[seed])
    universe[x_start:x_start+seed_array.shape[0], y_start:y_start+seed_array.shape[1]] = seed_array

    # Animate
    fig = plt.figure()
    plt.axis('off')
    ims = []

    for i in range(n_generations):
        ims.append((plt.imshow(universe, cmap='Purples'),))
        universe = generation(universe)

    im_ani = animation.ArtistAnimation(fig, ims, interval=interval, repeat_delay=3000,
                                       blit=True)

    # Optional: save the animation, with a name based on the seed.
    if save:
        im_ani.save((str(seed) + '.mp4'), writer=animation.FFMpegWriter())


# Example usage
"""
animate_life(universe_size=(100, 100), seed='infinite', seed_position=(40, 40),
             n_generations=500, interval=50, save=True)
"""
