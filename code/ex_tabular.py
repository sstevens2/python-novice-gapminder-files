## Data Excercise 1
# Read the data in gapminder_gdp_americas.csv (which should be in the same directory as gapminder_gdp_oceania.csv) into a variable called americas and display its summary statistics.

## Data Excercise 2
After reading the data for the Americas, use help(americas.head) and help(americas.tail)
to find out what DataFrame.head and DataFrame.tail do.

# Display the first three rows of this data

# Display the last three columns of this data?
# (Hint: you may need to change your view of the data.)

## Data Excercise 3
As well as the read_csv function for reading data from a file, Pandas provides a
 to_csv function to write dataframes to files. Applying what you’ve learned
 about reading from files, write one of your dataframes to a file called
 processed.csv. You can use help to get information on how to use to_csv.

## Data Exercise 4


1. Read "data/YpestisCO92.gff" into a data frame variable called `gff` using the `read_table` function from pandas.
Hint: You will need to check the head of the file and skip the first few lines.
Use the help to find the argument that will let you skip these lines.
2. Check your results by printing the first 5 lines of `gff` data frame. Does it look right? Your column names should be numbers from 0 to 8.  If not, look into the argument called `header` to see if you can fix it.
Bonus: Change the code to read in your table to specify the column names.
 
 
 
