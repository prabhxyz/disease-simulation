import create_data

# Parameters
DISEASE = "common cold"  # Disease name
POPULATION_SIZE = 800  # Total population size
INITIAL_INFECTED = 500  # Initial number of infected individuals
SIMULATION_DAYS = 90  # Number of simulation days

# Create data
create_data.create_data(DISEASE, POPULATION_SIZE, INITIAL_INFECTED, SIMULATION_DAYS)