FROM microsoft/mssql-server-linux
RUN mkdir -p /usr/data
COPY ./data /usr/data/
RUN chmod +x /usr/data/attach-databases.py
WORKDIR /usr/data
CMD python /usr/data/attach-databases.py & /opt/mssql/bin/sqlservr
