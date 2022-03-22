
from kivy.app import App
from os.path import dirname, join
from kivy.lang import Builder
from kivy.properties import NumericProperty, StringProperty, BooleanProperty,\
    ListProperty
from kivy.uix.screenmanager import Screen


class ShowcaseScreen(Screen):
    fullscreen = BooleanProperty(False)

    def add_widget(self, *args, **kwargs):
        if 'content' in self.ids:
            return self.ids.content.add_widget(*args, **kwargs)
        return super(ShowcaseScreen, self).add_widget(*args, **kwargs)


class ShowcaseApp(App):

    index = NumericProperty(-1)
    screen_names = ListProperty([])
    hierarchy = ListProperty([])

    def build(self):
        self.title = 'QuickStat'

        self.screens = {}
        self.available_screens = [
            'FileChooser', 'TabbedPanel',
            'Buttons', 'ToggleButton', 'Sliders',
            'Switches', 'CheckBoxes', 'TextInputs', 'Accordions', 
            'Carousel', 'Bubbles', 'DropDown',
            'Spinner', 'Scatter', 'Splitter',
            'RstDocument', 'Popups', 'ScreenManager']
        self.screen_names = self.available_screens
        curdir = dirname(__file__)
        self.available_screens = [join(curdir, 'data', 'screens',
            '{}.kv'.format(fn).lower()) for fn in self.available_screens]
        self.go_next_screen()

    
    def go_previous_screen(self):
        self.index = (self.index - 1) % len(self.available_screens)
        screen = self.load_screen(self.index)
        sm = self.root.ids.sm
        sm.switch_to(screen, direction='right')
        
    def go_next_screen(self):
        self.index = (self.index + 1) % len(self.available_screens)
        screen = self.load_screen(self.index)
        sm = self.root.ids.sm
        sm.switch_to(screen, direction='left')

    def go_screen(self, idx):
        self.index = idx
        self.root.ids.sm.switch_to(self.load_screen(idx), direction='left')

    

    def load_screen(self, index):
        if index in self.screens:
            return self.screens[index]
        screen = Builder.load_file(self.available_screens[index])
        self.screens[index] = screen
        return screen

    def showcase_floatlayout(self, layout):
        print("test")

    def showcase_boxlayout(self, layout):
        print('test')

    def showcase_gridlayout(self, layout):
        print('test')

    def showcase_stacklayout(self, layout):
        print('test')

    def showcase_anchorlayout(self, layout):
        print('test')

    def load(self, path, filename):
        # add screen changer to goto 2nd screen
        print(path, filename)


if __name__ == '__main__':
    ShowcaseApp().run()
