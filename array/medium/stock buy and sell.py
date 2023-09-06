def bestTimeToBuyAndSellStock(prices: [int]) -> int:
    # Write your code here.
    minn=prices[0]
    mp=[]
    for i in range(len(prices)):
        mp.append(minn)
        if prices[i]<minn:
            minn=prices[i]
    maxx=0
    for i in range(len(mp)):
        if maxx<prices[i]-mp[i]:
            maxx=prices[i]-mp[i]
    return maxx

