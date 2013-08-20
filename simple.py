# v1
def wordcount(corpus):
    counts = dict()
    for word in corpus.split():
        try:
            counts[word] += 1
        except KeyError:
            counts[word] = 1
    return counts

# v2 
def wordcount(corpus):
    counts = dict()
    for word in corpus.split():
        key = word.lower()
        try:
            counts[key] += 1
        except KeyError:
            counts[key] = 1
    return counts

class StatsTable(object):
    def __init__(self, corpus):
        self.counts = wordcount(corpus)

    # v1
    def count(self, word):
        if word in self.counts:
            return self.counts[word]
        return 0

    # v2
    def count(self, word):
        key = word.lower()
        if key in self.counts:
            return self.counts[key]
        return 0

    def frequency(self, word):
        totalcount = sum(self.counts.values())
        return self.count(word) / float(totalcount)

    def stddev(self):
        import math
        numwords = len(self.counts)
        mean_count = sum(self.counts.values()) / float(numwords)
        val = 0.0
        for word, count in self.counts.iteritems():
            val += self.frequency(word) * (count - mean_count)
        val = math.sqrt(float(val) / numwords)
        return val
