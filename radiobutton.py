import tkinter
import tkinter.messagebox

class GuiRadiButton:

    def __init__(self):
        self.main_window = tkinter.Tk()
        self.size = '300x300'
        self.main_window.geometry(self.size)
        self.main_window.title(f'Радиокнопка {self.size}')

        # Определение рамок
        self.top_frame = tkinter.Frame(self.main_window, border=2, relief='solid')
        self.mid_frame = tkinter.Frame(self.main_window, border=2, relief='solid')
        self.list_frame = tkinter.Frame(self.main_window, border=2, relief='solid')
        self.bottom_frame = tkinter.Frame(self.main_window, border=2, relief='flat')

        # Создание Заголовков для рамок
        self.top_frame_label = tkinter.Label(self.top_frame, text='Взаимоисключающий выбор', width=40)
        self.top_frame_label.pack()
        self.mid_frame_label = tkinter.Label(self.mid_frame, text='Множественный выбор', width=40)
        self.mid_frame_label.pack()
        self.list_frame_label = tkinter.Label(self.list_frame, text='Выпадающий список', width=40)
        self.list_frame_label.pack()
        self.bottom_frame_label = tkinter.Label(self.bottom_frame, text='Кнопки', width=40)
        self.bottom_frame_label.pack()


        # Создание СОБЫТИЯ RadioButton: переменной для радиоКнопки
        self.rad_var = tkinter.IntVar()
        self.rad_var.set(1)

        # Создание СОБЫТИЯ CheckButton: переменной для радиоКнопки
        self.check_b1 = tkinter.IntVar()
        self.check_b2 = tkinter.IntVar()
        self.check_b3 = tkinter.IntVar()
        # Присвоить  CheckButton значение 0
        self.check_b1.set(0)
        self.check_b2.set(0)
        self.check_b3.set(0)

        # Создание СОБЫТИЯ ListBox: переменной для списка
        self.list_var = tkinter.IntVar()

        # Создание выбора RadioButton из кнопок
        self.rb1 = tkinter.Radiobutton(self.top_frame, text='Вариант №1:', variable=self.rad_var, value=1)
        self.rb2 = tkinter.Radiobutton(self.top_frame, text='Вариант №2:', variable=self.rad_var, value=2)
        self.rb3 = tkinter.Radiobutton(self.top_frame, text='Вариант №3:', variable=self.rad_var, value=3)
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()

        # Создание выбора CheckButton из кнопок
        self.cb1 = tkinter.Checkbutton(self.mid_frame, text='Вариант №1:', variable=self.check_b1)
        self.cb2 = tkinter.Checkbutton(self.mid_frame, text='Вариант №1:', variable=self.check_b2)
        self.cb3 = tkinter.Checkbutton(self.mid_frame, text='Вариант №1:', variable=self.check_b3)
        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()

        # Создание кнопок управления
        self.ok_button = tkinter.Button(self.bottom_frame, text='ДА', command=self.show_choice)
        self.exit_button = tkinter.Button(self.bottom_frame, text='ВЫЙТИ', command=self.main_window.destroy)
        self.ok_button.pack(side='right')
        self.exit_button.pack(side='right')

        # Упаковка рамок
        self.top_frame.pack(padx=30, pady=5)
        self.mid_frame.pack(padx=30, pady=5)
        self.list_frame.pack(padx=30, pady=5)
        self.bottom_frame.pack(padx=30, pady=5)

        tkinter.mainloop()

    def show_choice(self):
        # Создать строковое сообщение
        self.message = f'а так же, Вы выбрали: \n'
        # Проверка выбора
        if self.check_b1.get() == 1:
            self.message = self.message + '1\n'
        if self.check_b2.get() == 1:
            self.message = self.message + '2\n'
        if self.check_b3.get() == 1:
            self.message = self.message + '3\n'

        # Вывести итоговое сообщение
        tkinter.messagebox.showinfo('ВЫБОР', f'Выбран вариант №{self.rad_var.get()}\n\n{self.message}')


if __name__ == '__main__':
    my_gui = GuiRadiButton()
