import pandas as pd
import numpy as np
import sys
from tkinter import *

# initialize list of lists
Frame0 = pd.read_csv("activity.csv")
Frame1 = pd.read_csv("bf.csv")
Frame2 = pd.read_csv("lf.csv")
Frame3 = pd.read_csv("df.csv")


def fractional_knapsack(value, weight, capacity):

    # index = [0, 1, 2, ..., n - 1] for n items
    index = list(range(len(value)))
    # contains ratios of values to weight
    ratio = [v / w for v, w in zip(value, weight)]
    # index is sorted according to value-to-weight ratio in decreasing order
    index.sort(key=lambda i: ratio[i], reverse=True)

    max_value = 0
    fractions = [0] * len(value)
    for i in index:
        if weight[i] <= capacity:
            fractions[i] = 1
            max_value += value[i]
            capacity -= weight[i]
        else:
            fractions[i] = capacity / weight[i]
            max_value += value[i] * capacity / weight[i]
            break

    return max_value, fractions


def exercise_plan(pref, max_time, w):
    for i in range(0, 4):
        if pref == 0:
            short = Frame0[Frame0["category"] == 'Gym and Aerobic Activities']
        elif pref == 1:
            short = Frame0[Frame0["category"] == 'water sports']
        elif pref == 2:
            short = Frame0[Frame0["category"] == 'Sports']
        elif pref == 3:
            short = Frame0[Frame0["category"] == 'Adventurous']
        elif pref == 4:
            short = Frame0[Frame0["category"] == 'general']
        else:
            print("Invalid Input")
            break;
    Exe_1 = short['Activity'].to_list()
    Calories_per_lb = short['Calories per lb'].tolist()
    values4 = []
    weight = (w)
    for i in range(0, len(Calories_per_lb)):
        r = float((Calories_per_lb[i])) * weight * 2.2
        values4.append(r)
    Timing = short['Time(min)'].tolist()
    value4 = [int(v) for v in values4]
    weight4 = [float(w) for w in Timing]
    capacity4 = (max_time)
    max_value4, fractions4 = fractional_knapsack(value4, weight4, capacity4)
    s4 = []
    for i in range(0, len(fractions4)):
        v4 = (fractions4[i])
        s4.append(v4)
    final = []
    for i in range(0, len(fractions4)):
        f = s4[i] * values4[i]
        final.append(f)
    dur = []
    for i in range(0, len(fractions4)):
        r = s4[i] * Timing[i]
        dur.append(r)
    data_tuples4 = list(zip(Exe_1, dur, final))
    result4 = pd.DataFrame(data_tuples4, columns=['Exe_list', 'Time of workout(in mins)', 'calories burnt'])
    List_exe4 = result4.loc[result4["Time of workout(in mins)"] > 0.0]
    List_exe4['calories burnt'] = List_exe4['calories burnt'].astype(int)
    List_exe4.head()
    return (List_exe4)


def calories_burnt_in_exercise(List_exe4):
    List_exe4['calories burnt'] = List_exe4['calories burnt'].astype(int)
    cal_burt = List_exe4['calories burnt'].sum()
    return (cal_burt)


def breakfast_plan(pref, break_fast):
    for i in range(0, 2):
        if pref == "SI":
            short1 = Frame1[Frame1["CATEGORY"] == 'South Indian']
        elif pref == "NI":
            short1 = Frame1[Frame1["CATEGORY"] == 'North Indian']
        elif pref == "C":
            short1 = Frame1[Frame1["CATEGORY"] == 'Continental']
        else:
            print("Invalid Input")
            break;
    food1 = short1['FOOD'].to_list()
    protein1 = short1['PROTEIN'].tolist()
    values1 = []
    for i in range(0, len(protein1)):
        r1 = int((protein1[i]))
        values1.append(r1)
    CALORIES1 = short1['CALORIES'].tolist()
    CATEGORY1 = short1['CATEGORY'].tolist()
    value1 = [int(v) for v in values1]
    weight1 = [float(w) for w in CALORIES1]
    capacity1 = float(break_fast)

    max_value1, fractions1 = fractional_knapsack(value1, weight1, capacity1)
    # print('The maximum value of items that can be carried:', max_value)
    # print('The fractions in which the items should be taken:', fractions)
    s1 = []
    for i in range(0, len(fractions1)):
        v1 = (fractions1[i])
        s1.append(v1)
    final1 = []
    for i in range(0, len(fractions1)):
        f1 = s1[i] * values1[i]
        final1.append(f1)
    dur1 = []
    for i in range(0, len(fractions1)):
        r1 = s1[i] * CALORIES1[i]
        dur1.append(r1)
    data_tuples1 = list(zip(food1, s1, dur1, final1, CATEGORY1))
    result1 = pd.DataFrame(data_tuples1, columns=['FOOD', 'QUANTITY', 'CALORIES', 'PROTEIN', 'CATEGORY'])
    list_food1 = result1.loc[result1["QUANTITY"] > 0.0]
    # (list_food1)

    return (list_food1)


