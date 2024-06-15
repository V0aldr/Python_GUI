import tkinter
import tkinter.font

class CanvasGui:

    def __init__(self):
        self.window = tkinter.Tk()
        self.size = '1200x900'
        self.window.geometry(self.size)
        self.window.title(f'ХОЛСТ{self.size}')

        self.top_frame = tkinter.Frame(self.window, borderwidth=1, relief='solid')
        self.top_frame.pack()
        self.top_label = tkinter.Label(self.top_frame, text='Верхняя рамка')
        self.top_label.pack()

        self.mid_frame = tkinter.Frame(self.window, borderwidth=1, relief='solid')
        self.mid_frame.pack()
        self.top_label = tkinter.Label(self.mid_frame, text='Средняя рамка')
        self.top_label.pack()

        self.bottom_frame = tkinter.Frame(self.window, borderwidth=1, relief='solid')
        self.bottom_frame.pack()
        self.top_label = tkinter.Label(self.bottom_frame, text='Нижняя рамка')
        self.top_label.pack()

        self.lines_frame = tkinter.Frame(self.top_frame, borderwidth=1, relief='solid')
        self.lines_frame.pack(side='left')
        self.lines_label = tkinter.Label(self.lines_frame, text='Рисование линий')
        self.lines_label.pack()

        self.canvas = tkinter.Canvas(self.lines_frame, width=200, height=200, borderwidth=1, background='white',
                                     relief='sunken')
        self.canvas.pack(side='left')

        # 3  линии
        self.canvas.create_line(0, 0, 199, 199)
        self.canvas.create_line(199, 0, 0, 199)

        # 3 посследовательные соеенённые линии
        # arrow.tk.FIRST - стрлочка-указатель в начале
        # arrow.tk.LAST - стрлочка-указатель в конце
        # arrow.tk.BOTH - стрлочка-указатель в обоих концах
        # dash - штрих-линия кортеж(5, 2) - 5 пикселей заполнено, 2 пропущено
        # fill - цвете(наплнение) линии
        # smooth - гладкость (по-умолчанию=False), smooth=True - превращает треугольник(3 линии) в петлю
        self.canvas.create_line(10, 10, 190, 10, 100, 190, 10, 10, arrow=tkinter.BOTH, dash=(5, 2), width=2,
                                fill='blue')

        # Прямоугольник
        self.rectang_frame = tkinter.Frame(self.top_frame, borderwidth=1, relief='solid')
        self.rectang_frame.pack(side='right')
        self.rectang_label = tkinter.Label(self.rectang_frame, text='Рисование прямоугольников')
        self.rectang_label.pack()

        self.canvas_r = tkinter.Canvas(self.rectang_frame, width=200, height=200, borderwidth=1, background='white',
                                       relief='sunken')
        self.canvas_r.pack(side='left')

        self.canvas_r.create_rectangle(10, 10, 190, 190, width=4, fill='red', outline='yellow')

        # Овал
        self.oval_frame = tkinter.Frame(self.mid_frame, borderwidth=1, relief='solid')
        self.oval_frame.pack(side='left')
        self.oval_label = tkinter.Label(self.oval_frame, text='Рисование Овалa')
        self.oval_label.pack()

        self.canvas_oval = tkinter.Canvas(self.oval_frame, width=200, height=200, borderwidth=1, background='white',
                                          relief='sunken')
        self.canvas_oval.pack(side='left')

        self.canvas_oval.create_oval(10, 40, 190, 160, width=2, dash=(6, 3), outline='Blue', fill='yellow')
        self.canvas_oval.create_oval(80, 80, 120, 120, width=2, fill='white')

        # Сектор
        # self.canvas_sector(имя холста).create_arc(10,10,190,190,(прямоугольник/овал) start=90(начальная позиция
        # сектора 90 градусов), extent=45(величина хода/отклонения сектора), fill='black')
        self.canvas_sector_frame = tkinter.Frame(self.mid_frame, borderwidth=1, relief='solid')
        self.canvas_sector_frame.pack(side='right')
        self.sector_label = tkinter.Label(self.canvas_sector_frame, text='Сектор')
        self.sector_label.pack()
        self.canvas_sector = tkinter.Canvas(self.canvas_sector_frame, width=200, height=200, borderwidth=1,
                                            background='white', relief='sunken')
        self.canvas_sector.pack()

        self.canvas_sector.create_arc(10, 10, 190, 190, start=90, extent=45, fill='black')
        self.canvas_sector.create_arc(10, 10, 190, 190, start=45, extent=45, style=tkinter.PIESLICE, fill='grey')
        self.canvas_sector.create_arc(10, 10, 190, 190, start=135, extent=45, style=tkinter.CHORD, fill='yellow')
        self.canvas_sector.create_arc(10, 10, 190, 190, start=180, extent=45, style=tkinter.ARC, fill='red')
        self.canvas_sector.create_arc(10, 10, 190, 190, start=225, extent=180, style=tkinter.PIESLICE, fill='red')

        # Полигон
        self.polygon_frame = tkinter.Frame(self.bottom_frame, borderwidth=1, relief='solid')
        self.polygon_frame.pack(side='left')
        self.polygon_label = tkinter.Label(self.polygon_frame, text='Полигон')
        self.polygon_label.pack()
        self.canvas_polygon = tkinter.Canvas(self.polygon_frame, width=200, height=200, borderwidth=1,
                                             background='white', relief='sunken')
        self.canvas_polygon.pack()

        self.canvas_polygon.create_polygon(60, 20, 100, 20, 140, 60, 140, 100, 100, 140,
                                           60, 140, 20, 100, 20, 60, fill='green', width=4, outline='black', smooth=False)


        # TEXT
        # self.canvas_text.create_text(100, 100, text='Привет, Мир!',
        # anchor= привязка относительно заданых координат tkinter.CENTER(N, W, S, E),
        # justify=tk.LEFT - выравнивание текста по краю рамки/поля,
        # font= - стиль текста задаётся отдельным объектом tkinter.font.Font(значение))
        self.text_frame = tkinter.Frame(self.bottom_frame, borderwidth=1, relief='solid')
        self.text_frame.pack(side='left')
        self.text_label = tkinter.Label(self.text_frame, text='TEXT')
        self.text_label.pack()
        self.canvas_text = tkinter.Canvas(self.text_frame, width=200, height=200, borderwidth=1,
                                             background='white', relief='sunken')
        # tkinter.font.Font(family='Helvetica'(Arial, Courier, Times New Roman etc.), size=14, weight = bold/normal,
        # sant=italic(наклонный текст), roman(прямой), underline=1/0 - подчеркивание, overstrike=1/0 - перчеркивание)
        my_font = tkinter.font.Font(family='Helvetica', size=14, weight='bold')
        self.canvas_text.create_text(100, 100, text='Привет, Мир!', font=my_font, anchor=tkinter.W)

        self.canvas_text.pack()

        # Control
        self.quit_button = tkinter.Button(self.window, text='ВЫЙТИ', command=self.window.destroy)
        self.quit_button.pack(side='bottom')

        tkinter.mainloop()


if __name__ == '__main__':
    canvas = CanvasGui()

