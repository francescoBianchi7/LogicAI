# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import sys
import fileinput
import numpy as np
import dpll_Init
import DPLLsolver
import cnf
from matplotlib import pyplot as plt
if __name__ == "__main__":
    sentence1=[]
    sentence2=[]
    sentence3=[]
    solvedClauses = {}

    with open ('inputs1.txt', 'r') as f:
        sentence1 = f.read().splitlines()
    print(sentence1)
    with open ('inputs2.txt', 'r') as f:
        sentence2 = f.read().splitlines()
    print(sentence2)
    with open ('inputs3.txt', 'r') as f:
        sentence3 = f.read().splitlines()
    print(sentence3)
    isSolved1 = False
    isSolved2 = False
    isSolved3 = False
    solvedLiterals1 = {}
    solvedLiterals2 = {}
    solvedLiterals3 = {}

    literals1, clauses1=dpll_Init.dpll_init(sentence1)
    solvedClauses1=dict.fromkeys(clauses1)
    print("first sentece", literals1, "\n", clauses1)
    isSolved1, solvedLiterals1=DPLLsolver.DPLL(clauses1, literals1,solvedClauses1,solvedLiterals1)

    literals2, clauses2 = dpll_Init.dpll_init(sentence2)
    print("second sentece",literals2,"\n",clauses2)
    solvedClauses2 = dict.fromkeys(clauses2)
    isSolved2, solvedLiterals2 = DPLLsolver.DPLL(clauses2, literals2, solvedClauses2, solvedLiterals2)

    literals3, clauses3 = dpll_Init.dpll_init(sentence3)
    print("third sentece", literals3, "\n", clauses3)
    solvedClauses3 = dict.fromkeys(clauses3)
    isSolved3, solvedLiterals3 = DPLLsolver.DPLL(clauses3, literals3, solvedClauses3, solvedLiterals3)

    print("first sentence has solution;", isSolved1, " with model", solvedLiterals1)
    print("second sentence has solution;", isSolved2, " with model", solvedLiterals2)
    print("third sentence has solution;", isSolved3, " with model", solvedLiterals3)

simbols = 15 #times 2 so it's 50 from -Z to Z
repeat_test= 5#how many times it gets repeated for num of clauses
next_num_clause = 15 #how many clauses to add
start_num_clauses = 15 #starting number of clauses
k=3# 3-CNF
 #num sat/total tests,each value is for a different number of clauses
clause_symbol_ratio=[]
m=0
for i in range(10):
    clause_symbol_ratio.append(m/(2*simbols))
    m += next_num_clause

P_sat = []

for i in range(len(clause_symbol_ratio)):
    times_sat_test=0
    for j in range(repeat_test):
        start_num_clauses = start_num_clauses+next_num_clause
        sentence = cnf.create_cnf_sentence(simbols, start_num_clauses, k)
        literals, clauses = dpll_Init.dpll_init(sentence)
        print(literals)
        solvedLiterals={}
        solvedClauses = dict.fromkeys(clauses)
        isSolved, solvedLiterals = DPLLsolver.DPLL(clauses, literals, solvedClauses,solvedLiterals)
        print(isSolved)
        if isSolved:
            times_sat_test += 1
    print(times_sat_test/repeat_test)
    P_sat.append(times_sat_test/repeat_test)

print(P_sat)
#creating graph
x=(clause_symbol_ratio)
y=list(P_sat)
plt.plot(x,y,label="p(satisfied)")
plt.xlabel("clause/symbol ratio (m/n)")
plt.ylabel("P(satisfiable)")
plt.legend()
plt.show()

#print(isSolved," with model",solvedLiterals)