#kwargs : key with arguments

# dictionary as a parameter

def my_fun(**kwargs):
    for k,v in kwargs.items():
        print(f"{k} = {v}")

my_fun(firstname="jadav",lastname="durgesh",subject="python")