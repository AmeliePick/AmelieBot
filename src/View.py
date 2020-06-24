import wpf

from System.Windows import Window
from System.Windows import Application, Window, MessageBox

class AppWindow(Window):
    def __init__(self):
        wpf.LoadComponent(self, 'View.xaml')



if __name__ == '__main__':
    Application().Run(AppWindow())