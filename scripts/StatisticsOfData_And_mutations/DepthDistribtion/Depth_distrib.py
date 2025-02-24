#!/usr/local/bin/python
# -*- coding: utf-8 -*-  
import os,sys,linecache,time
import numpy as np
from optparse import OptionParser
import Depth_distrib_modules  as CoverageMs


#This script is used to count the sequencing depth distribution of all samples at all loci..
################################################################################################################################
#
# For help as a standalone program type: python  Coverage_distrib.py   -h
#
# Examples:
#	python Coverage_distrib.py  -i  ../../../data/depthFiles/   -o  ../../result/allsamps.depth.txt
#	#parameters:
#		-i  input path,Sequencing depth statistics files generated by the “samtools depth” program.
#		-o  output file，output file for depth information of all samples that can be used to visualize the result by r script .
#
#	
################################################################################################################################


def main():
################################################################################################################################
# Parameters
################################################################################################################################
	usage = "usage:python  %prog [option]"
	parser = OptionParser(usage=usage)

	parser.add_option("-i","--inputpath",
	                  dest = "inputpath",
	                  default = "",
	                  metavar = "path",
	                  help = "Path to depth files generated from 'samtools depth' commond for all samples.  [required]")

	parser.add_option("-o","--outputfile",
	                  dest = "outputfile",
	                  default = "",
	                  metavar = "file",
	                  help = "Outfile path and name [required]")
	(options,args) = parser.parse_args()
	depthpath       = os.path.abspath(options.inputpath)
	outDepthStatF = os.path.abspath(options.outputfile)
	print 
	print "input path :  " + depthpath
	print "output file   : " + outDepthStatF
	if (os.path.exists(outDepthStatF)):
		os.remove(outDepthStatF)

	startTime = time.time()
	filenameLst = CoverageMs.fileLst(depthpath)

	out = CoverageMs.depStat(filenameLst)
	Head = CoverageMs.outHead()
	defFO = open(outDepthStatF,'a')
	defFO.write(Head + "\n")
	defFO.write(out + "\n")
	defFO.close()
	
	endTime = time.time()
	print "Total samples: " + str(len(filenameLst))
	sys.stdout.write("Total time taken: "+str(endTime-startTime)+" seconds\n")



if __name__ == "__main__":

	main()


