"""Basic connection example.
"""

import redis

r = redis.Redis(
    host='redis-17893.crce178.ap-east-1-1.ec2.redns.redis-cloud.com',
    port=17893,
    decode_responses=True,
    username="default",
    password="urzRoHfCK2AHEgmkIF8oJ9LwtNiUlOV2",
)

success = r.set('foo', 'bar')
# True

result = r.get('foo')
print(result)
# >>> bar
