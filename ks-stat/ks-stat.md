## Статистика

Данные - бросал монетку 100 раз по 50 бросков и считал число решек.

Код программы:

```python
import pandas
import matplotlib.pyplot as plt
from scipy import stats

df1 = pandas.read_csv("experiments.csv")
df1['experiments'].plot(kind='bar')
print(df1.experiments.describe())
df12 = pandas.DataFrame(data={
    'df1': df1['experiments']
})

df12.plot.kde()
plt.show()
d1 = df12['df1']
print(stats.kstest(d1, 'norm', (d1.mean(), d1.std()), N=5000))
```

Вывод:
```
count    100.000000
mean      24.760000
std        3.679372
min       18.000000
25%       22.000000
50%       24.000000
75%       27.000000
max       33.000000
Name: experiments, dtype: float64
KstestResult(statistic=0.09182207462355452, pvalue=0.3468196238800587)
```

Картинки:

![](https://github.com/Munchhau5en/python.au/raw/main/ks-stat/figure_1.png)
![](https://github.com/Munchhau5en/python.au/raw/main/ks-stat/figure_2.png)

Данные...
```
0,21 
1,27
2,27
3,25
4,20
5,28
6,28
7,19
8,30
9,22
10,27
11,26
12,23
13,23
14,21
15,25
16,30
17,28
18,23
19,20
20,23
21,27
22,20
23,27
24,22
25,21
26,29
27,33
28,23
29,27
30,24
31,25
32,24
33,24
34,20
35,24
36,25
37,23
38,24
39,22
40,27
41,22
42,27
43,28
44,18
45,25
46,28
47,18
48,24
49,28
50,20
51,33
52,23
53,27
54,19
55,26
56,26
57,26
58,23
59,28
60,32
61,28
62,27
63,30
64,20
65,25
66,24
67,19
68,30
69,18
70,30
71,23
72,24
73,21
74,24
75,28
76,21
77,24
78,27
79,27
80,24
81,32
82,24
83,19
84,22
85,24
86,25
87,21
88,26
89,18
90,21
91,23
92,30
93,32
94,31
95,28
96,24
97,21
98,28
99,25
```
