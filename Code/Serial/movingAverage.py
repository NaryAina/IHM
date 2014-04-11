def movingAverage(queue) :
    average = 0.0
    
    n = len(queue)
    #print n
    
    for i in range(n) :
       average +=  ( (n - i) * queue[i] ) / ( n*(n+1)/2 ) 
       
    return average