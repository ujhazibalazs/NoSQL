# -*- coding: windows-1250 -*-
from Osztaly import Osztaly

rf=Osztaly()

rf.felhasznalo_regisztracioja('Adam', 'adam')
rf.felhasznalo_regisztracioja('Anna', 'anna')
rf.felhasznalo_regisztracioja('Elek', 'elek')

print(rf.felhasznalok_listaja())

tok1=(rf.bejelentkezes('Anna', 'anna')
print(tok1)
tok2=(rf.bejelentkezes('Anna', 'anna')
print(tok2)
tok3=(rf.bejelentkezes('Anna', 'a')
print(tok3)

#---------------------------------

print(rf.tok_erv(tok1))

rf.kijelentkezes(tok1)
print(rf.tok_erv(tok1))
print(rf.tok_erv(tok3))
rf.kijelentkezes(tok2)

print(rf.elfelejtett_jelszo('Anna'))

#----------------------------

tok1=(rf.bejelentkezes('Anna', 'anna')
print(tok1)

rf.utasitas(tok1, 'alma')
rf.utasitas(tok1, 'korte')
rf.utasitas(tok1, 'alma')
rf.utasitas(tok1, 'alma')
rf.utasitas(tok1, 'korte')
rf.utasitas(tok1, 'dio')

print(rf.ut_list_leker(tok1))

rf.kijelentkezes(tok1)

#-----------------------------

tok1=(rf.bejelentkezes('Anna', 'anna')
print(tok1)

rf.utasitas(tok1, 'alma')
rf.utasitas(tok1, 'korte')
rf.utasitas(tok1, 'kobold')
rf.utasitas(tok1, 'aluminium')
rf.utasitas(tok1, 'korte')
rf.utasitas(tok1, 'dora')

print(rf.ut_list_leker(tok1))
print(rf.egyezo_ut(tok1, 'al'))
print(rf.egyezo_ut(tok1, 'ko'))
print(rf.egyezo_ut(tok1, 'd'))

rf.kijelentkezes(tok1)
