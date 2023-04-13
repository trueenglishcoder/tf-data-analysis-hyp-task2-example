import pandas as pd
import numpy as np
from statsmodels.stats.weightstats import ttest_ind

chat_id = 346373029 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    _, pval, _ = ttest_ind(x, y, alternative = 'larger')
    return pval < 0.09
