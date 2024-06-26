from statistics import mean
import matplotlib.pyplot as plt
import collections
import numpy as np


# https://matplotlib.org/stable/gallery/lines_bars_and_markers/barchart.html
# https://matplotlib.org/stable/gallery/misc/table_demo.html#sphx-glr-gallery-misc-table-demo-py
if __name__ == "__main__":
    """Main method"""

    # read in file
    f = open("times.csv", "r")
    lines = f.readlines()
    f.close()

    # parse data
    data = {}
    # for each line
    for line in lines:
        # split line
        tool, ont, time = line.strip().split(",")
        # convert to int
        time = int(time)
        # update dictionary
        data[(tool, ont)] = data.get((tool, ont), []) + [time]
    print(data)

    # calc average
    data = { key : int(round(mean(times), 0)) for (key, times) in data.items() }
    print(data)

    # parse data
    tools = set([ tool for (tool, _) in data.keys() ])
    tools = sorted(list(tools))
    print(tools)

    # onts = set([ ont for (_, ont) in data.keys() ])
    # onts = sorted(list(onts))
    onts = ["bfo.owl", "bfo.owx", "go.owl", "go.owx", "chebi.owl", "chebi.owx"]
    print(onts)

    bars = {}
    for tool in tools:
        for ont in onts:
            bars[tool] = bars.get(tool, []) + [data.get((tool, ont))]
    print(bars)

    x = np.arange(len(onts))  # the label locations
    width = 0.25  # the width of the bars
    multiplier = 0

    fig, ax = plt.subplots(layout='constrained')

    cell_text = []
    for tool, averages in bars.items():
        offset = width * multiplier
        rects = ax.bar(x + offset, averages, width, label=tool)
        # TODO -> UC
        # ax.bar_label(rects, padding=3, rotation=45)
        multiplier += 1
        # TODO -> C
        cell_text.append(averages)

    # TODO -> C
    colors = ["tab:blue", "orange", "green"]

    # TODO -> C
    # Add a table at the bottom of the Axes
    the_table = plt.table(cellText=cell_text,
                          rowLabels=tools,
                          rowColours=colors,
                          colLabels=onts,
                          loc='bottom')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Minimum memory required (MB)')
    # TODO -> UC
    # ax.set_xlabel('Ontology version used')
    ax.set_title('Bar plot comparing owl manipulation tools (memory)')
    # TODO -> UC
    # ax.set_xticks(x + width, onts, rotation=45)
    # TODO -> C
    ax.set_xticks([])
    # TODO -> UC
    # ax.legend(loc='upper left')
    ax.set_ylim(0, 9000)

    # savefig
    plt.savefig("memory.png")
