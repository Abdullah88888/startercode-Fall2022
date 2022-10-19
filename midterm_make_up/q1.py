from mrjob.job import MRJob

class Fight(MRJob):
    def mapper(self, key, line):
	parts = line.split("\t")
	origin_airport = parts[0]
	destination_state = parts[3]
	num_passengers = parts[5]
	
	for x in i:
	    if x == 2021:
	        value = (num_passengers)
	    else:
		value = (num_passengers) 

	key = origin_airport, destination_state
	value = (num_passengers,"2021")
	yield(key, value)

	key = origin_airport, destination_state
	value = (num_passenegers, "2022")
	yield(key, value)

    def reducer(self, key, values):
	yield (key, (a,b))

if __name__ == '__main__':
    Flight.run()

