# -*- coding: windows-1250 -*-

import redis
from _datetime import datetime
from datetime import timedelta
from time import sleep

class Demon():
    PERC=1
    KEVES_FELHASZNALO=1
    def __init__(self):
        
        redis_host='127.0.0.1'
        redis_port=6379
        redis_password='student'
        
        self.r=redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)
        
    def json_takarito(self):
        while True:
            json=self.r.blpop("json")
            print(json)#bárhova máshova írhatom
            
    def token_takarito(self):
        #while True:
        size=self.r.zcard('token_aktivitas')
        if size<self.KEVES_FELHASZNALO:
            sleep(10)#másodperc
        else:
            ido=(datetime.now().timedelta(minutes=self.PERC)).strftime("%Y%m%d%H%M%S")
            ta=self.r.zrangebyscore('token_aktivitas',0,ido)
            for t in ta:
                em=self.r.hget('tokenek', t)
                p=self.r.pipeline()
                p.r.hdel('tokenek', t)
                p.r.zrem('token_aktivitas', t)
                p.r.delete('felh_'+em+'kosar')
                p.r.srem('felh_'+em+'_tokenjei', t)
                p.execute()