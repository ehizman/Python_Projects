class Time_Class:
    def __init__(self, hour, minute, second):
        if 0 <= hour < 24:
            self.__hour = hour
        if 0 <= minute < 60:
            self.__minute = minute
        if 0 <= second < 60:
            self.__second = second
        print("Time has been set!")