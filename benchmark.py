import time
import importlib
import pandas as pd

class Benchmark(object):

    def __init__(self, classname='DNAReverseComplement'):

        self.scripts = []
        self.times = []
        self.classname = classname

    def add_script(self, script):
        self.scripts.appen(script):

    def run(self):
        for script in scripts:
            t1 = time.time()
            import importlib
            my_module = importlib.import_module(script)
            d = getattr(my_module, self.classname)()
            d.run()
            t2 = time.time()
            self.times.append(t2-t1)

   def ranking(self):
       # TODO 
       # use pandas to get ranking of times/scripts
       # provide dataframe ranked 




       # plot()
       pass
