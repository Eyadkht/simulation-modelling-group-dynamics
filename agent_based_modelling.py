import random
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Simulation Settings
HARD = "H"
LAZY = "L"

AGENT_EFFORT = {HARD:1, LAZY:0}

GROUP_NUMBER = 4

POPULATION = 10000

EFFORT = 0.5

class Agent():

    def __init__(self, agent_type, performance, mark):
        self.agent_type = agent_type
        self.performance = performance
        self.mark = mark

    def compare_performance(self, reference_agent):
        if reference_agent.performance > self.performance:
            return True
        return False

    def set_performance(self):
        self.performance = self.mark - EFFORT * AGENT_EFFORT[self.agent_type]

    def switch_strategy(self, reference_agent):
        probability = reference_agent.performance - self.performance
        if random.random() <= probability:
           # print("Imitated Successfuly", probability)
            self.agent_type = reference_agent.agent_type

    def __str__(self):
        return self.agent_type

class Group():

   def __init__(self):
          self.agents = []

   def list_agents(self):
       for x in self.agents:
           print(x.agent_type,x.mark, x.performance)

   def number_of_hard_agents(self):
       count = 0
       for agent in self.agents:
           if agent.agent_type == HARD:
               count = count + 1
       return count

   def number_of_lazy_agents(self):
       count = 0
       for agent in self.agents:
           if agent.agent_type == LAZY:
               count = count + 1
       return count

   def calculate_group_effort(self):
       h = self.number_of_hard_agents()
       l = self.number_of_lazy_agents()
       e = h*AGENT_EFFORT[HARD] + l*AGENT_EFFORT[LAZY]

       for a in self.agents:
           a.mark = e/GROUP_NUMBER
           a.set_performance()


list_agents = []

def create_population(population):
    count = 0
    list_agents.clear()
    for x in range(population):
        if count < population/2:
            list_agents.append(Agent(HARD,0,0))
        else:
            list_agents.append(Agent(LAZY,0,0))
        count += 1

def proportion_strategies(agents):
    hard_workers = 0
    lazy_workers = 0

    for a in agents:
        if a.agent_type == HARD:
            hard_workers +=1
        else:
            lazy_workers +=1
    print("Total Population",POPULATION)
    print("Hard Workers Percentage %", hard_workers,hard_workers/POPULATION)
    print("Lazy Workers Percentage %", lazy_workers,lazy_workers/POPULATION)
    return hard_workers/POPULATION,lazy_workers/POPULATION

def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]

def run_simulation():
    ## Groups Formation ##
    groups = [Group() for i in range(int(POPULATION/GROUP_NUMBER))]
    random_groups = list(chunks(random.sample(list_agents, POPULATION), GROUP_NUMBER))

    count = 0
    for element in random_groups:
        for a in element:
            groups[count].agents.append(a)
        #groups[count].list_agents()
        count = count + 1

    #print("~~~ Groups Formation ~~~")
    for g in groups:
        g.calculate_group_effort()
        #g.list_agents()
        #print("~~~")


    #for a in list_agents:
      #  print(a.agent_type,a.mark,a.performance)

    ## Pairwise Interaction ##
    random_individuals = list(chunks(random.sample(list_agents, POPULATION), 2))

    for pair in random_individuals:
        #print("Comparing Strategies.....")
        #print(pair[0].agent_type,pair[0].performance)
        #print(pair[1].agent_type,pair[1].performance)

        if pair[0].compare_performance(pair[1]):
            pair[0].switch_strategy(pair[1])

        elif pair[1].compare_performance(pair[0]):
            pair[1].switch_strategy(pair[0])

        #print("Imitation Results.....")
        #print(pair[0].agent_type,pair[0].performance)
        #print(pair[1].agent_type,pair[1].performance)



create_population(POPULATION)
list_runs = [0]
list_hard = [0.5]
list_lazy = [0.5]

proportion_strategies(list_agents)
RUNS = 1000

for x in range(100):
    print("## Run ##",x+1)
    run_simulation()
    hard,lazy = proportion_strategies(list_agents)
    list_runs.append(x)
    list_hard.append(hard)
    list_lazy.append(lazy)
    print("#######")

f, ax = plt.subplots(1)
ax.plot(list_runs,list_hard,marker='', markerfacecolor='blue', markersize=10, color='skyblue', linewidth=2)
ax.plot(list_runs,list_lazy,marker='',  markerfacecolor='red', markersize=10, color='red', linewidth=2)
ax.set_ylim(ymin=-0.1)
ax.set_ylim(ymax=1.1)
ax.legend(["Hard Workers","Lazy Workers"])

