import tkinter as tk


class Calculator:
    """Программа по изучению tkintera"""

    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Калькулятор')
        self.root.geometry('240x240')

        self.root.bind('<Key>', self.press_key)

        self.entry = tk.Entry(self.root, justify=tk.RIGHT, relief=tk.SUNKEN, font=('Arial', 14, 'bold'))
        self.entry.grid(row=0, column=0, columnspan=4, stick='we')

        self.root.grid_columnconfigure(0, minsize=60)
        self.root.grid_columnconfigure(1, minsize=60)
        self.root.grid_columnconfigure(2, minsize=60)
        self.root.grid_columnconfigure(3, minsize=60)

        self.make_button('CE').grid(row=1, column=0, padx=3, pady=3, stick='wesn')
        self.make_button('%').grid(row=1, column=1, padx=3, pady=3, stick='wesn')
        self.make_button('*').grid(row=1, column=2, padx=3, pady=3, stick='wesn')
        self.make_button('/').grid(row=1, column=3, padx=3, pady=3, stick='wesn')

        self.make_button('7').grid(row=2, column=0, padx=3, pady=3, stick='wesn')
        self.make_button('8').grid(row=2, column=1, padx=3, pady=3, stick='wesn')
        self.make_button('9').grid(row=2, column=2, padx=3, pady=3, stick='wesn')
        self.make_button('+').grid(row=2, column=3, padx=3, pady=3, stick='wesn')

        self.make_button('4').grid(row=3, column=0, padx=3, pady=3, stick='wesn')
        self.make_button('5').grid(row=3, column=1, padx=3, pady=3, stick='wesn')
        self.make_button('6').grid(row=3, column=2, padx=3, pady=3, stick='wesn')
        self.make_button('-').grid(row=3, column=3, padx=3, pady=3, stick='wesn')

        self.make_button('1').grid(row=4, column=0, padx=3, pady=3, stick='wesn')
        self.make_button('2').grid(row=4, column=1, padx=3, pady=3, stick='wesn')
        self.make_button('3').grid(row=4, column=2, padx=3, pady=3, stick='wesn')
        self.make_button('=').grid(row=4, column=3, padx=3, pady=3, stick='wesn', rowspan=2)

        self.make_button('.').grid(row=5, column=0, padx=3, pady=3, stick='wesn')
        self.make_button('0').grid(row=5, column=1, padx=3, pady=3, stick='wesn')
        self.make_button('?').grid(row=5, column=2, padx=3, pady=3, stick='wesn')

        self.root.mainloop()

    def make_button(self, symbol):
        return tk.Button(text=symbol, bd=3, command=lambda: self.add_symbol(symbol))

    def add_symbol(self, symbol):
        value = self.entry.get()
        print(value)

        if len(value) == 2 and value[0] == '0' and value[1] != '.':
            value = value[1:]
        elif symbol == 'CE':
            self.entry.delete(0, tk.END)
        elif symbol == '=':
            self.count()
        else:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, value + symbol)

    def count(self):
        value = self.entry.get()
        self.entry.delete(0, tk.END)
        try:
            self.entry.insert(tk.END, eval(value))
        except ZeroDivisionError:
            self.entry.insert(tk.END, "ZeroDivisionError")
        except NameError:
            self.entry.insert(tk.END, "NameError")
        except SyntaxError:
            self.entry.insert(tk.END, "SyntaxError")
    def press_key(self, event):
        print(event)
        if event.char.isdigit() or event.char in '/*-+%':
            self.add_symbol(event.char)
        elif event.char == '\x7f':
            self.entry.delete(0, tk.END)
        elif event.char == '\x08':
            self.entry.delete(0, tk.END)
        elif event.char == '\r':
            self.count()


if __name__ == '__main__':
    calculator = Calculator()