# breakfast_plan('South Indian')

def lunch_plan(pref, lunch):
    for i in range(0, 2):
        if pref == "SI":
            short1 = Frame2[Frame2["CATEGORY"] == 'South Indian']
        elif pref == "NI":
            short1 = Frame2[Frame2["CATEGORY"] == 'North Indian']
        elif pref == "C":
            short1 = Frame2[Frame2["CATEGORY"] == 'Continental']
        else:
            print("Invalid Input")
            break;
    food1 = short1['FOOD'].to_list()
    protein1 = short1['PROTEIN'].tolist()
    values1 = []
    for i in range(0, len(protein1)):
        r1 = int((protein1[i]))
        values1.append(r1)
    CALORIES1 = short1['CALORIES'].tolist()
    CATEGORY1 = short1['CATEGORY'].tolist()
    value1 = [int(v) for v in values1]
    weight1 = [float(w) for w in CALORIES1]
    capacity1 = float(lunch)

    max_value1, fractions1 = fractional_knapsack(value1, weight1, capacity1)
    # print('The maximum value of items that can be carried:', max_value)
    # print('The fractions in which the items should be taken:', fractions)
    s1 = []
    for i in range(0, len(fractions1)):
        v1 = (fractions1[i])
        s1.append(v1)
    final1 = []
    for i in range(0, len(fractions1)):
        f1 = s1[i] * values1[i]
        final1.append(f1)
    dur1 = []
    for i in range(0, len(fractions1)):
        r1 = s1[i] * CALORIES1[i]
        dur1.append(r1)
    data_tuples1 = list(zip(food1, s1, dur1, final1, CATEGORY1))
    result1 = pd.DataFrame(data_tuples1, columns=['FOOD', 'QUANTITY', 'CALORIES', 'PROTEIN', 'CATEGORY'])
    list_food1 = result1.loc[result1["QUANTITY"] > 0.4]
    return (list_food1)


def dinner_plan(pref, dinner):
    for i in range(0, 2):
        if pref == "SI":
            short1 = Frame3[Frame3["CATEGORY"] == 'South Indian']
        elif pref == "NI":
            short1 = Frame3[Frame3["CATEGORY"] == 'North Indian']
        elif pref == "C":
            short1 = Frame3[Frame3["CATEGORY"] == 'Continental']
        else:
            print("Invalid Input")
            break;
    food1 = short1['FOOD'].to_list()
    protein1 = short1['PROTEIN'].tolist()
    values1 = []
    for i in range(0, len(protein1)):
        r1 = int((protein1[i]))
        values1.append(r1)
    CALORIES1 = short1['CALORIES'].tolist()
    CATEGORY1 = short1['CATEGORY'].tolist()
    value1 = [int(v) for v in values1]
    weight1 = [float(w) for w in CALORIES1]
    capacity1 = float(dinner)

    max_value1, fractions1 = fractional_knapsack(value1, weight1, capacity1)
    # print('The maximum value of items that can be carried:', max_value)
    # print('The fractions in which the items should be taken:', fractions)
    s1 = []
    for i in range(0, len(fractions1)):
        v1 = (fractions1[i])
        s1.append(v1)
    final1 = []
    for i in range(0, len(fractions1)):
        f1 = s1[i] * values1[i]
        final1.append(f1)
    dur1 = []
    for i in range(0, len(fractions1)):
        r1 = s1[i] * CALORIES1[i]
        dur1.append(r1)
    data_tuples1 = list(zip(food1, s1, dur1, final1, CATEGORY1))
    result1 = pd.DataFrame(data_tuples1, columns=['FOOD', 'QUANTITY', 'CALORIES', 'PROTEIN', 'CATEGORY'])
    list_food1 = result1.loc[result1["QUANTITY"] > 0.0]
    return (list_food1)


