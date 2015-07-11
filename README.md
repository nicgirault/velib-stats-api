Installation
------------

TODO


Migration process
-----------------

```shell
# Prior to the first migration
python src/manage.py db init

# Create a new version of the database
python src/manage.py db migrate
# check file + remove comment + improve file if needed
vim migration/versions/<migration_id>.py

# Upgrade your database to the last version
python src/manage.py db upgrade
```

Run tests
---------

```shell
python -m unittest
```
