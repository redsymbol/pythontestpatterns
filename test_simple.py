import unittest

class TestSimple(unittest.TestCase):
    def test_wordcount(self):
        from simple import wordcount

        corpus = ''
        expected = dict()
        actual = wordcount(corpus)
        self.assertEqual(expected, actual)

        corpus = 'foo bar'
        expected = {
            'foo' : 1,
            'bar' : 1,
            }
        actual = wordcount(corpus)
        self.assertEqual(expected, actual)

        corpus = 'foo bar foo'
        expected = {
            'foo' : 2,
            'bar' : 1,
            }
        actual = wordcount(corpus)
        self.assertEqual(expected, actual)

        corpus = 'foo bar             foo  '
        expected = {
            'foo' : 2,
            'bar' : 1,
            }
        actual = wordcount(corpus)
        self.assertEqual(expected, actual)

        corpus = 'foo bar Foo'
        expected = {
            'foo' : 2,
            'bar' : 1,
            }
        actual = wordcount(corpus)
        self.assertEqual(expected, actual)

CORPUS = 'The quick brown fox jumped over the lazy dog'
class TestStatsTable(unittest.TestCase):
    def setUp(self):
        from simple import StatsTable
        self.stats = StatsTable(CORPUS)

    def test_counts(self):
        self.assertEqual(1, self.stats.count('quick'))
        self.assertEqual(2, self.stats.count('the'))
        self.assertEqual(2, self.stats.count('The'))
        self.assertEqual(2.0/9, self.stats.frequency('the'))
        self.assertAlmostEqual(.1102, self.stats.stddev(), places=4)

    def test_add(self):
        self.assertEqual(1, self.stats.count('quick'))
        self.stats.add('quick')
        self.assertEqual(2, self.stats.count('quick'))
        self.stats.add('quick')
        self.assertEqual(3, self.stats.count('quick'))
    
    def test_reset(self):
        self.assertEqual(1, self.stats.count('quick'))
        self.stats.add('quick')
        self.assertEqual(2, self.stats.count('quick'))
        self.stats.reset(CORPUS)
        self.assertEqual(1, self.stats.count('quick'))
