# Write up Directory Listing

## Exploration

During our exploration phase, we found the accessible `robots.txt` file.

In this file were mentioned two paths, `/whatever` and `/.hidden`.

Navigating to `/.hidden`, we stumbled upon a **directory listing**:

![Capture d'écran 2024-05-01 à 23:27:06.png](images/Capture_decran_2024-05-01_a_23.27.06.png)

It contained a set of subdirectories, each with a `README` file.

## Exploitation

The contents of the `README` files seem to indicate that what we were looking for was never in the right place.

We therefore wrote a small Python script to traverse all these paths with the intention of reading all `README` files and stopping once the one mentioning our flag, along with the path where it was found,
was discovered:

```python
~ python3 script.py
[... TRUNCATED DATA ...]
http://192.168.64.36/.hidden/whtccjokayshttvxycsvykxcfm/igeemtxnvexvxezqwntmzjltkt/lmpanswobhwcozdqixbowvbrhw/README
Here is your flag : d5eec3ec36cf80dce44a896f961c1831a05526ec215693c8f2c39543497d4466
[... TRUNCATED DATA ...]
```

## Remediation

A directory listing allows listing all files present on a given path when there is no index file (.html, .php etc.), or depending on the server web configuration.

It can be useful in certain cases, but it's generally recommended to disable it, mainly for security reasons. It can disclose sensitive information, such as filenames, software versions etc...

Although this doesn't represent a vulnerability per se, it can help a malicious person better understand their target and expand their attack surface.
