import pandas as pd
import numpy as np
from scipy.stats import norm
import math

chat_id = 441218136 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    p1 = x_success / x_cnt
    p2 = y_success / y_cnt

    se1 = math.sqrt(p1 * (1 - p1) / x_cnt)
    se2 = math.sqrt(p2 * (1 - p2) / y_cnt)

    z_score = (p2 - p1) / math.sqrt(se1**2 + se2**2)

    p_value = 1 - norm.cdf(abs(z_score))

    return p_value < 0.05
