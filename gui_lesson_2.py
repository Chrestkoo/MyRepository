from guizero import App, Combo, Text, TextBox, PushButton, CheckBox, ButtonGroup, info

app = App(title="My second GUI app", width=500, height=300, layout="grid")

cust_name_lbl = Text(app, text="Enter your name: ", grid=[0,0], align="left")

name_txtbox = TextBox(app, grid=[0,1], align="left")
def confirm_order():
    info('Order Confirmed', 'Your Order number is 1. Thank you for order ' + name_txtbox.get() + '. ')
    
food_lbl = "Select Food? " 
food_desc_txt = Text(app, text=food_lbl, grid=[1,0], align="left")

lv_food = [['No Select', 'N'],['Nasi Lemak', 'A'], ['Mihun Soup', 'B'], ['Mihun Goreng', 'C']]
food_choice_btngrp = ButtonGroup(app, options=lv_food, selected='N', horizontal=True, grid=[1,1], align="left")

drink_lbl = "Select Drink? " 
drink_desc_txt = Text(app, text=drink_lbl, grid=[2,0], align="left")

lv_drink = [['No Select', 'n'], ['Teh Tarik', 'a'], ['Milo Ais', 'b'], ['Coffee', 'c']]
drink_choice_btngrp = ButtonGroup(app, options=lv_drink, selected='n', horizontal=True, grid=[2,1], align="left")

vip_seat_lbl = Text(app, text="Seat Area: ", grid=[3,0], align="left") 
vip_seat_check_box = CheckBox(app, text="Air Conditional", grid=[3,1], align="left")

payment_type_lbl = Text(app, text="Payment Method: ", grid=[4,0], align="left")
lv_payment_type = ["Debit / Credit Card", "Cash"]
payment_type_combo = Combo(app, options=lv_payment_type, grid=[4,1], align="left")

pdate_text_btn = PushButton(app, command=confirm_order, grid=[5,0], text="Comfirm Order")
app.display()
