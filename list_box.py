import tkinter
import tkinter.messagebox


class ListboxExample:
    '''Выпадающий список'''

    def __init__(self):
        # Создание главного окна
        self.main_window = tkinter.Tk()
        self.size = '300x300'
        self.main_window.geometry(self.size)
        self.main_window.title(f'Список. Размер окна {self.size}')

        # Создание виджета Lisbox
        self.listbox = tkinter.Listbox(self.main_window, height=0, width=0)
        # self.listbox = tkinter.Listbox(self.main_window, selectmode=tkinter.EXTENDED)
        # tkinter.BROWSE - выбор по одному элементу спикса
        # tkinter.EXTENDED - выбор выделением многих элементов
        # tkinter.MULTIPLE - выбрать несколько мышью
        # tkinter.SINGLE - по-одиночный выбор
        #
        self.listbox.pack()

        # Определяем наполнение списка ВРУЧНУЮ
        # self.listbox.insert(1, 'Понедельник')
        # self.listbox.insert(2, 'Вторник')
        # self.listbox.insert(3, 'Среда')
        # self.listbox.insert(4, 'Четверг')
        # self.listbox.insert(5, 'Пятница')
        # self.listbox.insert(6, 'Суббота')
        # self.listbox.insert(7, 'Воскресенье')

        # Определяем наполнение списка ЧЕРЕЗ ЦИКЛ
        days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье', 'Конец списка']

        # tkinter.END - заглушка в спике. Проходит по всей длине списка
        [self.listbox.insert(tkinter.END, day) for day in days]

        # Создание кноки добычи результата
        self.result_button = tkinter.Button(self.main_window, text='Результат', command=self.__retrive_day)
        self.result_button.pack()

        # Запустить главный цикл
        tkinter.mainloop()

    def __retrive_day(self):
        # Получить индекс выбраного элемента
        indexes = self.listbox.curselection()
        print(type(indexes), indexes)
        # Если, элемент выбран, то показать его
        if len(indexes) > 0:
            tkinter.messagebox.showinfo(
                message=self.listbox.get(indexes[0]))
        else:
            tkinter.messagebox.showinfo(
                'Ни один элемент не выбран')


if __name__ == '__main__':
    listbox = ListboxExample()

print(listbox.__doc__)
