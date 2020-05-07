# -*- coding: windows-1250 -*-
import redis
from _datetime import datetime
from _ast import If

class OsztalySzavaz():
    def __init__(self):
        
        redis_host='127.0.0.1'
        redis_port=6379
        redis_password='student'
        
        self.r=redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)
        
    def cikk_post(self, cim, link, tulaj):
        
        azon=self.r.incr("p_id")
        d=datetime.now().strftime("%Y%m%d%H%M%S")
        p=self.r.pipeline(True,None)
        p.hmset('post'+str(azon), {'cim', cim, 'link', link, 'tulaj', tulaj, 'datum', d, 'szavazat':0})
        p.zadd('zset_szavazatok', {'post'+str(azon):0})
        p.zadd('zset_datum', {'post'+str(azon):d})
        p.execute()
        return 'post'+str(azon)
    
    def post_lista_szavazat(self):
        return self.r.zrevrange('zset_szavazatok', 0, -1, withscores=True)
    
    def cikk_leiras(self, postid):
        return self.r.hgetall(postid)
    
    def post_lista_szavazat_leirassal(self):
        vissza=[]
        for i in self.r.zrevrange('zset_szavazatok', 0, -1, withscores=True):
            cl=self.cikk_leiras(i[0])
            vissza.append(i)
            vissza.append(cl)
        return vissza
    
    def post_lista_datum(self):
        return self.r.zrevrange('zset_datum', 0, -1, withscores=True)
    
    def post_lista_datum_leirassal(self):
        vissza=[]
        for i in self.r.zrevrange('zset_datum', 0, -1, withscores=True):
            cl=self.cikk_leiras(i[0])
            vissza.append(i)
            vissza.append(cl)
        return vissza
    
    def __szavazas__(self, post, felh, pont):
        self.lejarat=7 #percben
        
        ido=datetime.today()
        
        d_str=self.r.hget(post, 'datum)
        print(d_str)
        d=datetime.strptime(d_str, "%Y%m%d%H%M%S")+timedelta(minutes=self.lejarat)
        
        if (ido<d):
            print('lejart az ido')
            return False
        
        if self.r.sismember('szavazat'+post, felh)==1
            print('már szavazott')
            return False
        else:
            p=self.r.pipeline(True, None)
            p.sadd('szavazat'+post, felh)
            p.expire('szavazat'+post, self.lejarat*60)
            p.hincrby(post, 'szavazat', 1)
            p.zincrby('zset_szavazatok', 1, post)
            p.execute(True)
            
    def poz_szavazas(self, post, felh):
        self.__szavazas__(post, felh, 1)
        
    def neg_szavazas(self, post, felh):
        self.__szavazas__(post, felh, -1)
        
    def legnagyobb_szavazatu_cikk(self):
        sz=self.r.zrevrange('zset_szavazatok', 0, 0, True)
        print(sz[0][1])
        return self.r.zrevrangebyscore('zset_szavazatok', sz[0][1], sz[0][1])
        
    def legkorabbi_cikk(self):
        sz=self.r.zrange('zset_datum', 0, 0, withscores=True)
        print(sz)
        return self.r.zrangebyscore('zset_datum', float(sz[0][1]), sz[0][1])
    
    def csoportba_cikk(self, csoport, cikk):
        p=self.r.pipeline(True, None)
        p.sadd('csoportok', csoport)
        p.sadd('csoport'+csoport, cikk)
        p.execute()
        
    def csoport_cikkei(self, csoport):
        return self.r.members('csoport'+csoport)
    
    def csoportbol_kivesz_cikket(self, csoport, cikk):
        self.r.srem('csoport'+csoport, cikk)
        if self.r.exists('csoport'+csoport)==0:
            self.r.srem('csoportok', csoport)
        
    def csoport_szavazatai(self, csoport):
        self.r.zinterstore('metszet'+csoport, {'zset_szavazatok', 'csoport'+csoport}, 'max')
        self.r.expire('metszet'+csoport, 2*60)
        return self.r.zrevrange('metszet'+csoport, 0, -1, withscore=True)