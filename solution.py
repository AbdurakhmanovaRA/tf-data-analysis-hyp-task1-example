import pandas as pd
import numpy as np
from scipy.stats import stats

chat_id = 241769496 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    stat_1, p = stats.ttest_ind(a = [x_cnt, y_cnt], b = [x_success, y_success])
    print(p)
    if p >= 0.06:
      flag = True
    else:
      flag = False
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    return flag # Ваш ответ, True или False
