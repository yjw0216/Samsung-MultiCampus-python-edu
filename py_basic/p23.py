# 예외처리
# 프로그램은 안정적으로 작동해야 하고 죽으면 안된다!
# 내가 작성한 코드를 try로 감싸서 잘 못 입력된 부분에 대해 죽지 않고 정상적으로 다시 작동할 수 있게 처리해준다.

try:       ## 정상 코드
    print(1)
    print(1/0)
    print(2)
except Exception as e:  ## 오류를 잡는 부분 // 오류나면 실행디는 부분
    print(3,e)          
else:      ## 위에서 오류가 없으면 실행되고 오류가잇으면 실행 안되는 부분
    print(4)
finally:   ## 최종적으로 무조건 수행되는 것
    print(5)
