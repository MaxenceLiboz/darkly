# Write up User Input Validation

## Exploration

While navigating through the web application, we stumbled upon a page acting as a survey, allowing users to vote for individuals and assign them a grade between 1 and 10:

![Capture d'écran 2024-05-01 à 23.42.56.png](images/Capture_decran_2024-05-01_a_23.42.56.png)

Users can vote for their preferred individual and assign a grade between 1 and 10.

## Exploitation

At first glance, there was nothing unusual about this page. We then attempted to modify the expected value, i.e., between 1 and 10, to 42 by making a direct request to the backend without passing through
the frontend.

We can use this request for that purpose:

```bash
curl -X POST 'http://192.168.64.36/?page=survey' -d 'sujet=2&valeur=42' | grep flag
[... TRUNCATED DATA ...]
The flag is 03a944b434d5baff05f46c4bede5792551a2595574bcafc9a6e25f67c382ccaa
[... TRUNCATED DATA ...]
```

We were thus able to obtain the flag.

## Remédiation

Here, we face a User Input Validation issue. The web application performs client-side validation but fails to validate user input on the server side. In this case, it can allow for completely tampering
with the ongoing survey.

To mitigate this vulnerability, it's crucial to implement server-side input validation. The expected value is already known and should correspond to a number between 1 and 10.

Therefore, any other input must be rejected.
