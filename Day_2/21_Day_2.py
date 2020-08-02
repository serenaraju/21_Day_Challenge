#Basic demo of decorators

def fun1(fun):
    def wrap():
        print("Hey")
        fun()
        print("Good Day!")
    return wrap
@fun1
def fun2():
    print("Hi! I'm function 2")

fun2()

#Decorators with arguments

def fun3(fun):
    def wrap(*args,**kwargs): #If the function in wrapper has an argument mention it in wrapper as well
        print("Hey")
        fun(*args,**kwargs)
        print("Good Day!")
    return wrap
@fun3
def fun4(name):
    print("{} is a part of function 4!".format(name))

fun4("This")


#Decorator problem from HackeRank (Standardize Mobile Number Using Decorators)
def wrapper(f):
    def fun(l):
        num = list()
        for item in l:
            if len(item) > 10:
                item = item[-10:]
                new_str = "+91" + " " + item[:5] + " " + item[5:]
                num.append(new_str)
            else:
                new_str = "+91" + " " + item[:5] + " " + item[5:]
                num.append(new_str)
        
        
        f(num)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 



