from audioop import mul

my_dict={}

def func(num1, num2, oper):

    for j in oper:

        if j == 'add':
            my_dict.update({"add": num1+num2})

        if j == 'sub':
            my_dict.update({"sub": num1-num2})

        if j == 'mul':
            my_dict.update({"mul": num1*num2})

        if j == 'div':
            my_dict.update({"div": num1/num2})

    return my_dict

print(my_dict.items())