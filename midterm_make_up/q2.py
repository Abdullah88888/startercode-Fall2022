from mrjob.job import MRJob

class Flight(MRJob):
    def mapper(self, key, line):
        parts = line.split("\t")
        num_passengers_2021 = float(parts[3])
        num_passenegrs_2022 = float(parts[5])
        origin_airport = parts[7]
        destination_state = parts[9]

        yield (origin_airport, destination_state, num_passengers_2021, num_passengers_2022)

    def reducer(self, key, values):
        yield(key, values)

if __name__ == '__main__':
    Flight.run()
    
