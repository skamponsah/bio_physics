#!/usr/bin/env python


#Import python libraries to be used
import turtle
import random
import numpy as np
import matplotlib.pyplot as plt
import sys,math

'''
we want to perform a random walk
1. 1-dimensional latice: either left or right
2. 
3. Start at origin x=0
4. steps are of size 1
5. record final distination X
'''
#initialize variables
directions = [-1,1] #2 directions (left=-1,right=1)
turtle_direction={'-1':0,'1':180}#Would be used in turtle graph
choosen_directions = []#
points_visited=[]
final_X =[]

mean_x=0.0
var_x =0.0
R=0.0
R_ex=[]
R_ob=[]

def rand_walks(by_how_much, how_many,x=0):
    random.seed()
    for i in range(how_many):
        get_rand_direction = random.choice(directions)
	if get_rand_direction ==-1:
            choosen_directions.append(-1)
            x =x-1
	else:
	   choosen_directions.append(1)
           x=x+1
        points_visited.append(x)
    final_X.append(x)
 
if __name__ == '__main__':
    simulations = int(raw_input("How many times?:"))
    steps =[100,200,300,400,500,600,700,800,900]
    count =0
    for N in  steps:
	    #N = int(raw_input("Number of walks, N ="))
	    print "\nPlotting graph please wait....\n\nSimulation for N =",str(N)
	    for i in range(simulations):
	    	rand_walks(1, N)
		if i==simulations/2:
			print "...50%..."

	    #Find average of the a_i's
	    mean_x = sum(choosen_directions)/len(choosen_directions)
	    print 'Mean steps: ', mean_x
	    print  sum(points_visited)/len(points_visited)
	    for i in final_X:
		var_x +=i**2
	    var_x = var_x/simulations
	    R = math.sqrt(var_x)
	    print 'R from simulation = ', R
	    print 'R = root(N) = ',math.sqrt(N)
            R_ob.append(R)
            R_ex.append(math.sqrt(N))
	    plt.hist(final_X,bins=40) 
	    plt.title(str(simulations)+" times for N = "+str(N))
	    plt.xlabel("Points")
	    plt.ylabel("Frequency")          
	    plt.show()
    plt.title("Graph of Observed R against Expected R")
    plt.xlabel('Observed R')
    plt.ylabel('Expected R')
    plt.plot(R_ob,R_ex,'ro')
    plt.show()
       
    
