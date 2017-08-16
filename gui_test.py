from guizero import App, Text, TextBox, PushButton, Slider 


app = App(title="Hello World")

welcome_message = Text(app, text="Welcome to new app", size=20, font="Times new romans", color="blue")

my_name = TextBox(app)

def disp_name():
    if welcome_message.text is None:
        welcome_message.text("Please Enter Name", size=20, font="Times new romans", color="red")
    else:
        welcome_message.set( my_name.get() )
    
update_text = PushButton(app, command=disp_name, text="Enter Name")

def change_text_size(slider_value):
    welcome_message.font_size(slider_value)
    
text_slider = Slider(app, command=change_text_size, start=10, end=80)

app.display()
