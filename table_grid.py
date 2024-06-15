import tkinter
import tkinter.messagebox
import tkinter.font


class TestGui:

    def __init__(self):
        self.window = tkinter.Tk()
        self.window.geometry('600x200')
        myfont = tkinter.font.Font(family='Arial', size=14, weight='bold')
        self.window.grid_columnconfigure(0, minsize=30)
        self.window.grid_columnconfigure(1, minsize=30)
        self.window.grid_columnconfigure(2, minsize=30)

        self.window.grid_rowconfigure(0, minsize=10)
        self.window.grid_rowconfigure(1, minsize=10)
        self.window.grid_rowconfigure(2, minsize=10)
        self.window.grid_rowconfigure(3, minsize=10)

        self.word1 = tkinter.StringVar()
        self.word2 = tkinter.StringVar()
        self.word3 = tkinter.StringVar()

        self.row0_label1 = tkinter.Label(self.window, text='Латинский', borderwidth=1, relief='solid', width=20)
        self.row0_label2 = tkinter.Label(self.window, text='Перевести', borderwidth=1, relief='solid', width=20)
        self.row0_label3 = tkinter.Label(self.window, text='Русский', borderwidth=1, relief='solid', width=20)
        self.row0_label2.grid(row=0, column=2, stick='wens')
        self.row0_label1.grid(row=0, column=1, stick='wens')
        self.row0_label3.grid(row=0, column=3, stick='wens')

        self.row1_label1 = tkinter.Label(self.window, text='sinister', borderwidth=1, relief='solid')
        self.row1_button2 = tkinter.Button(self.window, text='Перевести', borderwidth=1, relief='solid', command=self.trancelate)
        self.row1_label3 = tkinter.Label(self.window, textvariable=self.word1, borderwidth=1, relief='solid')
        self.row1_label1.grid(row=1, column=1, stick='wens')
        self.row1_button2.grid(row=1, column=2, stick='wens')
        self.row1_label3.grid(row=1, column=3, stick='wens')

        self.row2_label1 = tkinter.Label(self.window, text='dexter', borderwidth=1, relief='solid')
        self.row2_button2 = tkinter.Button(self.window, text='Перевести', borderwidth=1, relief='solid', command=self.trancelate)
        self.row2_label3 = tkinter.Label(self.window, textvariable=self.word2, borderwidth=1, relief='solid')
        self.row2_label1.grid(row=2, column=1, stick='wens')
        self.row2_button2.grid(row=2, column=2, stick='wens')
        self.row2_label3.grid(row=2, column=3, stick='wens')

        self.row3_label1 = tkinter.Label(self.window, text='medium', borderwidth=1, relief='solid')
        self.row3_button2 = tkinter.Button(self.window, text='Перевести', borderwidth=1, relief='solid', command=self.trancelate)
        self.row3_label3 = tkinter.Label(self.window, textvariable=self.word3, borderwidth=1, relief='solid')
        self.row3_label1.grid(row=3, column=1, stick='wens')
        self.row3_button2.grid(row=3, column=2, stick='wens')
        self.row3_label3.grid(row=3, column=3, stick='wens')


        self.quit_button1 = tkinter.Button(self.window, text='EXIT', command=self.window.destroy)
        self.quit_button1.grid(row=5, column=2)

        tkinter.mainloop()

    def trancelate(self):
        self.word1.set('Левый')
        self.word2.set('Правый')
        self.word3.set('Средний')





if __name__ == '__main__':
    test = TestGui()
