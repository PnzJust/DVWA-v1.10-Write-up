# Difficulty - Low

[Challange source code](https://github.com/PnzJust/DVWA-v1.10/blob/main/XSS%20DOM/Sources/low.php)

Any option we choose is reflected in URL:

![...](https://github.com/PnzJust/DVWA-v1.10/blob/main/XSS%20DOM/Pictures/1.png)

and also added at the top of the list like that (the url is parsed and it extract the default value):

![...](https://github.com/PnzJust/DVWA-v1.10/blob/main/XSS%20DOM/Pictures/2.png)

If we try something like that:
![...](https://github.com/PnzJust/DVWA-v1.10/blob/main/XSS%20DOM/Pictures/3.png)

The `</script>` will be converted in `<%2Fscript>` because / == %2F (URL encoded):

![...](https://github.com/PnzJust/DVWA-v1.10/blob/main/XSS%20DOM/Pictures/4.png)

So we are going to use the `#` character.
Let's try this link: `10.10.116.119/vulnerabilities/xss_d/#default=<script>alert(1)</script>`
![...](https://github.com/PnzJust/DVWA-v1.10/blob/main/XSS%20DOM/Pictures/5.png)

And it works.
Why?
Because:
- our browser will consider `#` as a fragment and will not forward it
- the server will not consider this part  `#default=<script>alert(1)</script>` so it will not be URL encoded
- the script still finds out the `default=(.*)` value and write it in document
- our browser will parse the document, it will see the <script> ... </script> and it will execute the script


# Difficulty - Medium

[Challange source code](https://github.com/PnzJust/DVWA-v1.10/blob/main/XSS%20DOM/Sources/medium.php)

This time the if the `<script` tag is located in url it will return an error:
```PHP
if ( array_key_exists( "default", $_GET ) && !is_null ($_GET[ 'default' ]) ) {
    $default = $_GET['default'];
    
    # Do not allow script tags
    if (stripos ($default, "<script") !== false) {
        header ("location: ?default=English");
        exit;
    }
}
```

Let's try this link: `10.10.116.119/vulnerabilities/xss_d/#default=<script>alert(1)</script>`
![...](https://github.com/PnzJust/DVWA-v1.10/blob/main/XSS%20DOM/Pictures/6.png)

This works too.

But why?

Like I said at previous difficulty:
- our browser will consider `#` as a fragment and will `not` forward it !
- the server will not consider this part  `#default=<script>alert(1)</script>` so it will `not` filtered

# Difficulty - High


[Challange source code](https://github.com/PnzJust/DVWA-v1.10/blob/main/XSS%20DOM/Sources/high.php)


This time the input is filtered like that:

```PHP
// Is there any input?
if ( array_key_exists( "default", $_GET ) && !is_null ($_GET[ 'default' ]) ) {

    # White list the allowable languages
    switch ($_GET['default']) {
        case "French":
        case "English":
        case "German":
        case "Spanish":
            # ok
            break;
        default:
            header ("location: ?default=English");
            exit;
    }
}
```
So our get request should be something like: 
`http://10.10.116.119/vulnerabilities/xss_d/?default=English`


But we can still sumbit more values to be processed by our browser:
`10.10.116.119/vulnerabilities/xss_d/?default=English#default=<script>alert(1)</script>`



# Difficulty - Impossible

[Challange source code](https://github.com/PnzJust/DVWA-v1.10/blob/main/XSS%20DOM/Sources/impossible.php)
