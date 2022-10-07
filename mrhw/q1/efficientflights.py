from mrjob.job import MRJob

class Flight(MRJob):
    
    def mapper(self,key,line):
	parts = line.split("\t")
	origin_airport = parts[0]
	destination_airport = parts[1}
	passengers = parts[2]
		
	key = origin_airport
	value = (passenegers, "arrive")
	yield(key, value)

	key = destination_airport
	value = (passenegers, "leave")
	yield(key, value)

    def reducer(self, key, values):
	yield (key, (x,y))

if __name__ == '__main__':
    Flight.run()

