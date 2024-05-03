# Write up Source code comments

# Exploration

Navigating through the site, if we click on the logo [© BornToSec](http://192.168.64.36/?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f) at the bottom of the page, we are redirected
to another page:

![Capture d'écran 2024-05-02 à 19.01.47.png](images/Capture_decran_2024-05-02_a_19.01.47.png)

At first glance, there doesn't seem to be any vulnerability to exploit.

# Exploitation

Upon inspecting the source code of this page, we came across a somewhat explicit comment:

![Capture d'écran 2024-05-02 à 19.02.55.png](images/Capture_decran_2024-05-02_a_19.02.55.png)

Through deduction, we sent a new request to this page but with the added header HTTP "**Referer: https://www.nsa.gov/**"

![Capture d'écran 2024-05-02 à 19.06.16.png](images/Capture_decran_2024-05-02_a_19.06.16.png)

Upon sending it, a second comment appeared:

![Capture d'écran 2024-05-02 à 19.10.47.png](images/Capture_decran_2024-05-02_a_19.10.47.png)

Once again, with some thought, we deduced that it referred to the User-Agent header. We changed it to the value **ft\_bornToSec** and thus obtained the flag.

# Remediation

Comments in source code are often left during the development of an application. These comments may contain a great deal of interesting information for an attacker, even going so far as to include
administrator passwords.

To mitigate this vulnerability, simply ensure that comments remain only in the source code of an application during production.
