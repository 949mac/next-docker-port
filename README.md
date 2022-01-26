# Next Docker Port

Find the next sequential port available for Docker

Usage
```
next-docker-port [starting port number]
```
Example:

If you want to look for ports starting with 9000, use:
```
next-docker-port 9
```

Sample Output:

```
next-docker-port 9
9aa29b9e342a   host-1   8000/tcp, 0.0.0.0:9003->80/tcp
c8eb7229a1a6   host-2   8000/tcp, 0.0.0.0:9002->80/tcp
cb26e320d69b   host-3   8000/tcp, 0.0.0.0:9001->80/tcp
5995edf6a45c   host-4   8000/tcp, 0.0.0.0:9000->80/tcp

9000
9001
9002
9003
👉  Next Available Port: 9004

```
Copy to /usr/local/bin
```
sudo cp next-docker-port.py /usr/local/bin/next-docker-port
sudo chmod +x /usr/local/bin/next-docker-port
```