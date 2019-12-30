# Computer-Architecture/Project3
## 簡介
* 實作Cache replacement
  * FIFO
  * LRU
* SETUP
  * Environment:WIN10
  * IDE:Pycharm 4.0 Python 3.7
  * Language:Python
### Parameter:
Initial:
```py    
method='LRU'
entrysize=4
```
### Input: 
    Eample :
    E4 2C
    E2 2C
    E4 2C
    E3 2C
    E5 2C
    E4 2C
    E2 2C
    E2 4C
    E4 2C
    E8 2C
    E2 2C
    E2 4C
    E4 2C
    E8 2C
### Output: 
    Method: LRU Entry: 4
    ----------------------------Round1----------------------------
    [['2C', None, None, None, None], ['4C', None, None, None, None]]
    Index=2C,Tag=E4,Miss
    ----------------------------Round14----------------------------
    [['2C', 'E2', 'E8', 'E2', 'E4'], ['4C', 'E2', None, None, None]]
    Index=2C,Tag=E8,Hit
    [['2C', 'E2', 'E2', 'E4', 'E8'], ['4C', 'E2', None, None, None]]
    Hit Rate=0.571429
### Step:
#### 1.Set parameter: entrysize //可設定entry個數 method//可設定為LRU or FIFO

#### 2.Read input file:
    Tag Index
     E2   2C
     E2   4C
     E4   2C
     E8   2C

#### 3.indexnum(index) 判斷總共有幾種index 根據個數創建需要的table 
    cache=[[None for i in range(entrysize+1)] for j in range(indexnum(index))] #Crate  cache table

#### 4.history() function會記錄前兩筆結果也就是Outcome
##### select() function 根據history選擇prediction要使用的2BC
##### prediction() function 根據選擇的2BC做預測 T or N
##### changeREG() function 根據history以及Outcome去修改上次使用的2BC 
    Selector=01,Pred=T,Outcome=T,Hit
#### 5.Loop
    for i in range (len(outcome))
#### 6.Result:根據miss次數計算misspredicton
    Misprediction=0.098039
