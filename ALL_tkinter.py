import tkinter
import tkinter.messagebox
from tkinter import ttk


# Томас Гэддис
class MyGui:
    '''Все изученые функции модля tkinter'''

    def __init__(self):
        # НАстройки окна
        self.main_window = tkinter.Tk()
        # Картинка для окна
        photo = tkinter.PhotoImage(file='123.png')
        self.main_window.iconphoto(False, photo)
        # self.main_window.iconbitmap('tree.ico')
        self.size = '1000x1000+600+75'
        self.main_window.geometry(self.size)
        self.main_window.config(background='#85B2AF')
        # Прозрачность окна
        self.main_window.attributes('-alpha', 1)
        # Окно ВСЕГДА поверх других окон
        self.main_window.attributes('-topmost', True)
        self.main_window.resizable(False, False)
        # Окно без рамки
        self.main_window.overrideredirect(False)
        self.main_window.title(f'ТКинтер {self.size}')


        # Панель управления
        menubar = tkinter.Menu(self.main_window)
        self.main_window.config(menu=menubar)

        drop_menu = tkinter.Menu(menubar, tearoff=0)
        drop_menu.add_command(label='Файл', command=None)
        drop_menu.add_command(label='О программе', command=None)
        drop_menu.add_command(label='Выход', command=self.main_window.destroy)
        menubar.add_cascade(label='Файл', menu=drop_menu)

        # Настройка изменния окна курсором мыши - по-умолчанию ДА
        self.main_window.minsize(200, 800)
        self.main_window.maxsize(1200, 1050)
        self.main_window.resizable(True, True)

        self.prompt_label = tkinter.Label(self.main_window,
                                          text='''Основные блоки/методы \nмодуля \ntkinter''',
                                          bg='grey',
                                          foreground='white',
                                          font=('Arial', 20, 'bold'),
                                          padx=20,
                                          pady=20,
                                          width=35,
                                          height=5,
                                          anchor='sw',
                                          relief=tkinter.RAISED,
                                          borderwidth=3,
                                          justify=tkinter.LEFT)
        self.prompt_label.pack(padx=20, pady=10)

        # ----------------------TOP FRAME--------------------
        self.top_frame = tkinter.Frame(self.main_window, borderwidth=1, relief='sunken')
        self.top_frame.pack(padx=20, pady=10)
        self.top_frame_label = tkinter.Label(self.top_frame, text='Верхняя рамка', font=('Arial', 14, 'bold'))
        self.top_frame_label.pack()
        # Рамка №1 - Список и прокрутка
        self.frame1 = tkinter.Frame(self.top_frame, borderwidth=1, relief='sunken')
        self.frame1.pack(side='left', padx=20, pady=10, anchor='n')
        self.frame1_label = tkinter.Label(self.frame1, text='Рамка №1 - Список и прокрутка')
        self.frame1_label.pack()
        # Доп. рамка для верт. прокрутки
        self.inner_frame = tkinter.Frame(self.frame1)
        self.inner_frame.pack()
        # Место под список
        self.listbox = tkinter.Listbox(self.inner_frame, height=6, width=30)
        self.listbox.pack(side='left')
        # Прокрутки
        self.x_scrollbar = tkinter.Scrollbar(self.frame1, orient=tkinter.HORIZONTAL)
        self.x_scrollbar.pack(side='bottom', fill=tkinter.X)
        self.y_scrollbar = tkinter.Scrollbar(self.inner_frame, orient=tkinter.VERTICAL)
        self.y_scrollbar.pack(side='right', fill=tkinter.Y)
        # Установки по прокрутке
        self.x_scrollbar.config(command=self.listbox.xview)
        self.y_scrollbar.config(command=self.listbox.yview)
        self.listbox.config(xscrollcommand=self.x_scrollbar.set, yscrollcommand=self.y_scrollbar.set)
        # Вывод выбора курсора
        self.output_frame = tkinter.Frame(self.top_frame)
        self.output_frame.pack(side='bottom', after=self.frame1)
        self.choice_var = tkinter.StringVar()
        self.descr_output_label = tkinter.Label(self.output_frame, text='Вывод выбора курсора', borderwidth=2,
                                                relief='sunken')
        self.descr_output_label.pack(side='left')
        self.output_label = tkinter.Label(self.output_frame, textvariable=self.choice_var, borderwidth=2, width=10,
                                          background='white', relief='sunken')
        self.output_label.pack(side='right')

        # Чего-нибудь для списка
        animals = ['Обезьяна - это первый месяц', 'Петух - это второй месяц', 'Собака - это третий месяц',
                   'Свинья - это четвёртый месяц', 'Крыса - это пятый месяц', 'Бык - это шестой месяц',
                   'Тигр - это седьмой месяц', 'Заяц - это восьмой месяц', 'Дракон - это девятый месяц',
                   'Змея - это десятый месяц', 'Лошадь - это одинадцатый месяц', 'Овца - это двенадцатый месяц']
        [self.listbox.insert(tkinter.END, animal) for animal in animals]
        self.listbox.bind('<<ListboxSelect>>', self.get_name)

        # Рамка №2 - Radio- & CheckButton
        self.frame2 = tkinter.Frame(self.top_frame, borderwidth=1, relief='solid')
        self.frame2.pack(side='right', padx=20, pady=10)
        self.frame2_label = tkinter.Label(self.frame2, text='Рамка №2 - Radio- & CheckButton')
        self.frame2_label.pack()
        # Доп. рамки
        # RadioButton
        self.rad_frame = tkinter.Frame(self.frame2, borderwidth=1, relief='solid')
        self.rad_frame.pack(side='left')
        self.rad_frame_label = tkinter.Label(self.rad_frame, text='RadioButton', borderwidth=4, relief='raised')
        self.rad_frame_label.pack()
        # IntVar для RadioButton 1,2,3 и т.д. - сколько цифр(флажков) - столько и выборов
        self.rad_var = tkinter.IntVar()
        self.rad_var.set(1)
        # Само меню выбора
        self.rad_choice1_label = tkinter.Radiobutton(self.rad_frame, text='Выбор №1', variable=self.rad_var, value=1)
        self.rad_choice2_label = tkinter.Radiobutton(self.rad_frame, text='Выбор №2', variable=self.rad_var, value=2)
        self.rad_choice3_label = tkinter.Radiobutton(self.rad_frame, text='Выбор №3', variable=self.rad_var, value=3)
        self.rad_choice4_label = tkinter.Radiobutton(self.rad_frame, text='Выбор №4', variable=self.rad_var, value=4)
        self.rad_choice1_label.pack()
        self.rad_choice2_label.pack()
        self.rad_choice3_label.pack()
        self.rad_choice4_label.pack()
        # Кнопки
        self.rad_ok_button = tkinter.Button(self.rad_frame, text='OK', command=self.show_rad_info)
        self.rad_ok_button.pack(side='bottom')

        # CheckButton
        self.check_frame = tkinter.Frame(self.frame2, borderwidth=1, relief='solid')
        self.check_frame.pack(side='right')
        self.check_frame_label = tkinter.Label(self.check_frame, text='CheckButton', borderwidth=4, relief='raised')
        self.check_frame_label.pack()
        self.check_ok_button = tkinter.Button(self.check_frame, text='OK', command=self.show_check_info)
        self.check_ok_button.pack(side='bottom')
        self.deselect_button = tkinter.Button(self.check_frame, text='СНЯТЬ ВСЁ', command=self.deselect_all)
        self.deselect_button.pack(side='bottom')
        self.all_button = tkinter.Button(self.check_frame, text='ВЫБРАТЬ ВСЁ', command=self.select_all)
        self.all_button.pack(side='bottom')
        self.switch_button = tkinter.Button(self.check_frame, text='ПОМЕНЯТЬ', command=self.togle_all)
        self.switch_button.pack(side='bottom')

        self.str_var = tkinter.StringVar()
        self.int_var = tkinter.IntVar()
        # IntVar для CheckButton (0,1) - два состояния флажка
        self.ch1_var = tkinter.IntVar()
        self.ch2_var = tkinter.IntVar()
        self.ch3_var = tkinter.IntVar()
        self.ch4_var = tkinter.IntVar()
        self.ch1_var.set(0)
        self.ch2_var.set(0)
        self.ch3_var.set(0)
        self.ch4_var.set(0)
        # Само меню выбора
        # indicatoron = 0 - флажок в виде кнопки
        self.ch1 = tkinter.Checkbutton(self.check_frame, text='Выбор №1', variable=self.ch1_var,
                                       offvalue=0, onvalue=1
                                       )
        self.ch2 = tkinter.Checkbutton(self.check_frame, text='Выбор №2', variable=self.ch2_var)
        self.ch3 = tkinter.Checkbutton(self.check_frame, text='Выбор №3', variable=self.ch3_var)
        self.ch4 = tkinter.Checkbutton(self.check_frame, text='Выбор №4', variable=self.ch4_var, indicatoron=0)
        self.ch1.pack()
        self.ch2.pack()
        self.ch3.pack()
        self.ch4.pack()

        # ----------------------MIDDLE FRAME--------------------
        self.mid_frame = tkinter.Frame(self.main_window, borderwidth=1, relief='solid')
        self.mid_frame.pack(padx=20, pady=10)
        self.mid_frame_label = tkinter.Label(self.mid_frame, text='Средняя рамка', font=('Arial', 14, 'bold'))
        self.mid_frame_label.pack()
        # Рамка №3 - окно ввода чего-либо Entry
        self.frame3 = tkinter.Frame(self.mid_frame, borderwidth=1, relief='solid')
        self.frame3.pack(side='left', padx=20, pady=10)
        self.frame3_label = tkinter.Label(self.frame3, text='Рамка №3 - окно ввода чего-либо Entry')
        self.frame3_label.grid(row=0, column=1)
        # Создане строки и поля дял ввода
        self.some_label = tkinter.Label(self.frame3, text='Строка с текстом: ')
        self.some_label.grid(row=1, column=0)
        self.some_label_entry = tkinter.Entry(self.frame3)
        self.some_label_entry.grid(row=1, column=1)
        self.password_label = tkinter.Label(self.frame3, text='PASSWORD')
        self.password_label.grid(row=2, column=0)
        self.password_entry = tkinter.Entry(self.frame3, show='*')
        self.password_entry.grid(row=2, column=1)

        # Задание параметров вывода переменной Entry
        self.descr_label = tkinter.Label(self.frame3, text='Что либо и/или пояснения')
        self.descr_label.grid(row=3, column=0)
        self.entries_var = tkinter.StringVar()
        self.show_something_label = tkinter.Label(self.frame3, textvariable=self.entries_var)
        self.show_something_label.grid(row=3, column=1)

        # Кнопки
        self.entry_ok_button = tkinter.Button(self.frame3, text='OK', command=self.show_something)
        self.entry_ok_button.grid(row=1, column=2)
        self.get_entry_button = tkinter.Button(self.frame3, text='GET', command=self.get_entry)
        self.get_entry_button.grid(row=4, column=0, stick='we')
        self.delete_button = tkinter.Button(self.frame3, text='DELETE', command=self.delete_entry)
        self.delete_button.grid(row=4, column=1, stick='we')
        self.insert_button = tkinter.Button(self.frame3, text='INSERT', \
                                            command=lambda: self.some_label_entry.insert(0, 'вставка'))
        self.insert_button.grid(row=4, column=2, stick='we')
        self.submit_button = tkinter.Button(self.frame3, text='SUBMIT', command=self.submit)
        self.submit_button.grid(row=2, column=2, stick='we')

        # Рамка №4 - ComboBox, выпадающее меню
        self.frame4 = tkinter.Frame(self.mid_frame, borderwidth=1, relief='solid')
        self.frame4.pack(side='left', padx=20, pady=10, anchor='n')
        self.frame4_label = tkinter.Label(self.frame4, text='Рамка №4 - ComboBox, выпадающее меню').pack()

        self.days = ("Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье")
        self.int_list = [1, 2, 3, 4, 5, 6, 7]

        self.combo_days = ttk.Combobox(self.frame4, values=self.days)
        self.combo_days.current(4)
        self.combo_days.pack()
        self.combo_int = ttk.Combobox(self.frame4, values=self.int_list)
        self.combo_int.pack()

        self.combo_button = tkinter.Button(self.frame4, text='Show combo', command=self.show_combo)
        self.combo_button.pack()
        self.combo_set_button = tkinter.Button(self.frame4, text='Set combo', command=self.set_combo)
        self.combo_set_button.pack()

        # Рамка №5 - кнопки и их возможности
        self.frame5 = tkinter.Frame(self.main_window, borderwidth=1, relief='solid')
        self.frame5.pack(padx=20, pady=10)
        self.frame5_label = tkinter.Label(self.frame5, text='Рамка №5 - кнопки и их возможности')
        self.frame5_label.pack()

        global count
        count = 0
        self.count_button = tkinter.Button(self.frame5, text=f'Счётчик {count}', bg='yellow', command=self.counter,
                                           activebackground='green',
                                           activeforeground='blue',
                                           highlightbackground='red')
        self.count_button.pack()

        # Рамка №? - кнопки управления
        self.button_frame = tkinter.Frame(self.main_window, borderwidth=1, relief='solid')
        self.button_frame.pack(padx=20, pady=10)
        self.button_frame_label = tkinter.Label(self.button_frame, text='Рамка №? - кнопки управления')
        self.button_frame_label.pack()
        # Кнопки и соответсвующие возможности
        self.ok_button = tkinter.Button(self.button_frame, text='OK', command=self.show_info)
        self.ok_button.pack(side='right')
        self.quit_button = tkinter.Button(self.button_frame, text='ВЫЙТИ', command=self.main_window.destroy)
        self.quit_button.pack(side='right')

        tkinter.mainloop()

    animals = ['Обезьяна - это первый месяц', 'Петух - это второй месяц', 'Собака - это третий месяц',
               'Свинья - это четвёртый месяц', 'Крыса - это пятый месяц', 'Бык - это шестой месяц',
               'Тигр - это седьмой месяц', 'Заяц - это восьмой месяц', 'Дракон - это девятый месяц',
               'Змея - это десятый месяц', 'Лошадь - это одинадцатый месяц', 'Овца - это двенадцатый месяц']

    def get_name(self, event):
        index = self.listbox.curselection()
        anima = self.listbox.get(index[0])
        print(anima)
        # if anima.startswith('Обезьяна'):
        #     self.choice_var.set('Обезьяна')
        # elif anima.startswith('Петух'):
        #     self.choice_var.set('Петух')
        # elif anima.startswith('Собака'):
        #     self.choice_var.set('Собака')
        # elif anima.startswith('Свинья'):
        #     self.choice_var.set('Свинья')
        # elif anima.startswith('Крыса'):
        #     self.choice_var.set('Крыса')
        # elif anima.startswith('Бык'):
        #     self.choice_var.set('Бык')
        # elif anima.startswith('Тигр'):
        #     self.choice_var.set('Тигр')
        # elif anima.startswith('Заяц'):
        #     self.choice_var.set('Заяц')
        # elif anima.startswith('Дракон'):
        #     self.choice_var.set('Дракон')
        # elif anima.startswith('Змея'):
        #     self.choice_var.set('Змея')
        # elif anima.startswith('Лошадь'):
        #     self.choice_var.set('Лошадь')
        # elif anima.startswith('Овца'):
        #     self.choice_var.set('Овца')
        # или поменьше текста
        self.choice_var.set(anima.split()[0])

    def show_something(self):
        value = self.some_label_entry.get()
        print(value)
        self.entries_var.set(value)

    def show_rad_info(self):
        tkinter.messagebox.showinfo('Итог', f'Вариант №{self.rad_var.get()}')

    def show_check_info(self):
        print('выбор', self.ch1_var.get())
        self.message = f'Ваш выбор - это:\n'
        if self.ch1_var.get() == 1:
            self.message += 'Вариант №1\n'
        if self.ch2_var.get() == 1:
            self.message += 'Вариант №2\n'
        if self.ch3_var.get() == 1:
            self.message += 'Вариант №3\n'
        if self.ch4_var.get() == 1:
            self.message += 'Вариант №4\n'
        tkinter.messagebox.showinfo('Итог', f'{self.message}')

    def select_all(self):
        [check.select() for check in [self.ch1, self.ch2, self.ch3, self.ch4]]

    def deselect_all(self):
        [check.deselect() for check in [self.ch1, self.ch2, self.ch3, self.ch4]]

    def togle_all(self):
        [check.toggle() for check in [self.ch1, self.ch2, self.ch3, self.ch4]]

    def show_info(self):
        self.show_rad_info()
        self.show_check_info()

    def counter(self):
        global count
        count += 1
        print(count)
        self.count_button['text'] = f'Счётчик {count}'

    def submit(self):
        value = self.password_entry.get()
        print(value)
        self.entries_var.set(value)
        self.delete_entry()
        self.password_entry.delete(0, tkinter.END)

    def get_entry(self):
        value = self.some_label_entry.get()
        if value:
            print(value)
        else:
            print('Empty Entry')

    def delete_entry(self):
        # (индекс)('end')(0, tk.END)
        self.some_label_entry.delete(0, tkinter.END)

    def show_combo(self):
        print(self.combo_days.get())

    def set_combo(self):
        self.combo_days.set('qwerty')
        # self.combo_days.set('Среда')
if __name__ == '__main__':
    my_gui = MyGui()
