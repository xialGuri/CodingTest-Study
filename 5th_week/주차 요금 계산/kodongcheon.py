import math
def solution(fees, records):
    arr1 = {}
    arr2 = {}
    results = []
    for record in records:
        clock, car_number, status = record.split()
        if status == "IN":
            arr1[car_number] = clock
        else:
            if car_number in arr2:
                arr2[car_number] = arr2[car_number] + (int(clock[:2]) - int(arr1[car_number][:2]))* 60 + int(clock[-2:]) - int(arr1[car_number][-2:])
            else:
                arr2[car_number] = (int(clock[:2]) - int(arr1[car_number][:2]))* 60 + int(clock[-2:]) - int(arr1[car_number][-2:])
            del arr1[car_number]
    for car_number in arr1:
        if car_number in arr2:
            arr2[car_number] = arr2[car_number] + (23 - int(arr1[car_number][:2]))* 60 + 59 - int(arr1[car_number][-2:])
        else:
            arr2[car_number] = (23 - int(arr1[car_number][:2]))* 60 + 59 - int(arr1[car_number][-2:])
    arr2 = sorted(arr2.items())
    for car_number, time in arr2:
        if time <= fees[0]:
            result = fees[1]
        else:
            result = fees[1] + math.ceil((time-fees[0])/fees[2]) * fees[3]
        results.append(result)
    return results