from utils import insert

def first(lhs, grammar, grammar_first):
    rhs = grammar[lhs]
    for i in rhs:
        k = 0
        flag = 0
        current = []
        confirm = 0
        flag2 = 0
        if(lhs in grammar and "`" in grammar_first[lhs]):
            flag2 = 1
        while(1):	
            check = []
            if(k>=len(i)):  # If the symbol is terminal, then to find First(X) = {X}
                if(len(current)==0 or flag == 1 or confirm == k or flag2 == 1):
                    grammar_first = insert(grammar_first, lhs, "`")
                break				
            if(i[k].isupper()):   # If the symbol is non-terminal, then to find First(Y1), then First(X) = First(Y1)
                if(grammar_first[i[k]] == "null"):
                    grammar_first = first(i[k], grammar, grammar_first)
                for j in grammar_first[i[k]]:
                    grammar_first = insert(grammar_first, lhs, j)
                    check.append(j)
            else:   # If it is terminal symbol, directly insert into grammar first 
                grammar_first = insert(grammar_first, lhs, i[k])
                check.append(i[k])
            if(i[k]=="`"):
                flag = 1
            current.extend(check)
            if("`" not in check): 

                if(flag2 == 1):
                    grammar_first = insert(grammar_first, lhs, "`")
                break
            else:
                confirm += 1
                k+=1
                grammar_first[lhs].remove("`")
    return(grammar_first)