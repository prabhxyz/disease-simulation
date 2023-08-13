from input import *
import random
import matplotlib.pyplot as plt

def assign_parameters(disease_name):
    disease_name = disease_name.upper().strip()
    global TRANSMISSION_RATE, MIN_RECOVERY_TIME, MAX_RECOVERY_TIME
    if disease_name == "COVID-19":
        TRANSMISSION_RATE = random.uniform(0.2, 0.3)
        MIN_RECOVERY_TIME = 7
        MAX_RECOVERY_TIME = 14
    elif disease_name == "FLU":
        TRANSMISSION_RATE = random.uniform(0.2, 0.3)
        MIN_RECOVERY_TIME = 4
        MAX_RECOVERY_TIME = 7
    elif disease_name == "COMMON COLD":
        TRANSMISSION_RATE = random.uniform(0.1, 0.2)
        MIN_RECOVERY_TIME = 7
        MAX_RECOVERY_TIME = 10

# Assign parameters
assign_parameters(DISEASE)

# Initialize infected individuals with recovery times
infected_individuals = [{'recovery_time': random.randint(MIN_RECOVERY_TIME, MAX_RECOVERY_TIME + 1)} for _ in range(INITIAL_INFECTED)]

infected_history = []
susceptible_history = []

# Run simulation
for day in range(SIMULATION_DAYS):
    new_infections = 0

    for infected_person in infected_individuals:
        if random.random() < TRANSMISSION_RATE:
            new_infections += 1

        infected_person['recovery_time'] -= 1

    new_infections = min(new_infections, POPULATION_SIZE - len(infected_individuals))  # Limit new infections

    # Remove individuals with recovery_time = 0
    infected_individuals = [person for person in infected_individuals if person['recovery_time'] > 0]

    # Add new infected individuals
    infected_individuals.extend([{'recovery_time': random.randint(MIN_RECOVERY_TIME, MAX_RECOVERY_TIME + 1)} for _ in range(new_infections)])

    susceptible_history.append(POPULATION_SIZE - len(infected_individuals))
    infected_history.append(len(infected_individuals))

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(range(SIMULATION_DAYS), susceptible_history, label='Susceptible')
plt.plot(range(SIMULATION_DAYS), infected_history, label='Infected')
plt.xlabel('Days')
plt.ylabel('Number of People')
plt.title(f'Disease Spread Simulation ({DISEASE.upper().strip()})')
plt.legend()
plt.grid()
plt.show()
