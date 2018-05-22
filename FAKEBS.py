# Fake Binary Search May Long 2018

    
t=int(input())
while(t!=0):
    t-=1
    n,q=[int(x) for x in input().strip().split()]
    a=[int(x) for x in input().strip().split()]
    sorted_a=sorted(a)  #sorted list 
    indexOf={} #retrieving index of elements in O(1) lookup
    index=0
    for ele in a:
        indexOf[ele]=index 
        index+=1
    
    index=0 #reset 
    countlessthan={}    #to predict number of elements less than ele
    countgreaterthan={} #to predict number of elements greater than ele
    for ele in sorted_a:
        countlessthan[ele]=index 
        countgreaterthan[ele]=n-1-index
        index+=1 
    
    while(q!=0):
        q=q-1
        x=int(input())
        low=0
        high=n-1 
        swapGreaterYes=0
        swapGreaterNo=0 
        swapLesserYes=0
        swapLesserNo=0 
        while(low<=high):
            
            mid=(low+high)//2 
            if(a[mid]==x):
                break
            elif(a[mid]<x and indexOf[x]>mid):
                low=mid+1
                swapLesserNo+=1 
            elif(a[mid]<x and indexOf[x]<mid): #FakeBS case 1
                high=mid-1 
                swapGreaterYes+=1 
            elif(a[mid]>x and indexOf[x]<mid):
                swapGreaterNo+=1 
                high=mid-1 
            elif(a[mid]>x and indexOf[x]>mid): #FakeBS case 2
                swapLesserYes+=1
                low=mid+1  
                
            
        neededswaps=max(swapLesserYes,swapGreaterYes) 
        ans=neededswaps

        #not enough elements in pool required for swapping
        if((swapLesserYes>countlessthan[x]- swapLesserNo) or (swapGreaterYes>countgreaterthan[x]- swapGreaterNo)):
            ans=-1 
       
        print(ans)
