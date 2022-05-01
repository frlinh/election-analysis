# The data we need to retrieve.

# import the datetime class from the datetime module.
import datetime as dt

# Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()

# Print the present time.
print("The time right now is ", now)

#Add our dependencies
import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
#Create a file name variable to a direct or indirect path to file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
# with statement replaced election_data = open(file_to_load, 'r')
with open(file_to_load) as election_data:

    # To do: read and analyze data here.
    file_reader = csv.reader(election_data) 

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)
    
    for row in file_reader:
        print(row)
        
    # Print the file object.
    #print(election_data)

# Close the file.
#election_data.close()

# Use the open() function with the "w" mode we will write data to the file.
#outfile = open(file_to_save, "w")
# Write some data to the file.
#outfile.write("Hello World")

# Close the file
#outfile.close()

# Using the with statement open the file as a text file
with open(file_to_save, "w") as txt_file:
    # Write some data to the file.
    txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")

# 1. Total number of votes cast


# 2. A complete list of candidates who received votes


# 3. Total number of votes each candidate received


# 4. Percentage of votes each candidate won


# 5. The winner of the election based on popular vote