# An Analysis of Election Votes
___
## Project Overview
Performed data analysis on election data for three counties in the State of Colorado.  The analysis calculated the total number of votes cast, compiled a list of candidates who received votes, calculated the total number of votes each candidate received, calculated the percentage of votes each candidate won, and determined the winner of the election based on the popular vote.

## Resources
- Data Source: election_results.csv
- Software: Python 3.10, Visual Studio 1.66.2

## Summary
![Election Result](https://github.com/frlinh/election-analysis/blob/c82f0bd742f7843d61d2044e5d8181bc5f264d03/Resources/Election%20Results.png)

The analysis of the election show that:
- There were a total of 368,711 votes cast in the election.
- The county results were:
    - Jefferson received 10.5% of the votes and 38,855 number of votes.
    - Denver recieved 82.8% of the votes and 306,055 number of votes.
    - Arapahoe received 6.7% of the votes and 24,801 number of votes.
- The county with the largest number of votes was:
    - Denver
- The candidates were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
- The candidate results were:
    - Charles Casper Stockham received 23.0% of the votes and 85,213 number of votes.
    - Diana DeGette recieved 73.8% of the votes and 272,892 number of votes.
    - Raymon Anthony Doane received 3.1% of the votes and 11,606 number of votes.
 - The winner of the election was:
    - Diana DeGette, who recieved 73.8% of the votes and 272,8992 number of votes.

## Challenge Summary
This python script was created with the intention of analyzing election data for the State of Colorado.  It summarizes the election results by delivering the total number of votes cast, percentage and total outcomes by county, percentage and total outcomes by candidate, county with the largest number of votes, and the winner of the election.  The election commission can use this script for elections in other counties as well.  The format of the new dataset would have to be the same as 'election_results.csv' and the file path in the script would have to be updated to where the file is located.  This script can also be used to perform election analysis for multiple States.  The variables and print statements in the script would have to be changed from 'county' to 'state'.  For example, 'county_list' and 'county_votes' would change to 'state_list' and 'state_votes' and 'County Votes' and 'Largest County Turnout' would change to 'State Votes' and 'Largest State Turnout'.
