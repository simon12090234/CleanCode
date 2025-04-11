from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.model import app

class SavingsCalculator(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=30, spacing=10, **kwargs)

        amount_layout = BoxLayout(orientation='horizontal', spacing=10)
        amount_label = Label(text="Cantidad mensual:")
        self.amount_input = TextInput(hint_text="Ingrese la cantidad de ahorro mensual", multiline=False)
        amount_layout.add_widget(amount_label)
        amount_layout.add_widget(self.amount_input)
        self.add_widget(amount_layout)

        months_layout = BoxLayout(orientation='horizontal', spacing=10)
        months_label = Label(text="Cantidad de meses:")
        self.months_input = TextInput(hint_text="Ingrese la cantidad de meses", multiline=False)
        months_layout.add_widget(months_label)
        months_layout.add_widget(self.months_input)
        self.add_widget(months_layout)

        interest_layout = BoxLayout(orientation='horizontal', spacing=10)
        interest_label = Label(text="Cantidad de meses:")
        self.interest_input = TextInput(hint_text="Ingrese la tasa de interes", multiline=False)
        interest_layout.add_widget(interest_label)
        interest_layout.add_widget(self.interest_input)
        self.add_widget(interest_layout)

        self.calculate_button = Button(text="Calcular Ahorro")
        self.calculate_button.bind(on_press=self.calculate)
        self.add_widget(self.calculate_button)

        self.result_label = Label(text="Resultado aparecerá aquí")
        self.add_widget(self.result_label)


    def show_error_popup(self, message):
        content = BoxLayout(orientation='vertical', padding=10, spacing=10)
        content.add_widget(Label(text=message))
        close_button = Button(text="Cerrar")
        content.add_widget(close_button)

        popup = Popup(title="Error", content=content, size_hint=(0.8, 0.4))
        close_button.bind(on_press=popup.dismiss)
        popup.open()

    def calculate(self, instance):
        MinimunValue = 0
        PercentageConvertor = 100
        MaximunValue = 64
        try:
            amount = float(self.amount_input.text)
            if amount <= MinimunValue:
                raise ValueError("La cantidad de ahorro debe ser mayor a 0.")

            months = int(self.months_input.text)
            if months <= MinimunValue:
                raise app.Invalidmonths("La cantidad de meses debe ser mayor a 0.")

            interest = float(self.interest_input.text) / PercentageConvertor
            if interest < MinimunValue or interest > MaximunValue:
                raise app.Invalidinterest("La tasa de interés debe estar entre 0 y 100.")

            result = app.Calculate_programmed_savings(amount, interest, months)
            self.result_label.text = f"Ahorro Total: {result:.2f}"
        except (ValueError, app.Invalidinterest, app.Invalidmonths) as e:
            self.show_error_popup(str(e))



class SavingsApp(App):
    def build(self):
        return SavingsCalculator()


if __name__ == "__main__":
    SavingsApp().run()
