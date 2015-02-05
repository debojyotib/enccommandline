# enccommandline
author = dbhat

A simple command line file encryption program in python. Uses pynacl as underlying crypto library.

This uses PyNaCl (https://github.com/pyca/pynacl) as underlying crypto library. Both pynacl and libsdium need to be installed on the system before trying out this program.
The program has been tested using python 2.7+.

Uses pynacl (in turn libsdium) as underlying crypto library. 

Usage: "python filecrypt.py -f <enc/dec> -i <input filename> -o <output filename> -k <key>
