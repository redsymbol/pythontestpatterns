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

    def test_StatsTable(self):
        from simple import StatsTable

        corpus = 'The quick brown fox jumped over the lazy dog'
        stats = StatsTable(corpus)
        self.assertEqual(1, stats.count('quick'))
        self.assertEqual(2, stats.count('the'))
        self.assertEqual(2, stats.count('The'))
        self.assertEqual(2.0/9, stats.frequency('the'))
        self.assertAlmostEqual(.1102, stats.stddev(), places=4)
        
