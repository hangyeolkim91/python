def test():
    print(__name__)

#모듈의 테스트 코드가 들어가고 최상위 이름공간이 아니면 실행 되지 않는다.
if __name__ == "__main__":
    test()