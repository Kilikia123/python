#!/usr/bin/env python
# -- coding: utf-8 --

import time

import requests
from bs4 import BeautifulSoup


class Weather:
    WEATHER_C = 'https://www.google.com/search?q=прогноз+погоды&oq=ghjuyj..'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
    degrees = 0  # температура
    prob_prec = 0  # вероятность осадков
    humidity = 0  # влажность
    wind_speed = 0  # ветер
    day_of_week = ""
    delta = 10

    def __init__(self):
        self.degrees = int(self.get_degrees())
        self.prob_prec = int(self.get_prob_prec()[:-1])
        self.humidity = int(self.get_humidity()[:-1])
        self.wind_speed = int(self.get_wind_speed()[0])
        self.day_of_week = str(self.get_day())

    def get_degrees(self):
        all_page = requests.get(self.WEATHER_C, headers=self.headers)
        soup = BeautifulSoup(all_page.content, 'html.parser')
        arr = soup.findAll("span", {"class": "wob_t TVtOme", "id": "wob_tm", "style": "display:inline"})
        return arr[0].text

    def get_prob_prec(self):
        all_page = requests.get(self.WEATHER_C, headers=self.headers)
        soup = BeautifulSoup(all_page.content, 'html.parser')
        arr = soup.findAll("span", {"id": "wob_pp"})
        return arr[0].text

    def get_humidity(self):
        all_page = requests.get(self.WEATHER_C, headers=self.headers)
        soup = BeautifulSoup(all_page.content, 'html.parser')
        arr = soup.findAll("span", {"id": "wob_hm"})
        return arr[0].text

    def get_wind_speed(self):
        all_page = requests.get(self.WEATHER_C, headers=self.headers)
        soup = BeautifulSoup(all_page.content, 'html.parser')
        arr = soup.findAll("span", {"class": "wob_t", "id": "wob_ws"})
        return arr[0].text

    def get_day(self):
        all_page = requests.get(self.WEATHER_C, headers=self.headers)
        soup = BeautifulSoup(all_page.content, 'html.parser')
        arr = soup.findAll("div", {"class": "wob_dts", "id": "wob_dts"})
        return arr[0].text

    def compare_degrees(self):
        other_deg = int(self.get_degrees())
        other_prob_prec = int(self.get_prob_prec()[:-1])  # вероятность осадков
        other_humidity = int(self.get_humidity()[:-1])
        other_wind_speed = int(self.get_wind_speed()[0])
        other_day_of_week = str(self.get_day())
        if other_deg >= self.degrees + self.delta:
            print("Наблюдается сильное потепление")
        elif other_deg + self.delta <= self.degrees:
            print("Наблюдается сильное похолодание")
        print(other_day_of_week)
        print("Температура: " + str(other_deg) + " ℃")
        print("Вероятность осадков: " + str(other_prob_prec) + " %")
        print("Влажность: " + str(other_humidity) + " %")
        print("Ветер: " + str(other_wind_speed) + " м/c")
        time.sleep(3600)
        self.compare_degrees()
