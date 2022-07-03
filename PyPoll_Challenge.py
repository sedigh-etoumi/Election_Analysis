# -*- coding: UTF-8 -*-
#"""PyPoll Homework Challenge Solution."""

# Add our dependencies.
import csv
from itertools import count
import os
from tokenize import Double

from pytz import country_timezones

# Add a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0
election_resuts = ""
winning_candidat=""


# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}

# 1: Create a county list and county votes dictionary.

counties_name = []
counties_options = []
counties_dict={}
counties_percentage_options = []


# Track the winning candidate, vote count and percentage
winning_candidatename = ""
winning_count = 0
winning_percentage = 0
temp11 = ""

# 2: Track the largest county and county voter turnout.

counties_votes = ""

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)
     # Read the header
    header = next(reader)
    # For each row in the CSV file.
    for row in reader:
        # Add to the total vote count
        total_votes = total_votes + 1
        # Get the candidate name from each row.
        candidate_name = row[2]
         
         # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:

        # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name]+=1
    
        # 3: Extract the county name from each row.
        counties_name = row[1]
        if counties_name not in counties_options:
            counties_options.append(counties_name) 
            counties_dict[counties_name] = 0
        counties_dict[counties_name]+=1
 
winning_count = max(candidate_votes.values())
winning_count1 = winning_count
#print(winning_count)

winning_percentage = winning_count / total_votes * 100
#print(total_votes)
#print(winning_percentage)

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")
    txt_file.write(election_results)

    for counties_name in counties_dict:
        votes = counties_dict[counties_name] 
        vote_percentage = float(votes) / float(total_votes) * 100
        #print(f"{counties_name}: {vote_percentage:.1f}% ({votes:,})\n")
        candidate_results = (
                f"{counties_name}: {vote_percentage:.1f}% ({votes:,})\n")

    
        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
    

        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_county = counties_name
        
    winning_countyname = (
        f"\n-------------------------\n"
        f"Largest County Turnout: {winning_county}")
    print(f"{winning_countyname}\n-------------------------")
    #  Save the candidate results to our text file.
    txt_file.write(winning_countyname)
    txt_file.write("\n-------------------------\n")

    

    # for candidate_name in candidate_votes:
    winning_count = 0
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name] 
        vote_percentage = float(votes) / float(total_votes) * 100
        #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
    #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        if (votes > winning_count):
            winning_count = votes
            winning_candidatename = candidate_name
            winning_percentage = vote_percentage
       
    winning_candidate_summary = (
            f"-------------------------\n"
            f"Winner:  {winning_candidatename}\n"
            f"Winning Vote Count: {winning_count1:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)








    




    




        


   