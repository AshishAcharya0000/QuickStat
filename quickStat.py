"""
A app for retreiving statistics from a csv file.
"""
# create a virtual environment in your current directory
# python -m virtualenv kivy_venv

# activate virtual environment
# kivy_venv\Scripts\activate

from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.tabbedpanel import TabbedPanel
from plyer import filechooser
import pandas as pd

# Set the app size
Window.size = (400, 260)

# Global variables
FILEPATH = ''
DF = pd.DataFrame()


# Main screen/window.
class Startup(Screen):
    """Startup screen with buttons for csv file selection"""
    # Get the csv file
    def file_chooser(self): 
        """Lets a user select a csv file"""
        global FILEPATH
        FILEPATH = filechooser.open_file(
            title="Pick a CSV file..",
            filters=[("Comma-separated Values", "*.csv")])
        print(FILEPATH)


# Data Analysis screen/window
class Display(Screen):
    """Screen for displaying statistics from given csv file."""
    # Create dataframe from selected csv
    def create_df(self):
        """Function for creating a dataframe from given csv file."""
        global FILEPATH
        global DF
        
        df = pd.read_csv(FILEPATH[0])
        print(df.head)
        print(df.describe())

        mask = df.select_dtypes(include='number')
        numeric_cols = mask.columns.values
        #print(numeric_cols)

        for column_headers in df.columns.values.tolist():
            print(column_headers)
        

# Designate Our .kv design file
kv_file = Builder.load_file('quickStatDesign.kv')


class QuickStat(App):
    """Main application"""
    # Window Title
    title = 'QuickStat'

    def build(self):
        """Builds the app"""
        return ScreenManager()


if __name__ == '__main__':
    QuickStat().run()