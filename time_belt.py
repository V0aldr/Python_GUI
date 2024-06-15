import tkinter
import tkinter.messagebox

class TimeBelt:
    """Часовой пояс
    Выполнено с помощью модуля TK"""

    def __init__(self):
        self.window = tkinter.Tk()
        self.size = '300x300'
        self.window.geometry(self.size)
        self.window.title(f'Часовой пояс. Размер окна {self.size}')

        # Создать виджеты
        self.__build_prompt_label()
        self.__build_listbox()
        self.__build_output_frame()
        self.__build_quit_button()

        # Запустить главцикл
        tkinter.mainloop()

    def __build_prompt_label(self):
        self.prompt_label = tkinter.Label(self.window, text='Выберите город:')
        self.prompt_label.pack(padx=5, pady=5)

    def __build_listbox(self):
        self.__cities = ['Львов', 'Киев', 'Моска', 'Казань',  'Екатеринбург', 'Томск', 'Хабаровск']
        self.city_listbox = tkinter.Listbox(self.window, height=0, width=0)
        self.city_listbox.pack(padx=5, pady=5)
        self.city_listbox.bind('<<ListboxSelect>>', self.get_time_belt)
        [self.city_listbox.insert(tkinter.END, city) for city in self.__cities]
    def __build_output_frame(self):
        # Создать рамку
        self.output_frame = tkinter.Frame(self.window)
        self.output_frame.pack(padx=5, pady=5)

        # Создать надпись
        self.descr_output_label = tkinter.Label(self.output_frame, text='Часовой пояс: ')
        self.descr_output_label.pack(side='left')

        # Создать переенную StrVar для хранения часового пояса
        self.__time_belt_var = tkinter.StringVar()

        # Создать метку Label для вывода часового пояса
        self.output_label = tkinter.Label(self.output_frame, textvariable=self.__time_belt_var)
        self.output_label.pack(side='right', padx=5, pady=5)

    def __build_quit_button(self):
        self.quit_button = tkinter.Button(self.window, text='ВЫХОД', command=self.window.destroy)
        self.quit_button.pack(padx=5, pady=5)

    def get_time_belt(self, event):
        # Получить индекс курсора
        indexes = self.city_listbox.curselection()
        # Получить город из списка по индексу курсора
        city = self.city_listbox.get(indexes[0])

        # определитиь временный пояс
        if city == 'Львов':
            self.__time_belt_var.set('-1')
        elif city == 'Киев':
            self.__time_belt_var.set('0')
        elif city == 'Моска':
            self.__time_belt_var.set('+2')
        elif city == 'Казань':
            self.__time_belt_var.set('+3')
        elif city == 'Екатеринбург':
            self.__time_belt_var.set('+4')
        elif city == 'Томск':
            self.__time_belt_var.set('+5')
        elif city == 'Хабаровск':
            self.__time_belt_var.set('+6')



if __name__ == '__main__':
    time_belt = TimeBelt()
