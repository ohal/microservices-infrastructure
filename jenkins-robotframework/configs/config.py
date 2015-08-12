#!/usr/bin/env python

import sys

# Robot root path. See note for required file structure.
ROBOT_ROOT = '/opt/robot/'

# Tenant settings, currenty not used
TENANT = 'CCS-MI-US-INTERNAL-1-QA-1'

# Host credentials/keys settings
USERNAME = 'centos'
PASSWWORD = ''
KEYFILE = '/opt/robot/id_rsa'

# Services security settings
SERVICE_USER = 'admin'
SERVICE_PASS = 'admin'

# Datacenter settings
HOST1 = 'host-01'
HOST2 = 'host-02'
HOST3 = 'host-03'
HOST4 = 'host-04'
HOST5 = 'host-05'
HOST6 = 'host-06'
HOST7 = 'host-07'
HOST8 = 'host-08'

# HDFS
HDFS = 'host-01 host-04 host-05'

# Mesos
MESOS = 'host-01 host-02 host-03'

# Control
#VAULT = 'host-03'
CONSUL = 'host-01 host-02 host-03'
#ZOOKEEPER = 'host-03'
MARATHON = 'host-03'
#NAME = 'host-03'

# Resource nodes
CONSUL_CLIENTS = 'host-04 host-05'
MESOS_FOLLOWERS = 'host-04 host-05'
#PROXY_SERVERS = 'host-05'
#DATA_NODES = 'host-05'
#KAFKA_SCHEDULER = 'host-05'

# Marathon
MARATHON_APP = '{"id": "/product/service/my-app", "cmd": "sleep 3600"}'

# Kafka-mesos
KAFKA_MESOS_DIRECTORY = '/opt/kafka-mesos'
KAFKA_BROKERS_AMOUNT = 3
KAFKA_BROKERS_STARTED = 1
KAFKA_NODES = 'host-04 host-05 host-06 host-07'
