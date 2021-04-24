import src.WeatherClass
import unittest


class MyTestCase(unittest.TestCase):
    def tuneIn(self):
        self.myWeather = weather.Weather()

    def testGetDegrees(self, ideal_value):
        my_degrees = int(self.myWeather.get_degrees())
        self.assertEqual(my_degrees, ideal_value)

    def testGetProbPrec(self, ideal_value):
        my_prob_prec = int(self.myWeather.get_prob_prec())
        self.assertEqual(my_prob_prec, ideal_value)

    def testGetHumidity(self, ideal_value):
        my_humidity = int(self.myWeather.get_humidity())
        self.assertEqual(my_humidity, ideal_value)

    def testGetWindSpeed(self, ideal_value):
        my_wind_speed = int(self.myWeather.get_wind_speed())
        self.assertEqual(my_wind_speed, ideal_value)
