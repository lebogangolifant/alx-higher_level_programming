# 0x0E. SQL - More queries

This repository contains a set of SQL scripts that demonstrate various queries and operations on a MySQL database. The scripts cover a range of tasks, from creating databases, tables, and users to performing complex queries on TV show data.

## Table of Contents

- [Project Overview](#project-overview)
- [Requirements](#requirements)
- [Getting Started](#getting-started)
  - [Installing MySQL](#installing-mysql)
  - [Running Scripts](#running-scripts)
- [Scripts](#scripts)

## Project Overview

This project focuses on practicing SQL queries and database management using MySQL. It includes a series of SQL scripts that perform tasks such as creating databases, tables, and users, as well as retrieving and manipulating data related to TV shows and genres.

## Requirements

- Ubuntu 20.04 LTS
- MySQL 8.0

## Getting Started

### Installing MySQL

1. Update the package list:
   ```bash
   sudo apt update
   ```

2. Install MySQL Server:
   ```bash
   sudo apt install mysql-server
   ```

3. Verify the installation:
   ```bash
   mysql --version
   ```

### Running Scripts

To execute the SQL scripts in this repository, follow these steps:

1. Clone this repository to your local machine.

2. Open a terminal and navigate to the project directory:
   ```bash
   $ cd path/to/your/project/directory
   ```

3. Run a script using `mysql` and provide the script filename:
   ```bash
   cat script_name.sql | mysql -hlocalhost -uroot -p database_name
   ```

   Replace `script_name.sql` with the name of the script you want to run and `database_name` with the appropriate database name.

## Scripts

List of all the scripts available in this project::

1. `0-privileges.sql`: Lists privileges of MySQL users.
2. `1-create_user.sql`: Creates a MySQL user with all privileges.
3. `2-create_read_user.sql`: Creates a MySQL user with SELECT privilege.
4. `3-force_name.sql`: Creates the `force_name` table.
5. `4-never_empty.sql`: Creates the `id_not_null` table.
6. `5-unique_id.sql`: Creates the `unique_id` table.
7. `6-states.sql`: Creates the `states` table.
8. `7-cities.sql`: Creates the `cities` table.
9. `8-cities_of_california_subquery.sql`: Lists cities in California using a subquery.
10. `9-cities_by_state_join.sql`: Lists cities and their states using a JOIN.
11. `10-genre_id_by_show.sql`: Lists genres linked to shows in `hbtn_0d_tvshows` with ratings.
12. `11-genre_id_all_shows.sql`: Lists all shows in `hbtn_0d_tvshows` with ratings and genres.
13. `12-no_genre.sql`: Lists shows without a genre in `hbtn_0d_tvshows`.
14. `13-count_shows_by_genre.sql`: Lists genres and the number of shows linked to them in `hbtn_0d_tvshows`.
15. `14-my_genres.sql`: Lists genres of the show "Dexter" in `hbtn_0d_tvshows`.
16. `15-comedy_only.sql`: Lists Comedy shows in `hbtn_0d_tvshows`.
17. `16-shows_by_genre.sql`: Lists shows and their linked genres in `hbtn_0d_tvshows`.
18. `100-not_my_genres.sql`: Lists genres not linked to the show "Dexter" in `hbtn_0d_tvshows`.
19. `101-not_a_comedy.sql`: Lists shows without the genre "Comedy" in `hbtn_0d_tvshows`.
20. `102-rating_shows.sql`: Lists shows and their rating sums in `hbtn_0d_tvshows_rate`.
21. `103-rating_genres.sql`: Lists genres and their rating sums in `hbtn_0d_tvshows_rate`.

