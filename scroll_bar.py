import tkinter


class ScrollBar:
    '''Пример программы с вертикальной прокруткой'''

    def __init__(self):
        self.window = tkinter.Tk()
        self.window.geometry('300x300')
        self.window.title(f'Список с прокруткой')

        # Создать внешнюю рамку, которая будет содержать внуртенюю рамку и верт прокрутку
        self.outer_frame = tkinter.Frame(self.window)
        self.outer_frame.pack(padx=20, pady=20)

        # Создать внутренюю рамку, которая будет содержать горизонтальную прокрутку
        self.inner_frame = tkinter.Frame(self.outer_frame)
        self.inner_frame.pack()


        # Создать список
        self.listbox = tkinter.Listbox(self.inner_frame, height=6, width=20)
        self.listbox.pack(side='left')

        # Bертикальную прокрутку
        self.scrollbar_y = tkinter.Scrollbar(self.inner_frame, orient=tkinter.VERTICAL)
        self.scrollbar_y.pack(side='right', fill=tkinter.Y)

        # Горизонтальная прокрутка
        self.scrollbar_x = tkinter.Scrollbar(self.outer_frame, orient=tkinter.HORIZONTAL)
        self.scrollbar_x.pack(side='bottom', fill=tkinter.X)

        # Совместить ScrollBar и ListBox для совместной работы
        self.scrollbar_x.config(command=self.listbox.xview)
        self.scrollbar_y.config(command=self.listbox.yview)
        self.listbox.config(xscrollcommand=self.scrollbar_x.set, yscrollcommand=self.scrollbar_y.set)


        self.quit_button = tkinter.Button(self.window, text='EXIT', command=self.window.destroy)
        self.quit_button.pack()

        # Заполнить список
        animals = ['Обезьяна - это первый месяц', 'Петух - это второй месяц', 'Собака - это третий месяц',
                   'Свинья - это четвёртый месяц', 'Крыса - это пятый месяц', 'Бык - это шестой месяц',
                   'Тигр - это седьмой месяц', 'Заяц - это восьмой месяц', 'Дракон - это девятый месяц',
                   'Змея - это десятый месяц', 'Лошадь - это одинадцатый месяц', 'Овца - это двенадцатый месяц']
        [self.listbox.insert(tkinter.END, animal) for animal in animals]

        tkinter.mainloop()


if __name__ == '__main__':
    scroll = ScrollBar()
