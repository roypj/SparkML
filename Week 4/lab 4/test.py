l =u'0,1,1,5,0,1382,4,15,2,181,1,2,,2,68fd1e64,80e26c9b,fb936136,7b4723c4,25c83c98,7e0ccccf,de7995b8,1f89b562,a73ee510,a8cd5504,b2cb9c98,37c9c164,2824a5f6,1adce6ef,8ba8b39a,891b62e7,e5ba7672,f54016b9,21ddcdc9,b1252a9d,07b5194c,,3a171ecb,c5c50484,e8b83407,9727dd16'
#splitStrng= ([i.split(',') for i in l])
#print(l.split(','))
#print(l.split(',')[1:])
print([(i, j) for i, j in enumerate(l.split(',')[1:])])

nonZeroIndices=[]
    for x in rawFeats:
      if x in OHEDict:
        nonZeroIndices.append(OHEDict[x]) 
        
        
    #nonZeroIndices = sorted([OHEDict[x] for x in rawFeats ])
    return SparseVector(numOHEFeats,sorted(nonZeroIndices),np.ones(len(nonZeroIndices)))
