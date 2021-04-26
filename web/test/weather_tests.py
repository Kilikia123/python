from src.weather_class import Weather
import unittest


class MyTestCase(unittest.TestCase):
    def tuneIn(self):
        self.myWeather = Weather()

    def testGetDegrees(self):
        my_degrees = int(self.myWeather.get_degrees())
        self.assertTrue(my_degrees <= 30 and my_degrees >= -30)

    def testGetProbPrec(self):
        my_prob_prec = int(self.myWeather.get_prob_prec())
        self.assertTrue(my_prob_prec <= 100 and my_prob_prec >= 0)

    def testGetHumidity(self):
        my_humidity = int(self.myWeather.get_humidity())
        self.assertTrue(my_humidity <= 100 and my_humidity >= 0)

    def testGetWindSpeed(self):
        my_wind_speed = int(self.myWeather.get_wind_speed())
        self.assertTrue(my_wind_speed <= 25 and my_wind_speed >= 0)
