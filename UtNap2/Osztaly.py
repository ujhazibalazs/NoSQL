# -*- coding: windows-1250 -*-

import redis
import uuid

class Osztaly():
    def __init__(self):
        
        redis_host='127.0.0.1'
        redis_port=6379
        redis_password='student'
        
        self.r=redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)
        
    def felhasznalo_regisztracioja(self, nev, jelszo):
        if self.r.hsetnx('felh', nev, jelszo)==0:
            print('Már van ilyen felhasználó')
            return False
        else:
            return True
        
    def felhasznalok_listaja(self):
        return self.r.hkeys('felh')
        #return self.r.hgetall('felh')
        
    def __generate_token__(self):
        return str(uuid.uuid4())
        
    def bejelentkezes(self, nev, jelszo):
        if self.r.hget('felh', nev)==jelszo:
            tok=self.__generate_token__()
            if self.r.hsetnx("tokenek", tok, nev)==0:
                return False
            else: return tok
        else: return "" #nem sikerült
        
    def kijelentkezes(self, tok):
        self.r.hdel('tokenek', tok)
        
    def tok_erv(self, tok):
        if self.r.hexist('tokenek', tok):
            return "Letezik"
        else:
            return "Nem letezik"
        
    def elfelejtett_jelszo(self, nev):
        return self.r.hget('felh', nev)
    
    def utasitas(self, tok, ut):
        if self.r.hexist('tokenek', tok):
            felh=self.r.hget('tokenek', tok)
            p=self.r.pipeline(True, None)
            p.lpush('ut'+felh, ut)
            p.ltrim('ut'+felh, 0,9)
            p.execute()
            return True
        else: return False
        
    def ut_list_leker(self, tok):
        if self.r.hexist('tokenek', tok):
            felh=self.r.hget('tokenek', tok)
            return self.r.lrange('ut'+felh, 0, -1)
        
    def egyezo_ut(self, tok, kezdet):
        if self.r.hexist('tokenek', tok):
            felh=self.r.hget('tokenek', tok)
            vissza=[]
            for i in self.r.lrange('ut'+felh, 0, -1):
                if i.startswith(kezdet):
                    vissza.append(i)
            return vissza