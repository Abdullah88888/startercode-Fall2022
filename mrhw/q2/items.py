
from mrjob.job import MRJob   # MRJob version

class items(MRJob):  #MRJob version
    def mapper(self, key, line):
        parts = line.split("\t")
	try:
            amount = float(parts[3])
            numcountries = float(parts[5])
            mostpopular = parts[7]
        except:
	    yield(parts[0],"|".join(parts))
	    
    def reducer(self, key, values):
        yield (key, "!".join(values))

if __name__ == '__main__':
    items.run()
