import tkinter as tk
import tkinter.messagebox


class TranseformerToMiles:
    """Преобразователь километров в мили"""

    def __init__(self):
        # Описание главного окна
        self.main_window = tk.Tk()
        self.window_size = '600x200'
        self.main_window.geometry(self.window_size)

        self.main_window.title(f'Преобразователь километров в мили {self.window_size}')

        # Создание рамок в глав. окне
        self.top_frame = tk.Frame(self.main_window, border=6, relief='solid')
        self.mid_frame = tk.Frame(self.main_window, border=6, relief='raised')
        self.bottom_frame = tk.Frame(self.main_window, border=6, relief='solid')

        # Задание параметров верхнего виджета
        self.top_frame.label1 = tk.Label(self.top_frame, text='Введите величину в км: ')
        self.kilo_entry = tk.Entry(self.top_frame, width=20)

        # Задание параметров среднего виджета
        self.description_mid_label = tk.Label(self.mid_frame, text='Преобразовано в мили: ')
        self.value = tk.StringVar()
        self.miles_label = tk.Label(self.mid_frame, textvariable=self.value)
        # self.value.set() -обязательно, это выводимое значение

        # Задание параметров нижнего виджета
        self.transfer_button = tk.Button(self.bottom_frame, text='Преобразовать', borderwidth=4, relief='raised',
                                         command=self.convert_to_miles)
        self.exit_button = tk.Button(self.bottom_frame, text='Выйти', borderwidth=4, relief='raised',
                                     command=self.main_window.destroy)

        # Упаковка вехних виджетов
        self.top_frame.label1.pack(side='left')
        self.kilo_entry.pack()

        # Упаковка средних виджетов
        self.description_mid_label.pack(side='left', padx=(10, 20))
        self.miles_label.pack(side='left')

        # Упаковка нижних виджетов
        self.transfer_button.pack(side='left', padx=10, pady=20)
        self.exit_button.pack(side='right', pady=20)

        # Упаковка рамок
        self.top_frame.pack(expand=True)
        self.mid_frame.pack(expand=True)
        self.bottom_frame.pack(expand=True)

        tk.mainloop()

    def convert_to_miles(self):
        kilo = float(self.kilo_entry.get())
        miles = kilo * 0.6214
        self.value.set(miles)
        #tk.messagebox.showinfo('Вывод', f'Расстояние в {kilo} км равно {miles} миль')


if __name__ == '__main__':
    my_gui = TranseformerToMiles()
