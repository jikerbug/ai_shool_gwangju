# 1주일 내용 10문제로 끝내기

# 1. 파이썬 조건문을 활용하여 장발장은 빵을 못먹게 하기
# - 실행 예시 : "장발장 차례 입니다, 빵을 드릴 수 없습니다."
# - 실행 예시 : "홍길동 차례 입니다, 빵을 하나 드리겠습니다."

people = ['홍길동', '성진', '심청이', '장발장', '심봉사']

for person in people:
    
    if(person is not '장발장'):
        print(person + " 차례 입니다, 빵을 하나 드리겠습니다.")
    else:
        print(person + ' 차례 입니다, 빵을 드릴 수 없습니다.')
# --------------------------------------------------------

# 2. 1번 문제의 구현된 부분을 함수로 바꾸기
# - 조건 : 입력값(사람 한 명씩) 을 받아서 빵을 먹으면 안되는 사람이면 0을, 먹어도 되면 1을 반환하기
# - 실행 예시 : "홍길동은 빵을 먹을 수 있는 사람 입니다."
# - 실행 예시 : "장발장은 빵을 먹을 수 있는 사람 입니다."
# 반복문을 활용하여 5 명 전원 다 출력 할 것


# is는 변수가 같은 Object(객체)를 가리키면 True
# ==는 변수가 같은 Value(값)을 가지면 True  **********->따라서 함수에서는 is 쓰면 안된다!
def is_bread_okay(person):
    if(not person == '장발장'):
        print(person + '은(는) 빵을 먹을 수 있는 사람입니다.')
        return 1
    else:
        print(person + '은(는) 빵을 먹을 수 없는 사람입니다.')
        return 0

for person in people:
    is_bread_okay(person)








# --------------------------------------------------------

# 3. 지역변수와 전역변수 이해하기

# 아래의 코드는 num_stamp 라는 전역변수를 함수 내에서 global 명령을 통해 수정가능하게 억지로 만든상태이다.
# 하지만, 함수의 기능과 본질을 생각하면 아래의 예시는 굉장히 바람직하지 못하다!
# global 명령은 안쓰는 것이 좋다!
# 그렇다면, global 명령을 사용하지 않고 아래의 로직을 함수의 입력값과 반환값을 활용하여 수정해보기!

num_stamp = 0  # 쿠폰 스탬프가 찍힌 횟수 (전역변수)


def stamp(num_stamp):
    """쿠폰 스탬프가 찍힌 횟수를 증가시키고, 화면에 출력한다."""
    
    num_stamp = num_stamp + 1  # 오류가 발생하지 않는다 (global 안쓰면 오류 발생함)
    print(num_stamp)
    return num_stamp


num_stamp = stamp(num_stamp)  # 화면에 1이 출력된다
num_stamp = stamp(num_stamp)  # 화면에 2가 출력된다


# --------------------------------------------------------

# 4. 클래스 이용하기
# 요구사항
# - 교통수단 클래스 만들기 (속성 : 이름, 가격, 출발시간, 도착시간 / 기능 : 출발시간, 도착시간 보기)
# - 비행기 클래스 만들기
# 속성 : 이름, 가격, 출발시간, 도착시간, 수하물 가능여부
# 기능 : 출발시간, 도착시간 보기, 수하물 맡기기(수하물이 가능하면 "수하물을 맡겼습니다!"출력, 불가능하면 "이 비행기는 수하물을 못맡깁니다!" 출력)
# - 기차 클래스 만들기
# 속성 : 이름, 가격, 출발시간, 도착시간, 좌석등급
# 기능 : 출발시간, 도착시간 보기, 좌석등급 보기

# 클래스를 상속을 활용해서 효율적으로 만들어 볼것! (메소드 오버라이딩)
# 두 개 이상의 인스턴스를 비행기, 기차 각각 만들어 볼것
class vehicle:
    def __init__(self, name, price, leave_time, arrive_time):
        self.name = name
        self.price = price
        self.leave_time = leave_time
        self.arrive_time = arrive_time
    
    def check_leave_time(self):
        print('출발시간은 ' + self.leave_time + '입니다.')

    def check_arrive_time(self):
        print('도착시간은 ' + self.arrive_time + '입니다.')

class airplane(vehicle):
    def __init__(self, name, price, leave_time, arrive_time, is_carrage):
        super().__init__(name, price, leave_time, arrive_time)
        self.is_carrage = is_carrage

    def hold_carrage(self):
        if self.is_carrage is True:
            print("수하물을 맡겼습니다!")
        else:
            print("이 비행기는 수하물을 못 맡깁니다!")




# 속성 : 이름, 가격, 출발시간, 도착시간, 좌석등급
# 기능 : 출발시간, 도착시간 보기, 좌석등급 보기

class train(vehicle):
    def __init__(self, name, price, leave_time, arrive_time, seat_class):
        super().__init__(name, price, leave_time, arrive_time)
        self.seat_class = seat_class

    def check_seat_class(self):
        print('이 기차의 등급은 ' + self.seat_class + '입니다.')

    def check_leave_time(self):
        print('이 기차의 출발시간은 ' + self.leave_time + '입니다.')


def class_test():
    asiana = airplane("보잉808", 150000, '13:00', '15:00', True)
    light_plane = airplane("경비행기", 30000, '11:00', '15:00', False)
    ktx = train("ktx", 49800, '08:34', '10:31', '1등급')

    asiana.check_arrive_time()
    asiana.hold_carrage()
    light_plane.hold_carrage()
    ktx.check_leave_time()
    ktx.check_seat_class()


class_test()
# --------------------------------------------------------

# 5. 문자열 이용하기


# 파이썬 io 하는거 2 문제
