# Check if the number provided is in the list or not:
def memr(a, x):
    if x == []:
        return False
    elif a == x[0]:
        return True
    else:
        return memr(a, x[1:])

if (memr(4, [1, 2, 3, 4])):
    print('found')
else:
    print('not found')


#EVEN ODD SEPERATOR
def even_odd(lst, rese=[], reso=[]):
    if lst == []:
        return rese, reso
    else:
        rese.append(lst[0]) if lst[0] % 2 == 0 else reso.append(lst[0])
    return even_odd(lst[1:], rese, reso)


# If the value provided is not list, append the result list;
def value_contain_var(ls, var, res=[]):
    if ls == []:
        return res
    elif ls[0] != var:
        res.append(ls[0])
    
    return value_contain_var(ls[1:], var, res)

# pretty self-explainable huh?
def divisbleOfNum(ls, num, res=[]):
    if ls == []:
        return res
    elif ls[0] % num != 0:
        res.append(ls[0])

    return divisbleOfNum(ls[1:], num, res)


# Mids Recursion Problem Solution
vowels = 'aeiouAEIOU'
def isVow(ls, vow=[], count=0):
    if ls == []:
        return vow, count
    elif ls[0] in vowels:
        vow.append(ls[0])
        count = count + 1
    return isVow(ls[1:], vow, count)

#Sum Nested List
def sum(ls):
    if ls == []:
        return 0
    elif type(ls[0]) == list:#type(ls[0]) is list:  # isinstance(ls[0], list): or type(ls[0]) == list
        return sum(ls[0]) + sum(ls[1:])
    else:
        return ls[0] + sum(ls[1:])
    


#displays series using rec

def series():
    num1 = int(input('Enter First: '))
    num2 = int(input('Enter Second: '))
    if num1 > num2:
        display_series(num2, num1)
    else:
        display_series(num1, num2)


def display_series(num1, num2):
    if num1 > num2:
        return
    else:
        print(num1)
        return display_series(num1+1, num2)


# Counts strings in a list ( list can be n-nested )
def countStr(ls, count=0):
    if ls == []:
        return count
    elif type(ls[0]) is list:
        return countStr(ls[1:], count + countStr(ls[0]))
    elif type(ls[0]) is str:
        return countStr(ls[1:], count + 1)
    return countStr(ls[1:], count)

print(countStr([10,'abc', 20 ,['20','fahad',100], 't', None, 10.5]))