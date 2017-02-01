#!/usr/bin/python

__author__ = "Your Name"
__copyright__ = "Copyright 2016"
__credits__ = ["Your Name"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Your Name"
__email__ = "firstname.lastname@yale.edu"

### Usage:      python hw2.py -i <input file> -s <score file>
### Example:    python hw2.py -i input.txt -s blosum62.txt
### Note:       Smith-Waterman Algorithm

### Scripting must be done from scratch, without the use of any pre-existing packages.
### Python standard library and numpy are allowed.
import argparse

### This is one way to read in arguments in Python. We need to read input file and score file.
parser = argparse.ArgumentParser(description='Smith-Waterman Algorithm')
parser.add_argument('-i', '--input', help='input file', required=True)
parser.add_argument('-s', '--score', help='score file', required=True)
args = parser.parse_args()

### Implement your Smith-Waterman Algorithm
def runSW(inputFile, scoreFile):
	### Print input and score file names. You can comment these out.
	print ("input file : %s" % inputFile)
	print ("score file : %s" % scoreFile)

### Run your Smith-Waterman Algorithm
runSW(args.input, args.score)
