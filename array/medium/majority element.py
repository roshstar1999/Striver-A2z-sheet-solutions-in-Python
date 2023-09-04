def majorityElement(v: [int]) -> int:
    # Write your code here
    ct=0
    
    for i in v:
        if ct==0:
            element=i
            ct+=1
        elif i==element:
            ct+=1
        else:
            ct-=1
    
    #incase if its not guaranteed that the majority element exists within the array,add this below too, to check the count of the element if>n/2
  ########  
  ct=0  
    for i in v:
        if i==element:
          ct+=1
        if ct>len(v)//2:
          return element
    #######
    return element


