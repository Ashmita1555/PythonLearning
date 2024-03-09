#This module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter. It is always available.
import sys
if len(sys.argv)<2:#sys.argu is the list of command line arguments passed to a Python script.argv[0]is the script name 
    sys.exit("Too few arguments")
for arg in sys.argv[1:]:#slice off the first element of the list as its filename(scriptname)
 print("Hello!! My name is", arg)
