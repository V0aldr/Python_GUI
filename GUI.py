import tkinter as tk
import tkinter.messagebox


class MyGUI:
    def __init__(self):
        # Создание окна
        self.main_window = tk.Tk()
        self.window_size = '1200x900'

        # Размер окна
        self.main_window.geometry(self.window_size)

        # Создание заголовка окна
        self.main_window.title(f'Заголовок GUI {self.window_size}')

        # Создание рамок в окне
        self.top_frame = tk.Frame(self.main_window)
        self.middle_mark_frame = tk.Frame(self.main_window)
        self.bottom_frame = tk.Frame(self.main_window)


        # self.button = tkinter.messagebox('Заголовок "Button"', 'Надпись в окне')
        self.my_button = tkinter.Button(self.main_window, text='Нажми меня!', borderwidth=2, relief='raised',
                                        command=self.do_something)
        # Кнопка "ВЫХОДА" из окна
        self.quit_button = tkinter.Button(self.top_frame, text='ВЫЙТИ!', borderwidth=4, relief='raised',
                                          command=self.main_window.destroy)

        # Упраление надписями в рамке
        self.label8 = tk.Label(self.top_frame, text='Мигнуть')
        self.label9 = tk.Label(self.top_frame, text='Моргнуть')
        self.label10 = tk.Label(self.top_frame, text='Кивнуть')

        self.label8.pack(side='top')
        self.label9.pack(side='top')
        self.label10.pack(side='top')

        self.label11 = tk.Label(self.top_frame, text='Мигнуть')
        self.label12 = tk.Label(self.top_frame, text='Моргнуть')
        self.label13 = tk.Label(self.top_frame, text='Кивнуть')

        self.label11.pack(side='left')
        self.label12.pack(side='left')
        self.label13.pack(side='left')

        # Создание надписей в окне
        self.label1 = tk.Label(self.main_window, text='Привет, Мир!', borderwidth=1, relief='solid')
        # borderwidth=1 - толщина границы вокруг текста еденица
        # relief='solid' - стиль границы - сплошная линия
        self.label2 = tk.Label(self.top_frame, text='Стиль рамки надписи#2 - канава',
                               borderwidth=4, relief='groove')
        # Примеры
        self.label3 = tk.Label(self.top_frame, text='Стиль рамки надписи#3 - вал',
                               borderwidth=6, relief='ridge')
        self.label4 = tk.Label(self.top_frame, text='Стиль рамки надписи#4 - возвышеность',
                               borderwidth=8, relief='raised')


        self.label5 = tk.Label(self.bottom_frame, text='Стиль рамки надписи#5 - овраг',
                               borderwidth=9, relief='sunken')
        self.label6 = tk.Label(self.bottom_frame, text='Стиль рамки надписи#6 - ничего(плоскость)',
                               borderwidth=10, relief='flat')
        # Sringvar

        self.middle_mark_label = tkinter.Label(self.middle_mark_frame, text='Средняя оценка: ')
        self.value = tkinter.StringVar()
        self.value_label = tkinter.Label(self.middle_mark_frame, textvariable=self.value)

        # Включение отображение(видимости)надписей в окне
        self.label1.pack(side='top', padx=20, pady=20, ipadx=20, ipady=20)
        # side='top', 'right', 'left', 'bottom'
        self.label2.pack(side='left')
        self.label3.pack(side='left', padx=(18, 30), pady=(50, 20))
        self.label4.pack(side='left', ipadx=20, ipady=50)
        self.label5.pack(side='left', padx=50, pady=20)
        self.label6.pack(side='left', padx=20, pady=50)

        self.label7 = tk.Label(self.bottom_frame, text='Вопрос 13.11', border=200, borderwidth=6, relief='ridge')
        self.label7.pack(side='left', padx=10, pady=20, ipadx=10, ipady=20)

        self.top_frame.pack()
        self.bottom_frame.pack()
        self.my_button.pack(expand=True, ipadx=20, ipady=20)
        self.quit_button.pack(side='top')


        self.middle_mark_label.pack()
        self.value_label.pack()

        # Главный цикл
        tk.mainloop()

    def do_something(self):
        self.value.set('Результат')
        tkinter.messagebox.showinfo('Результат', 'Текс в окне результата')


if __name__ == '__main__':
    my_gui = MyGUI()
