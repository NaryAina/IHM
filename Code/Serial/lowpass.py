def lowPass(queue, dt, rc) :
    otherQueue = []
    otherQueue.append(queue[0])
    
    alpha = dt / (rc + dt)
    
    for i in range(1, len(queue)) :
       otherQueue += [otherQueue[i - 1] + alpha * (queue[i] - otherQueue[i - 1])]
       
    return otherQueue[-1]