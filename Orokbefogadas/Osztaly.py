# -*- coding: windows-1250 -*-
import redis
from __builtin__ import True, False
from pickle import TRUE, FALSE

class Osztaly():
    def __init__(self):
        
        redis_host='127.0.0.1'
        redis_port=6379
        
        self.r=redis.StrictRedis(host=redis_host, port=redis_port, decode_responses=True)
        
    def szemely_letrehoz(self, nev, email, eletkor):
        azon = self.r.incr("sz_id")
        p = self.r.pipeline(True, None)
        p.hmset("szemely"+str(azon), {"nev":nev,"email":email,"eletkor":eletkor})
        p.sadd('szemelyek','szemely'+str(azon))
        p.execute()
        print("A(z) " + nev + " nevű személy létrejött.")
        return True
    
    def szemelyek_listaja(self):
        return self.r.smembers('szemelyek')
    
    def szemely_adatai(self, azon):
        return self.r.hgetall('szemely'+str(azon))
    
    def kutya_letrehoz(self, nev):
        kazon = self.r.incr("k_id")
        p = self.r.pipeline(True, None)
        p.hmset("kutya"+str(kazon), {"nev":nev, "gazda":"", "energia":100})
        p.sadd("kutyak", "kutya"+str(kazon))
        p.execute()
        print("A(z) " + nev + " nevű kutya létrejött.")
        return True
    
    def kutyak_listaja(self):
        return self.r.smembers("kutyak")
    
    def kutya_adatai(self, kazon):
        return self.r.hgetall("kutya"+str(kazon))
    
    def kutya_gazdaja(self, kazon):
        gazda = self.r.hget("kutya"+str(kazon), "gazda")
        if (gazda == ""):
            print("A kutyának nincs gazdája.")
        return gazda
    
    def van_gazdaja(self, kazon):
        gazda = self.r.hget("kutya"+str(kazon), "gazda")
        if (gazda == ""):
            return False
        return True
    
    def orokbefogad(self, azon, kazon):
        if (self.van_gazdaja(kazon)):
            print("A kutyának már van gazdája!")
            return False
        else:
            eletkor = self.r.hget("szemely"+str(azon), "eletkor")
            if (int(eletkor) >= 18):
                self.r.hset("kutya"+str(kazon), "gazda", "szemely"+str(azon))
                print("A kutya gazdája szemely" + str(azon) + " lett.")
            else:
                print("Csak 18 év fölött lehet örökbefogadni.")
                return False
        return True
    
    def kutyaval_jatszik(self, azon, kazon):
        if (self.kutya_gazdaja(kazon) == "szemely"+str(azon)):
            energia = self.r.hget("kutya"+str(kazon), "energia")
            energia = int(energia)
            if (energia >= 10):
                print("jelenlegi energia " + str(energia))
                energia -= 10
                print("játszás utáni energia: " + str(energia))
                self.r.hset("kutya"+str(kazon), "energia", energia)
            else:
                print("A kutya túl fáradt ahhoz, hogy játszon.")
                return False
        else:
            print("Nem ő a kutya gazdája.")
            return False
        return True
    
    def kutya_etetes(self, azon, kazon):
        if (self.kutya_gazdaja(kazon) == "szemely"+str(azon)):
            energia = self.r.hget("kutya"+str(kazon), "energia")
            energia = int(energia)
            if (energia == 100):
                print("A kutya nem éhes.")
                return False
            else:
                print("jelenlegi energia " + str(energia))
                energia += 5
                print("evés utáni energia: " + str(energia))
                self.r.hset("kutya"+str(kazon), "energia", energia)
        else:
            print("Nem ő a kutya gazdája.")
            return False
        return True
    
    def szemely_kutyai(self, azon):
        list = []
        darab = 0
        for i in self.r.smembers("kutyak"):
            gazda = self.r.hget(i, "gazda")
            if (gazda == "szemely"+str(azon)):
                darab += 1
                list.append(i)
        if (darab == 0):
            print("Nincs egy darab kutyája sem ennek a személynek.")
            return list
        else:
            print("A személynek " + str(darab) + " darab kutyája van.")
        return list
    
    def versenyre_jelentkez(self, azon, kazon):
        if (self.kutya_gazdaja(kazon) == "szemely"+str(azon)):
            if self.r.zscore("verseny_jeloltek", "kutya" + str(kazon)) is not None:
                print("A kutya már jelentkezett.")
                return False
            else:
                self.r.zadd("verseny_jeloltek", {"kutya"+str(kazon):0})
                print("kutya" + str(kazon) + " sikeresen nevezett a versenyre.")
        else:
            print("A kutyának nem szemely" + str(azon) + " a gazdája.")
            return False
        return True
    
    def kutyara_fogad(self, kazon):
        self.r.zincrby("verseny_jeloltek", 1, "kutya"+str(kazon))
        
    def kutya_fogadas_visszavon(self, kazon):
        if (self.r.zscore("verseny_jeloltek", "kutya"+str(kazon)) > 0):
            self.r.zincrby("verseny_jeloltek", -1, "kutya"+str(kazon))
        else:
            print("A kutyára nem szavazott senki.")
        
    def verseny_ranglista(self):
        return self.r.zrevrange("verseny_jeloltek", 0, -1, True)
    
    def legeselyesebb_versenyzo(self):
        kazon = self.r.zrevrange("verseny_jeloltek", 0, 0, False)[0]
        print("A legeselyesebb versenyzo: " + kazon)
        print("Hanyan fogadtak ra: " + str(self.r.zscore("verseny_jeloltek", kazon)))
        return True
    
    