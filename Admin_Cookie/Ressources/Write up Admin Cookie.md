# Write up Admin Cookie

# Exploration

Upon arriving on the main page of the application, a cookie is assigned to us:  

```bash
Set-Cookie: I_am_admin=68934a3e9455fa72420237eb05902327; expires=Wed, 24-Apr-2024 20:51:16 GMT; Max-Age=3600
```

This cookie seems to be related to whether or not we have the admin role. We can also note that it does not have the **HttpOnly** attribute, allowing it to be accessed via JavaScript code.


# Exploitation

The cookie has a value that is an md5 hash. We can easily retrieve this value with an [online tool](https://md5decrypt.net/), since it is a predictable value:

![Capture d’écran 2024-05-01 à 14.19.46.png](images/Capture_decran_2024-05-01_a_14.19.46.png)

Thus, we do not have the admin role, due to the value of this cookie which is a boolean. We tried to change this value to **true** with this bash command:

```bash
~ echo -n 'true' | md5
b326b5062b2f0e69046810717534cb09
```

By replacing the current value of the cookie with this one, we obtain the flag.

# Remediation

To remedy this vulnerability, several measures are necessary:


- Do not use a boolean or predictable value in a session cookie
- Implement an authorization system with a session cookie containing a random and unpredictable value, such as a JWT
- Store the token/role correspondence on the server side, an **I_am_admin** token should not be present on the client side


Although it did not have an impact here, it is also important to mark the cookies with the HttpOnly attribute, to prevent them from being accessible from JavaScript code, for example.
