import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

universe = np.zeros((6, 6))

beacon = [[1, 1, 0, 0],
          [1, 1, 0, 0],
          [0, 0, 1, 1],
          [0, 0, 1, 1]]

universe[1:5, 1:5] = beacon

plt.figure()
plt.imshow(universe, cmap='binary')
plt.show()

# Create an identical copy of the universe, which will be the next generation.
new_universe = np.copy(universe)


def survival(x, y):
    """
    :param x: x coordinate of the cell
    :param y: y coordinate of the cell
    """
    # Find the number of living neighbours by taking the sum of the 8 surrounding grid squares
    num_neighbours = np.sum(universe[x - 1:x + 2, y - 1:y + 2]) - universe[x, y]

    # If the cell is alive
    if universe[x, y] == 1:
        if num_neighbours < 2 or num_neighbours > 3:
            new_universe[x, y] = 0
    # Otherwise, the cell is dead...
    elif universe[x, y] == 0:
        # ... but it will rise again if there are three living neighbours
        if num_neighbours == 3:
            new_universe[x, y] = 1


def generation():
    # We are inside a function, so we must specify that we are referring to the global variable 'universe'.
    # Otherwise python will think that we are trying to create a new variable also called 'universe'.
    global universe

    # Simple loop over every possible xy coordinate.
    for i in range(universe.shape[0]):
        for j in range(universe.shape[1]):
            survival(i, j)

    # Set universe to be equal to new_universe.
    universe = np.copy(new_universe)

# Animation
fig = plt.figure()

# Remove the axes for aesthetics
plt.axis('off')
ims = []

for i in range(30):
    # Add a snapshot of the universe, then move to the next generation.
    ims.append((plt.imshow(universe, cmap='Purples'),))
    generation()

# Create the animation
im_ani = animation.ArtistAnimation(fig, ims, interval=700, repeat_delay=1000,
                                   blit=True)

# Optional to save the animation
im_ani.save('beacon.mp4', writer=animation.FFMpegWriter())
