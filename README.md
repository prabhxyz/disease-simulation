## Inspiration 💡

Imagine the incredible advantage we could have gained by predicting the COVID-19 pandemic in its early days! Just by analyzing the range of recovery days, we could have unlocked invaluable insights. This exciting realization fueled my determination to develop a tool capable of foreseeing the spread of future pandemics.

## What it does 🔨

Epidemia serves as a user-friendly website offering the opportunity to visually scrutinize the behaviors of prevailing illnesses and diseases, as well as novel maladies by considering their recovery time ranges. The platform boasts the flexibility to incorporate tailored parameters, encompassing factors such as hypothetical population and the count of infected individuals.

* <strong>Visual Insight:</strong> Generate graphical representations depicting the progression of disease or illness over time.
* <strong>Diverse Simulations:</strong> Simulate scenarios for prevalent infections like COVID-19, flu, and the common cold.
* <strong>Innovative Exploration:</strong> Conduct simulations for emerging diseases and illnesses, utilizing their recovery time range.
* <strong>Customizable Variables:</strong> Harness the potential of hypothetical inputs, including initial population and infected cases, to enhance the depth of simulations.

## How I built it 🛠️

<strong>Simulation:</strong> Epidemia utilizes backend simulation code to replicate the transmission of a disease throughout a given population. By adjusting parameters such as the disease's name, population size, initial infected count, simulation duration, and recovery time range, Epidemia tailors the simulation to specific scenarios. If the recovery time range isn't defined, Epidemia determines suitable parameters based on the disease's name. The simulation advances day by day, scrutinizing each infected person's likelihood of transmitting the disease based on a predefined transmission rate. The app then updates the recovery time for those infected and calculates new infections for the following day. As the simulation unfolds over the set number of days, Epidemia generates a visual representation showcasing the changing counts of susceptible and infected individuals, providing insights into the disease's progression within the chosen context.

<strong>Website:</strong> Epidemia integrates the power of Python, HTML/CSS, and JavaScript through Flask. The user-friendly interface features textboxes for inputting simulation variables. Upon clicking the 'Run Simulation' button, the website dynamically engages the simulation code. This code, in turn, leverages the capabilities of Matplotlib to generate a comprehensive graph depicting the simulation results, which are then displayed directly on the website.

## Challenges I ran into 🧗‍

* Epidemia was my first website made with Flask, learning it came with it's own challenges. 
* Conducting scientific research for accuracy about the diseases for the simulation was quite frustrating too. 
* Fixing issues in the simulation code was draining too because there were many variables.

## Accomplishments that I am proud of 🏆

* I take pride in creating my first website using Flask.
* I am surprised by the unexpectedly realistic results of the simulation I developed.
* It am proud to have successfully integrated Python with HTML, CSS, and JS for the project.

## What I learned 📚

I learnt to intergrate Python with web development using Flask, and improved further on my web development skills with HTML and CSS. 

## What's next for Epidemia - Disease Spread Simulator 🚀

* Explore expansion possibilities by transitioning the website to a React-based platform.
* Enhance speed by rewriting simulation code in C++ and potentially compiling it into a Python library.
* Integrate Machine Learning, focusing on polynomial regression, to build predictive models based on infection data generated by the project.