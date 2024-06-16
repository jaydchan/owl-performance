import argparse
import pyhornedowl
from pyhornedowl.model import *
import os.path


# https://stackoverflow.com/questions/11540854/file-as-command-line-argument-for-argparse-error-message-if-argument-is-not-va
def is_valid_file(parser, arg):
    print(arg)
    if not os.path.exists(arg):
        parser.error("The file %s does not exist!" % arg)
    else:
        return arg
    

if __name__ == "__main__":
    """Main method"""

    # parser for argument subset
    parser = argparse.ArgumentParser(description='Read in a given ontology.')
    parser.add_argument('ont_path', type=lambda x: is_valid_file(parser, x), help='Path to ontology')
    args = parser.parse_args()

    # open ontology
    o = pyhornedowl.open_ontology(args.ont_path)

    # TODO should save to stdout rather file
    o.save_to_file("temp.owx", serialization = "owx")

