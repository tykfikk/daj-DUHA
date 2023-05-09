from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout

class MainPage(FloatLayout):
    def __init__(self, **kwargs):
        super(MainPage, self).__init__(**kwargs)

        # Create the "SYTUACJA KRYZYSOWA" button and add it to the main layout
        crisis_button = Button(text='SYTUACJA KRYZYSOWA',
                               size_hint=(0.5, 0.4),
                               pos_hint={'x': 0.25, 'y': 0.05}
                               background_color=(1, 0, 1, 0))
        crisis_button.bind(on_press=self.on_crisis_button_press)
        self.add_widget(crisis_button)

        # Create the "NIE WIEM" button and add it to the main layout
        unsure_button = Button(text='NIE WIEM',
                               size_hint=(0.5, 0.4),
                               pos_hint={'x': 0.25, 'y': 0.5}
                               background_color=(1, 0, 1, 0))
        unsure_button.bind(on_press=self.on_unsure_button_press)
        self.add_widget(unsure_button)

        # Create the "DZWOŃ PO POMOC" button and add it to the main layout
        help_button = Button(text='DZWOŃ PO POMOC',
                             size_hint=(0.2, 0.2),
                             pos_hint={'x': 0.8, 'y': 0.8}
                             background_color=(1, 0, 1, 0))
        help_button.bind(on_press=self.on_help_button_press)
        self.add_widget(help_button)
        
        info_button = Button(text='PERSONAL INFO',
                             size_hint=(0.2, 0.2),
                             pos_hint = {'x':0.8, 'y': 0.6}
                             background_color=(1, 0, 1, 0))
        info_button.bind(on_press=self.on_info_button_press)
        self.add_widget(info_button)
        
    def on_info_button_press(self, instance):
        # Handle the "UZUPEŁNIJ INFORMACJE" button press
        print('Going to crisis screen')
        

    def on_crisis_button_press(self, instance):
        # Handle the "SYTUACJA KRYZYSOWA" button press
        print('Going to crisis screen')

    def on_unsure_button_press(self, instance):
        # Handle the "NIE WIEM" button press
        print('Going to unsure screen')

    def on_help_button_press(self, instance):
        # Handle the "DZWOŃ PO POMOC" button press
        print('Calling for help')

class DuhaApp(App):
    def build(self):
        return MainPage()

if __name__ == '__main__':
    DuhaApp().run()

