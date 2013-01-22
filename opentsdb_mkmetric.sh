#!/bin/sh

./tsdb mkmetric mongo.asserts \
mongo.backgroundFlushing.average_ms \
mongo.backgroundFlushing.flushes \
mongo.backgroundFlushing.total_ms \
mongo.connections.available \
mongo.connections.current \
mongo.cursors.totalOpen \
mongo.cursors.timedOut \
mongo.dur.commits \
mongo.dur.commitsInWriteLock \
mongo.dur.compression \
mongo.dur.earlyCommits \
mongo.dur.journaledMB \
mongo.dur.writeToDataFilesMB \
mongo.extra_info.heap_usage_bytes \
mongo.extra_info.page_faults \
mongo.globalLock.lockTime \
mongo.globalLock.totalTime \
mongo.indexCounters.btree.accesses \
mongo.indexCounters.btree.hits \
mongo.indexCounters.btree.missRatio \
mongo.indexCounters.btree.misses \
mongo.indexCounters.btree.resets \
mongo.mem.resident \
mongo.mem.virtual \
mongo.mem.mapped \
mongo.network.bytesIn \
mongo.network.bytesOut \
mongo.network.numRequests \
mongo.opcounters.command \
mongo.opcounters.delete \
mongo.opcounters.getmore \
mongo.opcounters.insert \
mongo.opcounters.query \
mongo.opcounters.update