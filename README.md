# update-jaas

Simple update all the DB2 related JAAS alias in your HCL Connections Environment.

If the *update-jaas.py* is located in the folder */tmp*, just run this from your *Dmgr/bin* directory.

Replace the *PASSWORD* with the new password for the LCUSER, before you call this script.

```sh
./wsadmin.sh -lang jython -f /tmp/update-jaas.py
```
