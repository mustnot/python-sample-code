import os
import imgkit
import string
import random
import requests
from pyvirtualdisplay import Display

from script import chart_script

def draw():
    
    labels = [''.join(random.sample(string.ascii_lowercase, 4)) for _ in range(10)]
    label1_data = [random.randrange(10, 100) for i in range(10)]
    label2_data = [random.randrange(10, 100) for i in range(10)]


    html = chart_script.format(
        labels=str(labels),
        label1_data=str(label1_data),
        label2_data=str(label2_data)
    )

    with open('./html/chart.html', 'w') as f:
        f.write(html)

    display = Display(visible=0, size=(5, 5))
    display.start()

    file_path = './imgs/sample.png'
    if os.path.exists(file_path): os.remove(file_path)
    imgkit.from_file('./html/chart.html', file_path)

    return file_path

if __name__ == "__main__":
    draw()