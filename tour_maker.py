import random

POSSIBLE_MOVES = [-17,-15,-10,-6,6,10,15,17]

#ckecks the 8 possible moves of a knight against previous moves,
#running off the board, or various excepions on the outer columns
#accepts the kinght's current position and a list of previous positions
#returns a list of legal moves from the possible 8 knight moves
def check_legal_moves(position, used_moves):
	legal_moves = []
	for possible_move in POSSIBLE_MOVES:
		final_position = position + possible_move
		if 		(final_position in used_moves
			    or final_position < 0 or final_position > 63
			    or check_first_column_exception(position, possible_move)
			    or check_second_column_exception(position, possible_move)
			    or check_seventh_column_exception(position, possible_move)
			    or check_eigth_column_exception(position, possible_move)):
			continue
		legal_moves.append(possible_move)
	return legal_moves

#these four methods define the explicit cases where moves don't work		
def check_first_column_exception(position, proposed_move):
	return position%8 == 0 and proposed_move in [-17,-10,6,15]

def check_second_column_exception(position, proposed_move):
	return position%8 == 1 and proposed_move in [-10,6]

def check_seventh_column_exception(position, proposed_move):
	return position%8 == 6 and proposed_move in [-6,10]

def check_eigth_column_exception(position, proposed_move):
	return position%8 == 7 and proposed_move in [-15,-6,10,17]

#input is a list of tuples that are
#(potential move, # of possible moves after that potential move) 
#output is a selection of one of those tuples w/ minimum 2nd value
def find_best_move(list_of_moves_and_viability):
	minimum = (99,99)
	for move_and_viability in list_of_moves_and_viability:
		if move_and_viability[1] < minimum[1]:
			minimum = move_and_viability
	return minimum

#selects a random most viable move by finding the most viable case
#and scanning all possible moves to see which are the most viable
#then selects one at random
def find_random_best_move(list_of_moves_and_viability):
	best_outcome = find_best_move(list_of_moves_and_viability)[1]
	best_moves = []
	for move_and_viability in list_of_moves_and_viability:
		if move_and_viability[1] == best_outcome:
			best_moves.append(move_and_viability)
	return best_moves[int(len(best_moves) * random.random())]

#creates a tour from a parameterized starting positiom
#before each move, code scans for possible moves and then
#analyzes possible moves from each
#succeeds by finding minimum number of moves as to not get skrewd
def run_game(starting_position):
	knight_position = starting_position

	#these variables are only defined here so they don't 
	#have to be recreated in every iteration of the loop
	used_spaces = [knight_position]
	temp_end_position = knight_position
	end_position = knight_position
	possible_moves = []
	viability_of_possible_moves = []
	temp_used_spaces = used_spaces[:]

	while True:
		if len(used_spaces) == 64:
			win_loss = True
			break
		possible_moves = check_legal_moves(knight_position, used_spaces)
		viability_of_possible_moves = []
		if len(possible_moves) == 0:
			break
		for temp_move in possible_moves:
			temp_end_position = knight_position + temp_move
			temp_used_spaces = used_spaces[:]
			temp_used_spaces.append(knight_position+temp_move)
			viability_of_possible_moves.append(
				(temp_move,
				len(check_legal_moves(temp_end_position,temp_used_spaces))))
		end_position = (knight_position 
					   +find_random_best_move(viability_of_possible_moves)[0])
		used_spaces.append(end_position)
		knight_position = end_position
	return used_spaces
	