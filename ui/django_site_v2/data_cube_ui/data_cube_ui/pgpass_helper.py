from __future__ import print_function

__all__ = ('read_pgpass',)


def read_pgpass(dbname):
    """
    Reads the pgpass. Returns the postgres settings dict for Django.
    :param str dbname:
    :return dict:
    """
    import os

    try:
        # See http://stackoverflow.com/questions/14742064/python-os-environhome-works-on-idle-but-not-in-a-script
        home_folder = os.path.expanduser('~')
        pgpass = os.path.join(home_folder, '.pgpass')
        pgpass_lines = open(pgpass).read().split()
    except IOError:
        print(
            """
            You don't have a ~/.pgpass file so we're using a sqlite database.
            To switch to a PostgreSQL database, create a ~/.pgpass file
            containing it's credentials.
            See http://www.postgresql.org/docs/9.3/static/libpq-pgpass.html
            """
            )
    else:
        for match in (dbname, '*'):
            for line in pgpass_lines:
                host, port, stored_dbname, user, password = line.strip().split(':')
                if stored_dbname == match:
                    return {
                        'ENGINE': 'django.db.backends.postgresql_psycopg2',
                        'NAME': dbname,
                        'USER': user,
                        'PASSWORD': password,
                        'HOST': host,
                        'PORT': port
                    }

