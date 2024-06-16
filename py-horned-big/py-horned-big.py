import argparse
import pyhornedowl
from pyhornedowl.model import *


# https://stackoverflow.com/questions/14117415/how-can-i-constrain-a-value-parsed-with-argparse-for-example-restrict-an-integ
def check_positive(value):
    ivalue = int(value)
    if ivalue <= 0:
        raise argparse.ArgumentTypeError("%s is an invalid positive int value" % value)
    return ivalue
    

if __name__ == "__main__":
    """Main method"""

    # parser for optional argument subset
    parser = argparse.ArgumentParser(description='Create a new ontology with n classes.')
    parser.add_argument('n', type=check_positive, help='n should be a positive value')
    args = parser.parse_args()
    
    # create an ontology
    o = pyhornedowl.PyIndexedOntology()

    # create classes
    for i in range(1, args.n+1):
            
        # create class
        clazz = Class(IRI.parse("https://www.example.com/o" + str(i)))
        # create declaration axiom
        da = DeclareClass(clazz)
        # add to ontology
        o.add_component(da);

    # TODO should save to stdout rather file
    o.save_to_file("temp.owx", serialization = "owx")

