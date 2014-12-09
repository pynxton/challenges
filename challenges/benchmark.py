import time
import importlib
import pandas as pd
from numpy import mean, std

class Benchmark(object):

    def __init__(self, classname='DNAReverseComplement', replicates=1):

        self.scripts = []
        self.times = []
        self.classname = classname
        self.replicates = replicates

    def add_script(self, script):
        for i in range(0, self.replicates):
            self.scripts.append(script)

    def run(self):
        N = len(self.scripts)
        for i, script in enumerate(self.scripts):
            print("Running %s %s/%s" % (script, i+1, N))
            t1 = time.time()
            import importlib
            my_module = importlib.import_module(script)
            d = getattr(my_module, self.classname)()
            d.run()
            t2 = time.time()
            self.times.append(t2-t1)

    def ranking(self):
        """Simple boxplot of the time taken for each script (if replicates)"""
        df = pd.DataFrame({'times':self.times, 'names': self.scripts}) 
        g = df.groupby('names')
        ranking =  g.aggregate([mean, std])
        g.boxplot()
        return ranking
