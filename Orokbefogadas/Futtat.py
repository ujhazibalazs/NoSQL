# -*- coding: windows-1250 -*-
from Osztaly import Osztaly

rf = Osztaly()

#Szemely letrehozasa
#rf.szemely_letrehoz('Bela', 'be@email.com', '18')
#rf.szemely_letrehoz("Alice", "al@test.com", 25)

#Kutya létrehozása
#rf.kutya_letrehoz('Kolbász')

print("Személyek listája:")
print(rf.szemelyek_listaja())
print("Egy bizonyos személy adatai:")
print(rf.szemely_adatai(15))

print("Kutyák listája:")
print(rf.kutyak_listaja())
print("Egy bizonyos kutya adatai:")
print(rf.kutya_adatai(11))

#print(rf.kutya_gazdaja(8))
#rf.orokbefogad(15, 11)
#rf.kutyaval_jatszik(13, 10)
#rf.kutya_etetes(13, 10)

#print(rf.szemely_kutyai(13))

#rf.versenyre_jelentkez(15, 11)
#rf.kutyara_fogad(11)
#rf.kutya_fogadas_visszavon(9)

print(rf.verseny_ranglista())
rf.legeselyesebb_versenyzo()


