# Программа построения графиков
 
import tkinter as tk

# Импорт внешних файлов
import chart1
import chart2
import chart3
import chart4
 
# Главная функция

def main():
    
    # График синуса matplotlib
    chart1.plot_chart
    
    # График нормального распределения
    chart2.plot_chart
    
    # График FillBetween
    chart3.plot_chart
    
    # Нормальное распределение - 3 графика
    chart2.plot_chart2
    
    # Гистограмма SeaBorn
    chart4.plot_chart
    
    # Сдвоенная гистограмма SeaBorn
    chart4.plot_chart2
    
    return 0

if __name__ == '__main__':
    main()

