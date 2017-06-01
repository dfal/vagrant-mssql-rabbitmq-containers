# vagrant-mssql-rabbitmq-containers

Vagrant to run Ubuntu with MSSQL Server and RabbitMQ as docker containers on developnet environment

* put your `mdf-` and `ldf-`files into `mssql/data` folder and modify `config.json`
* after `vagrant up` RabbitMQ and MSSQL will be available at `192.168.50.4` as well as at `localhost` on their default ports
* RabbitMQ user: `rabbit` password: `rabbit`
* MSSQL user: `sa` password: `#SAPassword!`
