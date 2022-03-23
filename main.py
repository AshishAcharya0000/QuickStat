
from kivy.app import App
from os.path import dirname, join
from kivy.lang import Builder
from kivy.properties import NumericProperty, StringProperty, BooleanProperty,\
    ListProperty
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
import pandas as pd

# Global variables
FILE_PATH = ''
DATA_FRAME = pd.DataFrame()

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

    # TODO: Ensure file is a csv file
    def load(self, path, filename):
        # TODO: add screen changer to goto 2nd screen
        global FILE_PATH
        FILE_PATH = filename

    # gets row/column of df to put in kivymd table
    def get_data_table(dataframe):
        column_data = list(dataframe.columns)
        row_data = dataframe.to_records(index=False)
        return column_data, row_data


if __name__ == '__main__':
    ShowcaseApp().run()
