# Write up Reset Password Account Takeover
## Exploration

On the `signin` page, there is a "Forgot Password" functionality. The interface contains only one button, `Submit`. Upon clicking it, we receive an error message, "Wrong Answer":

![Capture d’écran 2024-05-02 à 18.50.38.png](images/Capture_decran_2024-05-02_a_18.50.38.png)

## Exploitation

Upon inspecting the source code of the page, we notice a hidden value that contains the email address to which the password reset link will be sent:

![Capture d’écran 2024-05-02 à 18.52.11.png](images/Capture_decran_2024-05-02_a_18.52.11.png)

Here, the email will be sent to `webmaster@borntosec.com`.

By modifying the HTML code and returning the email address, we obtain the flag:

![Capture d’écran 2024-05-02 à 18.53.13.png](images/Capture_decran_2024-05-02_a_18.53.13.png)

## Remediation

A password reset account takeover is a common vulnerability found in web applications. It allows an attacker to register an email address they control for receiving the password reset link of a legitimate
user, and thus gain access to their account.

In this case, we could take control of the `webmaster` account, which could have severe consequences for the website owners.

To mitigate this vulnerability, here are some recommendations:

- Verify that the user requesting a password reset is indeed the legitimate owner of the account. In this scenario, our session should not be able to request a password reset for the `webmaster` user with
an email different from `webmaster@borntosec.com`
- In situations where only one registered user (webmaster) exists, prevent changing the email address client-side and always send it to the same email address
