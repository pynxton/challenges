#November 2014
#alistair.macdougall@ebi.ac.uk
#Input: DNA sequence in fasta format
#Output: Reverse complement of input file in fasta format
#Example: python rcfasta.py input.fa output.fa

__author__ = 'alistair'
from time import time
import sys

#Make a new reverse complement kmer
#Store the value for in rcmap for future use 
#Then return the value
def newrc(kmer, n):
    global rcmap
    rclist = []
    for i in range(n-1, -1, -1):
        c = kmer[i]
        if c == 'A':
            rclist.append('T')
        elif c == 'T':
            rclist.append('A')
        elif c == 'G':
            rclist.append('C')
        elif c == 'C':
            rclist.append('G')
        elif c == 'N':
            rclist.append('N')
        else:
            print "Error: Unrecognised Nucleotide " + c
    rc = ''.join(rclist)    
    rcmap[kmer] = rc
    return rc

#Show the time since last update of t1
def showTimeInterval(t):
    global t1
    global rclines
    ti = t - t1 
    print str('Lines: {0}\tSecs: '.format(len(rclines)) + "{:.2f}".format(ti))
    #Reset t1
    t1 = t


#THE START OF THE SCRIPT    
#Get the input and output file names from command line arguments
infname = sys.argv[1]
outfname = sys.argv[2]

#Dictionary to store reverse complement kmers in
rcmap = {}
#List for temporary storage of reverse complement lines
rclines = []
#Length of substring to use for reverse complement kmers
k = 10

#Open the infile and get the length of the lines
f = open(infname, 'r')
header = f.readline().rstrip()  #store header line 
l = len(f.readline().rstrip())
f.close()

#Check if the default k value of 10 is suitable
#Calculate number of k length substrings in a line
n = l / k
#Issue warning and call for user input
#if k does not divide into l exactly
if l % k != 0:
    m = ("Line length is {0} and k is {1}.\n"
         "Choose a value for k that divides into line length.")
    print m.format(l, k)
    k = int(raw_input("k: ")) 

#time points for keeping time
t0 = t1 = time()

#Open the files 
inf = open(infname, 'r')
outf = open(outfname, 'w')

#Counter for lines read
count = 0
stopcount = 5   #for testing

#Process the lines in input file
#The '\n' at the end of each line can be ignored
for line in inf:
    count += 1
    #Skip the header line
    if count == 1: continue
    #if count == stopcount: break   #for testing
    #The last line may be short, so check for this
    if len(line) < l + 1:
        s = line.rstrip()
        rcs = newrc(s, len(s))
        rclines.append(rcs)

    #Process regular lines
    else:
        dslist = []
        #split line into n blocks of k bases 
        #working from right to left
        for i in range(l - k, -1, -k):
            ds = line[i:i + k]
            #look to see if this rc has already been calculated
            if rcmap.has_key(ds):
                dslist.append(rcmap.get(ds))
            #calculate a new rc if we don't have it already
            else:
                dslist.append(newrc(ds, k))
        
        #Make string from list rather than by adding bit by bit
        os = ''.join(dslist)
        rclines.append(os)

    #Record progress
    if len(rclines) % 100000 == 0:
        showTimeInterval(time())

#Now write the output to file
#Write the header line 
outf.write(header + ' reverse complement\n')
#Check the length of the last line (may be short)
j = len(rclines[-1])
#Length of previous line that is needed to make up a whole line
c = l - j
#Create the first output line from the last two lines of rclines
rcs = rclines[-1] + rclines[-2][:c]
outf.write(rcs + '\n')

#Write output lines from rclines working backwards
for i in range(len(rclines) -2, 0, -1):
    #Takes from index c to end and adds from start to one before c
    rcs = rclines[i][c:] + rclines[i-1][:c]
    outf.write(rcs + '\n')
#Add the last piece from the first line
outf.write(rclines[0][c:] + '\n')

inf.close()
outf.close()

#Show total time taken
t = time() - t0
print "Time elapsed: " +  "{:.2f}".format(t) + " Seconds."
#Show number of stored reverse complement kmers
print "Reverse Complement kmers stored: " + str(len(rcmap))

