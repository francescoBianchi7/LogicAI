import string
import random
import dpll_Init
def create_cnf_sentence(n,m,k):
    sentence=[]
    for i in range(m):
        clause=generate_random_clause(n, k)
        repetition=check_clause_repetition(clause,sentence)
        if not repetition:
            sentence.append(clause)
    return sentence


def generate_random_clause(n,k):
    top_char=chr(65+n)
    random_string = ""
    for i in range(k):
        rand=random.randint(0,1)
        random_letter=chr(random.randint(ord('A'), ord(top_char)))
        while check_letter_repetition(random_string,random_letter):
            random_letter = chr(random.randint(ord('A'), ord(top_char)))
        if rand == 0:
            random_string+=random_letter
        elif rand==1:
            random_string+=("!"+random_letter)
        if i != k-1:
            random_string+=","
    return (''.join(random_string))


def check_letter_repetition(string,letter):
    if letter in string:
        return True
    else:
        return False

def check_clause_repetition(clause, clauses):
    repeated_literals=[]
    literals=dpll_Init.get_literal_with_complement(clause)
    for c in clauses:
        for l in literals:
            if l in c:
                repeated_literals.append(l)
        if len(repeated_literals) == len(literals):
            return True
        repeated_literals.clear()
    return False