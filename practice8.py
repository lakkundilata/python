var1=lambda n : n*n            #n value is 2 (2*2=4)
var2=lambda n : n*n*n          #n value is 4(4*4*4
ans=var1(2)
print(ans)
print(var2(ans))

def call_func():
    ans = var1(2) + 1
    print ("from user def:",ans)

call_func() 
