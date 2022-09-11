import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# 한글 폰트 사용을 위해서 세팅
from matplotlib import font_manager, rc
font_path = "C:/Windows/Fonts/NGULIM.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

from api.api import data_loading, dataset_extract

import os
dir= os.getcwd()

i= 1
file= os.listdir(os.path.join(dir, 'datasets'))[i]
file_dir= os.path.join('datasets', file)
graph_data= data_loading(file_dir)

for i in range(100):
    graph= dataset_extract(graph_data)
    plt.plot(np.arange(len(graph)), graph)
plt.title('지하공동구 화재 발생 시 시뮬레이션 데이터 그래프')
plt.show()