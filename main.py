import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.core.clipboard import Clipboard

import qgen2

kivy.require('2.3.0')


class MyRoot(BoxLayout):

    length = 8
    flags = [100, 0, 50, 0]
    is_random = True
    

    def __init__(self):
        super(MyRoot, self).__init__()
        self.qgen_instance = qgen2.QGen()
        self.generate_random()

    def pressed_random(self):
        self.is_random = True
        self.reset()
        self.generate_random()

    def pressed_readable(self):
        self.is_random = False
        self.reset()
        self.generate_random()

    def generate_random(self):
        # self.label_random_string.text = self.qgen_instance.random_string_digits(self.length)
        if self.is_random:
            self.label_random_string.text = self.qgen_instance.weighted_random(self.length, self.flags)
        else:
            self.label_random_string.text = self.qgen_instance.cluster_gen(self.length, self.flags)
    
    def slider_update_length(self, *args):
        self.length = int(args[1])
        self.generate_random()

    def slider_update_flags(self, flag_id, *args):
        self.flags[flag_id] = int(args[1])
        self.generate_random()

    def reset(self):
        self.length = 8
        self.flags = [100, 0, 50, 0]
        self.slider_length.value = self.length
        self.slider_flags_lowercase.value = self.flags[0]
        self.slider_flags_uppercase.value = self.flags[1]
        self.slider_flags_numbers.value = self.flags[2]
        self.slider_flags_punctuation.value = self.flags[3]

    def copy_to_clipboard(self):
        Clipboard.copy(self.label_random_string.text)




class QuackGen(App):

    def build(self):
        Window.size = (600, 950)
        return MyRoot()


if __name__ == '__main__':
    QuackGen().run()
