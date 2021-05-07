from src.weather_class import Weather
import unittest


class MyTestCase(unittest.TestCase):
    def testGetDegrees(self):
        my_degrees = int(Weather().get_degrees())
        self.assertTrue(30 >= my_degrees >= -30)

    def testGetProbPrec(self):
        my_prob_prec = int(Weather().get_prob_prec()[:-1])
        self.assertTrue(100 >= my_prob_prec >= 0)

    def testGetHumidity(self):
        my_humidity = int(Weather().get_humidity()[:-1])
        self.assertTrue(100 >= my_humidity >= 0)

    def testGetWindSpeed(self):
        my_wind_speed = int(Weather().get_wind_speed()[:-4])
        self.assertTrue(25 >= my_wind_speed >= 0)

