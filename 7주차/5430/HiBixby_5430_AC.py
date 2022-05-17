from collections import deque
for _ in range(int(input())):#테스트 케이스 개수 T 만큼 반복
    command=input() #수행할 함수 입력 받기
    n=int(input()) #배열에 들어있는 수의 개수 n
    q=deque(eval(input())) # 배열 입력 받기

    if n<command.count('D'): #D가 배열 요소 개수보다 많으면 error 출력
        print('error')
    else: #일반적인 경우
        step=1 #정방향 설정
        for p in command:
            if p=="R": #함수 R이면 flag변수 토글
                step*=-1
            else: #함수 D일때 정방향이면 popleft 뒤집힌 방향이면 pop
                q.popleft()if step==1 else q.pop()

        print(str(list(q)[::step]).replace(" ","")) #명령 수행후 바뀐 배열 출력