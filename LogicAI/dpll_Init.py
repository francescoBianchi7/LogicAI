
def dpll_init(sentence):
    clauses = get_clause(sentence)
    literals = get_clause_literals(clauses)

    return literals, clauses

def get_clause(sentence):
    clauses = []
    for clause in sentence:
        clauses.append(clause)
    return clauses


def remove_literal(pures, literals):
    new_literals=[]
    for key in literals:
        if key not in pures:
            compl_l=complement(key)
            if compl_l not in pures:
                new_literals.append(key)
    return new_literals


def unit_clause(clauses):
    unit = {}
    for clause in clauses:
        if "," not in clause:
            unit[clause] = True
    return unit


def get_clause_literals(clauses):
    literals = set()
    for i in range(len(clauses)):
        lit = clauses[i]
        i=0
        while i in range(len(lit)):
            if maiusc(lit[i]):
                literals.add(lit[i])
            i += 1
    return literals


def get_literal_with_complement(clause):
    literals = []
    temp=""
    for l in range (len(clause)):
        if clause[l] !=",":
            temp += clause[l]
        if clause[l] == "," or l==len(clause)-1:
            literals.append(temp)
            temp = ""
    return literals


def check_contains(lit, literals):
    for l in literals:
        if l == lit:
            return True
    return False


def pure_literal(clauses, solved_literals):
    pures = {}
    foundPure = False
    temp2 = ""
    complement = ""
    for clause in clauses:
        #print("checking literals of", clause)
        temp = ""
        for var in range(len(clause)):
            #print("remove",clause[var])
            if clause[var] != ",":
                temp += clause[var]
            if clause[var] == "," or var==len(clause)-1:
                if "!" in temp:
                    complement = temp.replace("!", "")
                elif "!" not in temp:
                    complement = "!"+temp
                #print("checking ",complement," complement of",temp)
                foundPure = check_impure(complement, clauses)
                if foundPure:
                    if complement not in solved_literals:
                        pures[temp] = True
                    temp = ""
                else:
                    temp = ""
    return pures


def check_impure(complement, clauses):
    temp = ""
    for clause in clauses:
        temp=""
        for var in range(len(clause)):
            #  print("remove",t)
            if clause[var] != ",":
                temp += clause[var]
                #  print("temp2",temp,t)
            if clause[var] == "," or var == len(clause)-1:
                #  print("test", temp, complement)
                if temp == complement:
                    return False
                else:
                    temp = ""
    return True


def maiusc(c):
    if(c >= "A") and (c <= "Z"):
        return True
    else:
        return False

def complement(literal):
    complemented = "!"+literal
    return complemented

def complement_negative(literal):
    complemented = literal.replace("!", "")
    return complemented