import pandas as pd
import numpy as np


def data_loading(file_dir):
    graph_data= pd.read_csv(file_dir, encoding='cp949')
    graph_data.loc[(graph_data.Temperature < 0), ['Temperature']] = 0
    graph_data.Time= graph_data.Time.astype('int')
    return graph_data

def dataset_extract(graph_data):
    ascending= []
    for i in range(len(graph_data)-1):
        if (graph_data.Temperature[i+1] - graph_data.Temperature[i]) > 0:
            ascending.append(\
                sorted(np.random.uniform(graph_data.Temperature[i], graph_data.Temperature[i+1], (graph_data.Time[i+1] - graph_data.Time[i])))
                )
        else:
            ascending.append(\
                list(np.flip(sorted(np.random.uniform(graph_data.Temperature[i+1], graph_data.Temperature[i], (graph_data.Time[i+1] - graph_data.Time[i])))))
                )
    graph_data= np.array(sum(ascending,[]))
    return graph_data
