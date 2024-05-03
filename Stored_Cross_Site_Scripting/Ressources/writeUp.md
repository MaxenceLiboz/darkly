# Write up Reflected XSS Media

## Exploration

During our exploration, we came across a feedback form where we could leave a comment which was then reflected on this page:

![Capture d’écran 2024-05-02 à 21.04.31.png](images/Capture_decran_2024-05-02_a_21.04.31.png)

## Exploitation

We quickly thought of the possibility of Reflected XSS, as this type of functionality is often vulnerable.

So we entered common XSS payloads, and noticed that our `<script>` tags were being stripped from our comments:

![Capture d’écran 2024-05-02 à 21.06.17.png](images/Capture_decran_2024-05-02_a_21.06.17.png)

![Capture d’écran 2024-05-02 à 21.06.25.png](images/Capture_decran_2024-05-02_a_21.06.25.png)

However, an XSS payload did work in the name field with the following:

`<img src=a onerror=alert(1)>`

![Capture d’écran 2024-05-02 à 21.10.11.png](images/Capture_decran_2024-05-02_a_21.10.11.png)

After using many payloads (6000, thanks Intruder), and several odd tests, it seems that simply writing `script` as a comment gave us the flag. Why not.

And that's how we got it:

![Capture d’écran 2024-05-02 à 21.18.42.png](images/Capture_decran_2024-05-02_a_21.18.42.png)

## Remédiation

Here we are dealing with a Stored XSS. The impact of such vulnerability can be significant, as the injection is stored in the database and executed in each user's browser where it is exposed.

The consequences can be numerous:

- Session cookie theft
- Privilege escalation
- Defacing
- etc...

To remediate this vulnerability, here are some precautions to take:

- User input validation and encode or remove special characters. Libraries are specifically designed for this
- Encode output special characters in HTML, especially when reflecting user input
- Configure appropriate headers such as CSP (Content Security Policy) to mitigate XSS impact
