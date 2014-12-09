"""author: TC, 2014 

"""
import sys
import string

class DNAReverseComplement(object):
    def __init__(self, sequence=None):
        #self.sequence = sequence 
        #self.table = bytes.maketrans(b'ACBDGHKMNSRUTWVYacbdghkmnsrutwvy',
        #                            b'TGVHCDMKNSYAAWBRTGVHCDMKNSYAAWBR'),
        try:
            self.table = bytes.maketrans(b'ACGTacgt', b'TGCAtgca'),
        except:
            self.table = string.maketrans(b'ACGTacgt', b'TGCAtgca'),


    #def _read(self, filename="Homo_sapiens.GRCh38.dna.chromosome.10.fa"):
    #    fh = open(filename, 'r')
    #    return fh

    def show(self, seq):
        # py3 write = sys.stdout.buffer.write
        write = sys.stdout.write

        nl = '\n'

        [header, s] = seq.split(nl, 1)
        try:
            s = s.translate(self.table, nl)[::-1]
        except:
            print("eeorr")

        write(b'>' + header + nl)
        for i in range(0, len(s), 60):
            write(s[i:i+60] + nl)

    def run(self):
        # python 3 sys.stdin = sys.stdin.detach()

        seqs = b''.join([line for line in sys.stdin]).split(b'>')[1:]
        for seq in seqs:
            self.show(seq)


if __name__ == "__main__":
    d = DNAReverseComplement()
    d.run()
