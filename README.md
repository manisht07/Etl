ETL.py is data pipeline to extract data from json files and load into postgresql tables. 

Using the song and log datasets, we created a star schema optimized for queries on song play analysis.

############################################################################################
Fact Table
songplays - records in log data associated with song plays i.e. records with page NextSong
songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent


Dimension Tables
users - users in the app
user_id, first_name, last_name, gender, level
songs - songs in music database
song_id, title, artist_id, year, duration
artists - artists in music database
artist_id, name, location, latitude, longitude
time - timestamps of records in songplays broken down into specific units
start_time, hour, day, week, month, year, weekday

#############################################################################################

The project workspace includes six files:

- create_tables.py- drops and creates your tables. You run this file to reset your tables before each time you run your ETL                           scripts.
- etl.ipynb-        reads and processes a single file from song_data and log_data and loads the data into your tables. This                           notebook contains detailed instructions on the ETL process for each of the tables.
- etl.py-           reads and processes files from song_data and log_data and loads them into your tables. You can fill this out                     based on your work in the ETL notebook.
- README.md-        provides discussion of project.
- sql_queries.py-   contains all your sql queries, and is imported into the last three files above.
- test.ipynb-       displays the first few rows of each table to let you check your database.

###############################################################################################

How to run the project?

Step-1 Open a terminal in Jupyter, run your Python scripts in the terminal like you would in your local terminal
           
           OR 
        Make a notebook, and use %run <create_tables.py> as an entry in a cell or do !python <create_tables.py>

Step-2 Execute etl.ipynb for detailed ETL process. Execute test.ipynb where applicable and do remember to restart kernel as per instruction in test.ipynb notebook.

Step-3 Execute etl.py for complete dataset on log and song files dataset. 

################################################################################################






