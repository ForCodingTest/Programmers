def solution(cap, n, deliveries, pickups):    
    ans = 0
    di, pi = n-1, n-1
    while di >= 0 or pi >= 0:
        while di >= 0 and deliveries[di] == 0:
            di -= 1
        while pi >= 0 and pickups[pi] == 0:
            pi -= 1
        ans += (di + 1) * 2 if di >= pi else (pi + 1) * 2
        
        dcap, pcap = cap, cap
        for i in range(di, -1, -1):
            box = deliveries[i] if deliveries[i] <= dcap else dcap
            deliveries[i] -= box
            dcap -= box
            if deliveries[i] > 0:
                break
        
        for i in range(pi, -1, -1):
            box = pickups[i] if pickups[i] <= pcap else pcap
            pickups[i] -= box
            pcap -= box
            if pickups[i] > 0:
                break
            
    return ans
