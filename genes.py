import random

POPULATION_SIZE = 100
GENERATIONS = 10
MUTATION_RATE = 0.01 

population = []
for _ in range(POPULATION_SIZE):
    gene1 = random.choice(['A', 'a'])
    gene2 = random.choice(['A', 'a'])
    population.append([gene1, gene2])

for gen in range(GENERATIONS):
    new_generation = []
    
    for _ in range(POPULATION_SIZE):
        parent1 = random.choice(population)
        parent2 = random.choice(population)
        child_gene1 = random.choice(parent1)
        child_gene2 = random.choice(parent2)
        
        if random.random() < MUTATION_RATE:
            child_gene1 = 'A' if child_gene1 == 'a' else 'a'
            
        new_generation.append([child_gene1, child_gene2])
    
    population = new_generation
    
    counts = {"AA": 0, "Aa": 0, "aa": 0}
    for person in population:
        person.sort() 
        genotype = "".join(person)
        counts[genotype] += 1
        
    print(f"Generation {gen}: {counts}")