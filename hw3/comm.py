#!/usr/bin/python

import random, sys, locale
from optparse import OptionParser

def main():
    version_msg= "%prog 2.0"
    usage_msg= """$prog [option]... FILE1 FILE2

Compare two files and show different and common lines in them.
Files must be non-empty.

OPTIONS:
    -u: unsorted files entered
    -1: do not show lines only in file1
    -2: do not show lines only in file2
    -3: do not show lines in both file1 and file2
"""
    parser = OptionParser(version=version_msg, usage=usage_msg)
    
    parser.add_option("-u", "--unsorted", 
                      action="store_true", dest="unsorted", default=False, 
                      help="with unsorted files input")
    parser.add_option("-1", "--nofile1",
		      action="store_true", dest="nofile1", default=False,
		      help="result without lines only in file1")
    parser.add_option("-2", "--nofile2",
		      action="store_true", dest="nofile2", default=False,
		      help="result without lines only in file2")
    parser.add_option("-3", "--nocommon",
		      action="store_true", dest="nocommon", default=False,
		      help="result without lines in both files")

    options, args  = parser.parse_args(sys.argv[1:])
    locale.setlocale(locale.LC_ALL, '')

    unsorted = bool(options.unsorted)
    nofile1 = bool(options.nofile1)
    nofile2 = bool(options.nofile2)
    nocommon = bool(options.nocommon)
    
    #there should be two inputs
    if len(args) != 2:
        parser.error("Error: wrong number of operands")

    if args[0] == "-":
        myFile2=open(args[1], 'r')
        lines2=myFile2.readlines()
        myFile2.close()
        lines1=sys.stdin.readlines()
    elif args[1] == "-":
        myFile1=open(args[0], 'r')
        lines1=myFile1.readlines()
        myFile1.close()
        lines2=sys.stdin.readlines()
    else:
        myFile1=open(args[0], 'r')
        myFile2=open(args[1], 'r')
        lines1=myFile1.readlines()
        lines2=myFile2.readlines()
        myFile1.close()
        myFile2.close()

    list1=[]
    list2=[]
    list3=[]
    outputlist=[]

    if not unsorted:
        lines1=set(lines1)
        lines2=set(lines2)
        #using exist functions to  get output lines in three columns
        list1=lines1.difference(lines2)
        list2=lines2.difference(lines1)
        list3=set.intersection(lines1,lines2)

    if unsorted:
        order1=lines1
        lines1=list(set(lines1))
        lines1.sort(key=order1.index)
        order2=lines2
        lines2=list(set(lines2))
        lines2.sort(key=order2.index)
        for i in lines1:
            test1=True
            for j in lines2:
                if i==j:
                    list3.append(i)
                    test1=False
                    break
            if test1==True:
                list1.append(i)
        for i in lines2:
            test2=True
            for j in lines1:
                if i==j:
                    test2=False
                    break
            if test2==True:
                list2.append(i)

        #according to different options, insert tuples with two elements into outputlist
    if( nofile1 & nofile2 & nocommon ):
        sys.stdout.write("")
    elif( nofile1 & nofile2 ):
        for item in list3:
             outputlist.append((0,item))
    elif( nofile1 & nocommon ):
        for item in list2:
             outputilst.append((0,item))
    elif( nofile2 & nocommon ):
        for item in list1:
             outputlist.append((0,item))
    elif( nofile1 ):
        for item in list3:
            outputlist.append((1,item))
        for item in list2:
            outputlist.append((0,item))
    elif( nofile2 ):
        for item in list1:
            outputlist.append((0,item))
        for item in list3:
            outputlist.append((1,item))
    elif( nocommon ):
        for item in list1:
            outputlist.append((0,item)) 
        for item in list2:
            outputlist.append((1,item))
    else:
        for item in list1:
            outputlist.append((0,item))
        for item in list3:
            outputlist.append((2,item))
        for item in list2:
            outputlist.append((1,item))

     #if inputs are sorted, print sorted lines; if inputs are unsorted, print unsorted lines
     #but if inputs are unsorted, the result can only be print column by column
    if not unsorted:
        outputlist=sorted(outputlist, key=lambda item:item[1], reverse=False)
        for item in outputlist:
            sys.stdout.write('\t'*item[0])
            sys.stdout.write(item[1])

    if unsorted:
        for item in outputlist:
            sys.stdout.write('\t'*item[0])
            sys.stdout.write(item[1])

if __name__ == "__main__":
    main()
