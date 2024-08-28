class MyDate:

    # 각 월에 마지막 날을 담은 리스트
    last_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 

    def __init__(self, year=0, month=0, day=0, hour=0, minute=0, sec=0):
        # 윤년 처리
        if MyDate.leap_year(year):
            MyDate.last_day[1] = 29
        else:
            MyDate.last_day[1] = 28

        # 월 유효성 검사: 1부터 12까지
        if not (0 <= month <= 12):
            raise ValueError("월에서 에러발생")
        
        # 일 유효성 검사: 해당 월의 마지막 날 이내
        if not (0 <= day <= self.last_day[month - 1]):
            raise ValueError(f"{day} 일에서 에러발생")
        
        # 시간, 분, 초 유효성 검사
        if not (0 <= hour <= 23):
            raise ValueError("시간에서 에러발생")
        if not (0 <= minute <= 59):
            raise ValueError("분에서 에러발생")
        if not (0 <= sec <= 59):
            raise ValueError("초에서 에러발생")
        
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.sec = sec


    
    def leap_year(year):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    
       
    def __add__(self, other):
        self_date = [self.year, self.month, self.day, self.hour, self.minute, self.sec]
        other_date = [other.year, other.month, other.day, other.hour, other.minute, other.sec]

        # 리스트 더하기
        sum_year = self_date[0] + other_date[0]
        sum_month = self_date[1] + other_date[1]
        sum_day = self_date[2] + other_date[2]
        sum_hour = self_date[3] + other_date[3]
        sum_minute = self_date[4] + other_date[4]
        sum_sec = self_date[5] + other_date[5]

        # 초, 분, 시, 일 반올림
        rounding_minute, sum_sec = divmod(sum_sec, 60)
        rounding_hour, sum_minute = divmod(sum_minute + rounding_minute, 60)
        rounding_day, sum_hour = divmod(sum_hour + rounding_hour, 24)
        sum_day += rounding_day 
        
        rounding_month, sum_day = divmod(sum_day - 1, self.last_day[sum_month - 1])  
        sum_month += rounding_month
        rounding_year, sum_month = divmod(sum_month - 1, 12) 
        sum_year += rounding_year
        
        
        sum_month += 1  # 1부터 시작
        sum_day += 1    # 1부터 시작

        return MyDate(sum_year, sum_month, sum_day, sum_hour, sum_minute, sum_sec) 

    def __sub__(self, other):
        sub_sec = self.sec - other.sec
        sub_minute = self.minute - other.minute
        sub_hour = self.hour - other.hour
        sub_day = self.day - other.day
        sub_month = self.month - other.month
        sub_year = self.year - other.year
        
    
        # 초 , 분 , 시 음수 처리
        if sub_sec < 0:
           sub_sec += 60
           sub_minute -= 1
        
        if sub_minute < 0:
           sub_minute += 60
           sub_hour -= 1
        
        if sub_hour < 0:
           sub_hour += 24
           sub_day -= 1

        # 일 처리
        if sub_day <= 0:
            sub_month -= 1
            if sub_month < 1:
                sub_month += 12
                sub_year -= 1


         # 윤년 고려 / 29일이 될 수 있음
            if sub_month == 2:  
                if MyDate.leap_year(sub_year):
                    sub_day += 29
                else:
                    sub_day += 28
            else:
                sub_day += self.last_day[sub_month - 1]


        # 월 처리
        if sub_month <= 0:
           sub_month += 12
           sub_year -= 1                

        
        return MyDate(sub_year, sub_month, sub_day, sub_hour, sub_minute, sub_sec)

  
         
    def __eq__(self, other):
        return (self.year == other.year and
                self.month == other.month and
                self.day == other.day and
                self.hour == other.hour and
                self.minute == other.minute and
                self.sec == other.sec)
                
    

    def __lt__(self, other):
       
       # 년
       if self.year < other.year:
           return True
       elif self.year > other.year:
           return False
        #월
       if self.month < other.month:
           return True
       elif self.month > other.month:
           return False
        # 일
       if self.day < other.day:
           return True
       elif self.day > other.day:
           return False
        # 시
       if self.hour < other.hour:
           return True
       elif self.hour > other.hour:
           return False
        # 분
       if self.minute < other.minute:
           return True
       elif self.minute > other.minute:
           return False
        # 초
       if self.sec < other.sec:
           return True
       else:
           return False   
    
    def __le__(self, other):
        return self <= other

    def __gt__(self, other):
        if self.year > other.year:
            return True
        elif self.year < other.year:
            return False

        if self.month > other.month:
            return True
        elif self.month < other.month:
            return False

        if self.day > other.day:
            return True
        elif self.day < other.day:
            return False

        if self.minute > other.minute:
            return True
        elif self.minute < other.minute:
            return False

        if self.sec > other.sec:
            return True
        else:
            return False 

    def __ge__(self, other):
        return self >= other 

    def __str__(self):
        return f'{self.year}/{self.month}/{self.day} {self.hour}:{self.minute}:{self.sec}'

if __name__ == '__main__':

    d1 = MyDate(2022, 4, 1, 14, 30)
    d2 = MyDate(2024, 8, 10, 23, 15)
    

    # d2 = MyDate(2024, 8, 100, 23, 10) # should raise an error 
    # d3 = MyDate(2024, 2, 30) # should raise an error 
    # MyDate.__init__(d3, 2024, 2, 30)
    
    # result = d1 + d2
    # print(result)

    d3 = MyDate(day = 1)
    assert d1 + d3 == MyDate(2022, 4, 2, 14, 30)
    print(d1+d3)
    assert d1 - d3 == MyDate(2022, 3, 31, 14, 30) 
    print(d1-d3)
    assert MyDate(2022, 1 ,1) - MyDate(day=30) == MyDate(2021, 12, 2) # 1-30+31
    assert MyDate(2022, 2 ,1) - MyDate(day=30) == MyDate(2022, 1, 2)  
    assert MyDate(2022, 3, 1) - MyDate(day=30) == MyDate(2022, 1, 31) 
    assert MyDate(2022, 4, 1) - MyDate(day=30) == MyDate(2022, 3, 2) 
    assert MyDate(2022, 5, 1) - MyDate(day=30) == MyDate(2022, 4, 1) 
    assert MyDate(2022, 6, 1) - MyDate(day=30) == MyDate(2022, 5, 2) 
    assert MyDate(2022, 7, 1) - MyDate(day=30) == MyDate(2022, 6, 1) 
    assert MyDate(2022, 8, 1) - MyDate(day=30) == MyDate(2022, 7, 2) 
    assert MyDate(2022, 9, 1) - MyDate(day=30) == MyDate(2022, 8, 1) 
    assert MyDate(2022, 10, 1)- MyDate(day=30) == MyDate(2022, 9, 2) 
    assert MyDate(2022, 11, 1)- MyDate(day=30) == MyDate(2022, 10,2) 
    assert MyDate(2022, 12, 1)- MyDate(day=30) == MyDate(2022, 11,2) 
  

    assert d1 < d2 

    
    d4 = MyDate(2023, 1, 31)
    d5 = MyDate(day = 30)
    assert d4 + d5 == MyDate(2023, 3, 2)
    
