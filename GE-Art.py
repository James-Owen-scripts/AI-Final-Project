import numpy as np
from PIL import Image
import random
import math

# Define constants for algorithm
POPULATION = 100
INITIAL_GENES = 1500
GENERATIONS = 60000
MAX_RADIUS = 20
TARGET_ARR = np.asarray(Image.open("Canada-Goose.jpg"))

#create a base constant for each chromosome to use
WIDTH, HEIGHT, _ = TARGET_ARR.shape
BASE = np.zeros((WIDTH, HEIGHT, 3), dtype=np.uint8)

# assign all elements in BASE array to = 255. So everything is white
MAX_COLOR = 255
BASE[:, :] = MAX_COLOR

# create a circle array to be later placed on canvas
def circle(arr, radius, color):
    diameter = radius*2
    # nested for loop to create 2d array
    for i in range(diameter):
        for j in range(diameter):
            # distance variabel to finds the hypotenuse of the current distance from middle of the array
            distance = math.sqrt((radius - i) ** 2 + (radius - j) ** 2)
            # check if distance is >= radius. True = add color to that vector
            if (distance <= radius):
                arr[i, j] = color

    # return array
    return arr

# draw the circles on the canvas
def draw(chromosome):
    canvas = BASE.copy()
    
    # iterate through each gene in cromosome and add it to canvas
    for gene in chromosome:
        cArr = gene[0]
        diameter = gene[1] * 2
        locationX = gene[2]
        locationY = gene[3]

        # Merge gene with canvas only where color is different
        canvas[locationX:locationX + diameter, locationY:locationY + diameter] = np.where(cArr != 0, cArr, canvas[locationX:locationX + diameter, locationY:locationY + diameter])

    return canvas

# function to add a new circle to the canvas
def newCircle():
    # create radius for new circle
    radius = random.randint(0,MAX_RADIUS)
    diameter = radius * 2 # also use diameter variable

    # Assign circle to random point on canvas
    locationX = random.randint(0, WIDTH - diameter)
    locationY = random.randint(0, HEIGHT - diameter)

    # Create array for circle
    cArr = np.zeros((diameter, diameter, 3), dtype=np.uint8)
    color = [random.randint(0, MAX_COLOR), random.randint(0, MAX_COLOR), random.randint(0, MAX_COLOR)]

    # put color on cArr
    cArr = circle(cArr, radius, color)

    return [cArr, radius, locationX, locationY]

# fitness function to find how close the circle is to the target
def fitness(canvas):
    canvasArr = np.array(canvas, np.int16)
    targetArr = np.array(canvas, np.int16)
    score = (np.sum(np.abs(canvas - targetArr)) / MAX_COLOR * 100.0) / canvasArr.size
    return score

# mutation function
def mutation(population, gen):
    # genMut to keep track if the generation has passed 1/4 of total generations
    genMut = GENERATIONS//4
    odd = 2 # odds initially set to be between 0-2 for 3 options

    # if statement to check for if gen has passed 1/4 of total generations
    # if True odds are set between 0-1 for 2 options
    if (gen == genMut):
        odd = 1
    
    for i in range(len(population)):
        genes = population[i][1]
        mutOdds = random.randint(0,odd)

        # change 30 genes if muOdds = 2
        if (mutOdds == 2 and len(genes) > 30):
            for j in range(30):
                genes[random.randint(0,len(genes)-1)] = newCircle()

        # add a circle if mutOdds = 1
        elif (mutOdds == 1 or len(genes) < 5):
            genes.append(newCircle())
        
        # delete a circle if mutOdds = 0
        else:
            deleteGene = random.randint(0, len(genes)-1)
            genes.pop(deleteGene)

        # re-create population
        canvas = draw(genes)
        population[i] = [canvas, genes, fitness(canvas)]

    # return population
    return population


def crossOver(population):
    i = 0
    # iterate through half the population
    while(i != POPULATION//2):
        parent1 = population[i][1] # First parent
        parent2 = population[i+1][1] # Second parent
        child = [] # child of parent 1 and 2 
        
        # add half of first parent genes to child
        child.extend(g.copy() for g in parent1[:len(parent1)//2])
        # add half of second parent genes to child
        child.extend(g.copy() for g in parent2[len(parent1)//2:])

        # create new population member
        canvas = draw(child)
        population.append([canvas, child, fitness(canvas)])

        # add 1 to i
        i+=1
    
    # return new population
    return population

# main driver
def main():
    #initial population
    pop = list()

    for j in range(POPULATION):
        genes = list()
        for i in range(INITIAL_GENES):
            genes.append(newCircle())
        canvas = draw(genes)
        pop.append([canvas, genes, fitness(canvas)])

    print("Initial population created")


    # main generation loop
    for i in range(GENERATIONS):
        print(f"Generation {i+1}")

        # sort the population
        pop = sorted(pop, key=lambda x: x[2])

        # output best canvas every 100 generations
        if ((i+1)%100 == 0):
            result = Image.fromarray(pop[len(pop)-1][0])
            result.save(f"Output//gen-{i+1}.png")
            print(f"The total gene count of best id {len(pop[len(pop)-1][1])}")

        # Delete the population least fit
        pop = pop[:-POPULATION//2]

        # cross over population
        pop = crossOver(pop)

        # mutate population
        pop = mutation(pop,i)

    # Output all final canvases
    for i in range(len(pop)):
        result = Image.fromarray(pop[i][0])
        result.save(f"Output/Final Output/final-{i}.png")

    
main()