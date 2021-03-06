# DROP TABLES

songplay_table_drop = ("""DROP TABLE IF EXISTS song_plays;""")
user_table_drop = ("""DROP TABLE IF EXISTS users;""")
song_table_drop = ("""DROP TABLE IF EXISTS songs;""")
artist_table_drop = ("""DROP TABLE IF EXISTS artists;""")
time_table_drop = ("""DROP TABLE IF EXISTS time;""")

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays (
                                song_play_id serial primary key,
                                start_time timestamp not null,
                                user_id int not null,
                                level varchar,
                                song_id varchar, 
                                artist_id varchar, 
                                session_id int,
                                location varchar,
                                user_agent varchar);""")

user_table_create = ("""CREATE TABLE IF NOT EXISTS users (
                                user_id int primary key,
                                first_name varchar (50) not null, 
                                last_name varchar (50),
                                gender varchar (1), 
                                level varchar (20));""")
                    
                     
                         

song_table_create = ("""CREATE TABLE IF NOT EXISTS songs (
                                song_id varchar(20) primary key,
                                title varchar (100) not null, 
                                artist_id varchar(20) not null,
                                year int not null, 
                                duration numeric(5,2) not null);""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists (
                                artist_id varchar(20) primary key,
                                name varchar (50) not null, 
                                location varchar (50),
                                latitude double precision, 
                                longitude double precision);""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS time (
                                start_time timestamp,
                                hour int, 
                                day varchar (50),
                                week int, 
                                month varchar(20),
                                year int,
                                weekday int);""")

# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO songplays
(
 start_time,
 user_id,
 level,
 song_id,
 artist_id,
 session_id,
 location,
 user_agent
 )
 VALUES(%s, %s, %s, %s, %s, %s, %s, %s)
""")

user_table_insert = ("""INSERT INTO users
(
 user_id,
 first_name,
 last_name,
 gender,
 level
 )
 VALUES(%s, %s, %s, %s, %s)
 ON CONFLICT (user_id) DO NOTHING
""")

song_table_insert = ("""INSERT INTO songs
(
 song_id,
 title,
 artist_id,
 year,
 duration
 )
 VALUES(%s, %s, %s, %s, %s)
""")

artist_table_insert = ("""INSERT INTO artists
(
 artist_id,
 name,
 location,
 latitude,
 longitude
 )
 VALUES(%s, %s, %s, %s, %s)
""")


time_table_insert = ("""INSERT INTO time
(
 start_time,
 hour,
 day,
 week,
 month,
 year,
 weekday
 )
 VALUES(%s, %s, %s, %s, %s, %s, %s)
""")

# FIND SONGS

song_select = ("""select s.song_id,a.artist_id 
                    from songs s inner join artists a 
                    on a.artist_id=s.artist_id 
                    where s.title=%s
                    and a.name=%s
                    and s.duration=%s
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]