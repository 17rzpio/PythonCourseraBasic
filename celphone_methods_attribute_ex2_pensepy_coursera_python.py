def ring_celphone(ringtone):
    for n in range(100):
        print(ringtone)
def call_number(number_call):
    for n in range(100):
        print("call",number_call)
def display_color(color_cellphone):
    print(color_cellphone)

number_cellphone = int(input("\ntype the number go call: "))
color_cellphone = input("\ntype the color of cellphone: ")
ringtone_cellphone = input("\nchose a ringtone")
ring_celphone(ringtone_cellphone)
call_number(number_cellphone)
display_color(color_cellphone)

