def solution(fees, records):
    import math
    a=[]
    d={e[6:10]:0 for e in records}
    for e in records:
        time=int(e[:2])*60+int(e[3:5])
        if e[11:]=='IN':
            time=-time
        d[e[6:10]]+=time
    for k in d.keys():
        if d[k]<=0:
            d[k]+=1439
        d[k]-=fees[0]
    for carnum in sorted(d):
        if d[carnum]<=0:
            a.append(fees[1])
        else:
            a.append(fees[1]+math.ceil(d[carnum]/fees[2])*fees[3])
    return a
#가독성 내다버린 코드
'''
if(1):
    fees=[180, 5000, 10, 600]
    records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
    #[14600, 34400, 5000]
elif 0:
    fees=[120, 0, 60, 591]
    records=["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]
    #[0, 591]
else:
    fees=[1, 461, 1, 10]
    records=["00:00 1234 IN"]
    #[14841]

solution(fees,records)
'''

'''
records[:5] - records[:2],records[3:5]
records[6:10]
records[11:]
'''
