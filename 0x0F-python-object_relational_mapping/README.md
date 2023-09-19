# 0x0F. Python - Object-relational mapping

This repository contains Python scripts and SQL files that demonstrate the use of SQLAlchemy for Object-Relational Mapping (ORM) with a MySQL database.

## Dependencies

Before running the scripts, make sure you have the following dependencies installed:

### MySQL Database

- [MySQL 8.0 Installation Guide for Ubuntu 20.04](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-8-0-on-ubuntu-20-04)

### Python Packages

- **MySQLdb (version 2.0.x)**: To interact with the MySQL database.
    ```bash
    $ sudo apt-get install python3-dev
    $ sudo apt-get install libmysqlclient-dev
    $ sudo apt-get install zlib1g-dev
    $ sudo pip3 install mysqlclient
    ```
    Verify the installation by launching a Python shell and checking the MySQLdb version:
    ```python
    >>> import MySQLdb
    >>> MySQLdb.version_info
    (2, 0, 3, 'final', 0)
    ```

- **SQLAlchemy (version 1.4.x)**: To work with the SQLAlchemy ORM.
    ```bash
    $ sudo pip3 install SQLAlchemy
    ```
    Verify the installation by launching a Python shell and checking the SQLAlchemy version:
    ```python
    >>> import sqlalchemy
    >>> sqlalchemy.__version__
    '1.4.22'
    ```

## Tasks

| File Name                            | Description                                                         |
|-------------------------------------|---------------------------------------------------------------------|
| [0-select_states.py](0-select_states.py) | Script that lists all states from the database hbtn_0e_0_usa. |
| [1-filter_states.py](1-filter_states.py) | Script that lists all states starting with 'N' from the database hbtn_0e_0_usa. |
| [2-my_filter_states.py](2-my_filter_states.py) | Script that takes an argument and lists all states starting with that argument from the database hbtn_0e_0_usa. |
| [3-my_safe_filter_states.py](3-my_safe_filter_states.py) | Script that takes an argument and lists all states starting with that argument from the database hbtn_0e_2_usa. |
| [4-cities_by_state.py](4-cities_by_state.py) | Script that lists all cities from the database hbtn_0e_4_usa. |
| [5-filter_cities.py](5-filter_cities.py) | Script that lists all cities of a given state from the database hbtn_0e_4_usa. |
| [6-model_state.py](6-model_state.py) | Script that defines a State class and creates the corresponding states table in the database hbtn_0e_6_usa. |
| [7-model_state_fetch_all.py](7-model_state_fetch_all.py) | Script that lists all State objects from the database hbtn_0e_6_usa. |
| [8-model_state_fetch_first.py](8-model_state_fetch_first.py) | Script that prints the first State object from the database hbtn_0e_6_usa. |
| [9-model_state_filter_a.py](9-model_state_filter_a.py) | Script that lists all State objects containing the letter 'a' from the database hbtn_0e_6_usa. |
| [10-model_state_my_get.py](10-model_state_my_get.py) | Script that prints the State object with a given name from the database hbtn_0e_6_usa. |
| [11-model_state_insert.py](11-model_state_insert.py) | Script that adds a State object to the database hbtn_0e_6_usa. |
| [12-model_state_update_id_2.py](12-model_state_update_id_2.py) | Script that changes the name of a State object with id=2 in the database hbtn_0e_6_usa. |
| [13-model_state_delete_a.py](13-model_state_delete_a.py) | Script that deletes all State objects containing the letter 'a' from the database hbtn_0e_6_usa. |
| [model_city.py](model_city.py) | Defines a City class for use in the SQLAlchemy ORM. |
| [relationship_city.py](relationship_city.py) | Defines a City class with a relationship to State for use in the SQLAlchemy ORM. |
| [relationship_state.py](relationship_state.py) | Defines a State class with a one-to-many relationship to City for use in the SQLAlchemy ORM. |
| [100-relationship_states_cities.py](100-relationship_states_cities.py) | Script that creates a State "California" with the City "San Francisco" in the database hbtn_0e_100_usa. |
| [101-relationship_states_cities_list.py](101-relationship_states_cities_list.py) | Script that lists all State objects and their corresponding City objects from the database hbtn_0e_101_usa. |
| [102-relationship_cities_states_list.py](102-relationship_cities_states_list.py) | Script that lists all City objects from the database hbtn_0e_101_usa along with their associated State names using SQLAlchemy relationships. |


## Usage

To execute any of the scripts, use the following command format:

```bash
./script_name.py <mysql_username> <mysql_password> <database_name>
```

Replace `script_name.py` with the name of the script you want to run, and provide the required arguments.

Make sure to have a MySQL server running locally on port `3306` and the necessary database set up before running the scripts.

Example:

```bash
./0-select_states.py root root hbtn_0e_0_usa
```
