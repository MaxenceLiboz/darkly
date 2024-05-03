# Write up Password Bruteforce

## Exploration

During our enumeration, we discovered a login panel on the **signin** page:

![Capture d'écran 2024-05-01 à 20.22.48.png](images/Capture_decran_2024-05-01_a_20.22.48.png)

## Exploitation

We tried some common default username/password combinations, like **admin:admin**, but it did not
work.

Instead, we decided to bruteforce the login using the wordlist
**10-million-password-list-top-100.txt**, which we found on
[Seclists](https://github.com/danielmiessler/SecLists), containing an enormous database of various
types of wordlists.

To carry out this operation, we used Burp Suite's Intruder:

![Capture d’écran 2024-05-01 à 20.32.00.png](images/Capture_decran_2024-05-01_a_20.32.00.png)

Upon completion, we observed that one of the **Length** responses was different from others, with
the payload being **"shadow"**. This indicates a different response, meaning a successful connection.

We then logged in using **admin:shadow** to retrieve the flag. Note that any username worked to
obtaining this flag.

## Remediation

Brute force attacks are commonly used techniques that can have severe consequences. A malicious
user gaining access to an administrator account on a platform could result in damage to integrity,
confidentiality or even availability, and harm the company's reputation.

To protect against this, here are some recommendations:

- Limit connection attempts, whether by user or IP address, within a given time frame
- Implement two-factor authentication
- Introduce an exponential delay between each failed login attempt, significantly slowing down a
brute force attack
- Require the use of robust passwords containing at least 12 characters and a combination of
uppercase letters, lowercase letters, numbers, and special characters.
