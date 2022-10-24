from kivymd.app import MDApp
from kivymd.uix.button import MDRoundFlatIconButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.label import MDLabel

import requests
from threading import *

from telegramExport import Bot


def checkConnection():
    try:
        response = requests.get('https://www.google.com/')
        return (1, 'Successful Connection', 'robot-happy')
    except requests.exceptions.ConnectionError:
        return (0, 'No Connection!', 'robot-dead')


class Container(MDFloatLayout):
    def startApp(self):
        global thread_bot
        status = checkConnection()
        self.status.text = status[1]
        self.iconStatus.icon = status[2]
        # if status[0] == True:
            # Bot()
            # Thread(target=Bot).start()
            # thread_bot.start()
            # thread_bot.join()


    def closeApp(self):
        self.status.text = 'Status'
        self.iconStatus.icon = 'robot'


class scheduleBotApp(MDApp):
    def build(self):
        self.icon = 'icon.png'
        self.theme_cls.material_style = "M3"
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Purple"
        return Container()


if __name__ == '__main__':
    scheduleBotApp().run()
