from mrjob.job import MRJob
import string

class MRWordFrequencyCount(MRJob):

    def mapper(self, _, line):
        results = []
        for word in line.split():
            results.append((word.lower().translate(None, string.punctuation), 1))
        return results

    def reducer(self, word, occurences):
        yield word, sum(occurences)


if __name__ == '__main__':
    MRWordFrequencyCount.run()
