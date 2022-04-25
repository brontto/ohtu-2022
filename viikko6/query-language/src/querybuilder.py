
from matchers import And, All, HasAtLeast, HasFewerThan, PlaysIn, Or


class QueryBuilder:
    def __init__(self, matchers = All()):
        self._matchers = matchers
    
    def playsIn(self, team):
        return QueryBuilder(And(self._matchers, PlaysIn(team)))
    
    def hasAtLeast(self, num, atrib):
        return QueryBuilder(And(self._matchers, HasAtLeast(num, atrib)))
    
    def hasFewerThan(self, num, atrib):
        return QueryBuilder(And(self._matchers, HasFewerThan(num, atrib)))
    
    def oneOf(self, m1, m2):
        return QueryBuilder(Or(m1, m2))
    
    def build(self):
        return self._matchers
