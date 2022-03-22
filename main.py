
from time import time
from kivy.app import App
from os.path import dirname, join
from kivy.lang import Builder
from kivy.properties import NumericProperty, StringProperty, BooleanProperty,\
    ListProperty
from kivy.clock import Clock
from kivy.animation import Animation
from kivy.uix.screenmanager import Screen


class ShowcaseScreen(Screen):
    fullscreen = BooleanProperty(False)

    def add_widget(self, *args, **kwargs):
        if 'content' in self.ids:
            return self.ids.content.add_widget(*args, **kwargs)
        return super(ShowcaseScreen, self).add_widget(*args, **kwargs)


class ShowcaseApp(App):

    index = NumericProperty(-1)
    current_title = StringProperty()
    time = NumericProperty(0)
    show_sourcecode = BooleanProperty(False)
    sourcecode = StringProperty()
    screen_names = ListProperty([])
    hierarchy = ListProperty([])

    def build(self):
        self.title = 'QuickStat'
        Clock.schedule_interval(self._update_clock, 1 / 60.)
        self.screens = {}
        self.available_screens = [
            'FileChoosers',
            'Buttons', 'ToggleButton', 'Sliders', 'ProgressBar',
            'Switches', 'CheckBoxes', 'TextInputs', 'Accordions', 
            'Carousel', 'Bubbles', 'CodeInput', 'DropDown', 
            'Spinner', 'Scatter', 'Splitter', 'TabbedPanel + Layouts', 
            'RstDocument', 'Popups', 'ScreenManager']
        self.screen_names = self.available_screens
        curdir = dirname(__file__)
        self.available_screens = [join(curdir, 'data', 'screens',
            '{}.kv'.format(fn).lower()) for fn in self.available_screens]
        self.go_next_screen()

    
    def on_pause(self):
        return True

    def on_resume(self):
        pass

    def on_current_title(self, instance, value):
        self.root.ids.spnr.text = value

    def go_previous_screen(self):
        self.index = (self.index - 1) % len(self.available_screens)
        screen = self.load_screen(self.index)
        sm = self.root.ids.sm
        sm.switch_to(screen, direction='right')
        self.current_title = screen.name
        

    def go_next_screen(self):
        self.index = (self.index + 1) % len(self.available_screens)
        screen = self.load_screen(self.index)
        sm = self.root.ids.sm
        sm.switch_to(screen, direction='left')
        self.current_title = screen.name
        

    def go_screen(self, idx):
        self.index = idx
        self.root.ids.sm.switch_to(self.load_screen(idx), direction='left')
        

    def go_hierarchy_previous(self):
        ahr = self.hierarchy
        if len(ahr) == 1:
            return
        if ahr:
            ahr.pop()
        if ahr:
            idx = ahr.pop()
            self.go_screen(idx)

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
        
    def _update_clock(self, dt):
        self.time = time()


if __name__ == '__main__':
    ShowcaseApp().run()
