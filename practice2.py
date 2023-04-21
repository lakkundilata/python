def myfun(**kwargs):
    for key,value in kwargs.items():
        print("%s == %s" % (key,value))

myfun(first='geeks', mid='for',last='geeks')        