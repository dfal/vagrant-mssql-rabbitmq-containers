#!/usr/bin/python

import json
import subprocess

def exec_sql(db, sql):
    subprocess.call("/opt/mssql-tools/bin/sqlcmd -S localhost -U sa -P '#SAPassword!' -d %s -Q \"%s\"" % (db, sql), shell=True)
    return;

with open('/data/config.json') as config_file:
    config = json.load(config_file)

if 'logins' in config:
    for login in config['logins']:
        exec_sql("master", "CREATE LOGIN [%s] WITH PASSWORD=N'%s', DEFAULT_DATABASE=[master], CHECK_EXPIRATION=OFF, CHECK_POLICY=OFF" %(login['name'], login['password']))

if 'databases' in config:
    for db in config['databases']:
        exec_sql("master", "CREATE DATABASE [%s] ON (FILENAME = '%s.mdf'),(FILENAME = '%s.ldf') FOR ATTACH" %(db['name'], db['mdf'], db['ldf']))
        if 'users' in db:
            for user in db['users']:
                sql = """ IF EXISTS (SELECT * FROM sys.database_principals WHERE name = N'{0}')
                            EXEC sp_change_users_login 'Auto_Fix', '{0}'
                        ELSE
                            CREATE USER [{0}] FOR LOGIN [{1}]
                        EXEC sp_addrolemember N'db_owner', N'{0}' """.format(user['userName'], user['loginName'])
                exec_sql(db['name'], sql)
