from statistics import mean
import matplotlib.pyplot as plt
import argparse
import collections
import numpy as np


def plot_line_plot(lines, subset=False):
    """Create line plot and display results for each tool"""

    # for each line
    for line, coords in lines.items():
        # initialise lists
        x_vals = []
        y_vals = []
      
        # for each coord
        for x, y in sorted(coords):
            # if subset then stop early
            if x > 100000 and subset:
                break
            # add xand y values to lists
            x_vals.append(x)
            y_vals.append(y)

        # plot line
        plt.plot(x_vals, y_vals, label=line)

    # plot x and y on a log scale
    plt.xscale("log")
    plt.yscale("log")

    # add labels
    plt.xlabel("Size of ontology (number of classes)")
    plt.ylabel("Average time taken (seconds)")

    # add title
    plt.title("Line plot comparing owl manipulation tools")
        
    # show legend
    plt.legend()
        
    # save plot
    plt.savefig("plot.png")


def plot_box_plots(data):
    """Create box plots and display results for each tool"""

    # parse data
    boxes = {}
    for ((tool, size), time) in sorted(data.items()):
        boxes[size] = boxes.get(size, []) + [( tool, time )]

    # create n subplots
    fig1, ax1 = plt.subplots(1, len(boxes))

    # initialise index
    i = 0

    # for each size
    for size, d in boxes.items():
        # get labels and points
        labels = []
        points = []
        for tool, times in d:
            labels = labels + [tool]
            points = points + [times]

        # create box plots
        ax1[i].boxplot(points)

        # set title of subplot
        ax1[i].set_title(size)

        # set labels
        ax1[i].set_xticklabels(labels, rotation=45)

        # increment index
        i = i + 1

    # add title
    plt.suptitle("Box plots showing the outliers for each size and tool")

    # save plot
    plt.savefig("boxplots.png")


if __name__ == "__main__":
    """Main method"""

    # parser for optional argument subset
    parser = argparse.ArgumentParser(description='Plot line plot.')
    parser.add_argument('--subset', action="store_true",
                        help='create a plot of 10^1 to 10^4')
    parser.add_argument('--boxplots', action="store_true",
                        help='create boxplots')
    args = parser.parse_args()

    # read in file
    f = open("times.csv", "r")
    lines = f.readlines()
    f.close()

    # parse data
    data = {}
    # for each line
    for line in lines:
        # split line
        tool, size, time = line.strip().split(",")
        # extract size
        size = int(size[1:-4])
        # extract time
        time = float(time[:-8])
        # update dictionary
        data[(tool, size)] = data.get((tool, size), []) + [time]

    # plot box plots
    if args.boxplots:
        plot_box_plots(data)
    else:
        # calc average
        data = { key : mean(times) for (key, times) in sorted(data.items()) }
        # print(data)

        # parse data
        lines = {}
        for ((tool, size), time) in data.items():
            lines[tool] = lines.get(tool, []) + [( size, time )]

        # plot line plot
        plot_line_plot(lines, args.subset)
