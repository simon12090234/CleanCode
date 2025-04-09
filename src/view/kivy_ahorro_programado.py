from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import sys
import os


# Agrega la carpeta raíz del proyecto al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.model import app  # <- Ahora esto funcionará


class SavingsCalculator(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)

        self.amount_input = TextInput(hint_text="Ingrese la cantidad de ahorro mensual", multiline=False)
        self.add_widget(self.amount_input)

        self.months_input = TextInput(hint_text="Ingrese la cantidad de meses", multiline=False)
        self.add_widget(self.months_input)

        self.interest_input = TextInput(hint_text="Ingrese la tasa de interes", multiline=False)
        self.add_widget(self.interest_input)

        self.calculate_button = Button(text="Calcular Ahorro")
        self.calculate_button.bind(on_press=self.calculate)
        self.add_widget(self.calculate_button)

        self.result_label = Label(text="Resultado aparecerá aquí")
        self.add_widget(self.result_label)

    def calculate(self, instance):
        amount = self.amount_input.text
        months = self.months_input.text
        interest = self.interest_input.text / 100

        try:
            amount = float(amount)
            months = int(months)
            interest = float(interest)
            result = app.Calculate_programmed_savings(amount, interest, months)
            self.result_label.text = f"Ahorro Total: {result:.2f}"
        except (ValueError, app.Invalidinterest, app.Invalidmonths) as e:
            self.result_label.text = f"Error: {str(e)}"


class SavingsApp(App):
    def build(self):
        return SavingsCalculator()


if __name__ == "__main__":
    SavingsApp().run()
