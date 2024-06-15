from tkinter import *
from tkinter import messagebox

def calculator_bmi():#Объявляем функцию.
    kg = int(weight_tf.get())   #С помощью метода .get получаем из поля ввода с именем weight_tf значение веса, которое ввёл пользователь и конвертируем в целое число с помощью int().
    m = int(height_tf.get())/100    #С помощью метода .get получаем из поля ввода с именем height_tf значение роста и конвертируем в целое число с помощью int(). Обязательно делим его на 100, так как пользователь вводит рост в сантиметрах, а в формуле для расчёта ИМТ используются метры.
    bmi = kg/(m*m)      #Рассчитываем значение индекса массы тела.
    bmi = round(bmi, 1)     #Округляем результат до одного знака после запятой.

    if bmi < 18.5:
        messagebox.showinfo('bmi-pythonguides', f'ИМТ = {bmi} соответствует недостаточному весу')
    elif (bmi > 18.5) and (bmi < 24.9):
        messagebox.showinfo('bmi-pythonguides', f'ИМТ = {bmi} соответствует нормальному весу')
    elif (bmi > 24.9) and (bmi < 29.9):
        messagebox.showinfo('bmi-pythonguides', f'ИМТ = {bmi} соответствует избыточному весу')
    else:
        messagebox.showinfo('bmi-pythonguides', f'ИМТ = {bmi} соответствует ожирению')

window = Tk()  # Создаём окно приложения.
window.title("Калькулятор индекса массы тела (ИМТ)")  # Добавляем название приложения.
window.geometry("400x300")


frame = Frame(
    window,  # Обязательный параметр, который указывает окно для размещения Frame.
    padx=10,  # Задаём отступ по горизонтали.
    pady=10  # Задаём отступ по вертикали.
)
frame.pack(expand=True)  # Не забываем позиционировать виджет в окне. Здесь используется метод pack. С помощью свойства expand=True указываем, что Frame заполняет весь контейнер, созданный для него.


height_lb = Label(
    frame,
    text="Введите свой рост (в см)  ",
)
height_lb.grid(row=3, column=1)


weight_lb = Label(
    frame,
    text="Введите свой вес (в кг)  ",
)
weight_lb.grid(row=4, column=1)


height_tf = Entry(
    frame,      #Используем нашу заготовку с настроенными отступами.
)
height_tf.grid(row=3, column=2)


weight_tf = Entry(
    frame,      #Используем нашу заготовку с настроенными отступами.
)
weight_tf.grid(row=4, column=2, pady=5)


cal_btn = Button(
    frame,
    text='Рассчитать ИМТ',
    command=calculator_bmi      #Позволяет запустить событие с функцией при нажатии на кнопку.
)
cal_btn.grid(row=5, column=2)

window.mainloop()  # окно приложения не должно закрываться