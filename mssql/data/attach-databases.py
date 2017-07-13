#!/usr/bin/python

import os
import json
import time
import subprocess

time.sleep(30) # wait for SQL Server to start

def exec_sql(db, sql):
    subprocess.call("/opt/mssql-tools/bin/sqlcmd -S localhost -U sa -P '#SAPassword!' -d %s -Q \"%s\"" % (db, sql), shell=True)
    return;

with open('./config.json') as config_file:
    config = json.load(config_file)

if 'logins' in config:
    for login in config['logins']:
        sql = """ IF NOT EXISTS (SELECT name FROM sys.server_principals WHERE name=N'{0}') 
                  BEGIN
                    CREATE LOGIN [{0}] WITH PASSWORD=N'{1}', DEFAULT_DATABASE=[master], CHECK_EXPIRATION=OFF, CHECK_POLICY=OFF
                  END 
              """.format(login['name'], login['password'])
        exec_sql("master", sql)

if 'databases' in config:
    for db in config['databases']:
        sql = """ IF db_id(N'{0}') IS NULL
                  BEGIN
                    CREATE DATABASE [{0}] ON (FILENAME = '{1}.mdf'),(FILENAME = '{2}.ldf') FOR ATTACH
                  END
              """.format(db['name'], os.path.abspath(db['mdf']), os.path.abspath(db['ldf']))
        exec_sql("master", sql)
        if 'users' in db:
            for user in db['users']:
                sql = """ IF EXISTS (SELECT * FROM sys.database_principals WHERE name = N'{0}')
                            EXEC sp_change_users_login N'Auto_Fix', N'{0}'
                        ELSE
                            CREATE USER [{0}] FOR LOGIN [{1}]
                        EXEC sp_addrolemember N'db_owner', N'{0}' """.format(user['userName'], user['loginName'])
                exec_sql(db['name'], sql)
