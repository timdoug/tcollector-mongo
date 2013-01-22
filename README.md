A tcollector collector for mongodb
==================================



What's wrong with [this project](https://github.com/greenmang0/opentsdb-mongo)?
--------------------------------

It requires mongod to be started with --rest, and this solution doesn't; it connects over the standard server port and runs the serverStatus command directly.

Requirements
------------

* OpenTSDB and tcollector
* MongoDB
* Python
* PyMmongo

Usage
-----

1. Ensure the metrics have been made in OpenTSDB with opentsdb_mkmetric.sh
2. Copy mongo.py to your collectors directory (is /usr/local/tcollector/collectors/0/ by default), and make sure it's executable.
3. tcollector should be smart and launch the script automatically-- you're now good to go.

