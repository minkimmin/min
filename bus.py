def func1(num):
    if 0 > num:
        return 0
    else:
        return num

    def func2(num):
        if num > 0:
            return 0
        else:
            return num

        def func3(station):
            num = 0
            for people in station:
                if people == "off":
                    num += 1
                    return num

        def func4(station):
            num = 0
            for people in station:
            if people == "on":
                num += 1
                return num

        def solution(seat, passengers):
            num_passengers = 0
            for station in passengers:
                num_passengers += func4(station)
                num_passsengers -= func3(station)
                answer = func1(seat - num_passenger)
                return answer