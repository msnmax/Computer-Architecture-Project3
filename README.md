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
 Index   | Entry1  | Entry2 |Entry3 |Entry4
 | ---------- | :-----------:  | :-----------: | :-----------:  | :-----------: |
 Index1    |     |     |      |     |
 Index2    |     |     |      |     | 

#### 4.Replace function會將Entry由右往左移並將新資料放置最後一格,最左邊則是最舊的資料,Setdata function則是會先判斷是否hit,如果hit回傳hit而LRU method則會在hit的同時把hit的資料放置最右邊
    def dataReplace(index,tag):
    def setdata(index,tag):

#### 5.Loop重複step4 判斷是否hit,然後移動data
    for i in range(len(tag)):
#### 6.Result:根據hit次數計算hit rate
    ----------------------------Round14----------------------------
    [['2C', 'E2', 'E8', 'E2', 'E4'], ['4C', 'E2', None, None, None]]
    Index=2C,Tag=E8,Hit
    [['2C', 'E2', 'E2', 'E4', 'E8'], ['4C', 'E2', None, None, None]]
    Hit Rate=0.571429
