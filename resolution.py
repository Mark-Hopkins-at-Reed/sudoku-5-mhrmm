import queue

def resolve_symbol(clause1, clause2, symbol):
    if (symbol in clause1 and 
        symbol in clause2 and
        ((clause1[symbol] and not clause2[symbol]) or
         (not clause1[symbol] and clause2[symbol]))):
            return clause1.remove(symbol) | clause2.remove(symbol)
    else:
        return None

def resolve(clause1, clause2):
    resolvents = []
    for sym in clause1.symbols() & clause2.symbols():
       resolvent = resolve_symbol(clause1, clause2, sym)  
       if resolvent is not None:
           resolvents.append(resolvent)
    return resolvents
    

class ClauseQueue:
    def __init__(self, 
                 queue = queue.PriorityQueue(), 
                 priority_function = lambda clause: len(clause)):
        self.queue = queue
        self.priority_function = priority_function
        self.cached_clauses = set([])
        
    def push(self, clause):
        is_new_clause = (not clause in self.cached_clauses)
        if is_new_clause:
            self.queue.put((self.priority_function(clause), clause))
            self.cached_clauses.add(clause)
        return is_new_clause
    
    def pop(self):
        if not self.empty():
            return self.queue.get()[1]
        else:
            return None
    
    def empty(self):
        return self.queue.empty()
    

