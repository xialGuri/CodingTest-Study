def solution(s):
    numarr = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i in range(0,len(numarr)):
        s = s.replace(numarr[i],str(i));
    return int(s)