from tkinter import *
import tkinter as tk
from tkinter import ttk

top = Tk()

top.geometry("1000x1000")
top.configure(bg='cyan3')
Font_tuple = ("Arial", 15, "bold")
Font_tuple1 = ("Arial", 11, "bold")
Font_tuple2 = ("Arial", 25, "bold")

Heading = Label(top, text="~INFIX FIT~", font=Font_tuple2,bg='cyan3')
Heading.place(x=430, y=20)
name = Label(top, text="Name", font=Font_tuple ,bg='cyan3')
name.place(x=10, y=70)
t4 = Entry(top, width=30, bd=5)
t4.place(x=200, y=70)

nn = DoubleVar()
weight = Label(top, text="Weight", font=Font_tuple ,bg='cyan3')
weight.place(x=10, y=120)
t5 = Entry(top, width=30, bd=5, textvariable=nn)
t5.place(x=200, y=120)

gender = Label(top, text="Gender", font=Font_tuple,bg='cyan3' )
gender.place(x=10, y=170)
n = StringVar()
t6 = ttk.Combobox(top, width=30, textvariable=n)
t6.place(x=200, y=170)
t6['values'] = (' Male', ' Female')
t6.current()

age = Label(top, text="Age", font=Font_tuple,bg='cyan3')
age.place(x=10, y=220)
n1 = StringVar()

brands = ["<18", "18-40", "41-55", "55<"]

wa = [[1, 2], [1, 2, 3, 4], [1, 2, 3], [1, 2]]
t7 = ttk.Combobox(top, width=30, value=(brands))
t7.place(x=200, y=220)
t7.current()


def callback(eventObject):
    abc = eventObject.widget.get()
    fit = t7.get()
    index = brands.index(fit)
    fit_model.config(values=wa[index])


weighttolose = Label(top, text="Weight to lose", font=Font_tuple ,bg='cyan3')
weighttolose.place(x=10, y=270)
nw = StringVar()
fit_model = ttk.Combobox(top, width=37, textvariable=nw)
fit_model.place(x=200, y=270)
fit_model.bind('<Button-1>', callback)

hours = tk.Label(top, text="Exercise Time", font=Font_tuple,bg='cyan3')
hours.place(x=10, y=320)
e3 = DoubleVar()
r3 = Entry(top, width=30, bd=5, textvariable=e3)
r3.place(x=200, y=320)

Exe = Label(top, text="Exercise Type", font=Font_tuple,bg='cyan3')
Exe.place(x=10, y=360)
n3 = StringVar()
t = ttk.Combobox(top, width=30, textvariable=n3)
t.place(x=200, y=360)
t['values'] = ('Gym and Aerobic Activities', 'water sports', 'Sports', 'Adventurous', 'general')
t.current()

Label1 = Label(top, text="Food Preference :", font=Font_tuple,bg='cyan3')
Label1.place(x=10, y=410)

breakfast = Label(top, text="BREAKFAST:", font=Font_tuple1,bg='cyan3')
breakfast.place(x=200, y=470)
n4 = IntVar()
Radiobutton(top, text="SOUTH INDIAN", font=Font_tuple1, variable=n4, value=1,bg='cyan3').place(x=320, y=470)
Radiobutton(top, text="NORTH INDIAN", font=Font_tuple1, variable=n4, value=2,bg='cyan3').place(x=480, y=470)
Radiobutton(top, text="CONTINENTAL", font=Font_tuple1, variable=n4, value=3,bg='cyan3').place(x=650, y=470)

