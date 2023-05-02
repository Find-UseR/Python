letters = "abcdefghijklmnopqrstuvwxyzABCEDFGHIJKLMNOPQRSTUVWXYZ"
def is_variable(pattern):
    return (type(pattern) is str  and pattern[0] == '?' and len(pattern) > 1
         and pattern[1] != '*' and pattern[1] in letters and ' ' not in pattern)

def contains_tokens(pattern):
    return type(pattern) is list and len(pattern) > 0

def match_variable(var, replacement, bindings):
    binding = bindings.get(var)
    if not binding:
        bindings.update({var: replacement})
        return bindings
    if replacement == bindings[var]:
        return bindings
    return False

def is_segment(pattern):
    return (type(pattern) is list
            and pattern  and len(pattern[0]) > 2
            and pattern[0][0] == '?'   and pattern[0][1] == '*'
            and pattern[0][2] in letters   and ' ' not in pattern[0])

def match_segment(var, pattern, input, bindings, start=0):
    if not pattern:
        return match_variable(var, input, bindings)
    word = pattern[0]
    try:
        pos = start + input[start:].index(word)
    except ValueError:
        return False
    var_match = match_variable(var, input[:pos], dict(bindings))
    match = match_pattern(pattern, input[pos:], var_match)
    if not match:
        return match_segment(var, pattern, input, bindings, start + 1)
    return match

def match_pattern(pattern, input, bindings=None):
    if bindings is False:
        return False
    if pattern == input:
        return bindings
    bindings = bindings or {}
    if is_segment(pattern):
        token = pattern[0]  # segment variable is the first token
        var = token[2:]  # segment variable is of the form ?*x
        return match_segment(var, pattern[1:], input, bindings)
    elif is_variable(pattern):
        var = pattern[1:]
        return match_variable(var, [input], bindings)
    elif contains_tokens(pattern) and contains_tokens(input):
        return match_pattern(pattern[1:],
                             input[1:],
                             match_pattern(pattern[0], input[0], bindings))
    else:
        return False

operators = "+-*/%"
numbers = "0123456789"
letters = "abcdefghijklmnopqrstuvwxyzABCEDFGHIJKLMNOPQRSTUVWXYZ"
student_rules = [
    ('find ?*a' , ['To-find' ,'=', '?a']),
    ('?*a is equal to ?*b' , ['?a' ,'=', '?b']),
    ('?*a makes ?*b' , ['?a' ,'=', '?b']),
    ('?*a are calculated by ?*b' , ['?a' ,'=', '?b']),
    ('?*a calculated by ?*b' , ['?a' ,'=', '?b']),
    ('?*a can be calculated as ?*b' , ['?a' ,'=', '?b']),
    ('?*a calculated as ?*b' , ['?a' ,'=', '?b']),
    ('?*a can be ?*b' , ['?a' ,'=', '?b']),
    ('?*a equal to ?*b' , ['?a' ,'=', '?b']),
    ('?*a equals ?*b', ['?a', '=', '?b']),
    ('?*a is ?*b' , ['?a' ,'=', '?b']),
    ('?*a are ?*b' , ['?a' ,'=', '?b']),
    ('?*a in ?*b' , ['?a' ,'=', '?b']),
    ('?*a plus ?*b', ['?a', '+', '?b']),
    ('?*a minus ?*b', ['?a', '-', '?b']),
    ('?*a divided by ?*b', ['?a', '/', '?b']),
    ('twice ?*a' , ['2' ,'*', '?a']),
    ('sum ?*a and ?*b' , ['?a' ,'+', '?b']),
    ('adding ?*a and ?*b' , ['?a' ,'+', '?b']),
    ('distributed into ?*a and ?*b', ['?a', '+', '?b']),
    ('divided into ?*a and ?*b', ['?a', '+', '?b']),
    ('one half ?*a' , ['?a' ,'/', '2']),
    ('half ?*a' , ['?a' ,'/', '2']),
    ('square ?*a' , ['?a' ,'*', '?a']),
    ('?*a times ?*b' , ['?a' ,'*', '?b']),
    ('?*a multiplied by ?*b' , ['?a' ,'*', '?b']),
    ('?*a multiplied with ?*b' , ['?a' ,'*', '?b']),
    ('difference between ?*a and ?*b' , ['?b' ,'-', '?a']),
    ('?*a % less than ?*b' , ['?b' ,'/', ['1', '-', ['?a', '/', '100']]])
]
def toeqstr(elst):
    ans = ''
    if type(elst) is str:
        return elst
    for item in elst:
        if type(item) is list:
            ans = ans + " ( " + toeqstr(item) + " )"
        else:
            if ans == '':
                ans= item
            else:
                ans = ans + ' '+ str( item)
    return ans
