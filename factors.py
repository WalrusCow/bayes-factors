class Factor():
    def __init__(self, vars, probabilities):
        """ Initialize a Factor with some set of variables and their
        corresponding probabilities. """
        self.vars = tuple(vars)
        self.probabilities = tuple(probabilities)

    def __mul__(self, other):
        """ Multiply two factors. """
        pass

    def __str__(self):
        """ Return the table. """
        maxVar = max(len(v) for v in self.vars)
        pass


    def restrict(self, variable, value):
        """ Restrict a variable to a given value. """
        if variable not in self.vars:
            raise ValueError('Given variable {} not in factor'.format(variable))

        index = self.vars.index(variable)
        newVars = tuple(v for v in self.vars if v != variable)
        newProbs = []

        for vals, prob in probabilities:
            # Keep only entries with the correct value for the variable
            if vals[index] != value: continue
            # Remove the value at the index of our variable to restrict
            newVals = tuple(v for i, v in enumerate(self.vars) if i != index)
            newProbs.append((newVals, prob))

        # Immutability 4eva
        return Factor(newVars, newProbs)

    def sumout(self, variable):
        """ Sum out a given variable. """
        pass

    def normalize(self):
        """ Normalize probabilities. """
        pass

def multiply(f1, f2):
    return f1 * f2

def restrict(factor, var, val):
    return factor.restrict(var, val)

def sumout(factor, var):
    return factor.sumout(var)

def normalize(factor):
    return factor.normalize()

def inference(factorList, queryVars, hiddenVars, evidence):
    """ Compute P(queryVars | evidence) by variable elimination.  This first
    restricts the factors according to the evidence, then sums out the hidden
    variables, in order.
    Finally, the result is normalized to return a probability over a
    distribution that sums to 1.
    """

a = Factor(['a', 'b'],
           [((True, False), 0.1),
            ((True, True), 0.9),
            ((False, False), 0.5),
            ((False, True), 0.5)])
