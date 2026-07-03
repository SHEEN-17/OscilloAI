import matplotlib.pyplot as plt

from waveform import *

from oscilloscope import *

fig, ax = create_scope()

t, y = generate_sine(
    5,
    5,
    1,
    1000
)

ax.plot(
    t,
    y,
    color="lime",
    linewidth=2
)

plt.show()