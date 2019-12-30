
def indexnum(array):
    x=len(array)
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            if array[j]==array[i]:
                x=x-1
                break
    return x
def setindex(array):
    for i in range(len(array)):
        for j in range(indexnum(index)):
            if cache[j][0]==None:
                cache[j][0]=array[i]
                break
            elif cache[j][0]==array[i]:
                break

def dataReplace(index,tag):
    for i in range(entrysize-1):
        cache[index][i+1]=cache[index][i+2]
    cache[index][entrysize]=tag
def LRU_datamove(index,tag):  #LRU data move
    count=0
    for i in range(entrysize):      #check entry is full or not
        if cache[index][i+1]==None:
            count=count+1
        elif cache[index][i+1]==tag: #recording hit data postion
            pointer=i+1
    if cache[index][entrysize-count]==tag: #if hit data in last entry ,data not move because priority is same
        return 0
    else:
        for i in range(entrysize-count-1):
            if i+2==pointer:    #move data right->left,if position is hit data ignore
                if i!=0:
                    cache[index][i+1]=cache[index][i+3]
            else:
                cache[index][i+1]=cache[index][i+2]
    cache[index][entrysize-count]=tag
def setdata(index,tag):
    for i in range(indexnum(index)):
        if index==cache[i][0]:
            for j in range(entrysize):
                if cache[i][j+1]==tag:
                    global hit
                    hit=True
                    if(method=='LRU'):
                        LRU_datamove(i,tag)
                        break
                    else:
                        break
                elif cache[i][j+1]==None:
                    cache[i][j+1]=tag
                    hit=False
                    break
                elif j==entrysize-1:
                    dataReplace(i,tag)
                    hit=False

if __name__ == "__main__":
    f = open('./input3.txt', 'r')
    tag=[]
    index=[]
    entrysize=4
    hitrate=0
    lines = f.readlines()
    for line in lines:     #split index & tag
        str1=line.split(' ')
        str1[1]=str1[1].strip('\n')
        tag.append(str1[0])
        index.append(str1[1])

    cache=[[None for i in range(entrysize+1)] for j in range(indexnum(index))] #Crate  cache table
    setindex(index)
    hit=False
    method='LRU'
    print('Method:',method,'Entry:',entrysize)
    for i in range(len(tag)):
        print('----------------------------Round%d----------------------------'%(i+1))
        print(cache)
        setdata(index[i],tag[i])
        if(hit==True):
            print('Index='+index[i]+',Tag='+tag[i]+',Hit')
            hitrate=hitrate+1
        else:
            print('Index='+index[i]+',Tag='+tag[i]+',Miss')
    print(cache)
    hitrate=hitrate/len(tag)
    print('Hit Rate=%f'%hitrate)


    f.close()
