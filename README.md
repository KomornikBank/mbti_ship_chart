This is a repository with the csv file containing data from posts from the "shipping chart" trend from r/mbti, and additional files and programs that helped with creating or analyzing it. Below I have written the descriptions and additional information about the files in the repo. Please keep in mind that the python programs use pandas, and won't work without it.

* **shipping_chart.csv** - The file containing all the collected data. Every row is the data from an individual post. The first column contains the personality type of the post author. The other 16 columns contain their ratings of the 16 personality types. A single cell will look something like this: "0;1;0;2;0;0;0". It will contain 7 numbers - one for every possible rating (otp; cute/like; brotp; platonic; don't care/neutral; dislike; make it stop). Each of those numbers is the count of how many times the poster has given a certain rating to the type. In the example cell I've given above, that would mean that the type got marked by the user as "cute/like" once, and "platonic" twice.
* **data_analysis_program.py** - This is the program I have made to sum up and visualize some of the data. It prints out the table of all the types with the total sum of their ratings, how many times each type made a post and the total sum of ratings for every letter in the mbti system. If you're having trouble with loading or analyzing the data yourself, try looking through this file for clues on how to solve your problem.
* **csv_creation_program.py** - I've used this program to easily append the data of the posts to the csv file. It does not have a use anymore, though I've chosen to leave it in, in case it becomes useful to someone in the future.
* **shipping_chart_backup_base.csv** - A copy of the csv file that I started with since *csv_creation_program.py* needs at least the headers to start working. I left it in for the aforementioned program.
