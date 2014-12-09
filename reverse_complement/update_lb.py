__author__ = "Thomas Cokelaer"
# need to get the chromosone fasta file from 
# https://github.com/pynxton/challenges/tree/master/reverse_complement 

from benchmark import Benchmark
from pylab import savefig

b = Benchmark(replicates=2)
b.add_script('maketrans')
b.run()
b.ranking()
savefig("lb.png")
