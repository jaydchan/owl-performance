from statistics import mean
import matplotlib.pyplot as plt


def plot_line_plot(lines):
    """Create line plot and display results for each tool"""
 
    # for each line
    for line, coords in lines.items():
        # initialise lists
        x_vals = []
        y_vals = []
      
        # for each coord
        for x, y in sorted(coords):
            x_vals.append(x)
            y_vals.append(y)

        # plot line
        plt.plot(x_vals, y_vals, label=line)

    # plot x on a log scale
    plt.xscale("log")
        
    # show legend
    plt.legend()
        
    # display plot
    plt.show()
            

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
    plot_line_plot(lines)

