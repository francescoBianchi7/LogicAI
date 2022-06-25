import dpll_Init


def DPLL(clauses, literals, solved_clauses, solved_literals,first=""):
    numsolved=0
    if not literals:
        return False,solved_literals
    if not clauses and not solved_literals: #empty clause
        return False, solved_literals
    for key in solved_clauses:#checks if all clauses are true
        if solved_clauses[key]==True:
            numsolved += 1
    if numsolved == len(solved_clauses):
        return True, solved_literals

    solved_clauses = clause_is_false(solved_clauses, solved_literals, clauses)
    for key in solved_clauses:
        if solved_clauses[key]==False:
            print("clause",key,"is False")
            return False, solved_literals

    pures = dpll_Init.pure_literal(clauses, solved_literals)
    new_literals = dpll_Init.remove_literal(pures, literals)
    solved_literals, new_literals=solved_literal_from_pure(pures, solved_literals, new_literals)
    solvedClauses = solve_from_solved_literals(solved_literals, solved_clauses, clauses)
    new_clauses=removeClause(solvedClauses)
    new_clauses=remove_literal_from_clauses(new_clauses,solved_literals)
    if pures:
        return DPLL(new_clauses,new_literals,solvedClauses,solved_literals)

    new_clauses = removeClause(solvedClauses)
    new_clauses = remove_literal_from_clauses(new_clauses, solved_literals)
    unit = dpll_Init.unit_clause(new_clauses)
    solved_literals, solved_clauses=solve_from_unit_clauses(unit, solved_literals, solved_clauses)
    if unit:
        new_literals=remove_literal_via_unit(unit,new_literals)
        return DPLL(new_clauses, new_literals, solvedClauses, solved_literals)
    #if first!="":
        #return False,solved_literals
    new_literals, solved_literals, first = try_literal_value(literals, solved_literals)
    return DPLL(new_clauses, new_literals, solvedClauses, solved_literals, first)


    #return solved, solved_literals


def clause_is_true(clauses, key, solvedClauses):
    for clause in clauses:
        temp1 = ","+key
        temp2 = key+","
        if key in clause:
            solvedClauses[clause]=True
    return solvedClauses

def remove_literal_via_unit(unit,literals):
    for key in unit:
        if "!" in key:
            lit=dpll_Init.complement_negative(key)
            new_literals=literals.remove(lit)
        else:
            new_literals=literals.remove(key)
        return new_literals

def clause_is_false(solvedClauses, solved_literals, clauses):
    values = []
    clauseisFalse=None
    for clause in clauses:
        literals = dpll_Init.get_literal_with_complement(clause)
        for l in range(len(literals)):
            if literals[l] not in solved_literals:
                values.append(None)
            elif literals[l] in solved_literals:
                values.append(True)
            elif "!" in literals[l]:
                complement = dpll_Init.complement_negative(literals[l])
                if complement in clause:
                    values.append(False)
            elif "!" not in literals[l]:
                complement=dpll_Init.complement(literals[l])
                if complement in clause:
                    values.append(False)

        #print("clause-false",values)
        i=0
        if values and all(elem==False for elem in values):
            solvedClauses[clause]=False
            return solvedClauses
        values.clear()
    return solvedClauses


def removeClause(solvedClauses):
    new_clauses=[]
    for key in solvedClauses:
        temp=solvedClauses.get(key)
        if not temp:
            new_clauses.append(key)
    return new_clauses


def solve_from_unit_clauses(unit_clauses, solved_literals, solved_clauses):
    for key in unit_clauses:
        solved_literals[key] = True
        solved_clauses.update([(key, True)])
    return solved_literals, solved_clauses


def solve_from_solved_literals(solvedLiterals, solvedClauses, clauses):
    for key in solvedLiterals:
        solvedClauses = clause_is_true(clauses, key, solvedClauses)
    return solvedClauses


def solved_literal_from_pure(pures,solvedLiterals,literals):
    for key in pures:
        solvedLiterals[key] = pures[key]
    new_literals=dpll_Init.remove_literal(pures,literals)
    return solvedLiterals, new_literals


def remove_literal_from_clauses(clauses,solved_literals):
    new_clauses=[]
    for clause in clauses:
        new_clause=clause
        for lit in solved_literals:
            if "!" in lit:
                complement=dpll_Init.complement_negative(lit)
            else:
                complement=dpll_Init.complement(lit)
            if complement in clause:
                new_clause.replace(complement,"")
        new_clauses.append(new_clause)
    return new_clauses

def try_literal_value(literals, solved_literals):
    lit = literals.pop()
    first=lit
    solved_literals[lit] = True
    return literals,solved_literals, first

def remove_literal(literals,lit):
    new_literals=literals.remove(lit)