def replace_item(n,o,lst):
    if lst == []:
        return []
    elif o == lst:
        return n
    elif type(lst) is not list:
        return lst
    else:
        ans = replace_item(n,o,lst[1:])
        ans.insert(0,replace_item(n,o,lst[0]))
        return ans

def translate_to_exp(eqwlst):
    print('Input: "', toeqstr(eqwlst),'"')
    for pattern, response in student_rules:
        pattern = pattern.split()
        bindings = match_pattern(pattern, eqwlst)
        if bindings:
            print('Rule:"',toeqstr(pattern),'",[', toeqstr(response),']')
            print('Binding:', bindings)
            for var,val in bindings.items():
                #print(var)
                tval = translate_to_exp(val)
                response = replace_item(tval,'?'+var,response)
            print('Output:',response)
            return response
    if eqwlst == []:
        return eqwlst
    print('Output:','"',eqwlst[0],'"')
    return eqwlst[0]


def remove_noise(txt):
    nwords =['a','the','number','of','this','if','that',
				'$',',and','his' ,'while']
    for w in nwords:
        if txt.count(w) > 0:
            txt = [a for a in txt if a != w]
    return txt


def student():
 for i in range(5):
    userinput = input("Enter Statement:")
    userinput = userinput.lower()
    engEqs = userinput.split('.')
    eqs = []
    for engeq in engEqs:
        engeq = engeq.split()
        eqwlst = remove_noise(engeq)
        eq1 = translate_to_exp(eqwlst)
        eqs.append(eq1)
    eqs = [eq for eq in eqs if eq != []]
    solve_equations(eqs)

def solve_equations(eqs):
    print("UNSOLVED EQUATIONS")
    print_equations(eqs)
    print('SOLVED EQUATIONS')
    solved = solve(eqs)
    print_equations(solved)

def print_equations(eqs):
    for eq in eqs:
        print(toeqstr(eq))

def solve(eqs,solved=[]):
    if len(eqs) == 0:
        return solved
    ans = find_one_unknowneq(eqs)
    var = ans[0]
    eq = ans[1]
    if eq != [] and var is not None:
        sol=solve_equation(var,eq)
        value = sol[1]
        eqs.remove(eq)
        eqs = replace_item(value, var,eqs)
        solved.append([var,'=',value])
        temp= solve(eqs,solved)
        return temp
    return solved

def solve_equation(var, eq):
    eq2 = isolate(var, eq)
    return eq2[0], str(eval(toeqstr(eq2[2])))

def find_one_unknowneq(eqs):
    for eq in eqs:
        ans = one_unknown2(eq)
        count = ans[1]
        var = ans[0]
        if count == 1:
            return var,eq
    return None,[]

def one_unknown2(equation):
    c = 0
    var = None
    for item in equation:
        if type(item) is list:
            ans= one_unknown2(item)
            c += ans[1]
            if ans[1] != 0:
                var = ans[0]
        else:
            flag = False
            for ch in item:
                if ch in letters:
                    flag = True
            if flag == True:
                c += 1
                var = item
    return var,c

def in_exp(itm, lst):
    if type(lst) is str:
        return itm == lst
    elif lst == []:
        return False
    elif type(lst) is list:
        return in_exp(itm, lst[0]) or in_exp(itm, lst[1:])

def reverse_op(op):
    if op == '+':
        return '-'
    elif op == '-':
        return '+'
    elif op == '*':
        return '/'
    elif op == '/':
        return '*'
    elif op == '=':
        return '='

def isolate(var, eq):
    lhs= eq[0]
    op = eq[1]
    rhs= eq[2]
    if var == lhs: #CASE 1: X = A
        return eq
    elif var == rhs:
        return [rhs, op, lhs]
    elif type(lhs) is str:
        return isolate(var, [rhs,op,lhs])
    elif type(rhs) is list and op == '=' and in_exp(var,rhs):
        return isolate(var, [rhs,op,lhs])
    elif in_exp(var,lhs[0]):
        return isolate(var, [lhs[0], '=', [rhs, reverse_op(lhs[1]), lhs[2]]])
    elif lhs[1] == '+' or lhs[1] == '*':
        return isolate(var, [lhs[2], '=', [rhs, reverse_op(lhs[1]), lhs[0]]])
    else:
        return isolate(var, [lhs[2], '=', [lhs[0], lhs[1], rhs]])

student()