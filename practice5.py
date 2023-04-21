x = " global scope"
def outer_func():
    x= "enclosing scope"

    def inner_func():
        x = "local scope"
        print(x)
    inner_func()
outer_func()        