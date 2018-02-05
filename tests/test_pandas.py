# -*- coding: utf-8 -*-

import pandas as pd

d = {'one' : pd.Series([1., 2., 3.], index=['a', 'b', 'c']),
     'two' : pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)


data = {'domain': pd.Series(['google.com'], index=['google']),
        'user': pd.Series(['f2a'], index=['google']),
        'password': pd.Series(['1234qwerty'], index=['google'])}

dataf = pd.DataFrame(data)

data2 = {'domain': 'gmail.com',
         'user': 'f2a',
         'password': '1234'}

dataf2 = pd.DataFrame(data2, index=['gmail'])

print(dataf2)

dataf3 = dataf2.append(dataf)
print(dataf3.loc['google'])

domain_column_find = dataf3.loc[dataf3['domain'] == 'google.com']
user_column_find = dataf3.loc[dataf3['user'] == 'f2a']

recover_for_domain = dataf3.loc[dataf3['domain'] == 'gmail.com']
recover_pass = dataf3.get_value('gmail','password')


dataf3.to_csv('../outputs/pass.csv',sep=';')