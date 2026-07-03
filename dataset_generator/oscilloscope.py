import matplotlib.pyplot as plt


def create_scope():

    fig = plt.figure(figsize=(10,5))

    ax = plt.gca()

    ax.set_facecolor("black")

    plt.grid(
        color="#00AA00",
        linestyle="--",
        linewidth=0.5
    )

    plt.xlim(0,1)

    plt.ylim(-6,6)

    return fig, ax
def save_scope(filename):

    plt.savefig(
        filename,
        dpi=150,
        bbox_inches="tight"
    )

    plt.close()