# Modules
import os
import csv

# Variable initialization
total_votes = 0
candidates = []
candidate_votes = []
vote_percent = []

# Enter CSV path
csvpath = os.path.join("..", "Resources", "election_data.csv")

with open(csvpath, newline="") as election_data:
	election = csv.reader(election_data, delimiter=",")
	next (election_data)

	for row in election:
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

				

print("Election Results")
print("---------------------------")
print("Total Votes: " + str(total_votes))
print("---------------------------")

# Calculates vote percent for each candidate. It's ugly but it works.
for i in range(0, len(candidates)):
	print(candidates[i] + ": " + str(round(((candidate_votes[i]/total_votes)*100), 2)) + "% (" + str(candidate_votes[i]) + ")")
print("---------------------------")

# Uses the index of the largest value in the votes list to determine the winner
print("Winner: " + candidates[candidate_votes.index(max(candidate_votes))])
print("---------------------------")

output_file = os.path.join("..", "Output", "Poll Analysis.txt")

with open(output_file, "w", newline='') as datafile:
	writer = csv.writer(datafile)
	writer.writerow(["Election Results"])
	writer.writerow(["---------------------------"])
	writer.writerow(["Total Votes: " + str(total_votes)])
	writer.writerow(["---------------------------"])
	for i in range(0, len(candidates)):
		writer.writerow([candidates[i] + ": " + str(round(((candidate_votes[i]/total_votes)*100), 2)) + "% (" + str(candidate_votes[i]) + ")"])
	writer.writerow(["---------------------------"])
	writer.writerow(["Winner: " + candidates[candidate_votes.index(max(candidate_votes))]])
	writer.writerow(["---------------------------"])
	
	
	
	
