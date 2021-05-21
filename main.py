from kivy.clock import Clock
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.app import MDApp


class ScaleHydra(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"

    def build(self):
        return Builder.load_file('main_ui.kv')

    def on_start(self):
        from kivy.base import EventLoop
        EventLoop.window.bind(on_keyboard=self.hook_keyboard)

    @staticmethod
    def is_android():
        return platform == 'android'

    def hook_keyboard(self, window, key, *largs):
        if key == 27:  # кнопка назад
            pass


if __name__ == '__main__':
    Window.softinput_mode = "below_target"
    ScaleHydra().run()
