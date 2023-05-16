from tkinter import *


canvas = Tk()
canvas.title("BMI Calculator")
canvas.minsize(300,400)

my_font = ("Arial",12,"bold")


weight_label = Label(text="Enter your weight (kg)",font=my_font)
weight_label.place(x=150-87,y=80)


kg_text= Entry()
kg_text.place(x=150-62,y=110)

height_label = Label(text="Enter your height (cm)",font=my_font)
height_label.place(x=150-87,y=170)

cm_text= Entry()
cm_text.place(x=150-62,y=200)


result_msg = None
error_msg = None


def bmi_calculate():
    global result_msg,error_msg

    if result_msg is not None:
        result_msg.destroy()
        result_msg = None

    if error_msg is not None:
        error_msg.destroy()
        error_msg = None

    try:
        kilo = int(kg_text.get())
        cm = int(cm_text.get())
        try:
            cm/=100
            cm*=cm
            result=kilo/cm
            result_final=round(result,2)

            if result_final<18.5:

                result_msg = Label(text=f"Your BMI is {result_final}\nYour weight type: Under Weight ", font=my_font, fg="red")
                result_msg.place(x=25, y=300)
            elif 18.5 <= result_final <=24.9:

                result_msg = Label(text=f"Your BMI is {result_final}\nYour weight type: Normal ", font=my_font, fg="red")
                result_msg.place(x=50, y=300)

            elif 25 <= result_final <= 29.9:

                result_msg = Label(text=f"Your BMI is {result_final}\nYour weight type: Over Weight ", font=my_font, fg="red")
                result_msg.place(x=30, y=300)

            elif 30 <= result_final <= 34.9:

                result_msg = Label(text=f"Your BMI is {result_final}\nYour weight type: Obesity (Class I) ", font=my_font, fg="red")
                result_msg.place(x=18, y=300)

            elif 35 <= result_final <= 39.9:

                result_msg = Label(text=f"Your BMI is {result_final}\nYour weight type: Obesity (Class II) ", font=my_font,fg="red")
                result_msg.place(x=15, y=300)

            if result_final >= 40:

                result_msg = Label(text=f"Your BMI is {result_final}\nYour weight type: Extreme Obesity ", font=my_font, fg="red")
                result_msg.place(x=15, y=300)
        except:
            pass


    except:

            error_msg = Label(text="Enter a valid number!\n", font=my_font, fg="red")
            error_msg.place(x=150 - 84, y=300)





calculator_button= Button(text="Calculate",height=1,width=10,command=bmi_calculate)
calculator_button.place(x=150-40,y=260)





canvas.mainloop()