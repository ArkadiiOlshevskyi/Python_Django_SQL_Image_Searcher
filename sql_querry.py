import logging

# database creation:
# create table for items
'''
Paramaters to move in table:

listing code
brand
model
reference_number
movement
casematerial
braclet_material
year_of_production
condition
scope_of_dilivery
gender
location
price
availability
'''

'''
\connect root@localhost -p      - connecting to database
SHOW DATABASES;     - showing all databases that we have
CREATE DATABSE {database.name};     - creating(initializing) nea database
CREATE TABLE {table.name};     - creating(initializing) nea database
'''


def db_init():
    '''launching database'''
    logging.info('Database initialized...')
    pass


def db_table_init():
    '''launching database'''
    logging.info('Database initialized...')
    pass


def db_table_create_record():
    '''creating new table in database'''
    logging.info('Database initialized...')
    pass


def db_table_remove_record():
    '''remove record'''
    logging.info('Database initialized...')
    pass


def db_table_modify_record():
    '''modify record in table'''
    logging.info('Database initialized...')
    pass


def db_table_update_record():
    '''updating record in table'''
    logging.info('Database initialized...')
    pass





# CRUD operations
