# -*- coding: windows-1250 -*-
from Osztaly import Osztaly

rf = Osztaly()

#Szemely letrehozasa
#rf.szemely_letrehoz('Bela', 'be@email.com', '18')
#rf.szemely_letrehoz("Alice", "al@test.com", 25)

#Kutya l�trehoz�sa
#rf.kutya_letrehoz('Kolb�sz')

print("Szem�lyek list�ja:")
print(rf.szemelyek_listaja())
print("Egy bizonyos szem�ly adatai:")
print(rf.szemely_adatai(15))

print("Kuty�k list�ja:")
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


