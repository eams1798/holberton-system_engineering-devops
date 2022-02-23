# Postmortem
On January 25, 2022, at 4 pm, while installing MySQL Client 8.0 on server 3401-web-01 for project 0x14 - MySQL, unexpected errors occurred that slowed down the installation and subsequently the entire system . This caused me to be unable to do the necessary configurations to set a "master/slave" replication relationship between the MySQL clients installed on this server and on 3401-web-02, respectively. This issue lasted until noon on January 28, at which point I was able to fix it for good.

## Root Cause
The MySQL client installation error I was presented with on server 3401-web-01 is very similar to the one that occurred to the person who asked [the following question on askubuntu](https://askubuntu.com/questions/1235829/cant-get-mysql8-to-work-on-ubuntu-20-04). The most important part of the installation error What I detected was this, followed by a `connection timed out`:

```
mysqld will log errors to /var/log/mysql/error.log
2022-01-26T00:00:19.270205Z 0 [ERROR] [MY-011065] [Server] Unable to determine if daemon is running: No such file or directory (rc=0).
2022-01-26T00:00:19.272430Z 0 [ERROR] [MY-010946] [Server] Failed to start mysqld daemon. Check mysqld error log.
Warning: Unable to start the server.
Created symlink /etc/systemd/system/multi-user.target.wants/mysql.service → /lib/systemd/system/mysql.service.
Job for mysql.service failed because a fatal signal was delivered to the control process.
See "systemctl status mysql.service" and "journalctl -xe" for details.
```

So, I tried to find the root of this problem and a solution for it, but the system was so slow that any command entered took several minutes to execute (from 5 minutes to more than an hour, instead of executing instantly in less than one second). However, after several new unsuccessful delete and reinstall attempts with the same version of MySQL, I believe it is a version incompatibility issue with some particular process on the server. What I could clearly detect is that the cause of the server slowness was caused by the corrupt `mysqld` process running, automatically activated despite not having completed the installation successfully, and occupying approximately 53.7% of memory.

## Problem Solution
The first thing that had to be achieved is that the server returned to normal. To do this, it had to see the running processes that were putting the most load on the server. So, I ran the `top` command. After a few minutes of waiting, the processes with the greatest impact on the system were shown on the screen, where `mysqld` stood out with an exaggeratedly high memory consumption (as I mentioned in the previous point, 53.7% approx.), besides I was able to recognize that said process was associated with the program you had just installed.

I then killed the process using the `kill -9 [mysqld PID]` command, which momentarily caused the system to return to normal speed, but then slowed down again the next minute while the same process was running automatically. So what I did the next time was to kill the process and immediately purge all the corrupted MySQL service via the `sudo apt-get -y purge mysql*` command. In this way, the autorun of `mysqld` was also removed.

However, when I tried to install the service again and, having previously reviewed some of the errors shown above, I could not detect the fundamental cause of the failure of this specific version of MySQL. After installation, the server was slow again, and sometimes it was so slow that you couldn't even access it via SSH. After several trial and error tests, I discovered that the way to access the server was to request a Hard reboot or a Soft reboot and after a minute, try to access the server as quickly as possible before the `mysqld` process starts to be able to kill it when it activates and purge it again.

Despite this, I still couldn't move forward with the project because MySQL still couldn't be installed for the reasons already mentioned. When I thought there was no solution for it, I tried installing the 5.7 version recommended for this project. So, the installation was completed successfully! And no slowness issues! But, since I knew there would be another version incompatibility issue when replicating from different versions (having "master" on 5.7 and "slave" on 8.0), I had no problem uninstalling the updated version of MySQL on server 3401-web -02 to also place version 5.7.

## Corrective and preventative measures
If any service has problems running, look for alternative versions, either more up-to-date or older, that have better system compatibility.
