"""author: TC, 2014 

"""
import sys
import string

class DNAReverseComplement(object):
    def __init__(self):
        self.mode = 'normal'  # could be stdin
        #self.sequence = sequence 
        #self.table = bytes.maketrans(b'ACBDGHKMNSRUTWVYacbdghkmnsrutwvy',
        #                            b'TGVHCDMKNSYAAWBRTGVHCDMKNSYAAWBR'),
        # python 3
        #   self.table = bytes.maketrans(b'ACGTacgt', b'TGCAtgca'),
        self.table = string.maketrans('ACGTacgt', 'TGCAtgca'),

    #def _read(self, filename="Homo_sapiens.GRCh38.dna.chromosome.10.fa"):
    #    fh = open(filename, 'r')
    #    return fh

    def show(self, seq):
        # py3 write = sys.stdout.buffer.write
        # somehow self.table does not work !!!
        # different in py3 !!
        table = string.maketrans('ACGTacgt\n', 'TGCAtgca\n')

        if self.mode == 'stdin':
            write = sys.stdout.write
            nl = '\n'
            [header, s] = seq.split(nl, 1)
            s = s.translate(table)[::-1]
            write(b'>' + header) # write create the \n automatically
            for i in range(0, len(s), 60):
                write(s[i:i+60])
        else:
            nl = '\n'
            [header, s] = seq.split(nl, 1)
            
            return ">"+ header +"\n" + s.translate(table)[::-1]
        print

    def run(self, filename="Homo_sapiens.GRCh38.dna.chromosome.10.fa", output='out.fa'):
        # python 3 sys.stdin = sys.stdin.detach()
        # split the file into sequences (separated by lines starting with >)
        if self.mode == 'stdin':
            seqs = b''.join([line for line in sys.stdin]).split(b'>')[1:]
            for seq in seqs:
                self.show(seq)
        else:
            fh = open(filename, "r")
            seqs = fh.readlines()
            seqs = "".join([line for line in seqs]).split(">")[1:]
            fh.close()
            fh = open(output, 'w')
            for seq in seqs:
                fh.write(self.show(seq))
            fh.close()



if __name__ == "__main__":
    d = DNAReverseComplement()
    #d.mode = 'other'
    d.run()
