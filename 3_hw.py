def max_num(num_1: int, num_2:int) -> int:
    print(max(num_1, num_2))

max_num(10, 15)

def find_dif(num_1, num_2) -> bool:
    print("yes" if num_1 - num_2 == 135 else "No")

find_dif(1, 2)

def get_season(month: int) -> str:
    season_dict = {1: "зима", 2: "зима", 12: "зима",
                   3: "весна", 4: "весна", 5: "весна",
                   6: "лето", 7: "лето", 8: "лето",
                   9: "осень", 10: "осень", 11: "осень"
                   }
    if 1<= month <= 12:
        print(season_dict[month])
    else:
        print("Неверный номер месяца")

get_season(6)

def foo_1(num_1: int, num_2: int, num_3: int) -> bool:
    print("yes" if num_1 > 10 and num_2 > 10 and num_3 > 10 else "no")

foo_1(45,12,1)

def find_sum(num_list: list) -> int:
    res = 0
    for i in num_list:
        if i > 0:
            res += 1
    print(res)

find_sum([1,1,2,5,-7])

def find_day_nums(num_years: int, num_months: int) -> int:
    print(num_years * 365 + num_months * 29)

find_day_nums(4, 4)

