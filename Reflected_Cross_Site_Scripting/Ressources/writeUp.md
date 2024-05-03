# Write up Reflected XSS Media

## Exploration

During our exploration, we noticed that clicking on an image redirected us to a page displaying the same image again:

![Capture d’écran 2024-05-02 à 20.44.21.png](images/Capture_decran_2024-05-02_a_20.44.21.png)

## Exploitation

Upon modifying the URL source with a random value, 'test', an error page appeared with our value reflected in an HTML tag:

![Capture d’écran 2024-05-02 à 20.46.27.png](images/Capture_decran_2024-05-02_a_20.46.27.png)

We attempted to input several XSS payloads in an attempt to obtain JavaScript execution and, after several tries, we succeeded:

![Capture d’écran 2024-05-02 à 20.47.57.png](images/Capture_decran_2024-05-02_a_20.47.57.png)

Unfortunately, we did not obtain the flag. We continued our investigation.

We delved into the **object** tag and found [this post](https://security.stackexchange.com/questions/258306/how-is-object-tag-data-uri-xss-actually-xss) which led us to [this
documentation](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/Data_URLs).

According to the explanations, we can load data directly encoded in base64 using this payload:

**data:[<mediatype>][;base64],<data>**

Since our goal is to execute JavaScript code, we chose to use the mediatype **text/html**

As for the value, we simply used the following command:

```bash
echo -n '<script>alert(1)</script>' | base64
```

Our final payload was therefore **data:text/html;base64,PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg==**

We entered it into the 'src' parameter and obtained the flag:

![Capture d’écran 2024-05-02 à 20.55.00.png](images/Capture_decran_2024-05-02_a_20.55.00.png)

## Remediation

We are dealing with Reflected XSS through the GET parameter here. A malicious actor could transmit this URL to a victim, making them execute JavaScript code on their browser. Consequences may include
cookie theft or account takeover.

To remediate this vulnerability, follow these precautions:

- Validate user input and encode or remove special characters. Libraries are specifically designed for this
- Encode output special characters in HTML, especially when the user input is reflected
- Configure appropriate security headers like CSP (Content Security Policy) to mitigate XSS impact
