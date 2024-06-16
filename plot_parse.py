from statistics import mean
import matplotlib.pyplot as plt
import collections
import numpy as np


# https://matplotlib.org/stable/gallery/lines_bars_and_markers/barchart.html
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
        # extract time
        time = float(time[:-8])
        # update dictionary
        data[(tool, ont)] = data.get((tool, ont), []) + [time]
    # print(data)

    # calc average
    data = { key : round(mean(times), 1) for (key, times) in data.items() }
    # print(data)

    # parse data
    tools = set([ tool for (tool, _) in data.keys() ])
    tools = sorted(list(tools))
    # print(tools)

    onts = set([ ont for (_, ont) in data.keys() ])
    onts = sorted(list(onts))
    # print(onts)

    bars = {}
    for tool in tools:
        for ont in onts:
            bars[tool] = bars.get(tool, []) + [data.get((tool, ont))]
    # print(bars)    

    x = np.arange(len(onts))  # the label locations
    width = 0.25  # the width of the bars
    multiplier = 0

    fig, ax = plt.subplots(layout='constrained')

    for attribute, measurement in bars.items():
        offset = width * multiplier
        rects = ax.bar(x + offset, measurement, width, label=attribute)
        ax.bar_label(rects, padding=3)
        multiplier += 1

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Average time taken (seconds)')
    ax.set_xlabel('Ontology version used')
    ax.set_title('Bar plot comparing owl manipulation tools')
    ax.set_xticks(x + width, onts)
    ax.legend(loc='upper left', ncols=3)
    ax.set_ylim(0, 250)

    # savefig
    plt.savefig("barchart.png")
