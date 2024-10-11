from django.test import SimpleTestCase
from platform_app.management.ratings import calculate_ratings

class CustomerSerializerTestCase(SimpleTestCase):

    maxDiff = None

    def test_that_ratings_are_calculated_for_no_channels_and_no_contents(self):
        ratings = calculate_ratings({}, {})
        self.assertEqual(ratings, {})

    def test_that_ratings_are_calculated_for_only_one_content(self):
        channels = {
            1 : (None, (1, ))
        }
        contents = {
            1 : 5
        }
        ratings = calculate_ratings(channels, contents)
        self.assertEqual(ratings, {
            1 : 5
        })

    def test_that_ratings_are_calculated_for_multiple_contents(self):
        channels = {
            1 : (None, (1, 2))
        }
        contents = {
            1: 4,
            2: 2 
        }
        ratings = calculate_ratings(channels, contents)
        self.assertEqual(ratings, {
            1 : 3
        })

    def test_that_ratings_are_calculated_for_subchannels(self):
        channels = {
            1 : ((2, ), None),
            2 : (None, (1,2))
        }
        contents = {
            1: 4,
            2: 2 
        }
        ratings = calculate_ratings(channels, contents)
        self.assertEqual(ratings, {
            1 : 3,
            2: 3
        })
        

    def test_that_ratings_are_calculated_for_subchannels(self):
        channels = {
            1 : ((2, 3), None),
            2 : (None, (1,2)),
            3 : (None, (2,3)),
        }
        contents = {
            1: 4,
            2: 2,
            3: 6
        }
        ratings = calculate_ratings(channels, contents)
        self.assertEqual(ratings, {
            1 : 1.75,
            2: 3,
            3: 4
        })

    def test_that_ratings_are_calculated_for_nested_subchannels(self):
        channels = {
            1 : ((2, 3), None),
            2 : ((4, 5, 6), None),
            3 : (None, (2,3)),
            4 : (None, (4,)),
            5 : (None, (5,)),
            6 : (None, (6,)), 
        }
        contents = {
            1: 4,
            2: 2,
            3: 6,
            4: 10,
            5: 20,
            6: 30
        }
        ratings = calculate_ratings(channels, contents)
        self.assertEqual(ratings, {
            1 : 4.0,
            2: 20,
            3: 4,
            4: 10.0, 5: 20.0, 6: 30.0
        })
        