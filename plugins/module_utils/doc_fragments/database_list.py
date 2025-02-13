"""Documentation fragments for the database_list module"""

specdoc_examples = ['''
- name: List all of the databases for the current Linode Account
  linode.cloud.database_list: {}''', '''
- name: Resolve all MySQL databases for the current Linode Account
  linode.cloud.database_list:
    filters:
      - name: engine
        values: mysql''']

result_images_samples = ['''[
   {
      "allow_list":[
         "203.0.113.1/32",
         "192.0.1.0/24"
      ],
      "cluster_size":3,
      "compression_type":"none",
      "created":"2022-01-01T00:01:01",
      "encrypted":false,
      "engine":"mongodb",
      "hosts":{
         "primary":"lin-0000-0000.servers.linodedb.net",
         "secondary":null
      },
      "id":123,
      "label":"example-db",
      "peers":[
         "lin-0000-0000.servers.linodedb.net",
         "lin-0000-0001.servers.linodedb.net",
         "lin-0000-0002.servers.linodedb.net"
      ],
      "port":27017,
      "region":"us-east",
      "replica_set":null,
      "ssl_connection":true,
      "status":"active",
      "storage_engine":"wiredtiger",
      "type":"g6-dedicated-2",
      "updated":"2022-01-01T00:01:01",
      "updates":{
         "day_of_week":1,
         "duration":3,
         "frequency":"weekly",
         "hour_of_day":0,
         "week_of_month":null
      },
      "version":"4.4.10"
   }
]''']
