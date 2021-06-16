from statistics import mean
import matplotlib.pyplot as plt
import argparse
import numpy as np


def plot_line_plot(lines, subset=False):
    """Create line plot and display results for each tool"""
 
    # for each line
    for line, coords in sorted(lines.items()):
        # initialise lists
        x_vals = []
        y_vals = []
      
        # for each coord
        for x, y in sorted(coords):
            # if subset then stop early
            if x > 100000 and subset:
                break
            # add x and y values to lists
            x_vals.append(x)
            y_vals.append(y)

        # plot line
        plt.plot(x_vals, y_vals, label=line)

    # plot x on a log scale
    plt.xscale("log")

    # add labels
    plt.xlabel("Size of ontology (number of classes)")
    plt.ylabel("Average time taken (seconds)")

    # add title
    plt.title("Line plot comparing owl manipulation tools")

    # show legend
    plt.legend()
        
    # display plot
    plt.show()


def plot_bar_graph(bars):
    """Create bar plot and display results for each ontology and tool"""

    # Adapted from https://www.datasciencemadesimple.com/bar-plot-bar-chart-in-python-legend-using-matplotlib/
    # define pos and bar_width
    pos = np.arange(len(bars))
    bar_width = 0.3

    # initialise counter
    i = 0

    # for each tool
    for tool, times in sorted(bars.items()):

        # initialise list
        x_vals = []

        # for each ontology
        for ont, time in sorted(times):
            # add x value to list
            x_vals.append(time)

        # plot bars
        plt.bar(pos+(bar_width*i),x_vals,bar_width)

        # increment counter
        i=i+1

    # isolate ontologies for x ticks
    onts = [ont for (ont, time) in list(bars.values())[0]]
        
    # set x ticks
    mid = pos+((bar_width*(i-1))/2)
    plt.xticks(mid, onts)
        
    # add axis labels
    plt.xlabel("Ontology version used")
    plt.ylabel("Average time taken (seconds)")

    # add title
    plt.title("Bar plot comparing owl manipulation tools")

    # isolate tools for legend
    tools = sorted(bars.keys())

    # show legend
    plt.legend(tools,loc=2)

    # display plot
    plt.show()


def read_in_and_parse_data(fname, big=False):
    """Read a given csv file and generate equivalent dictionary"""

    # read in file
    f = open(fname, "r")
    lines = f.readlines()
    f.close()

    # parse data
    data = {}
    # for each line
    for line in lines:
        # split line
        tool, size, time = line.strip().split(",")
        if big:
            # extract size
            size = int(size[1:-4])
        # extract time
        time = float(time[:-8])
        # update dictionary
        data[(tool, size)] = data.get((tool, size), []) + [time]

    # return dictionary
    return data


if __name__ == "__main__":
    """Main method"""

    # parser for optional argument subset
    parser = argparse.ArgumentParser(description='Plot line plot.')
    parser.add_argument('--subset', action="store_true",
                        help='create a plot of 10^1 to 10^4')
    args = parser.parse_args()

    # timings for big
    # get data
    data = read_in_and_parse_data("times.csv", True)

    # calc average
    data = { key : mean(times)  for (key, times) in data.items() }

    # parse data (could be embedded in plot_line_plot?)
    lines = {}
    for ((tool, size), time) in data.items():
        lines[tool] = lines.get(tool, []) + [( size, time )]

    # plot line plot
    plot_line_plot(lines, args.subset)

    # timings for parse
    # get data
    data = read_in_and_parse_data("times_parse.csv")

    # calc average
    data = { key : mean(times)  for (key, times) in data.items() }

    # parse data (could be embedded in plot_line_plot?)
    bars = {}
    for ((tool, ont), time) in data.items():
        bars[tool] = bars.get(tool, []) + [(ont, time)]

    # plot bar graph
    plot_bar_graph(bars)
