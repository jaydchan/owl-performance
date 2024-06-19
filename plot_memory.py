from statistics import mean
import matplotlib.pyplot as plt
import matplotlib as mpl
import collections
import numpy as np


# https://matplotlib.org/stable/gallery/images_contours_and_fields/image_annotated_heatmap.html
if __name__ == "__main__":
    """Main method"""

    # read in file
    # f = open("times.csv", "r")
    # lines = f.readlines()
    # f.close()

    # data
    data = {
            # smallest for bfo.owl is 2M, killed on 1M
            # max needed for ncbi.taxon is ???
            "horned-parse" :
            [[1, 1, 1], [1, 0, 0], [1, 0, 0], [0, 0, 0]],
            # bfo.owl 50M only runs if you remove the initial heapsize of 1G
            # smallest for bfo.owl is 44M, killed on 43M
            "owl-api-parse" :
            [[1, 1, 1], [1, 0, 0], [1, 0, 0], [0, 0, 0]],
            # smallest for bfo.owl is 8M, killed on 7M
            "py-horned-parse" :
            [[1, 1, 1], [1, 0, 0], [1, 0, 0], [0, 0, 0]]}
    ontologies = ["bfo.owl", "go.owl", "chebi.owl", "ncbitaxon.owl"]
    memory = ["5000M", "500M", "50M"]

    fig, all_ax = plt.subplots(1, 3)

    i = 0
    for tool, results in data.items():
        # fig, ax = plt.subplots()
        ax = all_ax[i]
        results = np.array(results)

        # https://stackoverflow.com/questions/28517400/matplotlib-binary-heat-plot
        # define the colors
        cmap = mpl.colors.ListedColormap(['r', 'g'])
        
        im = ax.imshow(results, cmap=cmap)

        # Show all ticks and label them with the respective list entries
        ax.set_xticks(np.arange(len(memory)), labels=memory)
        if i == 0:
            ax.set_yticks(np.arange(len(ontologies)), labels=ontologies)
        else:
            ax.set_yticks([])

        # Rotate the tick labels and set their alignment.
        plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
                 rotation_mode="anchor")

        ax.set_title(tool)
        # fig.tight_layout()

        i = i + 1

    fig.suptitle("Results of limiting the memory")
    fig.set_tight_layout(True)
    
    # savefig
    plt.savefig("heatmap.png")
