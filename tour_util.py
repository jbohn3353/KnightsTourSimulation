import pickle
import os
import numpy as np
import matplotlib.pyplot as plt

#given a starting location <start_pos> 
#pulls the list of lists from that locations file
def pull_tour_list(start_pos):
	file_name = "unique_tours_files/Position"+str(start_pos)+"UniqueToursList.txt"
	tour_list = []
	if os.path.isfile(file_name) and os.path.getsize(file_name) != 0:
		active_file = open(file_name,"rb")
		tour_list = pickle.load(active_file)
	else:
		active_file = open(file_name,"wb")
	active_file.close()
	return tour_list

#given a starting location <start_pos>
#and and updated tour list <tour_list>
#updates the file for the given location with the new list
def put_tour_list(start_pos, tour_list):
	file_name = "unique_tours_files/Position"+str(start_pos)+"UniqueToursList.txt"
	active_file = open(file_name,"wb")
	unique_tours_list = pickle.dump(tour_list, active_file)
	active_file.close()

#This generates a heat map formatted for the problem given a 2d list
def make_graph(two_d_list):	
	col_labels = ['', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
	row_labels = list(reversed(range(1,9)))
	row_labels.insert(0,'')

	grid = np.matrix(two_d_list)
	
	fig, ax = plt.subplots(1,1)

	ax.imshow(grid, cmap='YlOrRd', interpolation='nearest')
	ax.set_xticklabels(col_labels)
	ax.set_yticklabels(row_labels)

	for (j,i),label in np.ndenumerate(grid):
		ax.text(i,j,round(label/100)/100.0,ha='center',va='center')

	plt.title("Knight's tour", fontsize=24)
	plt.show()

#the following two functions were made to remedy the fact that
#the original algorithm for generating tours did not have a 0%
#fail rate and I discovered that there were incomplete tours
#in the database
def fix_failed_tours_with_diagnostics(start_pos):
	tour_list = pull_tour_list(start_pos)
	failed_tours = 0
	for tour in tour_list:
		if len(tour_list[i]) != 64:
			failed_tours += 1
			tour_list.remove(tour)
	print("Failed Tours: " + str(failed_tours))
	print("Proportion: " + str(failed_tours/len(tour_list)))
	put_tour_list(start_pos,tour_list)

def fix_failed_tours(start_pos):
	tour_list = pull_tour_list(start_pos)
	failed_tours = 0
	for i in range(len(tour_list)):
		if i < len(tour_list) and len(tour_list[i]) != 64:
			failed_tours += 1
			del tour_list[i]
			i -= 1
	put_tour_list(start_pos,tour_list)


