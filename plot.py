from statistics import mean
import matplotlib.pyplot as plt
import argparse


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
            

if __name__ == "__main__":
    """Main method"""

    # parser for optional argument subset
    parser = argparse.ArgumentParser(description='Plot line plot.')
    parser.add_argument('--subset', action="store_true",
                        help='create a plot of 10^1 to 10^4')
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

    # calc average
    data = { key : mean(times)  for (key, times) in data.items() }

    # parse data
    lines = {}
    for ((tool, size), time) in data.items():
        lines[tool] = lines.get(tool, []) + [( size, time )]

    # plot line plot
    plot_line_plot(lines, args.subset)

