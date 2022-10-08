from mrjob.job import MRJob   # MRJob version

class Efficientitems(MRJob):  #MRJob version
    def mapper(self, key, line):
        parts = line.split("\t")
        stock_code = float(parts[0])
        amount = float(parts[3])
        numcountries = parts[5]
	mostpopular = parts[7]
        yield (stock_code, amount, numcountries, mostpopular)

    def reducer(self, key, values):
        yield (key, values)

if __name__ == '__main__':
    Efficientitems.run()
