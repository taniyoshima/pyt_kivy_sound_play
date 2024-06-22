# -*- coding: utf-8 -*-

import os
import kivy

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.audio import SoundLoader
from kivy.core.window import Window

kivy.require('2.2.0')

# 画面サイズの指定
Window.size = (500, 150)

Builder.load_file(os.path.dirname(__file__) + "/interface.kv")


class AudioTest(Widget):

    def __init__(self, **kwargs):
        super(AudioTest, self).__init__(**kwargs)

        # Audioファイルの読み込み
        self.sound = SoundLoader.load('test.mp3')

        # 再生位置データ
        self.time = 0

    # 再生ボタンの処理
    def on_play_press(self):
        if self.sound and self.sound.state == 'stop':
            self.sound.seek(self.time)
            self.sound.play()

    # 停止ボタンの処理
    def on_stop_press(self):
        if self.sound.state == 'play':
            self.time = self.sound.get_pos()
            self.sound.stop()

    # 巻き戻しボタンの処理（10秒戻る）
    def on_feedb_press(self):
        if self.sound.state == 'play':
            self.time = self.sound.get_pos() - 10
            self.sound.seek(self.time)
            self.sound.play()

    # 早送りボタンの処理（10秒進む）
    def on_feedf_press(self):
        if self.sound.state == 'play':
            self.time = self.sound.get_pos() + 10
            self.sound.seek(self.time)
            self.sound.play()


class AudioTestApp(App):
    def __init__(self, **kwargs):
        super(AudioTestApp, self).__init__(**kwargs)
        self.title = 'Audio Test'

    def build(self):
        return AudioTest()


if __name__ == '__main__':
    app = AudioTestApp()
    app.run()
