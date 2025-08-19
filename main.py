from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class MainScreen(BoxLayout):
    pass

class ToDoApp(App):
    def build(self):
        return MainScreen()
    
    def add_item(self):
        input_box = self.root.ids.input_box
        task_text = input_box.text.strip()
        if task_text:
            from kivy.uix.label import Label
            from kivy.uix.button import Button
            from kivy.uix.boxlayout import BoxLayout

            item_layout = BoxLayout(size_hint_y=None, height=40, spacing=10)
            item_label = Label(text=task_text, halign="left", valign="middle")
            item_label.bind(size=item_label.setter('text_size'))

            delete_btn = Button(text='Delete', size_hint_x=None, width=80)
            delete_btn.bind(on_press=lambda x: self.delete_item(item_layout))

            item_layout.add_widget(item_label)
            item_layout.add_widget(delete_btn)

            self.root.ids.item_box.add_widget(item_layout)
            input_box.text = ""

    def delete_item(self, item_layout):
        self.root.ids.item_box.remove_widget(item_layout)

    def clear_all(self):
        self.root.ids.item_box.clear_widgets()

if __name__ == "__main__":
    ToDoApp().run()
