#!/usr/bin/env python3
lst=[["","","","","",""],["","","","","",""],["","","","","",""],["","","","","",""],["","","","","",""],["","","","","",""],["","","","","",""]]
sıra="t" #sıranın turuncudan başlaması
tablo="""
		1		2		3		4		5		6		7
	|	{5}	|	{11}	|	{17}	|	{23}	|	{29}	|	{35}	|	{41}	|
	|	{4}	|	{10}	|	{16}	|	{22}	|	{28}	|	{34}	|	{40}	|
	|	{3}	|	{9}	|	{15}	|	{21}	|	{27}	|	{33}	|	{39}	|
	|	{2}	|	{8}	|	{14}	|	{20}	|	{26}	|	{32}	|	{38}	|
	|	{1}	|	{7}	|	{13}	|	{19}	|	{25}	|	{31}	|	{37}	|
	|	{0}	|	{6}	|	{12}	|	{18}	|	{24}	|	{30}	|	{36}	|

"""
while True:
	d=[z for n in lst for z in n]
	print(tablo. format(*d).expandtabs(2))
	kor=input("Sıra {}'de, kaçıncı sıraya atılacak?:".format(sıra)) #kordinat sorgusu.
	if kor.isdigit() and 1<=int(kor)<=7: #girdinin istenen değerler arasında olma sorgusu
		for y in range(len(lst[int(kor)-1])): #girilen kordinatta bulunan boş olan ilk nesneye sıra sahibinin hamlesi. (pulun aşağı düşmesi)
			if not lst[int(kor)-1][y]:
				lst[int(kor)-1][y]=sıra
				break
		
		for x in range(len(lst)): #4'lü tekrarlayan belirleme bölümü: 4'lü tekrarlayan bulunduğunda küçük harften büyük harfe çevrilecek, kazanan açıklanacak
			if bool(lst[x]):
				for y in range(len(lst[x])):
					if bool(lst[x][y]):	#listenin boş olmayan adreslerinden başlayıp 3 sıra farklı yönlerde eş değerler var mı kontrolü

						if x+3<len(lst) and y<len(lst[x]):
							if lst[x+1][y]==lst[x+2][y]==lst[x+3][y]==lst[x][y]: #sağa doğru
								lst[x+1][y]=lst[x+1][y].upper()
								lst[x+2][y]=lst[x+2][y].upper()
								lst[x+3][y]=lst[x+3][y].upper()
								lst[x][y]=lst[x][y].upper()
								d=[z for n in lst for z in n]
								print(tablo. format(*d).expandtabs(2))
								print("Kazanan",sıra)
								quit()


						if x+3<len(lst) and y+3<len(lst[x]):
							if lst[x+1][y+1]==lst[x+2][y+2]==lst[x+3][y+3]==lst[x][y]:	#sağ yukarı
								lst[x+1][y+1]=lst[x+1][y+1].upper()
								lst[x+2][y+2]=lst[x+2][y+2].upper()
								lst[x+3][y+3]=lst[x+3][y+3].upper()
								lst[x][y]=lst[x][y].upper()
								d=[z for n in lst for z in n]
								print(tablo. format(*d).expandtabs(2))
								print("Kazanan",sıra)
								quit()


						if x-3>=0 and y+3<len(lst[x]) and bool(lst[x])==True:
							if lst[x-1][y+1]==lst[x-2][y+2]==lst[x-3][y+3]==lst[x][y]:	#sol yukarı
								lst[x-1][y+1]=lst[x-1][y+1].upper()
								lst[x-2][y+2]=lst[x-2][y+2].upper()
								lst[x-3][y+3]=lst[x-3][y+3].upper()
								lst[x][y]=lst[x][y].upper()
								d=[z for n in lst for z in n]
								print(tablo. format(*d).expandtabs(2))
								print("Kazanan",sıra)
								quit()


						if y+3<len(lst[x]):
							if lst[x][y+1]==lst[x][y+2]==lst[x][y+3]==lst[x][y]:	#yukarı
								lst[x][y+1]=lst[x][y+1].upper()
								lst[x][y+2]=lst[x][y+2].upper()
								lst[x][y+3]=lst[x][y+3].upper()
								lst[x][y]=lst[x][y].upper()
								d=[z for n in lst for z in n]
								print(tablo. format(*d).expandtabs(2))
								print("Kazanan",sıra)
								quit()

						elif lst[0][5] and lst[1][5] and lst[2][5] and lst[3][5] and lst[4][5] and lst[5][5] and lst[6][5]: #boş yer kaldı mı kontrolü
								d=[z for n in lst for z in n]
								print(tablo. format(*d).expandtabs(2))
								print("Boş yer kalmadı. Berabere")
								quit()
		
		if sıra=="t":	#sıra belirleme
			sıra="s"
		else:
			sıra="t"
	else:
		print("Yanlış giriş!")

