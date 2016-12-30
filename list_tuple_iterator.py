def list_tuple(lst):
	d ={}
	for i in lst:
		if i[2] not in d:
			d[i[2]]= [i[0], i[1], i[2],0]
		d[i[2]][3] += i[3]
	print d.values()
	print type(d)




lst = [('lau_san', '999999.BTCom', 142493, 2),
       ('tay_rua', '100000.BTCom', 142495, 6),
       ('lau_san', '100500.BTCom', 142493, 5),
       ('au_nhua', '100000.BTCom', 666552, 7),
       ('lau_san', '100670.BTCom', 142493, 9),
       ('au_nhua', '189000.BTCom', 666552, 3),
       ('tay_rua', '189000.BTCom', 142495, 11),
       ('bon_cau', '189000.BTCom', 111111, 13),
       ('au_nhua', '189000.BTCom', 666552, 16)]

list_tuple(lst)