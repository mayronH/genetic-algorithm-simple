import random

def foo(x, y, z):
    return 3 * x**3 - 5 * y**2 + 10*z

def objective_function(x, y, z):
    return foo(x,y,z) - 100

def fitness(s):
    ans = objective_function(s[0],s[1],s[2])
    
    if ans == 0:
        return 9999999
    
    return abs(1/ans)


def gen_zero(size):
    solutions = []
    
    for _ in range(size):
        solutions.append( (random.uniform(0,10000), 
                        random.uniform(0,10000), 
                        random.uniform(0,10000)))
        
    return solutions


def genetic_algorithm(interations, solutions):
    for i in range(interations):    
        solutions = sorted(
            solutions,
            key=lambda s: fitness(s),
            reverse= True
        )
                
        if fitness(solutions[0]) >= 9999999:
            return solutions[0], i
        
        bestsolutions = solutions[:100]
        
        variables = []
        for s in bestsolutions:
            variables.append(s[0])
            variables.append(s[1])
            variables.append(s[2])
            
        new_gen = []
        
        for _ in range(len(solutions)):
            var1 = random.choice(variables)
            var2 = random.choice(variables)
            var3 = random.choice(variables)
            
            if(random.random() < 0.5):
                var1 = var1 * random.uniform(0.99, 1.01)
                var2 = var2 * random.uniform(0.99, 1.01)
                var3 = var3 * random.uniform(0.99, 1.01)
                
            new_gen.append((var1, var2, var3))
            
        solutions = new_gen
        
    return solutions[0], i
        
def main():
    solutions = gen_zero(1000)
    bestsolution, gen = genetic_algorithm(10000, solutions)
    
    print(f'The algorithm runs {gen} generations and found {bestsolution} as the best solution')
    print("---------------------------------------------------------------------------------------------------------------------")
    print(f'Result: {foo(bestsolution[0], bestsolution[1], bestsolution[2])}')
    
    

if __name__ == "__main__":
    main()