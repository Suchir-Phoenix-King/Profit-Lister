# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 17:12:51 2022

@author: PC_RC
"""

month = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
profits = (23984, 74653, 12534, 20000, 34000, 45100, 97080, 12000, 67900, 56700, 34100, 78461)


max_profit = max(profits)
max_profit_index = profits.index(max_profit)
print(max_profit_index)

max_profit_month = month[max_profit_index]
print("The max profit of "+ str(max_profit)+ " was recorded in the month of "+ str(max_profit_month))

min_profit = min(profits)
min_profit_index = profits.index(min_profit)

min_profit_month = month[min_profit_index]
print("The min profit of "+ str(min_profit)+ " was recorded in the month of "+ str(min_profit_month))