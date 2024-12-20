# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 10:28:41 2020

@author: cm
"""


from networks import SentimentAnalysis

SA = SentimentAnalysis()


def predict(sent):
    """
    1: positif
    0: neutral
    -1: negatif
    """
    score1,score0 = SA.normalization_score(sent)
    if score1 == score0:
        result = 0
    elif score1 > score0:
        result = 1
    elif score1 < score0:
        result = -1
    return result

def main():
    while True:
        text = input('请输入需要判断的语句:')
        result = predict(text)
        if result == -1:
            print('判断为负面')
        elif result == 1:
            print('判断为正面')
        else:
            print('判断为中立')
        action = input('还要继续吗？输入q退出，任意键继续:')
        if action == 'q':
            break

if __name__ =='__main__':
    main()