# 0x0D. SQL - Introduction

This project provides a series of SQL scripts that demonstrate various database operations using MySQL . 

# SQL Introduction Project

## Table of Contents
- [Project Overview](#project-overview)
- [Requirements](#requirements)
- [Getting Started](#getting-started)
    - [Installing MySQL](#installing-mysql)
    - [Running Scripts](#running-scripts)
- [Scripts](#scripts)

## Project Overview
This project involves writing SQL scripts with MySQL to perform various tasks such as database creation, table manipulation, data querying, database management and more.

## Requirements
- Ubuntu 20.04 LTS
- MySQL 8.0

## Getting Started

### Installing MySQL
To install MySQL 8.0 on Ubuntu 20.04 LTS, follow these steps:

```bash
$ sudo apt update
$ sudo apt install mysql-server
...
$ mysql --version
mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
```

### Running Scripts
1. Clone this repository to your local machine.

2. Open a terminal and navigate to the project directory:
   ```bash
   $ cd path/to/your/project/directory
   ```

3. Run the SQL scripts using the `mysql` command. For example:
   ```bash
   $ cat 0-list_databases.sql | mysql -uroot -p
   ```

4. Follow a similar approach to run other scripts provided in the project.

## Scripts

List of all the scripts available in this project::

1. [`0-list_databases.sql`](./0-list_databases.sql): Lists all databases on the MySQL server.
2. [`1-create_database_if_missing.sql`](./1-create_database_if_missing.sql): Creates the database `hbtn_0c_0` if it doesn't already exist.
3. [`2-remove_database.sql`](./2-remove_database.sql): Removes the database `hbtn_0c_0` if it exists.
4. [`3-list_tables.sql`](./3-list_tables.sql): Lists all tables in a specified database.
5. [`4-first_table.sql`](./4-first_table.sql): Creates a table `first_table` with columns `id` and `name`.
6. [`5-full_table.sql`](./5-full_table.sql): Displays the full description of the table `first_table`.
7. [`6-list_values.sql`](./6-list_values.sql): Lists all rows of the table `first_table`.
8. [`7-insert_value.sql`](./7-insert_value.sql): Inserts a new row into the table `first_table`.
9. [`8-count_89.sql`](./8-count_89.sql): Displays the number of records with id = 89 in the table `first_table`.
10. [`9-full_creation.sql`](./9-full_creation.sql): Creates a table `second_table` and adds multiple rows.
11. [`10-top_score.sql`](./10-top_score.sql): Lists all records of `second_table` ordered by score (top first).
12. [`11-best_score.sql`](./11-best_score.sql): Lists records with score >= 10 in `second_table`.
13. [`12-no_cheating.sql`](./12-no_cheating.sql): Updates the score of Bob to 10 in `second_table`.
14. [`13-change_class.sql`](./13-change_class.sql): Removes records with score <= 5 in `second_table`.
16. [`14-average.sql`](./14-average.sql): Computes the score average of `second_table` records.
17. [`15-groups.sql`](./15-groups.sql): Lists the number of records with the same score in `second_table`.
18. [`16-no_link.sql`](./16-no_link.sql): Lists records of `second_table` without rows without a name value.
19. [`17-container-on-demand.sql`](./17-container-on-demand.sql): Information on using container on demand for MySQL.
20. [`18-ssl_termination.sql`](./18-ssl_termination.sql): Information on SSL termination with MySQL.
21. [`100-move_to_utf8.sql`](./100-move_to_utf8.sql): Converts database, table, and field to UTF8.
22. [`101-avg_temperatures.sql`](./101-avg_temperatures.sql):Displays average temperatures by city.
23. [`102-top_city.sql`](./102-top_city.sql): Displays top 3 city temperatures during July and August.
24. [`103-max_state.sql`](./103-max_state.sql): Displays the max temperature of each state.


