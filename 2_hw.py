def task_1() -> None:
    var_1:int = 10
    var_2:float = 10.1
    var_3:str = "hello"
    var_4:list = [10, 20, -5, 15]
    var_5:bool = False

    print(f"var_1: {type(var_1)}")

task_1()


def task_2()-> list:
    a = [1, 2, 3, 5, 8, 13, 21] #последовательность Фибоначчи
    print(a[:3])

task_2()


def task_3(var) -> int:
    print(var*var)

task_3(7)