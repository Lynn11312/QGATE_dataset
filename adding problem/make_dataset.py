import math as m
import numpy as np
import pandas as pd
import random
from pyqpanda import *

if __name__ == '__main__':
    """
    生成100个长度为100的数据序列,每个数据序列包含两个长度为100的随机数序列（Seq1和Seq2）和一个目标值（Seqy）
    """
    T = 100  # 时间序列长度
    iterations = 1500  # 迭代次数(生成的样本数量)
    Data = []
    for i in range(iterations):
        Seq1 = []
        Seq2 = [0.00001 for _ in range(T)]
        Seqy = []
        # rand_index = random.sample(range(0, T), 2)    # 随机数作索引，即随机位置
        rand_index1 = random.choice(range(0, T //2))
        rand_index2 = random.choice(range(T // 2, T))
        for j in range(T):
            data_1 = random.random()  # 生成0-1的随机数
            Seq1.append(data_1)
        # Seq2[rand_index[0]] = 0.99999   # 序列②中的两个数 变成0.9999
        # Seq2[rand_index[1]] = 0.99999
        Seq2[rand_index1] = 0.99999   # 序列②中的两个数 变成0.9999
        Seq2[rand_index2] = 0.99999
        # Y_true = Seq1[rand_index[0]] + Seq1[rand_index[1]]  # 序列①中的两个数相加
        Y_true = Seq1[rand_index1] + Seq1[rand_index2]  # 序列①中的两个数相加
        Seqy.append(Y_true)
        Seq = Seq1+Seq2+Seqy
        Data.append(Seq)
    Data = pd.DataFrame(Data)
    Data.to_csv('lp_100_1500.csv', header=None, index=None)
