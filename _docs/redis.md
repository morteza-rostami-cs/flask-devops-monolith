```text

# redis cli

redis-cli
127.0.0.1:6379> SET name ali
OK
127.0.0.1:6379> GET name
"ali"
127.0.0.1:6379> DEL name
(integer) 1
127.0.0.1:6379> GET name
(nil)
127.0.0.1:6379> exit

SET temporary hello EX 10

GET temporary

# inspect remaining time
TTL temporary

EXISTS user:1

# Redis keys

# A common Redis convention is to structure keys using :

# For example:

# user:1
# user:2
# user:3

#====

redis_client.set(key, value)
redis_client.get(key)
redis_client.delete(key)
redis_client.exists(key)
redis_client.expire(key, seconds)

redis_client.set(
    "some:key",
    "some value",
    ex=60,
)

# redis test
    @app.get("/redis/test")
    def redis_test():
        redis_client.set("devops:test", "hello redis")

        value = redis_client.get("devops:test")

        return dict(value=value)


```
