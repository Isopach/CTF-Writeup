# MD5Play 2
##### Just understand the code ;)

This one's easy. We find that the code takes an md5 param and a value with the following rules:
- Must be an MD5    
- Length = 3
- Non-numeric
- floatval of MD5 must be equal to md5 value

Now, you should know that PHP truncates floatval, so it's simple to find the answer.

Just try something like `http://blackfoxs.org/radar/md5play/?md5=cq1` and you got it.

<details>
<summary>FLAG</summary> 

`radar{s0m3_bug5_1s_fun}`
</summary>
