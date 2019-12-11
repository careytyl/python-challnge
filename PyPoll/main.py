import os
import csv

# Variable initialization
total_votes = 0
candidates = []
candidate_votes = []

# Define and open CSV path
csvpath = os.path.join("..", "Resources", "election_data.csv")


def poll_data(candidates, candidate_votes, write_csv=False):
	for i in range(0, len(candidates)):
		if write_csv == False:
			print(candidates[i] + ": " + str(round(((candidate_votes[i]/total_votes)*100), 2)) + "% (" + str(candidate_votes[i]) + ")")
		else:
			writer.writerow([candidates[i] + ": " + str(round(((candidate_votes[i]/total_votes)*100), 2)) + "% (" + str(candidate_votes[i]) + ")"])


with open(csvpath, newline="") as election_data:
	election = csv.reader(election_data, delimiter=",")
	next (election_data)

	for row in election:
		
		# Adds to total votes for each row
		total_votes += 1
		
		# Checks each candidate against the initialized list
		# and adds to list if not already present
		if row[2] not in candidates:
			candidates.append(row[2])
			candidate_votes.append(0)
		
		# Compares each candidate to those in the list created
		# above and adds 1 to the appropriate candidate
		for i in range(0, len(candidate_votes)):
			if row[2] == candidates[i]:
				candidate_votes[i] += 1


winner = candidates[candidate_votes.index(max(candidate_votes))]

output_string = [
	"Election Results\n---------------------------\nTotal Votes: " + 
	str(total_votes) + "\n---------------------------",
	"---------------------------\nWinner: " + winner +
	"\n---------------------------"
	]


print(output_string[0])
poll_data(candidates, candidate_votes)
print(output_string[1])

# Uses the index of the largest value in the votes list to determine the winner

output_file = os.path.join("..", "Output", "Poll Analysis.txt")

with open(output_file, 'w', newline='') as datafile:
	writer = csv.writer(datafile)
	writer.writerow([output_string[0]])
	poll_data(candidates, candidate_votes, True)
	writer.writerow([output_string[1]])
