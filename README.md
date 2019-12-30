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
    -------------------Round51-------------------
    2BC State:WN,ST,ST,SN
    Selector=01,Pred=T,Outcome=T,Hit
    Misprediction=0.098039
### Step:
#### 1.Set parameter: initial state
#### 2.Read input file:T,N,T,N,T,N,T,N
#### 3.REGstate function會顯示目前4個2BC的狀態
    REGstate()
    Example:
    2BC State:WN,ST,ST,SN
#### 4.history() function會記錄前兩筆結果也就是Outcome
##### select() function 根據history選擇prediction要使用的2BC
##### prediction() function 根據選擇的2BC做預測 T or N
##### changeREG() function 根據history以及Outcome去修改上次使用的2BC 
    Selector=01,Pred=T,Outcome=T,Hit
#### 5.Loop
    for i in range (len(outcome))
#### 6.Result:根據miss次數計算misspredicton
    Misprediction=0.098039
