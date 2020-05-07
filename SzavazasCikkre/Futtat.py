from OsztalySzavaz import OsztalySzavaz

rf=OsztalySzavaz()
rf.cikk_post('alma', 'wwwalma', 'user1')
#rf.cikk_post('korte', 'wwwkorte', 'user1')
#rf.cikk_post('citrom', 'wwwcitrom', 'user2')
#rf.cikk_post('dio', 'wwwdio', 'user5')

rf.szavazas('post9', 'user2')
#rf.szavazas('post9', 'user1')
#rf.szavazas('post9', 'user3')
#rf.szavazas('post7', 'user1')
#rf.szavazas('post7', 'user2')

#rf.poz_szavazas('post12', 'user1'')

#po=rf.cikk_post('narancs', 'wwwnarancs', 'user10')
#rf.poz_szavazas(po, 'user1')
#rf.poz_szavazas(po, 'user2')
#rf.poz_szavazas(po, 'user2')

#print(rf.post_lista_szavazat())
#print(rf.post_lista_szavazat_leirassal())
#print(rf.legnagyobb_szavazatu_cikk())
#print(rf.legkorabbi_cikk())

#rf.csoportba_cikk('allatok', 'post19')
#rf.csoportba_cikk('allatok', 'post20')

#print(rf.csoport_cikkei('allatok'))
#rf.csoportbol_kivesz_cikket('allatok', 'post20')
#rf.csoportbol_kivesz_cikket('allatok', 'post19')

#print(rf.csoport_szavazatai('allatok'))