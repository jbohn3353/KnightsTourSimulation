import pickle
import os
import time
import tour_maker
import tour_util
import numpy as np
import matplotlib.pyplot as plt

# runs an <attempts> number of simulations starting at <active_position>
# also prints diagnostics for those simulations
def collect_data_for_position_with_diagnostics(active_position, attempts):

	unique_tours_list = tour_util.pull_tour_list(active_position)

	start_size_of_tours_list = len(unique_tours_list)
	num_of_attempts = float(attempts)
	failed_tours = 0

	print("Simulating...")

	start_time = time.time()
	for sim_num in range(int(num_of_attempts)):
		if sim_num%50 == 0:
			print("Sim "+ str(sim_num) + ", " + 
				  str(round(((time.time()-start_time)*1000))) + " ms elapsed")

		new_tour = tour_maker.run_game(active_position)

		if len(new_tour) != 64:
			failed_tours += 1
		elif not new_tour in unique_tours_list:
			unique_tours_list.append(new_tour)
	
	end_size_of_tours_list = len(unique_tours_list)
	new_unique_tours = end_size_of_tours_list - start_size_of_tours_list
	proportion_of_new_tours = new_unique_tours / num_of_attempts

	print("Starting position: " + str(active_position))
	print("Time Elapsed: " + 
		   str(round(((time.time()-start_time)*1000))) + "ms")
	print("Average time per simulation: " +
		   str(round(((time.time()-start_time)*1000))/num_of_attempts) + "ms")
	print("The number of unique tours before simulation was " + 
		   str(start_size_of_tours_list))
	print("The number of failed tours was " + str(failed_tours))
	print("The number of attempted simulations was " + 
		   str(num_of_attempts))
	print("The number of unique tours after simulation was " + 
		   str(end_size_of_tours_list))
	print("The number of unique tours found during this simulation was " +
	       str(new_unique_tours))
	print("The proportion of all simulated tours that were unique was " + 
		   str(proportion_of_new_tours))
	
	tour_util.put_tour_list(active_position, unique_tours_list)

# runs an <attempts> number of simulations starting at <active_position>
def collect_data_for_position(active_position, attempts):

	unique_tours_list = tour_util.pull_tour_list(active_position)

	start_size_of_tours_list = len(unique_tours_list)
	num_of_attempts = float(attempts)
	failed_tours = 0

	for sim_num in range(int(num_of_attempts)):

		new_tour = tour_maker.run_game(active_position)

		if len(new_tour) != 64:
			failed_tours += 1
		elif not new_tour in unique_tours_list:
			unique_tours_list.append(new_tour)

	end_size_of_tours_list = len(unique_tours_list)
	new_unique_tours = end_size_of_tours_list - start_size_of_tours_list
	proportion_of_new_tours = new_unique_tours / num_of_attempts
	proportion_of_failed_tours = failed_tours / num_of_attempts

	tour_util.put_tour_list(active_position, unique_tours_list)

	return (proportion_of_new_tours, proportion_of_failed_tours)

# runs a user inputted number of simulations and checks if they're unique
# prints diagnostics for each starting location and then shows a heat map
# of starting locations and the current number of unique tours from each
# location
def collect_all_data():
	n_attempts= int(input("How many times would you like to simulate each " +
					      "starting position (~1 minute per 100 attempts): "))

	start_time = time.time()
	last_time = time.time()

	visual = [[None for _ in range(8)] for _ in range(8)]

	for position in range(64):
		analytics = collect_data_for_position(position, n_attempts)
		print("Position " + str(position) + " currently has " +
			  str(len(tour_util.pull_tour_list(position))) + " unique tours."
			  +"\n\tProportion of new tours = " + str(analytics[0])
			  +"\n\tProportion of failed tours = " + str(analytics[1])
			  +"\n\tTime for position = " +
			  str(round((time.time()-last_time) * 1000)) + "ms")

		last_time = time.time()

		visual[int(position/8)][position%8] = len(tour_util.pull_tour_list(position))

	tour_util.make_graph(visual)

	print("Total time elapsed: " + 
		   str(round(((time.time()-start_time)*1000))) + "ms")
