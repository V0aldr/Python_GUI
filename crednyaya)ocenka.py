import tkinter
import tkinter.messagebox


class MidMark:
    '''Средняя оценка'''

    def __init__(self):
        self.main_window = tkinter.Tk()
        self.window_size = '600x300'
        self.main_window.geometry(self.window_size)
        self.main_window.title('Вычислитель средней оценки')

        self.fist_mark_frame = tkinter.Frame()
        self.snd_mark_frame = tkinter.Frame()
        self.third_mark_frame = tkinter.Frame()
        self.middle_mark_frame = tkinter.Frame()
        self.button_frame = tkinter.Frame()

        self.fist_mark_label = tkinter.Label(self.fist_mark_frame, text='Ввести экзаменационную оценку №1: ')
        self.mark1_entry = tkinter.Entry(self.fist_mark_frame, width=10)
        self.snd_mark_label = tkinter.Label(self.snd_mark_frame, text='Ввести экзаменационную оценку №2: ')
        self.mark2_entry = tkinter.Entry(self.snd_mark_frame, width=10)
        self.third_mark_label = tkinter.Label(self.third_mark_frame, text='Ввести экзаменационную оценку №3:')
        self.mark3_entry = tkinter.Entry(self.third_mark_frame, width=10)

        self.middle_mark_label = tkinter.Label(self.middle_mark_frame, text='Средняя оценка: ')
        self.value = tkinter.StringVar()
        self.value_label = tkinter.Label(self.middle_mark_frame, textvariable=self.value)

        self.middle_mark_button = tkinter.Button(self.button_frame, text='Усреднить', command=self.get_middle_mark)
        self.exit_button = tkinter.Button(self.button_frame, text='ВЫЙТИ', command=self.main_window.destroy)

        self.fist_mark_frame.pack()
        self.snd_mark_frame.pack()
        self.third_mark_frame.pack()
        self.middle_mark_frame.pack()
        self.button_frame.pack()

        self.fist_mark_label.pack(side='left')
        self.mark1_entry.pack()
        self.snd_mark_label.pack(side='left')
        self.mark2_entry.pack()
        self.third_mark_label.pack(side='left')
        self.mark3_entry.pack()

        self.middle_mark_label.pack(side='left')
        self.value_label.pack()

        self.middle_mark_button.pack(side='left')
        self.exit_button.pack(side='left')

        tkinter.mainloop()

    def get_middle_mark(self):
        mark1 = int(self.mark1_entry.get())
        mark2 = int(self.mark2_entry.get())
        mark3 = int(self.mark3_entry.get())
        print(mark1, mark2, mark3)
        mm = (mark1 + mark2 + mark3) / 3
        self.value.set(str(mm))
        tkinter.messagebox.showinfo('Средняя оценка', f'{mm}')



if __name__ == '__main__':
    my_gui = MidMark()
