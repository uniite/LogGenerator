# LogGenerator

Generates fake logs for testing.

Currently, only generates Nginx Access Logs:

```
$ python log_generator.py 100
133.236.45.104 - - [2013-06-10 09:13:54] 301 "POST /settings/4695/components/" 268 "http://logs.vcap.me/settings/4695/components/" "(compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0) Firefox" ""
# ... 99 more lines of fake logs
```
