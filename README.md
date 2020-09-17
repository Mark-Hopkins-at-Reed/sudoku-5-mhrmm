HW: Sudoku 5
------------

We've formulated a CNF sentence that encodes the rules of a valid Sudoku
board. Now if we only we could reason about it automatically. For instance,
if I partially fill in a board, can I leverage that CNF sentence to ask the
computer for a satisfying solution? That'd be nice, because then we could
use that to help us build new puzzles! You know, solvable puzzles, rather
than publishing impossible-to-solve Sudokus that frustrate the masses.

We'll need a way to check whether a sentence is satisfiable, so we need to
build a satisfiability solver, or SAT solver.

The first kind of solver we're going to build is a resolution solver. In
order to do so, let's first create some helpful data structures, methods, and
functions.

1. Extend the Clause class so that we can easily disjoin clauses using the 
   pipe operator. For instance, typing ```cnf.c('!a || b') | cnf.c('c || !e')```
   should return a Clause instance equal to ```cnf.c('!a || b || c || !e')```.
   If we disjoin two clauses with opposite-polarity literals (e.g. b and !b),
   then the operator should return None. Other edge cases are covered in
   the unit tests.

   Once you have a successful implementation, the following unit tests should
   succeed:
   
       python -m unittest test_part5.TestClauseDisjunction

2. In ```resolution.py``` create a function called ```resolve_symbol```
   that resolves a specified symbol, given two clauses. For instance, typing:
   
       resolve_symbol(cnf.c('!b || !c'), cnf.c('b || d'), 'b') 
       
   should return a Clause instance equal to:
   
       cnf.c('!c || d')
       
   There are two important edge cases. As with the disjunction operator
   above, if the resulting clause would contain opposite-polarity literals,
   (e.g. b and !b), then return None. Also, if the specified literal
   cannot be resolved (e.g. it doesn't appear in both clauses), then
   return None.

   Once you have a successful implementation, the following unit tests should
   succeed:
   
       python -m unittest test_part5.TestResolveSymbol


3. In ```resolution.py``` create a function called ```resolve```
   that, given two clauses, returns a list of all possible clauses ("resolvents")
   that can be obtained by calling ```resolve_symbol``` on each symbol in the
   two clauses. For instance, typing:
   
       resolve(cnf.c('!b || !c'), cnf.c('b || d'))
       
   should return a list of Clause instances equal to:
   
       [cnf.c('!c || d')]
       
   If no resolvents can be obtained, just return the empty list. What is
   the maximum length of the returned list? (No need to hand in an answer,
   but please do think it over.)
   
   Once you have a successful implementation, the following unit tests should
   succeed:
   
       python -m unittest test_part5.TestResolve

4. Finally, in preparation for writing a resolution solver, it could be
   convenient to have a priority queue set up for our specific purposes.
   Create a class called ```ClauseQueue``` such that we can construct
   a new instance by typing ```ClauseQueue()```. The class should support
   the following methods:
      - ```.empty()```: Returns True iff the queue is empty.
      - ```.pop()```: Returns the Clause in the queue with highest priority.
      Priority should be based on Clause length (i.e. the number of literals).
      Shorter Clauses should get higher priority. Break ties arbitrarily (for
      now).
      - ```.push(c)``` Adds Clause ```c``` to the queue if it hasn't already
      been added. Returns ```True``` if the Clause was successfully added (i.e.
      it hadn't been previously added); otherwise ```False```.

   Once you have a successful implementation, the following unit tests should
   succeed:
   
       python -m unittest test_part5.TestClauseQueue
