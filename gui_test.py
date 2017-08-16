from guizero import App, Text, TextBox, PushButton

def your_name():
    welcome_message.set( my_name.get() )

app = App(title="Hello World")

welcome_message = Text(app, text="Welcome to new app", size=20, font="Times new romans", color="blue")

my_name = TextBox(app)

update_text = PushButton(app, command=your_name, text="Enter Name")

app.display()
