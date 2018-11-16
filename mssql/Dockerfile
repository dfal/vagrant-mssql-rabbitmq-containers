FROM microsoft/mssql-server-linux:latest
COPY ./data /var/opt/mssql/user-data/
RUN chmod +x /var/opt/mssql/user-data/attach-databases.py
WORKDIR /var/opt/mssql/user-data
CMD python /var/opt/mssql/user-data/attach-databases.py & /opt/mssql/bin/sqlservr
