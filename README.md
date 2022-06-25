# LogicAI
[main.py]
in questo modulo vengono impostate le variabile e chiamati i test
qui viene anche fatta la plot

[cnf.py]
questo modulo si occupa di creare delle "sentence" in formato k-cnf

[dpll_init]
inizializza il dpll solver, inoltre contiene le funzioni per trovare unit clauses e pure literals, e altre funzioni di supporto.

[DPLLsolver]
DPLL è la funzione solver.
In questo modulo sono inoltre implementate le funzioni per che determinano se una "clause" è risolta (chiamate solvedClause), e se un letterale appartiene
al modello (solvedLiterals).
ci sono le funzioni per determinare se una clausola è vera o falsa
la parte di "backtracking" è implementato assegnado sempre TRUE, ergo è possibile che alcuni cnf risultino UNSAT anche se sarebbero SAT.
