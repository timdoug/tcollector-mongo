#!/usr/bin/python

import sys
import time
import pymongo

HOST = 'localhost'
PORT = 27017
METRICS = [
    'backgroundFlushing.average_ms',
    'backgroundFlushing.flushes',
    'backgroundFlushing.total_ms',
    'connections.available',
    'connections.current',
    'cursors.totalOpen',
    'cursors.timedOut',
    'dur.commits',
    'dur.commitsInWriteLock',
    'dur.compression',
    'dur.earlyCommits',
    'dur.journaledMB',
    'dur.writeToDataFilesMB',
    'extra_info.heap_usage_bytes',
    'extra_info.page_faults',
    'globalLock.lockTime',
    'globalLock.totalTime',
    'indexCounters.btree.accesses',
    'indexCounters.btree.hits',
    'indexCounters.btree.missRatio',
    'indexCounters.btree.misses',
    'indexCounters.btree.resets',
    'mem.resident',
    'mem.virtual',
    'mem.mapped',
    'network.bytesIn',
    'network.bytesOut',
    'network.numRequests',
    'opcounters.command',
    'opcounters.delete',
    'opcounters.getmore',
    'opcounters.insert',
    'opcounters.query',
    'opcounters.update',
]

def main():
    c = pymongo.Connection(host=HOST, port=PORT)

    while True:
        res = c.admin.command('serverStatus')
        ts = int(time.time())

        for assert_tag in ('msg', 'regular', 'user', 'warning',):
            print 'mongo.asserts', ts, res['asserts'][assert_tag], 'type=' + assert_tag
        for metric in METRICS:
            cur = res
            try:
                for m in metric.split('.'):
                    cur = cur[m]
            except KeyError:
                continue
            print 'mongo.' + metric, ts, cur

        sys.stdout.flush()
        time.sleep(15)

if __name__ == '__main__':
    main()
