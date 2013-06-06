#!/usr/bin/env python
####File Splitter
# splits a single python file in to several python files 
# for a file in the form:
# ###Hello, World!###
# print "Hello, World!"
# ##
# ###Goodbye to the world Types###
# ...
# code
# ...
# ##
# ###Next Code Segment###
# ...
####

import os, re, sys

# replace all function to help with the clean up
def replace_all(text, dic):
    for i, j in dic.iteritems():
        text = text.replace(i, j)
    return text


def filecreator(a,b):
  symbols = {",":".","!":"", " ":"","\n":""}
  filename = "%s.py" % replace_all(a,symbols)
  writefile = open(writelocation + filename, 'w')
  print("Filename: %s " % filename)
  writefile.write(b)
  print("File contents: \n%s" % b)

# current directory
currDir = os.path()

# read in file

origfile = open("pythontidbits.txt")
writelocation  = "\\output\\"
# read in contents
origcontents = origfile.read()

# setup re so it can easily split the lists into file then file names from the files
myre = re.compile("\n##\n")
filenamere = re.compile("###\n")

# split the file original files into lists based on
# ##\n which is the indicator of end of a file
origFileList = myre.split(origcontents)
filesChomped = [ origFile.replace("###","",1) for origFile in origFileList]

# a list of lists ...
# this has a list of [ file name, file contents] lists
files = [ filenamere.split(indvfile) for indvfile in filesChomped]

# use a list comprehension to iterate through the list of files and create the files
[filecreator(x[0],x[1]) for x in files]
