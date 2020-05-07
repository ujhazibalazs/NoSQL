# -*- coding: windows-1250 -*-
from Osztaly import Osztaly
from Demonok import Demon

rf=Osztaly()

#print(rf.proba())

#rf.felhasznalo_regisztracioja('g@g.c', 'dio', 'G', '2000')
#rf.felhasznalo_regisztracioja('g@g.c', 'dio', 'G', '2000')
#rf.felhasznalo_regisztracioja('a@g.c', 'mandula', 'A', '2000')
#rf.felhasznalo_regisztracioja('f@g.c', 'alma', 'F', '2001')
#rf.felhasznalo_regisztracioja('f@g.c', 'alma', 'F', '2001')
#rf.felhasznalo_regisztracioja('d@g.c', 'dalma', 'D', '2003')

#print(rf.felhasznalo_lista_email())
#print(rf.felhasznalo_lista_attr())

#print(rf.felhasznalo_attr('g@g.c'))

#rf.felhasznalo_torlese('f@g.c')

#print(rf.elfelejtett_jelszo('a@g.c'))
#rf.jelszo_valtoztatas('g@g.c', 'dio', 'dio2')
#rf.jelszo_valtoztatas('b@g.c', 'dio', 'dio2')
#rf.jelszo_valtoztatas('a@g.c', 'dio', 'dio2')

#print(rf.felhasznalo_lista_attr())

'''
token1=rf.felhasznalo_bejelentkezik('a@g.c', 'mandula')
print(token1)
token2=rf.felhasznalo_bejelentkezik('a@g.c', 'mandula2')
print(token2)
token3=rf.felhasznalo_bejelentkezik('w@g.c', 'mandula2')
print(token3)
token4=rf.felhasznalo_bejelentkezik('a@g.c', 'mandula')
print(token4)
token5=rf.felhasznalo_bejelentkezik('g@g.c', 'dio2')
print(token5)

print(rf.felh_tokenjei('a@g.c'))
print(rf.felh_tokenjei('g@g.c'))

print(rf.tokenek())

rf.felh_kijelentkezik(token5)
rf.felh_kijelentkezik(token1)

print(rf.tokenek())
'''

'''
rf.uj_cikk('tej')
rf.uj_cikk('kenyer')
rf.uj_cikk('tejfol')
rf.uj_cikk('vaj')
rf.uj_cikk('babkonzerv')

print(rf.cikk_lista())
'''

#print(rf.tokenek())

'''
token1=rf.felhasznalo_bejelentkezik('a@g.c', 'mandula')
print(token1)
token2=rf.felhasznalo_bejelentkezik('a@g.c', 'mandula')
print(token2)
token3=rf.felhasznalo_bejelentkezik('w@g.c', 'mandula')
print(token3)
token4=rf.felhasznalo_bejelentkezik('g@g.c', 'dio2')
print(token4)
token5=rf.felhasznalo_bejelentkezik('g@g.c', 'dio2')
print(token5)

print(rf.tokenek())

rf.kosarba_tesz(token1, 'tej', 3)
rf.kosarba_tesz(token2, 'tej', -2)
rf.kosarba_tesz(token1, 'vaj', -2)
rf.kosarba_tesz(token1, 'babkonzerv', 5)
rf.kosarba_tesz(token4, 'kenyer', 1)

print(rf.kosar_tartalom(token4))

rf.kosarba_tesz(token5, 'tej', 3)
rf.kosarba_tesz(token6, 'vaj', 2)
rf.kosarba_tesz(token5, 'babkonzerv', 5)
rf.kosarba_tesz(token6, 'kenyer', 1)

rf.megrendeles(token2, 'A', 'Db', '1234')
rf.megrendeles(token2, 'G', 'Bp', '1236')
'''
'''
d=Demon()
#d.json_takarito()

print(rf.tokenek())

#rf.kosarba_tesz(token4, 'kenyer', 1)
#rf.kosarba_tesz(token3, 'vaj', 2)
#rf.kosarba_tesz(token1, 'vaj', 2)

d.token_takarito()

print(rf.kosar_tartalom(token4))
print(rf.kosar_tartalom(token3))
print(rf.tokenek)
'''