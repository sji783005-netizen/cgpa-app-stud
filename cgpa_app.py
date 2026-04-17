from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class CGPAApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=15, spacing=10)

        self.inputs = []

        for i in range(1, 5):
            layout.add_widget(Label(text=f"{i} Semester Total Marks"))
            t1 = TextInput(multiline=False, input_filter='float')
            layout.add_widget(t1)

            layout.add_widget(Label(text=f"{i} Semester Obtained Marks"))
            t2 = TextInput(multiline=False, input_filter='float')
            layout.add_widget(t2)

            self.inputs.append((t1, t2))

        btn = Button(text="Calculate CGPA")
        btn.bind(on_press=self.calculate)
        layout.add_widget(btn)

        self.result = Label(text="")
        layout.add_widget(self.result)

        return layout

    def calculate(self, instance):
        try:
            output = ""

            for i in range(4):
                total = float(self.inputs[i][0].text)
                obtain = float(self.inputs[i][1].text)

                per = (obtain / total) * 100
                cgpa = per / 9.5

                output += f"Sem {i+1}: {per:.2f}% | CGPA {cgpa:.2f}\n"

            self.result.text = output

        except:
            self.result.text = "Invalid Input"

CGPAApp().run()
