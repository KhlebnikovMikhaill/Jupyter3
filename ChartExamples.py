# Программа построения графиков
 
import tkinter as tk

# Импорт внешних файлов
import chart1
import chart2
import chart3
import chart4
 
# Создание главного окна
window = tk.Tk()
window.geometry("450x600")
window.title("Программа построения графиков")

# Функция закрытия программы
def do_close():
    window.destroy()
    
# Добавление метки заголовка
lblTitle = tk.Label(text = "Примеры построения графиков", font = ('Helvetica', 16, 'bold'), fg = '#0000cc')
lblTitle.place(x=55, y=25)

# Добавление кнопки и метки для графика 1 (Синус)
btnChart1 = tk.Button(window, text = "График 1", font = ('Helvetica', 10, 'bold'), command=chart1.plot_chart)
btnChart1.place(x=40, y=115, width=90, height=30)

lblChart1 = tk.Label(text = "График синуса matplotlib")
lblChart1.place(x=170, y=122)

# Добавление кнопки и метки для графика 2 (Нормальное распределение)
btnChart2 = tk.Button(window, text = "График 2", font = ('Helvetica', 10, 'bold'), command=chart2.plot_chart)
btnChart2.place(x=40, y=165, width=90, height=30)

lblChart2 = tk.Label(text = "Нормальное распределение")
lblChart2.place(x=170, y=172)

# Добавление кнопки и метки для графика 3 (График FillBetween)
btnChart3 = tk.Button(window, text = "График 3", font = ('Helvetica', 10, 'bold'), command=chart3.plot_chart)
btnChart3.place(x=40, y=215, width=90, height=30)

lblChart3 = tk.Label(text = "График FillBetween")
lblChart3.place(x=170, y=222)

# Добавление кнопки и метки для графика 4 (Нормальное распределение - 3 графика)
btnChart4 = tk.Button(window, text = "График 4", font = ('Helvetica', 10, 'bold'), command=chart2.plot_chart2)
btnChart4.place(x=40, y=265, width=90, height=30)

lblChart4 = tk.Label(text = "Нормальное распределение - 3 графика")
lblChart4.place(x=170, y=272)

# Добавление кнопки и метки для графика 5 (Гистограмма SeaBorn)
btnChart5 = tk.Button(window, text = "График 5", font = ('Helvetica', 10, 'bold'), command=chart4.plot_chart)
btnChart5.place(x=40, y=315, width=90, height=30)

lblChart6 = tk.Label(text = "Гистограмма SeaBorn")
lblChart6.place(x=170, y=322)

# Добавление кнопки и метки для графика 6 (Сдвоенная гистограмма SeaBorn)
btnChart7 = tk.Button(window, text = "График 6", font = ('Helvetica', 10, 'bold'), command=chart4.plot_chart2)
btnChart7.place(x=40, y=365, width=90, height=30)

lblChart7 = tk.Label(text = "Сдвоенная гистограмма SeaBorn")
lblChart7.place(x=170, y=372)

# Добавление кнопки и метки для графика 7 ()
#btnChart3 = tk.Button(window, text = "График 7", font = ('Helvetica', 10, 'bold'), command=chart2.plot_chart)
#btnChart3.place(x=40, y=415, width=90, height=30)

#lblChart1 = tk.Label(text = "Описание графика")
#lblChart1.place(x=170, y=422)

# Добавление кнопки закрытия программы
btnClose = tk.Button(window, text = "Закрыть", font = ('Helvetica', 10, 'bold'), command = do_close)
btnClose.place(x=330, y=550, width=90, height=30)
 
# Запуск цикла ожидания
window.mainloop() 
