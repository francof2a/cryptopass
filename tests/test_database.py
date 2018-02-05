# -*- coding: utf-8 -*-

import user_managment as um

db_ok = um.test_users_database()

if db_ok:
    udb = um.load_users_database(um._USERS_DB_DEFAULT_)
else:
    print('Database error!')

