packageName = "packageName"
localPath = "/home/path"
# directory that should be watched for changes
wpath = "%s/%s/"%(localPath, packageName)

excludeFile = "%s/%s/rsyncExclude.txt"%(localPath, packageName)

# common remote path
rpath = "./%s"%(packageName)

# remote locations in rsync syntax
rnodes = [
      "dynacase@dynacase.local:" + rpath,
]

# limit remote sync speed (in KB/s, 0 = no limit)
#rspeed = 0

# event mask (only sync on these events)
#emask = [
#     "IN_CLOSE_WRITE",
#     "IN_CREATE",
#     "IN_DELETE",
#     "IN_MOVED_FROM",
#     "IN_MOVED_TO",
#]

# event delay in seconds (this prevents huge
# amounts of syncs, but dicreases the
# realtime side of things)
edelay = 1

# rsync binary path
rsync = "/usr/bin/rsync"