lunch = Label(top, text="LUNCH:", font=Font_tuple1,bg='cyan3')
lunch.place(x=200, y=520)
nl4 = IntVar()
Radiobutton(top, text="SOUTH INDIAN", font=Font_tuple1, variable=nl4, value=1,bg='cyan3').place(x=320, y=520)
Radiobutton(top, text="NORTH INDIAN", font=Font_tuple1, variable=nl4, value=2,bg='cyan3').place(x=480, y=520)
Radiobutton(top, text="CONTINENTAL", font=Font_tuple1, variable=nl4, value=3,bg='cyan3').place(x=650, y=520)

dinner = Label(top, text="DINNER:", font=Font_tuple1,bg='cyan3')
dinner.place(x=200, y=570)
nd4 = IntVar()
Radiobutton(top, text="SOUTH INDIAN", font=Font_tuple1, variable=nd4, value=1,bg='cyan3').place(x=320, y=570)
Radiobutton(top, text="NORTH INDIAN", font=Font_tuple1, variable=nd4, value=2,bg='cyan3').place(x=480, y=570)
Radiobutton(top, text="CONTINENTAL", font=Font_tuple1, variable=nd4, value=3,bg='cyan3').place(x=650, y=570)


def someFunction():
    # exercise_plan(t.current(),r3.get(),50)

    cal_burt = calories_burnt_in_exercise(exercise_plan(t.current(), float(r3.get()), float(t5.get())))
    print("WORKOUT PLAN")
    print("     ")
    print(exercise_plan(t.current(), float(r3.get()), float(t5.get())))
    print("     ")
    print("     ")
    weight_loss = float(fit_model.get())
    X = (1600 / weight_loss) + (cal_burt - (weight_loss * 300))
    break_fast = X * (2 / 5)

    lunch = X * (2 / 5)

    dinner = X * (1 / 5)
    print(" DIET PLAN FOR A DAY ")
    print("     ")
    print(" ----------------------------500 ML OF WATER ----------------------------")
    print("     ")
    for i in range(1, 3):
        if (n4.get() == 1):
            x = breakfast_plan("SI", break_fast)
            print("BREAKFAST PLAN")
            print(x)
            print("     ")
            break;
        elif (n4.get() == 2):
            x = breakfast_plan("NI", break_fast)
            print("BREAKFAST PLAN")
            print(x)
            print("     ")
            break;
        else:
            x = breakfast_plan("C", break_fast)
            print("BREAKFAST PLAN")
            print(x)
            print("     ")
            break;
    print(" ----------------------------500 ML OF WATER ----------------------------")
    print("     ")
    for i in range(1, 3):
        if (nl4.get() == 1):
            y = lunch_plan("SI", lunch)
            print("LUNCH PLAN")
            print(y)
            print("     ")
            break;
        elif (nl4.get() == 2):
            y = lunch_plan("NI", lunch)
            print("LUNCH PLAN")
            print(y)
            print("     ")
            break;
        else:
            y = lunch_plan("C", lunch)
            print("LUNCH PLAN")
            print(y)
            print("     ")
            break;
    print(" ----------------------------500 ML OF WATER ----------------------------")
    print("     ")
    for i in range(1, 3):
        if (nd4.get() == 1):
            z = dinner_plan("SI", dinner)
            print("DINNER PLAN")
            print(z)
            print("     ")
            break;
        elif (nd4.get() == 2):
            z = dinner_plan("NI", dinner)
            print("DINNER PLAN")
            print(z)
            print("     ")
            break;
        else:
            z = dinner_plan("C", dinner)
            print("DINNER PLAN")
            print(z)
            print("     ")
            break;
    print(" ----------------------------500 ML OF WATER ----------------------------")


button = tk.Button(top, text="  PLAN  ", font=("Arial", 15), command=someFunction ,bg='light cyan')
button.place(x=430, y=650)



root = Tk()
root.geometry('800x800')

txt = Text(root, height = 500, width = 600)

txt.pack()


class PrintToTXT():
    def write(self, s):
        txt.insert(END, s)

sys.stdout = PrintToTXT()

top.mainloop()

