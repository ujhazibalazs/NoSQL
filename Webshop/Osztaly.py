# -*- coding: windows-1250 -*-

import redis
import uuid
from _datetime import datetime

class Osztaly():
    def __init__(self):
        
        redis_host='127.0.0.1'
        redis_port=6379
        redis_password='student'
        
        self.r=redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)

    def felhasznalo_regisztracioja(self, email, jelszo, nev, szul_dat):
        if self.r.sismember('felh_lista', email)==1:
            print('Létező email cím')
            return False
        else:
            p=self.r.pipeline(True, None)
            p.sadd('felh_lista', email)
            p.hmset('felh_'+email, {'jelsz':jelszo, 'nev':nev, 'szul_dat':szul_dat})
            p.execute(True)
            print('a felhasználó létrejött')
            return True
            
    def felhasznalo_lista_email(self):
        return self.r.smembers('felh_lista')
    
    def felhasznalo_attr(self, email):
        return self.r.hgetall('felh_'+email)
    
    def felhasznalo_lista_attr(self):
        vissza=[]
        for i in self.r.smembers('felh_lista'):
            f=self.felhasznalo_attr(i)
            vissza.append(i)
            vissza.append(f)
        return vissza
    
    def felhasznalo_torlese(self, email):
        p=self.r.pipeline(True, None)
        p.delete('felh_'+email)
        p.srem('felh_lista', email)
        p.execute(True)
        
    def elfelejtett_jelszo(self, email):
        return self.r.hget('felh_'+email, 'jelsz')
    
    def jelszo_valtoztatas(self, email, regi_jelszo, uj_jelszo):
        trj=self.r.hget('felh_'+email, 'jelsz')
        if trj==regi_jelszo:
            self.r.hset('felh_'+email, 'jelsz', uj_jelszo)

    def __generate_token__(self):
        return str(uuid.uuid4())
    
    def felhasznalo_bejelentkezik(self, email, jelszo):
        trj=self.r.hget('felh_'+email, 'jelsz')
        if trj!=jelszo:
            print('Hibás jelszo')
            return ''
        else:
            token=self.__generate_token__()
            if self.r.hexists('tokenek', token)==1:
                print('Hibás bejelentkezés')
                return ''
            
            p=self.r.pipeline(True, None)
            p.hset('tokenek', token, email)
            p.sadd('felh_'+email+'_tokenjei', token)
            p.execute(True)
            self.kattint(token)
            return token
        
    def tokenek(self):
        return self.r.hgetall('tokenek')
    
    def felh_tokenjei(self, email):
        return self.r.smembers('felh_'+email+'_tokenjei')
    
    def felh_kijelentkezik(self, token):
        em=self.r.hget('tokenek', token)
        p=self.r.pipeline(True, None)
        p.hdel('tokenek', token)
        p.srem('felh_'+email+'_tokenjei', token)
        p.execute()
        
    def uj_cikk(self, cikk_szama):
        self.r.sadd('cikk', cikk_szama)
        
    def cikk_lista(self):
        return self.r.smembers('cikk')
    
    def kosarba_tesz(self, token, cikk, db):
        if self.r.hexists('tokenek', token)==0:
            return False
        em=self.r.hget('tokenek', token)
        self.r.hincrby('felh_'+em+'kosar', cikk, db)
        db2=self.r.hget('felh_'+em+'kosar', cikk)
        if int(db2)<=0:
            self.r.hdel('felh_'+em+'kosar', cikk)
        self.kattint(token)
        return True
        
    def kosar_tartalom(self, token):
        if self.r.hexists('tokenek', token)==0:
            return False
        em=self.r.hget('tokenek', token)
        self.kattint(token)
        return self.r.hgetall('felh_'+em+'kosar')
    
    def megrendeles(self, token, nev, cim, telefon):
        if self.r.hexists('tokenek', token)==0:
            return False
        em=self.r.hget('tokenek', token)
        self.kattint(token)
        
        kt=self.r.hgetall('felh_'+em+'kosar')
        json="{nev:"+nev+",cim:"+cim+",telefon:"+telefon+",rendeles:["
        for i in kt:
            json=json+"{cikk:"+i[0]+" ,db:"+i[1]+"},"
        json=json[0:-1]+"]}"
        print(json)
        p=self.r.pipeline(True, None)
        p.rpush("json", json)
        p.delete('felh_'+em+'kosar')
        p.execute(True)
        
    def kattint(self, token):
        if self.r.hexists('tokenek', token)==0:
            return False
        ido=datetime.now().strftime("%Y%m%d%H%M%S")
        self.r.zadd('token_aktivitas', {token:ido})