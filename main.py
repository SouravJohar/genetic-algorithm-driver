from evolution import Evolution, Species

# define a species (gene pool, gene length)
species = Species()

# define a set of 10 organisms of species `Species`
organisms = Evolution(species, pop_size=10)

organims.create()
fittest_organism = organisms.evolve(evolve_until_thresh_reached=True)
