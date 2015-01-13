"""author: TC, 2014 

"""
import sys
import string

class DNAReverseComplement(object):
    def __init__(self):
        self.mode = 'normal'  # could be stdin


    def run(self, filename="Homo_sapiens.GRCh38.dna.chromosome.10.fa", output='out.fa'):
        # python 3 sys.stdin = sys.stdin.detach()
        # split the file into sequences (separated by lines starting with >)
        fh = open(filename, "r")
        seqs = fh.readlines()
        seqs = "".join([line for line in seqs]).split(">")[1:]
        seqs = seqs[0]
        fh.close()

        from Bio.Seq import Seq
        from Bio.Alphabet import IUPAC
        from Bio.SeqUtils import GC
        seq1 = Seq(seqs, IUPAC.unambiguous_dna)
        rev = seq1.reverse_complement()
        with open(output, 'w') as fh:
            fh.write(rev.tostring())




if __name__ == "__main__":
    d = DNAReverseComplement()
    #d.mode = 'other'
    d.run()
