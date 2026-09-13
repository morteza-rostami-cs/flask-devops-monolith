```text
3. Do you need a “Shutdown” cleanup?

Even with a pool, you should close the pool when the app shuts down so that the database server is notified that the connections are intentionally closing (otherwise, the DB thinks the app crashed and keeps the sockets open until they timeout).

```
