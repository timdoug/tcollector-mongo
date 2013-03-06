mongo.py -- a tcollector script for OpenTSDB
============================================

Note: merged upstream
---------------------

This collector has been merged upstream [here](https://github.com/OpenTSDB/tcollector/commit/192af2ff3a4e3fcd7a547197f2ef15c7a5ef39e1). Continued development will happen in the official repo. Thanks!


What is this?
-------------

It's a tcollector-compatible script for inserting MongoDB statistics into OpenTSDB.


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

