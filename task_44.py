# В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. 
# Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?

from pandas import DataFrame, get_dummies
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = DataFrame({'whoAmI':lst})
print(data.head(20))
print()
print("Результат: ")
print()
new_data = data
data.loc[new_data['whoAmI'] == 'human', 'human'] = 'True'
data.loc[new_data['whoAmI'] != 'human', 'human'] = 'False'
data.loc[new_data['whoAmI'] == 'robot', 'robot'] = 'True'
data.loc[new_data['whoAmI'] != 'robot', 'robot'] = 'False'
print(new_data[['human', 'robot']].head(20))