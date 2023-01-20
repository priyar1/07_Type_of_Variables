''' The following are the variables which are valid '''
# a=1
# A=2
# _b=3
# _1=4
# c_a=5
# v_3=6
# _=7
# x_y3=8
# r6=9
# t_4_d=10 
# print(A)
# print(_b)
# print(_1) 
# print(c_a)
# print(v_3)
# print(_)
# print(x_y3)
# print(r6)
# print(t_4_d)
# print(ABC) # NameError: name 'ABC' is not defined

''' The following are the rules which are not valid '''
"""
.a=5
@=7
7_@4=6
$q=8
2_=9
r t=10
f 
"""
# print('hello'.isidentifier())
# print('4ello'.isidentifier())
# print('_4ello'.isidentifier())


# a='python'
# print(a.isidentifier())
# b='_hello'
# print(b.isidentifier())
# c='23hh'
# print(c.isidentifier())
# d='p_y'
# print(d.isidentifier())
# e='_'
# print(e.isidentifier())
# f='_@45'
# print(f.isidentifier())
# g='a b'
# print(g.isidentifier())


""" ways to assign the variables """
# First way to assign values
# a=1
# b=2
# c=3
# d=2
# e=4
# print(b)
# print(a)
# print(c)
# print(d)
# print(e)

"""ways to print values"""
# a=1
# b=2
# c=3
# d=2
# e=4
# print(a), print(b), print(c), print(d), print(e)
# print(a); print(b); print(c); print(d); print(e)
# print(a,b,c,d,e)
# print(e,e,b,e,a)

''' Second way to assign the values '''
# a=1, b=2, c=3, d=2, e=4  
# a=1; b=2; c=3; d=2; e=4  
# print(a); print(b); print(c); print(d); print(e)
# print(a,b,c,d,e) 
# print(a,b,c,d,e,f) 

"""Third way to assign the values"""
# a,b,c,d,e=1,2,3,4   # ValueError: not enough values to unpack (expected 5. got 4)
# a,b,c,d,e=1,2,3,4,5,6

# a,b,c,d,e=1,2,3,4,5
# print(a,b,c,d,e) 
# print(a);print(b);print(c);print(d);print(e)

'''Fourth way to assign the values'''
# a=d=2;b,c,e=1,3,4
# print(a,b,c,e,d) 
# print(a);print(b);print(c)