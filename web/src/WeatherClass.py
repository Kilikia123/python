import requests
from bs4 import BeautifulSoup
import time
import smtplib

class Weather:
	WEATHER_C = 'https://www.google.com/search?q=%D0%BF%D1%80%D0%BE%D0%B3%D0%BD%D0%BE%D0%B7+%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D1%8B&oq=ghjuyj&aqs=chrome.1.69i57j0i1i10i457j0i402l2j0i1i10l6.2098j0j7&sourceid=chrome&ie=UTF-8'
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
	degrees = 0
	delta = 4
	def __init__(self):
		self.degrees = int(self.get_degrees())

	def get_degrees(self):
		all_page = requests.get(self.WEATHER_C, headers=self.headers)
		soup = BeautifulSoup(all_page.content, 'html.parser')
		arr = soup.find_all("span", {"class": "wob_t TVtOme", "id": "wob_tm", "style": "display:inline"})
		return arr[0].text

	def compare_degrees(self):
		other_deg = int(self.get_degrees())
		if other_deg >= self.degrees + self.delta:
			print("Сильно потеплело")
		elif other_deg + self.delta <= self.degrees:
			print("Cильно похолодало")
		print("Сейчас: " + str(other_deg) + " ℃")
		time.sleep(600)
		self.compare_degrees()
