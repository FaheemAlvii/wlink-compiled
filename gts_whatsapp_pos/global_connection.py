import shelve

with shelve.open('global_connection') as connection_db:
    if 'connection' not in connection_db:
        connection_db['connection'] = None


def set_connection(new_connection):
    with shelve.open('global_connection') as connection_db:
        connection_db['connection'] = new_connection.id


def get_connection():
    with shelve.open('global_connection') as connection_db:
        return connection_db['connection']
