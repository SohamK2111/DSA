
def findRelativeRanks(score):
    sortedscores = [0]*len(score)
    a = sorted(score, reverse=True)
    for i in range(len(a)):
        if i == 0:
            sortedscores[i] = "Gold Medal"
        elif i == 1:
            sortedscores[i] = "Silver Medal"
        elif i == 2:
            sortedscores[i] = "Bronze Medal"
        else:
            sortedscores[i] = i+1
    
    for i in range(len(score)):
        score[i] = sortedscores[a.index(score[i])]
    return score
    

score = [3,2,4,1,5]

print(findRelativeRanks(score))