import operator as op

class Solution:
    def __init__(self):
        self.env = {
            'add': op.add,
            'mult': op.mul,
        }
        
    def atom(self, token):
        try: return int(token)
        except ValueError:
            try: return float(token)
            except ValueError:
                return str(token)

    def tokenize(self, expr):
        #print(expr)
        return expr.replace('(', ' ( ').replace(')', ' ) ').split()

    def read_from_tokens(self, tokens):
        #print(tokens)
        if len(tokens) == 0:
            assert False, 'len tokens is 0'
            
        token = tokens.pop(0)
        if token == '(':
            L = []
            while tokens[0] != ')':
                L.append(self.read_from_tokens(tokens))
            tokens.pop(0)
            return L
        elif token == ')':
            assert False, 'unexpected )'
        else:
            return self.atom(token)
    
    def parse(self, expr):
        return self.read_from_tokens(self.tokenize(expr))
    
    def eval_(self, parsed, env):
        if isinstance(parsed, str):
            return env[parsed]
        elif isinstance(parsed, (int, float)):
            return parsed
        elif parsed[0] == 'let':
            #print(parsed)
            env_copy = copy.copy(env)
            i = 1
            while i < len(parsed) - 1:
                symbol = parsed[i]
                exp = parsed[i+1]
                env_copy[symbol] = self.eval_(exp, env_copy)
                i += 2
            #print(self.env)
            
            return self.eval_(parsed[-1], env_copy)
        else:
            proc = self.eval_(parsed[0], env)
            args = [self.eval_(x, env) for x in parsed[1:]]
            return proc(*args)
        
    def evaluate(self, expression: str) -> int:
        parsed = self.parse(expression)
        return self.eval_(parsed, self.env)
