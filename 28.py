def weightcal(coins,left,right):
    sum=0
    for i in range(left,right):
        sum+=coins[i]
    
    w=sum/(max(right-left,1))
    return w
global count

def findFalseCoin(coins,start,end):
    count=0
    if(start>=end ):
        return start
    else:
        w_left=weightcal(coins,start,int( (end+start)/2)  )
        # print(w_left)
        w_right=weightcal(coins,int( (end+start)/2),end)
        # print(w_right)
        if (w_left==w_right ):
            return -1
        elif(w_left<=w_right):
            index=findFalseCoin(coins,start,int( (end+start)/2))  
        elif(w_left>=w_right):
            index=findFalseCoin(coins,int( (end+start)/2),end)
        return index
            
            
coins=list(map(eval,(input().split(','))))
n=findFalseCoin(coins,0,len(coins))
if n==-1:
    print("Fake coin is not found")
else:
    print("Fake coin:{}".format(n))


