import sys


#def editNumberSeparated(num) 
#	t, s = num
#	while t != s
#		t = s s = t.replace(/^([\+\-]?\d+)(\d\d\d)/,"$1,$2")
#	return s
#

class Cal():
	hoken_dict = {
			"北海道": 0.1045,
			"青森県": 0.0996,
			"岩手県": 0.0974,
			"宮城県": 0.1001,
			"秋田県": 0.1016,
			"山形県": 0.1003,
			"福島県": 0.0964,
			"茨城県": 0.0974,
			"栃木県": 0.0987,
			"群馬県": 0.0966,
			"埼玉県": 0.0980,
			"千葉県": 0.0979,
			"東京都": 0.0984,
			"神奈川県": 0.0999,
			"山梨県": 0.0979,
			"新潟県": 0.0950,
			"富山県": 0.0959,
			"石川県": 0.1011,
			"福井県": 0.0998,
			"長野県": 0.0971,
			"岐阜県": 0.0983,
			"静岡県": 0.0972,
			"愛知県": 0.0991,
			"三重県": 0.0981,
			"滋賀県": 0.0978,
			"京都府": 0.1006,
			"大阪府": 0.1029,
			"兵庫県": 0.1024,
			"奈良県": 0.1000,
			"和歌山県": 0.1011,
			"鳥取県": 0.0997,
			"島根県": 0.1003,
			"岡山県": 0.1018,
			"広島県": 0.1004,
			"山口県": 0.1022,
			"徳島県": 0.1029,
			"香川県": 0.1028,
			"愛媛県": 0.1022,
			"高知県": 0.1017,
			"福岡県": 0.1022,
			"佐賀県": 0.1068,
			"長崎県": 0.1026,
			"熊本県": 0.1029,
			"大分県": 0.1030,
			"宮崎県": 0.0983,
			"鹿児島県": 0.1036,
			"沖縄県": 0.0995
		}
	def __init__(self, Kihonkyu, Age, Pref, Kotsuhi, Zangyodai, Fuyo):
		self.Kihonkyu = Kihonkyu
		self.Age = Age
		self.Pref = Pref
		self.Kotsuhi = Kotsuhi
		self.Zangyodai = Zangyodai
		self.Fuyo = Fuyo
		self.Komi = int(Kihonkyu) + int(Kotsuhi) + int(Zangyodai)
		

		self.KenhoTokyu, self.KenhoTokyuNum = self.Kenho()
		self.NenkinTokyu, self.NenkinTokyuNum = self.Nenkin()
		
		self.Kenho = self.KenhoVal()
		self.Kaiho = self.KaihoVal()
		self.Nenkin = self.NenkinVal()
		self.Koyo = self.KoyoVal()
		self.Gensen = self.GensenVal()
		self.Jumin = self.JuminVal()

	def __age_index(self):
		if (self.Age >= 40) and (self.Age<65):
			return 0.0180
		return 0

	def OutTedori(self):
		return {"Gakumen": self.Komi,
			"Tedori":self.TedoriVal(),
			"Kenho": self.Kenho,
			"Kaiho": self.Kaiho,
			"Nenkin":self.Nenkin,
			"Koyo": self.Koyo,
			"Syotoku": self.Gensen,
			"Jumin": self.Jumin
			}
	

	def Kenho(self):
		# 交通費＋月給+残業
		soushikyu = str(self.Komi)

		# 健康保険用 報酬分岐
		if (0<=self.Komi)and(self.Komi<63000):
			KenhoTokyu = 58000 
			KenhoTokyuNum = 1
		
		elif ((63000<=self.Komi)and(self.Komi<73000)):
			KenhoTokyu = 68000 
			KenhoTokyuNum = 2
		
		elif ((73000<=self.Komi)and(self.Komi<83000)):
			KenhoTokyu = 78000 
			KenhoTokyuNum = 3
		
		elif ((83000<=self.Komi)and(self.Komi<93000)):
			KenhoTokyu = 88000 
			KenhoTokyuNum = 4
		
		elif ((93000<=self.Komi)and(self.Komi<101000)):
			KenhoTokyu = 98000 
			KenhoTokyuNum = 5
		
		elif ((101000<=self.Komi)and(self.Komi<107000)):
			KenhoTokyu = 104000 
			KenhoTokyuNum = 6
		
		elif ((107000<=self.Komi)and(self.Komi<114000)):
			KenhoTokyu = 110000 
			KenhoTokyuNum = 7
		
		elif ((114000<=self.Komi)and(self.Komi<122000)):
			KenhoTokyu = 118000 
			KenhoTokyuNum = 8
		
		elif ((122000<=self.Komi)and(self.Komi<130000)):
			KenhoTokyu = 126000 
			KenhoTokyuNum = 9
		
		elif ((130000<=self.Komi)and(self.Komi<138000)):
			KenhoTokyu = 134000 
			KenhoTokyuNum = 10
		
		elif ((138000<=self.Komi)and(self.Komi<146000)):
			KenhoTokyu = 142000 
			KenhoTokyuNum =11
		
		elif ((146000<=self.Komi)and(self.Komi<155000)):
			KenhoTokyu = 150000 
			KenhoTokyuNum = 12
		
		elif ((155000<=self.Komi)and(self.Komi<165000)):
			KenhoTokyu = 160000 
			KenhoTokyuNum = 13
		
		elif ((165000<=self.Komi)and(self.Komi<175000)):
			KenhoTokyu = 170000 
			KenhoTokyuNum = 14
		
		elif ((175000<=self.Komi)and(self.Komi<185000)):
			KenhoTokyu = 180000 
			KenhoTokyuNum = 15
		
		elif ((185000<=self.Komi)and(self.Komi<195000)):
			KenhoTokyu = 190000 
			KenhoTokyuNum = 16
		
		elif ((195000<=self.Komi)and(self.Komi<210000)):
			KenhoTokyu = 200000 
			KenhoTokyuNum = 17
		
		elif ((210000<=self.Komi)and(self.Komi<230000)):
			KenhoTokyu = 220000 
			KenhoTokyuNum = 18
		
		elif ((230000<=self.Komi)and(self.Komi<250000)):
			KenhoTokyu = 240000 
			KenhoTokyuNum = 19
		
		elif ((250000<=self.Komi)and(self.Komi<270000)):
			KenhoTokyu = 260000 
			KenhoTokyuNum = 20
		
		elif ((270000<=self.Komi)and(self.Komi<290000)):
			KenhoTokyu = 280000 
			KenhoTokyuNum = 21
		
		elif ((290000<=self.Komi)and(self.Komi<310000)):
			KenhoTokyu = 300000 
			KenhoTokyuNum = 22
		
		elif ((310000<=self.Komi)and(self.Komi<330000)):
			KenhoTokyu = 320000 
			KenhoTokyuNum = 23
		
		elif ((330000<=self.Komi)and(self.Komi<350000)):
			KenhoTokyu = 340000 
			KenhoTokyuNum = 24
		
		elif ((350000<=self.Komi)and(self.Komi<370000)):
			KenhoTokyu = 360000 
			KenhoTokyuNum = 25
		
		elif ((370000<=self.Komi)and(self.Komi<395000)):
			KenhoTokyu = 380000 
			KenhoTokyuNum = 26
		
		elif ((395000<=self.Komi)and(self.Komi<425000)):
			KenhoTokyu = 410000 
			KenhoTokyuNum = 27
		
		elif ((425000<=self.Komi)and(self.Komi<455000)):
			KenhoTokyu = 440000 
			KenhoTokyuNum = 28
		
		elif ((455000<=self.Komi)and(self.Komi<485000)):
			KenhoTokyu = 470000 
			KenhoTokyuNum = 29
		
		elif ((485000<=self.Komi)and(self.Komi<515000)):
			KenhoTokyu = 500000 
			KenhoTokyuNum = 30
		
		elif ((515000<=self.Komi)and(self.Komi<545000)):
			KenhoTokyu = 530000 
			KenhoTokyuNum = 31
		
		elif ((545000<=self.Komi)and(self.Komi<575000)):
			KenhoTokyu = 560000 
			KenhoTokyuNum = 32
		
		elif ((575000<=self.Komi)and(self.Komi<605000)):
			KenhoTokyu = 590000 
			KenhoTokyuNum = 33
		
		elif ((605000<=self.Komi)and(self.Komi<635000)):
			KenhoTokyu = 620000 
			KenhoTokyuNum = 34
		
		elif ((635000<=self.Komi)and(self.Komi<665000)):
			KenhoTokyu = 650000 
			KenhoTokyuNum = 35
		
		elif ((665000<=self.Komi)and(self.Komi<695000)):
			KenhoTokyu = 680000 
			KenhoTokyuNum = 36
		
		elif ((695000<=self.Komi)and(self.Komi<730000)):
			KenhoTokyu = 710000 
			KenhoTokyuNum = 37
		
		elif ((730000<=self.Komi)and(self.Komi<770000)):
			KenhoTokyu = 750000 
			KenhoTokyuNum = 38
		
		elif ((770000<=self.Komi)and(self.Komi<810000)):
			KenhoTokyu = 790000 
			KenhoTokyuNum = 39
		
		elif ((810000<=self.Komi)and(self.Komi<855000)):
			KenhoTokyu = 830000 
			KenhoTokyuNum = 40
		
		elif ((855000<=self.Komi)and(self.Komi<905000)):
			KenhoTokyu = 880000 
			KenhoTokyuNum = 41
		
		elif ((905000<=self.Komi)and(self.Komi<955000)):
			KenhoTokyu = 930000 
			KenhoTokyuNum = 42
		
		elif ((955000<=self.Komi)and(self.Komi<1005000)):
			KenhoTokyu = 980000 
			KenhoTokyuNum = 43
		
		elif ((1005000<=self.Komi)and(self.Komi<1055000)):
			KenhoTokyu = 1030000 
			KenhoTokyuNum = 44
		
		elif ((1055000<=self.Komi)and(self.Komi<1115000)):
			KenhoTokyu = 1090000 
			KenhoTokyuNum = 45
		
		elif ((1115000<=self.Komi)and(self.Komi<1175000)):
			KenhoTokyu = 1150000 
			KenhoTokyuNum = 46
		
		elif (1175000<=self.Komi):
			KenhoTokyu = 1210000 
			KenhoTokyuNum = 47
		
		return KenhoTokyu, KenhoTokyuNum

	def Nenkin(self):
		#報酬（厚生年金）分岐
		if((0<=self.Komi)and(self.Komi<93000)):
			NenkinTokyu = 88000 
			NenkinTokyuNum = 1
		
		elif((93000<=self.Komi)and(self.Komi<101000)):
			NenkinTokyu = 98000 
			NenkinTokyuNum = 2
		
		elif((101000<=self.Komi)and(self.Komi<107000)):
			NenkinTokyu = 104000 
			NenkinTokyuNum = 3
		
		elif((107000<=self.Komi)and(self.Komi<114000)):
			NenkinTokyu = 110000 
			NenkinTokyuNum = 4
		
		elif((114000<=self.Komi)and(self.Komi<122000)):
			NenkinTokyu = 118000 
			NenkinTokyuNum = 5
		
		elif((122000<=self.Komi)and(self.Komi<130000)):
			NenkinTokyu = 126000 
			NenkinTokyuNum = 6
		
		elif((130000<=self.Komi)and(self.Komi<138000)):
			NenkinTokyu = 134000 
			NenkinTokyuNum = 7
		
		elif((138000<=self.Komi)and(self.Komi<146000)):
			NenkinTokyu = 142000 
			NenkinTokyuNum = 8
		
		elif((146000<=self.Komi)and(self.Komi<155000)):
			NenkinTokyu = 150000 
			NenkinTokyuNum = 9
		
		elif((155000<=self.Komi)and(self.Komi<165000)):
			NenkinTokyu = 160000 
			NenkinTokyuNum = 10
		
		elif((165000<=self.Komi)and(self.Komi<175000)):
			NenkinTokyu = 170000 
			NenkinTokyuNum = 11
		
		elif((175000<=self.Komi)and(self.Komi<185000)):
			NenkinTokyu = 180000 
			NenkinTokyuNum = 12
		
		elif((185000<=self.Komi)and(self.Komi<195000)):
			NenkinTokyu = 190000 
			NenkinTokyuNum = 13
		
		elif((195000<=self.Komi)and(self.Komi<210000)):
			NenkinTokyu = 200000 
			NenkinTokyuNum = 14
		
		elif((210000<=self.Komi)and(self.Komi<230000)):
			NenkinTokyu = 220000 
			NenkinTokyuNum = 15
		
		elif((230000<=self.Komi)and(self.Komi<250000)):
			NenkinTokyu = 240000 
			NenkinTokyuNum = 16
		
		elif((250000<=self.Komi)and(self.Komi<270000)):
			NenkinTokyu = 260000 
			NenkinTokyuNum = 17
		
		elif((270000<=self.Komi)and(self.Komi<290000)):
			NenkinTokyu = 280000 
			NenkinTokyuNum = 18
		
		elif((290000<=self.Komi)and(self.Komi<310000)):
			NenkinTokyu = 300000 
			NenkinTokyuNum = 19
		
		elif((310000<=self.Komi)and(self.Komi<330000)):
			NenkinTokyu = 320000 
			NenkinTokyuNum = 20
		
		elif((330000<=self.Komi)and(self.Komi<350000)):
			NenkinTokyu = 340000 
			NenkinTokyuNum = 21
		
		elif((350000<=self.Komi)and(self.Komi<370000)):
			NenkinTokyu = 360000 
			NenkinTokyuNum = 22
		
		elif((370000<=self.Komi)and(self.Komi<395000)):
			NenkinTokyu = 380000 
			NenkinTokyuNum = 23
		
		elif((395000<=self.Komi)and(self.Komi<425000)):
			NenkinTokyu = 410000 
			NenkinTokyuNum = 24
		
		elif((425000<=self.Komi)and(self.Komi<455000)):
			NenkinTokyu = 440000 
			NenkinTokyuNum = 25
		
		elif((455000<=self.Komi)and(self.Komi<485000)):
			NenkinTokyu = 470000 
			NenkinTokyuNum = 26
		
		elif((485000<=self.Komi)and(self.Komi<515000)):
			NenkinTokyu = 500000 
			NenkinTokyuNum = 27
		
		elif((515000<=self.Komi)and(self.Komi<545000)):
			NenkinTokyu = 530000 
			NenkinTokyuNum = 28
		
		elif((545000<=self.Komi)and(self.Komi<575000)):
			NenkinTokyu = 560000 
			NenkinTokyuNum = 29
		
		elif((575000<=self.Komi)and(self.Komi<605000)):
			NenkinTokyu = 590000 
			NenkinTokyuNum = 30
		
		elif((605000<=self.Komi)and(self.Komi<635000)):
			NenkinTokyu = 620000 
			NenkinTokyuNum = 31
		
		elif(635000<=self.Komi):
			NenkinTokyu = 650000 
			NenkinTokyuNum = 32
		
		return NenkinTokyu, NenkinTokyuNum
		
	def HokenRate(self):
		#健康保険率料
		return round(self.hoken_dict[self.Pref] * 100)
	
	def KenhoVal(self):
		#健康保険 自己負担額
		return int(self.KenhoTokyu * self.hoken_dict[self.Pref] / 2)

	def KaihoVal(self):
		# 介護保険料 折半額
		Hihoken = self.KenhoTokyu * (self.__age_index()+self.hoken_dict[self.Pref])/2
		Kaiho = int((int(Hihoken+0.4))-(int(self.Kenho+0.49)))
		return Kaiho

	def NenkinVal(self):
		# 厚生年金 折半額 出力
		Nenkin = int(((self.NenkinTokyu)*0.0915)+0.49) #17.474%(26年9月分から)
		return Nenkin
	
	def KoyoVal(self):
		# 労働者負担雇用保険
		Rkoyo = int(((self.Komi)*0.003)+0.49)
		return Rkoyo
	
	def GensenVal(self):
		#源泉所得税額表
		Gensenkeisan = int((self.Kihonkyu)-(self.Kenho+self.Kaiho+self.Nenkin+self.Koyo))
		Gensen = 0
		# 扶養1人で0円の範囲
		if((0<=Gensenkeisan)and(Gensenkeisan<88000)and(self.Fuyo==0)):
			Gensen = 0 
			
		# 扶養1人で0円の範囲
		elif((0<=Gensenkeisan)and(Gensenkeisan<119000)and(self.Fuyo==1)):
			Gensen = 0 
			
		# 扶養2人で0円の範囲
		elif((0<=Gensenkeisan)and(Gensenkeisan<159000)and(self.Fuyo==2)):
			Gensen = 0 
			
		# 扶養3人で0円の範囲
		elif((0<=Gensenkeisan)and(Gensenkeisan<205000)and(self.Fuyo==3)):
			Gensen = 0 
			
		# 扶養4人で0円の範囲
		elif((0<=Gensenkeisan)and(Gensenkeisan<251000)and(self.Fuyo==4)):
			Gensen = 0 
			
		# 扶養5人で0円の範囲
		elif((0<=Gensenkeisan)and(Gensenkeisan<296000)and(self.Fuyo==5)):
			Gensen = 0 
			
		# 扶養6人で0円の範囲
		elif((0<=Gensenkeisan)and(Gensenkeisan<335000)and(self.Fuyo==6)):
			Gensen = 0 
			
		# 扶養7人で0円の範囲
		elif((0<=Gensenkeisan)and(Gensenkeisan<374000)and(self.Fuyo==7)):
			Gensen = 0 
			
		#1
		elif((88000<=Gensenkeisan)and(Gensenkeisan<89000)and(self.Fuyo==0)):
			Gensen = 130 
		
		#2
		elif((89000<=Gensenkeisan)and(Gensenkeisan<90000)and(self.Fuyo==0)):
			Gensen = 180 
		
		#3
		elif((90000<=Gensenkeisan)and(Gensenkeisan<91000)and(self.Fuyo==0)):
			Gensen = 230 
		
		#4
		elif((91000<=Gensenkeisan)and(Gensenkeisan<92000)and(self.Fuyo==0)):
			Gensen = 290 
		
		#5
		elif((92000<=Gensenkeisan)and(Gensenkeisan<93000)and(self.Fuyo==0)):
			Gensen = 340 
		
		#6
		elif((93000<=Gensenkeisan)and(Gensenkeisan<94000)and(self.Fuyo==0)):
			Gensen = 390 
		
		#7
		elif((94000<=Gensenkeisan)and(Gensenkeisan<95000)and(self.Fuyo==0)):
			Gensen = 440 
		
		#8
		elif((95000<=Gensenkeisan)and(Gensenkeisan<96000)and(self.Fuyo==0)):
			Gensen = 490 
		
		#9
		elif((96000<=Gensenkeisan)and(Gensenkeisan<97000)and(self.Fuyo==0)):
			Gensen = 540 
		
		#10
		elif((97000<=Gensenkeisan)and(Gensenkeisan<98000)and(self.Fuyo==0)):
			Gensen = 590 
		
		#11
		elif((98000<=Gensenkeisan)and(Gensenkeisan<99000)and(self.Fuyo==0)):
			Gensen = 640 
		
		#12
		elif((99000<=Gensenkeisan)and(Gensenkeisan<101000)and(self.Fuyo==0)):
			Gensen = 720 
		
		#13
		elif((101000<=Gensenkeisan)and(Gensenkeisan<103000)and(self.Fuyo==0)):
			Gensen = 830 
		
		#14
		elif((103000<=Gensenkeisan)and(Gensenkeisan<105000)and(self.Fuyo==0)):
			Gensen = 930 
		
		#15
		elif((105000<=Gensenkeisan)and(Gensenkeisan<107000)and(self.Fuyo==0)):
			Gensen = 1030 
		
		#16
		elif((107000<=Gensenkeisan)and(Gensenkeisan<109000)and(self.Fuyo==0)):
			Gensen = 1130 
		
		#17
		elif((109000<=Gensenkeisan)and(Gensenkeisan<111000)and(self.Fuyo==0)):
			Gensen = 1240 
		
		#18
		elif((111000<=Gensenkeisan)and(Gensenkeisan<113000)and(self.Fuyo==0)):
			Gensen = 1340 
		
		#19
		elif((113000<=Gensenkeisan)and(Gensenkeisan<115000)and(self.Fuyo==0)):
			Gensen = 1440 
		
		#20
		elif((115000<=Gensenkeisan)and(Gensenkeisan<117000)and(self.Fuyo==0)):
			Gensen = 1540 
		
		#21
		elif((117000<=Gensenkeisan)and(Gensenkeisan<119000)and(self.Fuyo==0)):
			Gensen = 1640 
		
		#22
		elif((119000<=Gensenkeisan)and(Gensenkeisan<121000)and(self.Fuyo==0)):
			Gensen = 1850 
		
		elif((119000<=Gensenkeisan)and(Gensenkeisan<121000)and(self.Fuyo==1)):
			Gensen = 120 
		
		#23
		elif((121000<=Gensenkeisan)and(Gensenkeisan<123000)and(self.Fuyo==0)):
			Gensen = 1850 
		
		elif((121000<=Gensenkeisan)and(Gensenkeisan<123000)and(self.Fuyo==1)):
			Gensen = 220 
		
		#24
		elif((123000<=Gensenkeisan)and(Gensenkeisan<125000)and(self.Fuyo==0)):
			Gensen = 1950 
		
		elif((123000<=Gensenkeisan)and(Gensenkeisan<125000)and(self.Fuyo==1)):
			Gensen = 330 
		
		#25
		elif((125000<=Gensenkeisan)and(Gensenkeisan<127000)and(self.Fuyo==0)):
			Gensen = 2050 
		
		elif((125000<=Gensenkeisan)and(Gensenkeisan<127000)and(self.Fuyo==1)):
			Gensen = 430 
		
		#26
		elif((127000<=Gensenkeisan)and(Gensenkeisan<129000)and(self.Fuyo==0)):
			Gensen = 2150 
		
		elif((127000<=Gensenkeisan)and(Gensenkeisan<129000)and(self.Fuyo==1)):
			Gensen = 530 
		
		#27
		elif((129000<=Gensenkeisan)and(Gensenkeisan<131000)and(self.Fuyo==0)):
			Gensen = 2260 
		
		elif((129000<=Gensenkeisan)and(Gensenkeisan<131000)and(self.Fuyo==1)):
			Gensen = 630 
		
		#28
		elif((131000<=Gensenkeisan)and(Gensenkeisan<133000)and(self.Fuyo==0)):
			Gensen = 2360 
		
		elif((131000<=Gensenkeisan)and(Gensenkeisan<133000)and(self.Fuyo==1)):
			Gensen = 740 
		
		#29
		elif((133000<=Gensenkeisan)and(Gensenkeisan<135000)and(self.Fuyo==0)):
			Gensen = 2460 
		
		elif((133000<=Gensenkeisan)and(Gensenkeisan<135000)and(self.Fuyo==1)):
			Gensen = 840 
		
		#30
		elif((135000<=Gensenkeisan)and(Gensenkeisan<137000)and(self.Fuyo==0)):
			Gensen = 2550 
		
		elif((135000<=Gensenkeisan)and(Gensenkeisan<137000)and(self.Fuyo==1)):
			Gensen = 930 
		
		#31
		elif((137000<=Gensenkeisan)and(Gensenkeisan<139000)and(self.Fuyo==0)):
			Gensen = 2610 
		
		elif((137000<=Gensenkeisan)and(Gensenkeisan<139000)and(self.Fuyo==1)):
			Gensen = 990 
		
		#32
		elif((139000<=Gensenkeisan)and(Gensenkeisan<141000)and(self.Fuyo==0)):
			Gensen = 2680 
		
		elif((139000<=Gensenkeisan)and(Gensenkeisan<141000)and(self.Fuyo==1)):
			Gensen = 1050 
		
		#33
		elif((141000<=Gensenkeisan)and(Gensenkeisan<143000)and(self.Fuyo==0)):
			Gensen = 2740 
		
		elif((141000<=Gensenkeisan)and(Gensenkeisan<143000)and(self.Fuyo==1)):
			Gensen = 1110 
		
		#34
		elif((143000<=Gensenkeisan)and(Gensenkeisan<145000)and(self.Fuyo==0)): 
			Gensen = 2800   
		
		elif((143000<=Gensenkeisan)and(Gensenkeisan<145000)and(self.Fuyo==1)):
			Gensen = 1170 
		
		#35
		elif((145000<=Gensenkeisan)and(Gensenkeisan<147000)and(self.Fuyo==0)): 
			Gensen = 2860   
		
		elif((145000<=Gensenkeisan)and(Gensenkeisan<147000)and(self.Fuyo==1)):
			Gensen = 1240 
		
		#36
		elif((147000<=Gensenkeisan)and(Gensenkeisan<149000)and(self.Fuyo==0)): 
			Gensen = 2920   
		
		elif((147000<=Gensenkeisan)and(Gensenkeisan<149000)and(self.Fuyo==1)):
			Gensen = 1300 
		
		#37
		elif((149000<=Gensenkeisan)and(Gensenkeisan<151000)and(self.Fuyo==0)): 
			Gensen = 2980   
		
		elif((149000<=Gensenkeisan)and(Gensenkeisan<151000)and(self.Fuyo==1)):
			Gensen = 1360 
		
		#38
		elif((151000<=Gensenkeisan)and(Gensenkeisan<153000)and(self.Fuyo==0)): 
			Gensen = 3050   
		
		elif((151000<=Gensenkeisan)and(Gensenkeisan<153000)and(self.Fuyo==1)):
			Gensen = 1430 
		
		#39
		elif((153000<=Gensenkeisan)and(Gensenkeisan<155000)and(self.Fuyo==0)): 
			Gensen = 3120   
		
		elif((153000<=Gensenkeisan)and(Gensenkeisan<155000)and(self.Fuyo==1)):
			Gensen = 1500 
		
		#40
		elif((155000<=Gensenkeisan)and(Gensenkeisan<157000)and(self.Fuyo==0)): 
			Gensen = 3200   
		
		elif((155000<=Gensenkeisan)and(Gensenkeisan<157000)and(self.Fuyo==1)):
			Gensen = 1570 
		
		#41
		elif((157000<=Gensenkeisan)and(Gensenkeisan<159000)and(self.Fuyo==0)): 
			Gensen = 3270   
		
		elif((157000<=Gensenkeisan)and(Gensenkeisan<159000)and(self.Fuyo==1)):
			Gensen = 1640 
		
		#42
		elif((159000<=Gensenkeisan)and(Gensenkeisan<161000)and(self.Fuyo==0)): 
			Gensen = 3340   
		
		elif((159000<=Gensenkeisan)and(Gensenkeisan<161000)and(self.Fuyo==1)):
			Gensen = 1720 
		
		elif((159000<=Gensenkeisan)and(Gensenkeisan<161000)and(self.Fuyo==2)):
			Gensen = 100
		
		#43
		elif((161000<=Gensenkeisan)and(Gensenkeisan<163000)and(self.Fuyo==0)): 
			Gensen = 3410   
		
		elif((161000<=Gensenkeisan)and(Gensenkeisan<163000)and(self.Fuyo==1)):
			Gensen = 1790 
		
		elif((161000<=Gensenkeisan)and(Gensenkeisan<163000)and(self.Fuyo==2)):
			Gensen = 170
		
		#44
		elif((163000<=Gensenkeisan)and(Gensenkeisan<165000)and(self.Fuyo==0)): 
			Gensen = 3480   
		
		elif((163000<=Gensenkeisan)and(Gensenkeisan<165000)and(self.Fuyo==1)):
			Gensen = 1860 
		
		elif((163000<=Gensenkeisan)and(Gensenkeisan<165000)and(self.Fuyo==2)):
			Gensen = 250
		
		#45
		elif((165000<=Gensenkeisan)and(Gensenkeisan<167000)and(self.Fuyo==0)): 
			Gensen = 3550   
		
		elif((165000<=Gensenkeisan)and(Gensenkeisan<167000)and(self.Fuyo==1)):
			Gensen = 1930 
		
		elif((165000<=Gensenkeisan)and(Gensenkeisan<167000)and(self.Fuyo==2)):
			Gensen = 320
		
		#46
		elif((167000<=Gensenkeisan)and(Gensenkeisan<169000)and(self.Fuyo==0)): 
			Gensen = 3620   
		
		elif((167000<=Gensenkeisan)and(Gensenkeisan<169000)and(self.Fuyo==1)):
			Gensen = 2000 
		
		elif((167000<=Gensenkeisan)and(Gensenkeisan<169000)and(self.Fuyo==2)):
			Gensen = 390
		
		#47
		elif((169000<=Gensenkeisan)and(Gensenkeisan<171000)and(self.Fuyo==0)): 
			Gensen = 3700   
		
		elif((169000<=Gensenkeisan)and(Gensenkeisan<171000)and(self.Fuyo==1)):
			Gensen = 2070 
		
		elif((169000<=Gensenkeisan)and(Gensenkeisan<171000)and(self.Fuyo==2)):
			Gensen = 460
		
		#48
		elif((171000<=Gensenkeisan)and(Gensenkeisan<173000)and(self.Fuyo==0)): 
			Gensen = 3770   
		
		elif((171000<=Gensenkeisan)and(Gensenkeisan<173000)and(self.Fuyo==1)):
			Gensen = 2140 
		
		elif((171000<=Gensenkeisan)and(Gensenkeisan<173000)and(self.Fuyo==2)):
			Gensen = 530
		
		#49
		elif((173000<=Gensenkeisan)and(Gensenkeisan<175000)and(self.Fuyo==0)): 
			Gensen = 3840   
		
		elif((173000<=Gensenkeisan)and(Gensenkeisan<175000)and(self.Fuyo==1)):
			Gensen = 2220 
		
		elif((173000<=Gensenkeisan)and(Gensenkeisan<175000)and(self.Fuyo==2)):
			Gensen = 600
		
		#50
		elif((175000<=Gensenkeisan)and(Gensenkeisan<177000)and(self.Fuyo==0)): 
			Gensen = 3910   
		
		elif((175000<=Gensenkeisan)and(Gensenkeisan<177000)and(self.Fuyo==1)):
			Gensen = 2290 
		
		elif((175000<=Gensenkeisan)and(Gensenkeisan<177000)and(self.Fuyo==2)):
			Gensen = 670
		
		#51
		elif((177000<=Gensenkeisan)and(Gensenkeisan<179000)and(self.Fuyo==0)): 
			Gensen = 3980   
		
		elif((177000<=Gensenkeisan)and(Gensenkeisan<179000)and(self.Fuyo==1)):
			Gensen = 2360 
		
		elif((177000<=Gensenkeisan)and(Gensenkeisan<179000)and(self.Fuyo==2)):
			Gensen = 750
		
		#52
		elif((179000<=Gensenkeisan)and(Gensenkeisan<181000)and(self.Fuyo==0)): 
			Gensen = 4050   
		
		elif((179000<=Gensenkeisan)and(Gensenkeisan<181000)and(self.Fuyo==1)):
			Gensen = 2430 
		
		elif((179000<=Gensenkeisan)and(Gensenkeisan<181000)and(self.Fuyo==2)):
			Gensen = 820
		
		#53
		elif((181000<=Gensenkeisan)and(Gensenkeisan<183000)and(self.Fuyo==0)): 
			Gensen = 4120   
		
		elif((181000<=Gensenkeisan)and(Gensenkeisan<183000)and(self.Fuyo==1)):
			Gensen = 2500 
		
		elif((181000<=Gensenkeisan)and(Gensenkeisan<183000)and(self.Fuyo==2)):
			Gensen = 890
		
		#54
		elif((183000<=Gensenkeisan)and(Gensenkeisan<185000)and(self.Fuyo==0)): 
			Gensen = 4200   
		
		elif((183000<=Gensenkeisan)and(Gensenkeisan<185000)and(self.Fuyo==1)):
			Gensen = 2570 
		
		elif((183000<=Gensenkeisan)and(Gensenkeisan<185000)and(self.Fuyo==2)):
			Gensen = 960
		
		#55
		elif((185000<=Gensenkeisan)and(Gensenkeisan<187000)and(self.Fuyo==0)): 
			Gensen = 4270 
		
		elif((185000<=Gensenkeisan)and(Gensenkeisan<187000)and(self.Fuyo==1)):
			Gensen = 2640 
		
		elif((185000<=Gensenkeisan)and(Gensenkeisan<187000)and(self.Fuyo==2)):
			Gensen = 1030
		
		#56
		elif((187000<=Gensenkeisan)and(Gensenkeisan<189000)and(self.Fuyo==0)): 
			Gensen = 4340   
		
		elif((187000<=Gensenkeisan)and(Gensenkeisan<189000)and(self.Fuyo==1)):
			Gensen = 2720 
		
		elif((187000<=Gensenkeisan)and(Gensenkeisan<189000)and(self.Fuyo==2)):
			Gensen = 1100
		
		#57
		elif((189000<=Gensenkeisan)and(Gensenkeisan<191000)and(self.Fuyo==0)): 
			Gensen = 4410   
		
		elif((189000<=Gensenkeisan)and(Gensenkeisan<191000)and(self.Fuyo==1)):
			Gensen = 2790 
		
		elif((189000<=Gensenkeisan)and(Gensenkeisan<191000)and(self.Fuyo==2)):
			Gensen = 1170
		
		#58
		elif((191000<=Gensenkeisan)and(Gensenkeisan<193000)and(self.Fuyo==0)): 
			Gensen = 4480   
		
		elif((191000<=Gensenkeisan)and(Gensenkeisan<193000)and(self.Fuyo==1)):
			Gensen = 2860 
		
		elif((191000<=Gensenkeisan)and(Gensenkeisan<193000)and(self.Fuyo==2)):
			Gensen = 1250
		
		#59
		elif((193000<=Gensenkeisan)and(Gensenkeisan<195000)and(self.Fuyo==0)): 
			Gensen = 4550   
		
		elif((193000<=Gensenkeisan)and(Gensenkeisan<195000)and(self.Fuyo==1)):
			Gensen = 2930 
		
		elif((193000<=Gensenkeisan)and(Gensenkeisan<195000)and(self.Fuyo==2)):
			Gensen = 1320
		
		#60
		elif((195000<=Gensenkeisan)and(Gensenkeisan<197000)and(self.Fuyo==0)): 
			Gensen = 4630   
		
		elif((195000<=Gensenkeisan)and(Gensenkeisan<197000)and(self.Fuyo==1)):
			Gensen = 3000 
		
		elif((195000<=Gensenkeisan)and(Gensenkeisan<197000)and(self.Fuyo==2)):
			Gensen = 1390
		
		#61
		elif((197000<=Gensenkeisan)and(Gensenkeisan<199000)and(self.Fuyo==0)): 
			Gensen = 4700   
		
		elif((197000<=Gensenkeisan)and(Gensenkeisan<199000)and(self.Fuyo==1)):
			Gensen = 3070 
		
		elif((197000<=Gensenkeisan)and(Gensenkeisan<199000)and(self.Fuyo==2)):
			Gensen = 1460
		
		#62
		elif((199000<=Gensenkeisan)and(Gensenkeisan<201000)and(self.Fuyo==0)): 
			Gensen = 4770   
		
		elif((199000<=Gensenkeisan)and(Gensenkeisan<201000)and(self.Fuyo==1)):
			Gensen = 3140 
		
		elif((199000<=Gensenkeisan)and(Gensenkeisan<201000)and(self.Fuyo==2)):
			Gensen = 1530
		
		#63
		elif((201000<=Gensenkeisan)and(Gensenkeisan<203000)and(self.Fuyo==0)): 
			Gensen = 4840   
		
		elif((201000<=Gensenkeisan)and(Gensenkeisan<203000)and(self.Fuyo==1)):
			Gensen = 3220 
		
		elif((201000<=Gensenkeisan)and(Gensenkeisan<203000)and(self.Fuyo==2)):
			Gensen = 1600
		
		#64
		elif((203000<=Gensenkeisan)and(Gensenkeisan<205000)and(self.Fuyo==0)): 
			Gensen = 4910   
		
		elif((203000<=Gensenkeisan)and(Gensenkeisan<205000)and(self.Fuyo==1)):
			Gensen = 3290 
		
		elif((203000<=Gensenkeisan)and(Gensenkeisan<205000)and(self.Fuyo==2)):
			Gensen = 1670
		
		#65
		elif((205000<=Gensenkeisan)and(Gensenkeisan<207000)and(self.Fuyo==0)): 
			Gensen = 4980   
		
		elif((205000<=Gensenkeisan)and(Gensenkeisan<207000)and(self.Fuyo==1)):
			Gensen = 3360 
		
		elif((205000<=Gensenkeisan)and(Gensenkeisan<207000)and(self.Fuyo==2)):
			Gensen = 1750
		
		elif((205000<=Gensenkeisan)and(Gensenkeisan<207000)and(self.Fuyo==3)):
			Gensen = 130
		
		#66
		elif((207000<=Gensenkeisan)and(Gensenkeisan<209000)and(self.Fuyo==0)): 
			Gensen = 5050   
		
		elif((207000<=Gensenkeisan)and(Gensenkeisan<209000)and(self.Fuyo==1)):
			Gensen = 3430 
		
		elif((207000<=Gensenkeisan)and(Gensenkeisan<209000)and(self.Fuyo==2)):
			Gensen = 1820
		
		elif((207000<=Gensenkeisan)and(Gensenkeisan<209000)and(self.Fuyo==3)):
			Gensen = 200
		
		#67
		elif((209000<=Gensenkeisan)and(Gensenkeisan<211000)and(self.Fuyo==0)): 
			Gensen = 5130   
		
		elif((209000<=Gensenkeisan)and(Gensenkeisan<211000)and(self.Fuyo==1)):
			Gensen = 3500 
		
		elif((209000<=Gensenkeisan)and(Gensenkeisan<211000)and(self.Fuyo==2)):
			Gensen = 1890
		
		elif((209000<=Gensenkeisan)and(Gensenkeisan<211000)and(self.Fuyo==3)):
			Gensen = 280
		
		#68
		elif((211000<=Gensenkeisan)and(Gensenkeisan<213000)and(self.Fuyo==0)): 
			Gensen = 5200   
		
		elif((211000<=Gensenkeisan)and(Gensenkeisan<213000)and(self.Fuyo==1)):
			Gensen = 3570 
		
		elif((211000<=Gensenkeisan)and(Gensenkeisan<213000)and(self.Fuyo==2)):
			Gensen = 1960
		
		elif((211000<=Gensenkeisan)and(Gensenkeisan<213000)and(self.Fuyo==3)):
			Gensen = 350
		
		#69
		elif((213000<=Gensenkeisan)and(Gensenkeisan<215000)and(self.Fuyo==0)): 
			Gensen = 5270   
		
		elif((213000<=Gensenkeisan)and(Gensenkeisan<215000)and(self.Fuyo==1)):
			Gensen = 3640 
		
		elif((213000<=Gensenkeisan)and(Gensenkeisan<215000)and(self.Fuyo==2)):
			Gensen = 2030
		
		elif((213000<=Gensenkeisan)and(Gensenkeisan<215000)and(self.Fuyo==3)):
			Gensen = 420
		
		#70
		elif((215000<=Gensenkeisan)and(Gensenkeisan<217000)and(self.Fuyo==0)): 
			Gensen = 5340   
		
		elif((215000<=Gensenkeisan)and(Gensenkeisan<217000)and(self.Fuyo==1)):
			Gensen = 3720 
		
		elif((215000<=Gensenkeisan)and(Gensenkeisan<217000)and(self.Fuyo==2)):
			Gensen = 2100
		
		elif((215000<=Gensenkeisan)and(Gensenkeisan<217000)and(self.Fuyo==3)):
			Gensen = 490
		
		#71
		elif((217000<=Gensenkeisan)and(Gensenkeisan<219000)and(self.Fuyo==0)): 
			Gensen = 5410   
		
		elif((217000<=Gensenkeisan)and(Gensenkeisan<219000)and(self.Fuyo==1)):
			Gensen = 3790 
		
		elif((217000<=Gensenkeisan)and(Gensenkeisan<219000)and(self.Fuyo==2)):
			Gensen = 2170
		
		elif((217000<=Gensenkeisan)and(Gensenkeisan<219000)and(self.Fuyo==3)):
			Gensen = 560
		
		#72
		elif((219000<=Gensenkeisan)and(Gensenkeisan<221000)and(self.Fuyo==0)): 
			Gensen = 5480   
		
		elif((219000<=Gensenkeisan)and(Gensenkeisan<221000)and(self.Fuyo==1)):
			Gensen = 3860 
		
		elif((219000<=Gensenkeisan)and(Gensenkeisan<221000)and(self.Fuyo==2)):
			Gensen = 2250
		
		elif((219000<=Gensenkeisan)and(Gensenkeisan<221000)and(self.Fuyo==3)):
			Gensen = 630
		
		#73
		elif((221000<=Gensenkeisan)and(Gensenkeisan<224000)and(self.Fuyo==0)): 
			Gensen = 5560   
		
		elif((221000<=Gensenkeisan)and(Gensenkeisan<224000)and(self.Fuyo==1)):
			Gensen = 3950 
		
		elif((221000<=Gensenkeisan)and(Gensenkeisan<224000)and(self.Fuyo==2)):
			Gensen = 2340
		
		elif((221000<=Gensenkeisan)and(Gensenkeisan<224000)and(self.Fuyo==3)):
			Gensen = 710
		
		#74
		elif((224000<=Gensenkeisan)and(Gensenkeisan<227000)and(self.Fuyo==0)): 
			Gensen = 5680   
		
		elif((224000<=Gensenkeisan)and(Gensenkeisan<227000)and(self.Fuyo==1)):
			Gensen = 4060 
		
		elif((224000<=Gensenkeisan)and(Gensenkeisan<227000)and(self.Fuyo==2)):
			Gensen = 2440
		
		elif((224000<=Gensenkeisan)and(Gensenkeisan<227000)and(self.Fuyo==3)):
			Gensen = 830
		
		#75
		elif((227000<=Gensenkeisan)and(Gensenkeisan<230000)and(self.Fuyo==0)): 
			Gensen = 5780   
		
		elif((227000<=Gensenkeisan)and(Gensenkeisan<230000)and(self.Fuyo==1)):
			Gensen = 4170 
		
		elif((227000<=Gensenkeisan)and(Gensenkeisan<230000)and(self.Fuyo==2)):
			Gensen = 2550
		
		elif((227000<=Gensenkeisan)and(Gensenkeisan<230000)and(self.Fuyo==3)):
			Gensen = 930
		
		#76
		elif((230000<=Gensenkeisan)and(Gensenkeisan<233000)and(self.Fuyo==0)): 
			Gensen = 5890   
		
		elif((230000<=Gensenkeisan)and(Gensenkeisan<233000)and(self.Fuyo==1)):
			Gensen = 4280 
		
		elif((230000<=Gensenkeisan)and(Gensenkeisan<233000)and(self.Fuyo==2)):
			Gensen = 2650
		
		elif((230000<=Gensenkeisan)and(Gensenkeisan<233000)and(self.Fuyo==3)):
			Gensen = 1040
		
		#77
		elif((233000<=Gensenkeisan)and(Gensenkeisan<236000)and(self.Fuyo==0)): 
			Gensen = 5990   
		
		elif((233000<=Gensenkeisan)and(Gensenkeisan<236000)and(self.Fuyo==1)):
			Gensen = 4380 
		
		elif((233000<=Gensenkeisan)and(Gensenkeisan<236000)and(self.Fuyo==2)):
			Gensen = 2770
		
		elif((233000<=Gensenkeisan)and(Gensenkeisan<236000)and(self.Fuyo==3)):
			Gensen = 1140
		
		#78
		elif((236000<=Gensenkeisan)and(Gensenkeisan<239000)and(self.Fuyo==0)): 
			Gensen = 6110   
		
		elif((236000<=Gensenkeisan)and(Gensenkeisan<239000)and(self.Fuyo==1)):
			Gensen = 4490 
		
		elif((236000<=Gensenkeisan)and(Gensenkeisan<239000)and(self.Fuyo==2)):
			Gensen = 2870
		
		elif((236000<=Gensenkeisan)and(Gensenkeisan<239000)and(self.Fuyo==3)):
			Gensen = 1260
		
		#79
		elif((239000<=Gensenkeisan)and(Gensenkeisan<242000)and(self.Fuyo==0)): 
			Gensen = 6210   
		
		elif((239000<=Gensenkeisan)and(Gensenkeisan<242000)and(self.Fuyo==1)):
			Gensen = 4590 
		
		elif((239000<=Gensenkeisan)and(Gensenkeisan<242000)and(self.Fuyo==2)):
			Gensen = 2980
		
		elif((239000<=Gensenkeisan)and(Gensenkeisan<242000)and(self.Fuyo==3)):
			Gensen = 1360
		
		#80
		elif((242000<=Gensenkeisan)and(Gensenkeisan<245000)and(self.Fuyo==0)): 
			Gensen = 6320   
		
		elif((242000<=Gensenkeisan)and(Gensenkeisan<245000)and(self.Fuyo==1)):
			Gensen = 4710 
		
		elif((242000<=Gensenkeisan)and(Gensenkeisan<245000)and(self.Fuyo==2)):
			Gensen = 3080
		
		elif((242000<=Gensenkeisan)and(Gensenkeisan<245000)and(self.Fuyo==3)):
			Gensen = 1470
		
		#81
		elif((245000<=Gensenkeisan)and(Gensenkeisan<248000)and(self.Fuyo==0)): 
			Gensen = 6420   
		
		elif((245000<=Gensenkeisan)and(Gensenkeisan<248000)and(self.Fuyo==1)):
			Gensen = 4810 
		
		elif((245000<=Gensenkeisan)and(Gensenkeisan<248000)and(self.Fuyo==2)):
			Gensen = 3200
		
		elif((245000<=Gensenkeisan)and(Gensenkeisan<248000)and(self.Fuyo==3)):
			Gensen = 1570
		
		#82
		elif((248000<=Gensenkeisan)and(Gensenkeisan<251000)and(self.Fuyo==0)): 
			Gensen = 6530   
		
		elif((248000<=Gensenkeisan)and(Gensenkeisan<251000)and(self.Fuyo==1)):
			Gensen = 4920 
		
		elif((248000<=Gensenkeisan)and(Gensenkeisan<251000)and(self.Fuyo==2)):
			Gensen = 3300
		
		elif((248000<=Gensenkeisan)and(Gensenkeisan<251000)and(self.Fuyo==3)):
			Gensen = 1680
		
		#83
		elif((251000<=Gensenkeisan)and(Gensenkeisan<254000)and(self.Fuyo==0)): 
			Gensen = 6640   
		
		elif((251000<=Gensenkeisan)and(Gensenkeisan<254000)and(self.Fuyo==1)):
			Gensen = 5020 
		
		elif((251000<=Gensenkeisan)and(Gensenkeisan<254000)and(self.Fuyo==2)):
			Gensen = 3410
		
		elif((251000<=Gensenkeisan)and(Gensenkeisan<254000)and(self.Fuyo==3)):
			Gensen = 1790
		
		elif((251000<=Gensenkeisan)and(Gensenkeisan<254000)and(self.Fuyo==4)):
			Gensen = 170
		
		#84
		elif((254000<=Gensenkeisan)and(Gensenkeisan<257000)and(self.Fuyo==0)): 
			Gensen = 6750   
		
		elif((254000<=Gensenkeisan)and(Gensenkeisan<257000)and(self.Fuyo==1)):
			Gensen = 5140 
		
		elif((254000<=Gensenkeisan)and(Gensenkeisan<257000)and(self.Fuyo==2)):
			Gensen = 3510
		
		elif((254000<=Gensenkeisan)and(Gensenkeisan<257000)and(self.Fuyo==3)):
			Gensen = 1900
		
		elif((254000<=Gensenkeisan)and(Gensenkeisan<257000)and(self.Fuyo==4)):
			Gensen = 290
		
		#85
		elif((257000<=Gensenkeisan)and(Gensenkeisan<260000)and(self.Fuyo==0)): 
			Gensen = 6850   
		
		elif((257000<=Gensenkeisan)and(Gensenkeisan<260000)and(self.Fuyo==1)):
			Gensen = 5240 
		
		elif((257000<=Gensenkeisan)and(Gensenkeisan<260000)and(self.Fuyo==2)):
			Gensen = 3620
		
		elif((257000<=Gensenkeisan)and(Gensenkeisan<260000)and(self.Fuyo==3)):
			Gensen = 2000
		
		elif((257000<=Gensenkeisan)and(Gensenkeisan<260000)and(self.Fuyo==4)):
			Gensen = 390
		
		#86
		elif((260000<=Gensenkeisan)and(Gensenkeisan<263000)and(self.Fuyo==0)): 
			Gensen = 6960   
		
		elif((260000<=Gensenkeisan)and(Gensenkeisan<263000)and(self.Fuyo==1)):
			Gensen = 5350 
		
		elif((260000<=Gensenkeisan)and(Gensenkeisan<263000)and(self.Fuyo==2)):
			Gensen = 3730
		
		elif((260000<=Gensenkeisan)and(Gensenkeisan<263000)and(self.Fuyo==3)):
			Gensen = 2110
		
		elif((260000<=Gensenkeisan)and(Gensenkeisan<263000)and(self.Fuyo==4)):
			Gensen = 500
		
		#87
		elif((263000<=Gensenkeisan)and(Gensenkeisan<266000)and(self.Fuyo==0)): 
			Gensen = 7070   
		
		elif((263000<=Gensenkeisan)and(Gensenkeisan<266000)and(self.Fuyo==1)):
			Gensen = 5450 
		
		elif((263000<=Gensenkeisan)and(Gensenkeisan<266000)and(self.Fuyo==2)):
			Gensen = 3840
		
		elif((263000<=Gensenkeisan)and(Gensenkeisan<266000)and(self.Fuyo==3)):
			Gensen = 2220
		
		elif((263000<=Gensenkeisan)and(Gensenkeisan<266000)and(self.Fuyo==4)):
			Gensen = 600
		
		#88
		elif((266000<=Gensenkeisan)and(Gensenkeisan<269000)and(self.Fuyo==0)): 
			Gensen = 7180   
		
		elif((266000<=Gensenkeisan)and(Gensenkeisan<269000)and(self.Fuyo==1)):
			Gensen = 5560 
		
		elif((266000<=Gensenkeisan)and(Gensenkeisan<269000)and(self.Fuyo==2)):
			Gensen = 3940
		
		elif((266000<=Gensenkeisan)and(Gensenkeisan<269000)and(self.Fuyo==3)):
			Gensen = 2330
		
		elif((266000<=Gensenkeisan)and(Gensenkeisan<269000)and(self.Fuyo==4)):
			Gensen = 710
		
		#89
		elif((269000<=Gensenkeisan)and(Gensenkeisan<272000)and(self.Fuyo==0)): 
			Gensen = 7280   
		
		elif((269000<=Gensenkeisan)and(Gensenkeisan<272000)and(self.Fuyo==1)):
			Gensen = 5670 
		
		elif((269000<=Gensenkeisan)and(Gensenkeisan<272000)and(self.Fuyo==2)):
			Gensen = 4050
		
		elif((269000<=Gensenkeisan)and(Gensenkeisan<272000)and(self.Fuyo==3)):
			Gensen = 2430
		
		elif((269000<=Gensenkeisan)and(Gensenkeisan<272000)and(self.Fuyo==4)):
			Gensen = 820
		
		#90
		elif((272000<=Gensenkeisan)and(Gensenkeisan<275000)and(self.Fuyo==0)): 
			Gensen = 7390   
		
		elif((272000<=Gensenkeisan)and(Gensenkeisan<275000)and(self.Fuyo==1)):
			Gensen = 5780 
		
		elif((272000<=Gensenkeisan)and(Gensenkeisan<275000)and(self.Fuyo==2)):
			Gensen = 4160
		
		elif((272000<=Gensenkeisan)and(Gensenkeisan<275000)and(self.Fuyo==3)):
			Gensen = 2540
		
		elif((272000<=Gensenkeisan)and(Gensenkeisan<275000)and(self.Fuyo==4)):
			Gensen = 930
		
		#91
		elif((275000<=Gensenkeisan)and(Gensenkeisan<278000)and(self.Fuyo==0)): 
			Gensen = 7490   
		
		elif((275000<=Gensenkeisan)and(Gensenkeisan<278000)and(self.Fuyo==1)):
			Gensen = 5880 
		
		elif((275000<=Gensenkeisan)and(Gensenkeisan<278000)and(self.Fuyo==2)):
			Gensen = 4270
		
		elif((275000<=Gensenkeisan)and(Gensenkeisan<278000)and(self.Fuyo==3)):
			Gensen = 2640
		
		elif((275000<=Gensenkeisan)and(Gensenkeisan<278000)and(self.Fuyo==4)):
			Gensen = 1030
		
		#92
		elif((278000<=Gensenkeisan)and(Gensenkeisan<281000)and(self.Fuyo==0)): 
			Gensen = 7610   
		
		elif((278000<=Gensenkeisan)and(Gensenkeisan<281000)and(self.Fuyo==1)):
			Gensen = 5990 
		
		elif((278000<=Gensenkeisan)and(Gensenkeisan<281000)and(self.Fuyo==2)):
			Gensen = 4370
		
		elif((278000<=Gensenkeisan)and(Gensenkeisan<281000)and(self.Fuyo==3)):
			Gensen = 2760
		
		elif((278000<=Gensenkeisan)and(Gensenkeisan<281000)and(self.Fuyo==4)):
			Gensen = 1140
		
		#93
		elif((281000<=Gensenkeisan)and(Gensenkeisan<284000)and(self.Fuyo==0)): 
			Gensen = 7710   
		
		elif((281000<=Gensenkeisan)and(Gensenkeisan<284000)and(self.Fuyo==1)):
			Gensen = 6100 
		
		elif((281000<=Gensenkeisan)and(Gensenkeisan<284000)and(self.Fuyo==2)):
			Gensen = 4480
		
		elif((281000<=Gensenkeisan)and(Gensenkeisan<284000)and(self.Fuyo==3)):
			Gensen = 2860
		
		elif((281000<=Gensenkeisan)and(Gensenkeisan<284000)and(self.Fuyo==4)):
			Gensen = 1250
		
		#94
		elif((284000<=Gensenkeisan)and(Gensenkeisan<287000)and(self.Fuyo==0)): 
			Gensen = 7820   
		
		elif((284000<=Gensenkeisan)and(Gensenkeisan<287000)and(self.Fuyo==1)):
			Gensen = 6210 
		
		elif((284000<=Gensenkeisan)and(Gensenkeisan<287000)and(self.Fuyo==2)):
			Gensen = 4580
		
		elif((284000<=Gensenkeisan)and(Gensenkeisan<287000)and(self.Fuyo==3)):
			Gensen = 2970
		
		elif((284000<=Gensenkeisan)and(Gensenkeisan<287000)and(self.Fuyo==4)):
			Gensen = 1360
		
		#95
		elif((287000<=Gensenkeisan)and(Gensenkeisan<290000)and(self.Fuyo==0)): 
			Gensen = 7920   
		
		elif((287000<=Gensenkeisan)and(Gensenkeisan<290000)and(self.Fuyo==1)):
			Gensen = 6310 
		
		elif((287000<=Gensenkeisan)and(Gensenkeisan<290000)and(self.Fuyo==2)):
			Gensen = 4700
		
		elif((287000<=Gensenkeisan)and(Gensenkeisan<290000)and(self.Fuyo==3)):
			Gensen = 3070
		
		elif((287000<=Gensenkeisan)and(Gensenkeisan<290000)and(self.Fuyo==4)):
			Gensen = 1460
		
		#96
		elif((290000<=Gensenkeisan)and(Gensenkeisan<293000)and(self.Fuyo==0)): 
			Gensen = 8040   
		
		elif((290000<=Gensenkeisan)and(Gensenkeisan<293000)and(self.Fuyo==1)):
			Gensen = 6420 
		
		elif((290000<=Gensenkeisan)and(Gensenkeisan<293000)and(self.Fuyo==2)):
			Gensen = 4800
		
		elif((290000<=Gensenkeisan)and(Gensenkeisan<293000)and(self.Fuyo==3)):
			Gensen = 3190
		
		elif((290000<=Gensenkeisan)and(Gensenkeisan<293000)and(self.Fuyo==4)):
			Gensen = 1570
		
		#97
		elif((293000<=Gensenkeisan)and(Gensenkeisan<296000)and(self.Fuyo==0)): 
			Gensen = 8140   
		
		elif((293000<=Gensenkeisan)and(Gensenkeisan<296000)and(self.Fuyo==1)):
			Gensen = 6520 
		
		elif((293000<=Gensenkeisan)and(Gensenkeisan<296000)and(self.Fuyo==2)):
			Gensen = 4910
		
		elif((293000<=Gensenkeisan)and(Gensenkeisan<296000)and(self.Fuyo==3)):
			Gensen = 3290
		
		elif((293000<=Gensenkeisan)and(Gensenkeisan<296000)and(self.Fuyo==4)):
			Gensen = 1670
		
		#98
		elif((296000<=Gensenkeisan)and(Gensenkeisan<299000)and(self.Fuyo==0)): 
			Gensen = 8250   
		
		elif((296000<=Gensenkeisan)and(Gensenkeisan<299000)and(self.Fuyo==1)):
			Gensen = 6640 
		
		elif((296000<=Gensenkeisan)and(Gensenkeisan<299000)and(self.Fuyo==2)):
			Gensen = 5010
		
		elif((296000<=Gensenkeisan)and(Gensenkeisan<299000)and(self.Fuyo==3)):
			Gensen = 3400
		
		elif((296000<=Gensenkeisan)and(Gensenkeisan<299000)and(self.Fuyo==4)):
			Gensen = 1790
		
		elif((296000<=Gensenkeisan)and(Gensenkeisan<299000)and(self.Fuyo==5)):
			Gensen = 160
		
		#99
		elif((299000<=Gensenkeisan)and(Gensenkeisan<302000)and(self.Fuyo==0)): 
			Gensen = 8420   
		
		elif((299000<=Gensenkeisan)and(Gensenkeisan<302000)and(self.Fuyo==1)):
			Gensen = 6740 
		
		elif((299000<=Gensenkeisan)and(Gensenkeisan<302000)and(self.Fuyo==2)):
			Gensen = 5130
		
		elif((299000<=Gensenkeisan)and(Gensenkeisan<302000)and(self.Fuyo==3)):
			Gensen = 3510
		
		elif((299000<=Gensenkeisan)and(Gensenkeisan<302000)and(self.Fuyo==4)):
			Gensen = 1890
		
		elif((299000<=Gensenkeisan)and(Gensenkeisan<302000)and(self.Fuyo==5)):
			Gensen = 280
		
		#100
		elif((302000<=Gensenkeisan)and(Gensenkeisan<305000)and(self.Fuyo==0)): 
			Gensen = 8670   
		
		elif((302000<=Gensenkeisan)and(Gensenkeisan<305000)and(self.Fuyo==1)):
			Gensen = 6860 
		
		elif((302000<=Gensenkeisan)and(Gensenkeisan<305000)and(self.Fuyo==2)):
			Gensen = 5250
		
		elif((302000<=Gensenkeisan)and(Gensenkeisan<305000)and(self.Fuyo==3)):
			Gensen = 3630
		
		elif((302000<=Gensenkeisan)and(Gensenkeisan<305000)and(self.Fuyo==4)):
			Gensen = 2010
		
		elif((302000<=Gensenkeisan)and(Gensenkeisan<305000)and(self.Fuyo==5)):
			Gensen = 400
		
		#101
		elif((305000<=Gensenkeisan)and(Gensenkeisan<308000)and(self.Fuyo==0)): 
			Gensen = 8910   
		
		elif((305000<=Gensenkeisan)and(Gensenkeisan<308000)and(self.Fuyo==1)):
			Gensen = 6980 
		
		elif((305000<=Gensenkeisan)and(Gensenkeisan<308000)and(self.Fuyo==2)):
			Gensen = 5370
		
		elif((305000<=Gensenkeisan)and(Gensenkeisan<308000)and(self.Fuyo==3)):
			Gensen = 3760
		
		elif((305000<=Gensenkeisan)and(Gensenkeisan<308000)and(self.Fuyo==4)):
			Gensen = 2130
		
		elif((305000<=Gensenkeisan)and(Gensenkeisan<308000)and(self.Fuyo==5)):
			Gensen = 520
		
		#102
		elif((308000<=Gensenkeisan)and(Gensenkeisan<311000)and(self.Fuyo==0)): 
			Gensen = 9160   
		
		elif((308000<=Gensenkeisan)and(Gensenkeisan<311000)and(self.Fuyo==1)):
			Gensen = 7110 
		
		elif((308000<=Gensenkeisan)and(Gensenkeisan<311000)and(self.Fuyo==2)):
			Gensen = 5490
		
		elif((308000<=Gensenkeisan)and(Gensenkeisan<311000)and(self.Fuyo==3)):
			Gensen = 3880
		
		elif((308000<=Gensenkeisan)and(Gensenkeisan<311000)and(self.Fuyo==4)):
			Gensen = 2260
		
		elif((308000<=Gensenkeisan)and(Gensenkeisan<311000)and(self.Fuyo==5)):
			Gensen = 640
		
		#103
		elif((311000<=Gensenkeisan)and(Gensenkeisan<314000)and(self.Fuyo==0)): 
			Gensen = 9400   
		
		elif((311000<=Gensenkeisan)and(Gensenkeisan<314000)and(self.Fuyo==1)):
			Gensen = 7230 
		
		elif((311000<=Gensenkeisan)and(Gensenkeisan<314000)and(self.Fuyo==2)):
			Gensen = 5620
		
		elif((311000<=Gensenkeisan)and(Gensenkeisan<314000)and(self.Fuyo==3)):
			Gensen = 4000
		
		elif((311000<=Gensenkeisan)and(Gensenkeisan<314000)and(self.Fuyo==4)):
			Gensen = 2380
		
		elif((311000<=Gensenkeisan)and(Gensenkeisan<314000)and(self.Fuyo==5)):
			Gensen = 770
		
		#104
		elif((314000<=Gensenkeisan)and(Gensenkeisan<317000)and(self.Fuyo==0)): 
			Gensen = 9650   
		
		elif((314000<=Gensenkeisan)and(Gensenkeisan<317000)and(self.Fuyo==1)):
			Gensen = 7350 
		
		elif((314000<=Gensenkeisan)and(Gensenkeisan<317000)and(self.Fuyo==2)):
			Gensen = 5740
		
		elif((314000<=Gensenkeisan)and(Gensenkeisan<317000)and(self.Fuyo==3)):
			Gensen = 4120
		
		elif((314000<=Gensenkeisan)and(Gensenkeisan<317000)and(self.Fuyo==4)):
			Gensen = 2500
		
		elif((314000<=Gensenkeisan)and(Gensenkeisan<317000)and(self.Fuyo==5)):
			Gensen = 890
		
		#105
		elif((317000<=Gensenkeisan)and(Gensenkeisan<320000)and(self.Fuyo==0)): 
			Gensen = 9890   
		
		elif((317000<=Gensenkeisan)and(Gensenkeisan<320000)and(self.Fuyo==1)):
			Gensen = 7470 
		
		elif((317000<=Gensenkeisan)and(Gensenkeisan<320000)and(self.Fuyo==2)):
			Gensen = 5860
		
		elif((317000<=Gensenkeisan)and(Gensenkeisan<320000)and(self.Fuyo==3)):
			Gensen = 4250
		
		elif((317000<=Gensenkeisan)and(Gensenkeisan<320000)and(self.Fuyo==4)):
			Gensen = 2620
		
		elif((317000<=Gensenkeisan)and(Gensenkeisan<320000)and(self.Fuyo==5)):
			Gensen = 1010
		
		#106
		elif((320000<=Gensenkeisan)and(Gensenkeisan<323000)and(self.Fuyo==0)): 
			Gensen = 10140   
		
		elif((320000<=Gensenkeisan)and(Gensenkeisan<323000)and(self.Fuyo==1)):
			Gensen = 7600 
		
		elif((320000<=Gensenkeisan)and(Gensenkeisan<323000)and(self.Fuyo==2)):
			Gensen = 5980
		
		elif((320000<=Gensenkeisan)and(Gensenkeisan<323000)and(self.Fuyo==3)):
			Gensen = 4370
		
		elif((320000<=Gensenkeisan)and(Gensenkeisan<323000)and(self.Fuyo==4)):
			Gensen = 2750
		
		elif((320000<=Gensenkeisan)and(Gensenkeisan<323000)and(self.Fuyo==5)):
			Gensen = 1130
		
		#107
		elif((323000<=Gensenkeisan)and(Gensenkeisan<326000)and(self.Fuyo==0)): 
			Gensen = 10380   
		
		elif((323000<=Gensenkeisan)and(Gensenkeisan<326000)and(self.Fuyo==1)):
			Gensen = 7720 
		
		elif((323000<=Gensenkeisan)and(Gensenkeisan<326000)and(self.Fuyo==2)):
			Gensen = 6110
		
		elif((323000<=Gensenkeisan)and(Gensenkeisan<326000)and(self.Fuyo==3)):
			Gensen = 4490
		
		elif((323000<=Gensenkeisan)and(Gensenkeisan<326000)and(self.Fuyo==4)):
			Gensen = 2870
		
		elif((323000<=Gensenkeisan)and(Gensenkeisan<326000)and(self.Fuyo==5)):
			Gensen = 1260
		
		#108
		elif((326000<=Gensenkeisan)and(Gensenkeisan<329000)and(self.Fuyo==0)): 
			Gensen = 10630   
		
		elif((326000<=Gensenkeisan)and(Gensenkeisan<329000)and(self.Fuyo==1)):
			Gensen = 7840 
		
		elif((326000<=Gensenkeisan)and(Gensenkeisan<329000)and(self.Fuyo==2)):
			Gensen = 6230
		
		elif((326000<=Gensenkeisan)and(Gensenkeisan<329000)and(self.Fuyo==3)):
			Gensen = 4610
		
		elif((326000<=Gensenkeisan)and(Gensenkeisan<329000)and(self.Fuyo==4)):
			Gensen = 2990
		
		elif((326000<=Gensenkeisan)and(Gensenkeisan<329000)and(self.Fuyo==5)):
			Gensen = 1380
		
		#109
		elif((329000<=Gensenkeisan)and(Gensenkeisan<332000)and(self.Fuyo==0)): 
			Gensen = 10870   
		
		elif((329000<=Gensenkeisan)and(Gensenkeisan<332000)and(self.Fuyo==1)):
			Gensen = 7960 
		
		elif((329000<=Gensenkeisan)and(Gensenkeisan<332000)and(self.Fuyo==2)):
			Gensen = 6350
		
		elif((329000<=Gensenkeisan)and(Gensenkeisan<332000)and(self.Fuyo==3)):
			Gensen = 4740
		
		elif((329000<=Gensenkeisan)and(Gensenkeisan<332000)and(self.Fuyo==4)):
			Gensen = 3110
		
		elif((329000<=Gensenkeisan)and(Gensenkeisan<332000)and(self.Fuyo==5)):
			Gensen = 1500
		
		#110
		elif((332000<=Gensenkeisan)and(Gensenkeisan<335000)and(self.Fuyo==0)): 
			Gensen = 11120   
		
		elif((332000<=Gensenkeisan)and(Gensenkeisan<335000)and(self.Fuyo==1)):
			Gensen = 8090 
		
		elif((332000<=Gensenkeisan)and(Gensenkeisan<335000)and(self.Fuyo==2)):
			Gensen = 6470
		
		elif((332000<=Gensenkeisan)and(Gensenkeisan<335000)and(self.Fuyo==3)):
			Gensen = 4860
		
		elif((332000<=Gensenkeisan)and(Gensenkeisan<335000)and(self.Fuyo==4)):
			Gensen = 3240
		
		elif((332000<=Gensenkeisan)and(Gensenkeisan<335000)and(self.Fuyo==5)):
			Gensen = 1620
		
		#111
		elif((335000<=Gensenkeisan)and(Gensenkeisan<338000)and(self.Fuyo==0)): 
			Gensen = 11360   
		
		elif((335000<=Gensenkeisan)and(Gensenkeisan<338000)and(self.Fuyo==1)):
			Gensen = 8210 
		
		elif((335000<=Gensenkeisan)and(Gensenkeisan<338000)and(self.Fuyo==2)):
			Gensen = 6600
		
		elif((335000<=Gensenkeisan)and(Gensenkeisan<338000)and(self.Fuyo==3)):
			Gensen = 4980
		
		elif((335000<=Gensenkeisan)and(Gensenkeisan<338000)and(self.Fuyo==4)):
			Gensen = 3360
		
		elif((335000<=Gensenkeisan)and(Gensenkeisan<338000)and(self.Fuyo==5)):
			Gensen = 1750
		
		elif((335000<=Gensenkeisan)and(Gensenkeisan<338000)and(self.Fuyo==6)):
			Gensen = 130
		
		#112
		elif((338000<=Gensenkeisan)and(Gensenkeisan<341000)and(self.Fuyo==0)): 
			Gensen = 11610   
		
		elif((338000<=Gensenkeisan)and(Gensenkeisan<341000)and(self.Fuyo==1)):
			Gensen = 8370 
		
		elif((338000<=Gensenkeisan)and(Gensenkeisan<341000)and(self.Fuyo==2)):
			Gensen = 6720
		
		elif((338000<=Gensenkeisan)and(Gensenkeisan<341000)and(self.Fuyo==3)):
			Gensen = 5110
		
		elif((338000<=Gensenkeisan)and(Gensenkeisan<341000)and(self.Fuyo==4)):
			Gensen = 3480
		
		elif((338000<=Gensenkeisan)and(Gensenkeisan<341000)and(self.Fuyo==5)):
			Gensen = 1870
		
		elif((338000<=Gensenkeisan)and(Gensenkeisan<341000)and(self.Fuyo==6)):
			Gensen = 260
		
		#113
		elif((341000<=Gensenkeisan)and(Gensenkeisan<344000)and(self.Fuyo==0)): 
			Gensen = 11850   
		
		elif((341000<=Gensenkeisan)and(Gensenkeisan<344000)and(self.Fuyo==1)):
			Gensen = 8620 
		
		elif((341000<=Gensenkeisan)and(Gensenkeisan<344000)and(self.Fuyo==2)):
			Gensen = 6840
		
		elif((341000<=Gensenkeisan)and(Gensenkeisan<344000)and(self.Fuyo==3)):
			Gensen = 5230
		
		elif((341000<=Gensenkeisan)and(Gensenkeisan<344000)and(self.Fuyo==4)):
			Gensen = 3600
		
		elif((341000<=Gensenkeisan)and(Gensenkeisan<344000)and(self.Fuyo==5)):
			Gensen = 1990
		
		elif((341000<=Gensenkeisan)and(Gensenkeisan<344000)and(self.Fuyo==6)):
			Gensen = 380
		
		#114
		elif((344000<=Gensenkeisan)and(Gensenkeisan<347000)and(self.Fuyo==0)): 
			Gensen = 12100   
		
		elif((344000<=Gensenkeisan)and(Gensenkeisan<347000)and(self.Fuyo==1)):
			Gensen = 8860 
		
		elif((344000<=Gensenkeisan)and(Gensenkeisan<347000)and(self.Fuyo==2)):
			Gensen = 6960
		
		elif((344000<=Gensenkeisan)and(Gensenkeisan<347000)and(self.Fuyo==3)):
			Gensen = 5350
		
		elif((344000<=Gensenkeisan)and(Gensenkeisan<347000)and(self.Fuyo==4)):
			Gensen = 3730
		
		elif((344000<=Gensenkeisan)and(Gensenkeisan<347000)and(self.Fuyo==5)):
			Gensen = 2110
		
		elif((344000<=Gensenkeisan)and(Gensenkeisan<347000)and(self.Fuyo==6)):
			Gensen = 500
		
		#115
		elif((347000<=Gensenkeisan)and(Gensenkeisan<350000)and(self.Fuyo==0)): 
			Gensen = 12340   
		
		elif((347000<=Gensenkeisan)and(Gensenkeisan<350000)and(self.Fuyo==1)):
			Gensen = 9110 
		
		elif((347000<=Gensenkeisan)and(Gensenkeisan<350000)and(self.Fuyo==2)):
			Gensen = 7090
		
		elif((347000<=Gensenkeisan)and(Gensenkeisan<350000)and(self.Fuyo==3)):
			Gensen = 5470
		
		elif((347000<=Gensenkeisan)and(Gensenkeisan<350000)and(self.Fuyo==4)):
			Gensen = 3850
		
		elif((347000<=Gensenkeisan)and(Gensenkeisan<350000)and(self.Fuyo==5)):
			Gensen = 2240
		
		elif((347000<=Gensenkeisan)and(Gensenkeisan<350000)and(self.Fuyo==6)):
			Gensen = 620
		
		#116
		elif((350000<=Gensenkeisan)and(Gensenkeisan<353000)and(self.Fuyo==0)): 
			Gensen = 12590   
		
		elif((350000<=Gensenkeisan)and(Gensenkeisan<353000)and(self.Fuyo==1)):
			Gensen = 9350 
		
		elif((350000<=Gensenkeisan)and(Gensenkeisan<353000)and(self.Fuyo==2)):
			Gensen = 7210
		
		elif((350000<=Gensenkeisan)and(Gensenkeisan<353000)and(self.Fuyo==3)):
			Gensen = 5600
		
		elif((350000<=Gensenkeisan)and(Gensenkeisan<353000)and(self.Fuyo==4)):
			Gensen = 3970
		
		elif((350000<=Gensenkeisan)and(Gensenkeisan<353000)and(self.Fuyo==5)):
			Gensen = 2360
		
		elif((350000<=Gensenkeisan)and(Gensenkeisan<353000)and(self.Fuyo==6)):
			Gensen = 750
		
		#117
		elif((353000<=Gensenkeisan)and(Gensenkeisan<356000)and(self.Fuyo==0)): 
			Gensen = 12830   
		
		elif((353000<=Gensenkeisan)and(Gensenkeisan<356000)and(self.Fuyo==1)):
			Gensen = 9600 
		
		elif((353000<=Gensenkeisan)and(Gensenkeisan<356000)and(self.Fuyo==2)):
			Gensen = 7330
		
		elif((353000<=Gensenkeisan)and(Gensenkeisan<356000)and(self.Fuyo==3)):
			Gensen = 5720
		
		elif((353000<=Gensenkeisan)and(Gensenkeisan<356000)and(self.Fuyo==4)):
			Gensen = 4090
		
		elif((353000<=Gensenkeisan)and(Gensenkeisan<356000)and(self.Fuyo==5)):
			Gensen = 2480
		
		elif((353000<=Gensenkeisan)and(Gensenkeisan<356000)and(self.Fuyo==6)):
			Gensen = 870
		
		#118
		elif((356000<=Gensenkeisan)and(Gensenkeisan<359000)and(self.Fuyo==0)): 
			Gensen = 13080   
		
		elif((356000<=Gensenkeisan)and(Gensenkeisan<359000)and(self.Fuyo==1)):
			Gensen = 9840 
		
		elif((356000<=Gensenkeisan)and(Gensenkeisan<359000)and(self.Fuyo==2)):
			Gensen = 7450
		
		elif((356000<=Gensenkeisan)and(Gensenkeisan<359000)and(self.Fuyo==3)):
			Gensen = 5840
		
		elif((356000<=Gensenkeisan)and(Gensenkeisan<359000)and(self.Fuyo==4)):
			Gensen = 4220
		
		elif((356000<=Gensenkeisan)and(Gensenkeisan<359000)and(self.Fuyo==5)):
			Gensen = 2600
		
		elif((356000<=Gensenkeisan)and(Gensenkeisan<359000)and(self.Fuyo==6)):
			Gensen = 990
		
		#119
		elif((359000<=Gensenkeisan)and(Gensenkeisan<362000)and(self.Fuyo==0)): 
			Gensen = 13320   
		
		elif((359000<=Gensenkeisan)and(Gensenkeisan<362000)and(self.Fuyo==1)):
			Gensen = 10090 
		
		elif((359000<=Gensenkeisan)and(Gensenkeisan<362000)and(self.Fuyo==2)):
			Gensen = 7580
		
		elif((359000<=Gensenkeisan)and(Gensenkeisan<362000)and(self.Fuyo==3)):
			Gensen = 5960
		
		elif((359000<=Gensenkeisan)and(Gensenkeisan<362000)and(self.Fuyo==4)):
			Gensen = 4340
		
		elif((359000<=Gensenkeisan)and(Gensenkeisan<362000)and(self.Fuyo==5)):
			Gensen = 2730
		
		elif((359000<=Gensenkeisan)and(Gensenkeisan<362000)and(self.Fuyo==6)):
			Gensen = 1110
		
		#120
		elif((362000<=Gensenkeisan)and(Gensenkeisan<365000)and(self.Fuyo==0)): 
			Gensen = 13570   
		
		elif((362000<=Gensenkeisan)and(Gensenkeisan<365000)and(self.Fuyo==1)):
			Gensen = 10330 
		
		elif((362000<=Gensenkeisan)and(Gensenkeisan<365000)and(self.Fuyo==2)):
			Gensen = 7700
		
		elif((362000<=Gensenkeisan)and(Gensenkeisan<365000)and(self.Fuyo==3)):
			Gensen = 6090
		
		elif((362000<=Gensenkeisan)and(Gensenkeisan<365000)and(self.Fuyo==4)):
			Gensen = 4460
		
		elif((362000<=Gensenkeisan)and(Gensenkeisan<365000)and(self.Fuyo==5)):
			Gensen = 2850
		
		elif((362000<=Gensenkeisan)and(Gensenkeisan<365000)and(self.Fuyo==6)):
			Gensen = 1240
		
		#121
		elif((365000<=Gensenkeisan)and(Gensenkeisan<368000)and(self.Fuyo==0)): 
			Gensen = 13810   
		
		elif((365000<=Gensenkeisan)and(Gensenkeisan<368000)and(self.Fuyo==1)):
			Gensen = 10580 
		
		elif((365000<=Gensenkeisan)and(Gensenkeisan<368000)and(self.Fuyo==2)):
			Gensen = 7820
		
		elif((365000<=Gensenkeisan)and(Gensenkeisan<368000)and(self.Fuyo==3)):
			Gensen = 6210
		
		elif((365000<=Gensenkeisan)and(Gensenkeisan<368000)and(self.Fuyo==4)):
			Gensen = 4580
		
		elif((365000<=Gensenkeisan)and(Gensenkeisan<368000)and(self.Fuyo==5)):
			Gensen = 2970
		
		elif((365000<=Gensenkeisan)and(Gensenkeisan<368000)and(self.Fuyo==6)):
			Gensen = 1360
		
		#122
		elif((368000<=Gensenkeisan)and(Gensenkeisan<371000)and(self.Fuyo==0)): 
			Gensen = 14060   
		
		elif((368000<=Gensenkeisan)and(Gensenkeisan<371000)and(self.Fuyo==1)):
			Gensen = 10820 
		
		elif((368000<=Gensenkeisan)and(Gensenkeisan<371000)and(self.Fuyo==2)):
			Gensen = 7940
		
		elif((368000<=Gensenkeisan)and(Gensenkeisan<371000)and(self.Fuyo==3)):
			Gensen = 6330
		
		elif((368000<=Gensenkeisan)and(Gensenkeisan<371000)and(self.Fuyo==4)):
			Gensen = 4710
		
		elif((368000<=Gensenkeisan)and(Gensenkeisan<371000)and(self.Fuyo==5)):
			Gensen = 3090
		
		elif((368000<=Gensenkeisan)and(Gensenkeisan<371000)and(self.Fuyo==6)):
			Gensen = 1480
		
		#123
		elif((371000<=Gensenkeisan)and(Gensenkeisan<374000)and(self.Fuyo==0)): 
			Gensen = 14300   
		
		elif((371000<=Gensenkeisan)and(Gensenkeisan<374000)and(self.Fuyo==1)):
			Gensen = 11070 
		
		elif((371000<=Gensenkeisan)and(Gensenkeisan<374000)and(self.Fuyo==2)):
			Gensen = 8070
		
		elif((371000<=Gensenkeisan)and(Gensenkeisan<374000)and(self.Fuyo==3)):
			Gensen = 6450
		
		elif((371000<=Gensenkeisan)and(Gensenkeisan<374000)and(self.Fuyo==4)):
			Gensen = 4830
		
		elif((371000<=Gensenkeisan)and(Gensenkeisan<374000)and(self.Fuyo==5)):
			Gensen = 3220
		
		elif((371000<=Gensenkeisan)and(Gensenkeisan<374000)and(self.Fuyo==6)):
			Gensen = 1600
		
		#124
		elif((374000<=Gensenkeisan)and(Gensenkeisan<377000)and(self.Fuyo==0)): 
			Gensen = 14550   
		
		elif((374000<=Gensenkeisan)and(Gensenkeisan<377000)and(self.Fuyo==1)):
			Gensen = 11310 
		
		elif((374000<=Gensenkeisan)and(Gensenkeisan<377000)and(self.Fuyo==2)):
			Gensen = 8190
		
		elif((374000<=Gensenkeisan)and(Gensenkeisan<377000)and(self.Fuyo==3)):
			Gensen = 6580
		
		elif((374000<=Gensenkeisan)and(Gensenkeisan<377000)and(self.Fuyo==4)):
			Gensen = 4950
		
		elif((374000<=Gensenkeisan)and(Gensenkeisan<377000)and(self.Fuyo==5)):
			Gensen = 3340
		
		elif((374000<=Gensenkeisan)and(Gensenkeisan<377000)and(self.Fuyo==6)):
			Gensen = 1730
		
		elif((374000<=Gensenkeisan)and(Gensenkeisan<377000)and(self.Fuyo==7)):
			Gensen = 100
		
		#125
		elif((377000<=Gensenkeisan)and(Gensenkeisan<380000)and(self.Fuyo==0)): 
			Gensen = 14790   
		
		elif((377000<=Gensenkeisan)and(Gensenkeisan<380000)and(self.Fuyo==1)):
			Gensen = 11560 
		
		elif((377000<=Gensenkeisan)and(Gensenkeisan<380000)and(self.Fuyo==2)):
			Gensen = 8320
		
		elif((377000<=Gensenkeisan)and(Gensenkeisan<380000)and(self.Fuyo==3)):
			Gensen = 6700
		
		elif((377000<=Gensenkeisan)and(Gensenkeisan<380000)and(self.Fuyo==4)):
			Gensen = 5070
		
		elif((377000<=Gensenkeisan)and(Gensenkeisan<380000)and(self.Fuyo==5)):
			Gensen = 3460
		
		elif((377000<=Gensenkeisan)and(Gensenkeisan<380000)and(self.Fuyo==6)):
			Gensen = 1850
		
		elif((377000<=Gensenkeisan)and(Gensenkeisan<380000)and(self.Fuyo==7)):
			Gensen = 220
		
		#126
		elif((380000<=Gensenkeisan)and(Gensenkeisan<383000)and(self.Fuyo==0)): 
			Gensen = 15040   
		
		elif((380000<=Gensenkeisan)and(Gensenkeisan<383000)and(self.Fuyo==1)):
			Gensen = 11800 
		
		elif((380000<=Gensenkeisan)and(Gensenkeisan<383000)and(self.Fuyo==2)):
			Gensen = 8570
		
		elif((380000<=Gensenkeisan)and(Gensenkeisan<383000)and(self.Fuyo==3)):
			Gensen = 6820
		
		elif((380000<=Gensenkeisan)and(Gensenkeisan<383000)and(self.Fuyo==4)):
			Gensen = 5200
		
		elif((380000<=Gensenkeisan)and(Gensenkeisan<383000)and(self.Fuyo==5)):
			Gensen = 3580
		
		elif((380000<=Gensenkeisan)and(Gensenkeisan<383000)and(self.Fuyo==6)):
			Gensen = 1970
		
		elif((380000<=Gensenkeisan)and(Gensenkeisan<383000)and(self.Fuyo==7)):
			Gensen = 350
		
		#127
		elif((383000<=Gensenkeisan)and(Gensenkeisan<386000)and(self.Fuyo==0)): 
			Gensen = 15280   
		
		elif((383000<=Gensenkeisan)and(Gensenkeisan<386000)and(self.Fuyo==1)):
			Gensen = 12050 
		
		elif((383000<=Gensenkeisan)and(Gensenkeisan<386000)and(self.Fuyo==2)):
			Gensen = 8810
		
		elif((383000<=Gensenkeisan)and(Gensenkeisan<386000)and(self.Fuyo==3)):
			Gensen = 6940
		
		elif((383000<=Gensenkeisan)and(Gensenkeisan<386000)and(self.Fuyo==4)):
			Gensen = 5320
		
		elif((383000<=Gensenkeisan)and(Gensenkeisan<386000)and(self.Fuyo==5)):
			Gensen = 3710
		
		elif((383000<=Gensenkeisan)and(Gensenkeisan<386000)and(self.Fuyo==6)):
			Gensen = 2090
		
		elif((383000<=Gensenkeisan)and(Gensenkeisan<386000)and(self.Fuyo==7)):
			Gensen = 470
		
		#128
		elif((386000<=Gensenkeisan)and(Gensenkeisan<389000)and(self.Fuyo==0)): 
			Gensen = 15530   
		
		elif((386000<=Gensenkeisan)and(Gensenkeisan<389000)and(self.Fuyo==1)):
			Gensen = 12290 
		
		elif((386000<=Gensenkeisan)and(Gensenkeisan<389000)and(self.Fuyo==2)):
			Gensen = 9060
		
		elif((386000<=Gensenkeisan)and(Gensenkeisan<389000)and(self.Fuyo==3)):
			Gensen = 7070
		
		elif((386000<=Gensenkeisan)and(Gensenkeisan<389000)and(self.Fuyo==4)):
			Gensen = 5440
		
		elif((386000<=Gensenkeisan)and(Gensenkeisan<389000)and(self.Fuyo==5)):
			Gensen = 3830
		
		elif((386000<=Gensenkeisan)and(Gensenkeisan<389000)and(self.Fuyo==6)):
			Gensen = 2220
		
		elif((386000<=Gensenkeisan)and(Gensenkeisan<389000)and(self.Fuyo==7)):
			Gensen = 590
		
		#129
		elif((389000<=Gensenkeisan)and(Gensenkeisan<392000)and(self.Fuyo==0)): 
			Gensen = 15770   
		
		elif((389000<=Gensenkeisan)and(Gensenkeisan<392000)and(self.Fuyo==1)):
			Gensen = 12540 
		
		elif((389000<=Gensenkeisan)and(Gensenkeisan<392000)and(self.Fuyo==2)):
			Gensen = 9300
		
		elif((389000<=Gensenkeisan)and(Gensenkeisan<392000)and(self.Fuyo==3)):
			Gensen = 7190
		
		elif((389000<=Gensenkeisan)and(Gensenkeisan<392000)and(self.Fuyo==4)):
			Gensen = 5560
		
		elif((389000<=Gensenkeisan)and(Gensenkeisan<392000)and(self.Fuyo==5)):
			Gensen = 3950
		
		elif((389000<=Gensenkeisan)and(Gensenkeisan<392000)and(self.Fuyo==6)):
			Gensen = 2340
		
		elif((389000<=Gensenkeisan)and(Gensenkeisan<392000)and(self.Fuyo==7)):
			Gensen = 710
		
		#130
		elif((392000<=Gensenkeisan)and(Gensenkeisan<395000)and(self.Fuyo==0)): 
			Gensen = 16020   
		
		elif((392000<=Gensenkeisan)and(Gensenkeisan<395000)and(self.Fuyo==1)):
			Gensen = 12780 
		
		elif((392000<=Gensenkeisan)and(Gensenkeisan<395000)and(self.Fuyo==2)):
			Gensen = 9550
		
		elif((392000<=Gensenkeisan)and(Gensenkeisan<395000)and(self.Fuyo==3)):
			Gensen = 7310
		
		elif((392000<=Gensenkeisan)and(Gensenkeisan<395000)and(self.Fuyo==4)):
			Gensen = 5690
		
		elif((392000<=Gensenkeisan)and(Gensenkeisan<395000)and(self.Fuyo==5)):
			Gensen = 4070
		
		elif((392000<=Gensenkeisan)and(Gensenkeisan<395000)and(self.Fuyo==6)):
			Gensen = 2460
		
		elif((392000<=Gensenkeisan)and(Gensenkeisan<395000)and(self.Fuyo==7)):
			Gensen = 840
		
		#131
		elif((395000<=Gensenkeisan)and(Gensenkeisan<398000)and(self.Fuyo==0)): 
			Gensen = 16260   
		
		elif((395000<=Gensenkeisan)and(Gensenkeisan<398000)and(self.Fuyo==1)):
			Gensen = 13030 
		
		elif((395000<=Gensenkeisan)and(Gensenkeisan<398000)and(self.Fuyo==2)):
			Gensen = 9790
		
		elif((395000<=Gensenkeisan)and(Gensenkeisan<398000)and(self.Fuyo==3)):
			Gensen = 7430
		
		elif((395000<=Gensenkeisan)and(Gensenkeisan<398000)and(self.Fuyo==4)):
			Gensen = 5810
		
		elif((395000<=Gensenkeisan)and(Gensenkeisan<398000)and(self.Fuyo==5)):
			Gensen = 4200
		
		elif((395000<=Gensenkeisan)and(Gensenkeisan<398000)and(self.Fuyo==6)):
			Gensen = 2580
		
		elif((395000<=Gensenkeisan)and(Gensenkeisan<398000)and(self.Fuyo==7)):
			Gensen = 960
		
		#132
		elif((398000<=Gensenkeisan)and(Gensenkeisan<401000)and(self.Fuyo==0)): 
			Gensen = 16510   
		
		elif((398000<=Gensenkeisan)and(Gensenkeisan<401000)and(self.Fuyo==1)):
			Gensen = 13270 
		
		elif((398000<=Gensenkeisan)and(Gensenkeisan<401000)and(self.Fuyo==2)):
			Gensen = 10040
		
		elif((398000<=Gensenkeisan)and(Gensenkeisan<401000)and(self.Fuyo==3)):
			Gensen = 7560
		
		elif((398000<=Gensenkeisan)and(Gensenkeisan<401000)and(self.Fuyo==4)):
			Gensen = 5930
		
		elif((398000<=Gensenkeisan)and(Gensenkeisan<401000)and(self.Fuyo==5)):
			Gensen = 4320
		
		elif((398000<=Gensenkeisan)and(Gensenkeisan<401000)and(self.Fuyo==6)):
			Gensen = 2710
		
		elif((398000<=Gensenkeisan)and(Gensenkeisan<401000)and(self.Fuyo==7)):
			Gensen = 1080
		
		#133
		elif((401000<=Gensenkeisan)and(Gensenkeisan<404000)and(self.Fuyo==0)): 
			Gensen = 16750   
		
		elif((401000<=Gensenkeisan)and(Gensenkeisan<404000)and(self.Fuyo==1)):
			Gensen = 13520 
		
		elif((401000<=Gensenkeisan)and(Gensenkeisan<404000)and(self.Fuyo==2)):
			Gensen = 10280
		
		elif((401000<=Gensenkeisan)and(Gensenkeisan<404000)and(self.Fuyo==3)):
			Gensen = 7680
		
		elif((401000<=Gensenkeisan)and(Gensenkeisan<404000)and(self.Fuyo==4)):
			Gensen = 6050
		
		elif((401000<=Gensenkeisan)and(Gensenkeisan<404000)and(self.Fuyo==5)):
			Gensen = 4440
		
		elif((401000<=Gensenkeisan)and(Gensenkeisan<404000)and(self.Fuyo==6)):
			Gensen = 2830
		
		elif((401000<=Gensenkeisan)and(Gensenkeisan<404000)and(self.Fuyo==7)):
			Gensen = 1200
		
		#134
		elif((404000<=Gensenkeisan)and(Gensenkeisan<407000)and(self.Fuyo==0)): 
			Gensen = 17000   
		
		elif((404000<=Gensenkeisan)and(Gensenkeisan<407000)and(self.Fuyo==1)):
			Gensen = 13760 
		
		elif((404000<=Gensenkeisan)and(Gensenkeisan<407000)and(self.Fuyo==2)):
			Gensen = 10530
		
		elif((404000<=Gensenkeisan)and(Gensenkeisan<407000)and(self.Fuyo==3)):
			Gensen = 7800
		
		elif((404000<=Gensenkeisan)and(Gensenkeisan<407000)and(self.Fuyo==4)):
			Gensen = 6180
		
		elif((404000<=Gensenkeisan)and(Gensenkeisan<407000)and(self.Fuyo==5)):
			Gensen = 4560
		
		elif((404000<=Gensenkeisan)and(Gensenkeisan<407000)and(self.Fuyo==6)):
			Gensen = 2950
		
		elif((404000<=Gensenkeisan)and(Gensenkeisan<407000)and(self.Fuyo==7)):
			Gensen = 1330
		
		#135
		elif((407000<=Gensenkeisan)and(Gensenkeisan<410000)and(self.Fuyo==0)): 
			Gensen = 17240   
		
		elif((407000<=Gensenkeisan)and(Gensenkeisan<410000)and(self.Fuyo==1)):
			Gensen = 14010 
		
		elif((407000<=Gensenkeisan)and(Gensenkeisan<410000)and(self.Fuyo==2)):
			Gensen = 10770
		
		elif((407000<=Gensenkeisan)and(Gensenkeisan<410000)and(self.Fuyo==3)):
			Gensen = 7920
		
		elif((407000<=Gensenkeisan)and(Gensenkeisan<410000)and(self.Fuyo==4)):
			Gensen = 6300
		
		elif((407000<=Gensenkeisan)and(Gensenkeisan<410000)and(self.Fuyo==5)):
			Gensen = 4690
		
		elif((407000<=Gensenkeisan)and(Gensenkeisan<410000)and(self.Fuyo==6)):
			Gensen = 3070
		
		elif((407000<=Gensenkeisan)and(Gensenkeisan<410000)and(self.Fuyo==7)):
			Gensen = 1450
		
		#136
		elif((410000<=Gensenkeisan)and(Gensenkeisan<413000)and(self.Fuyo==0)): 
			Gensen = 17490   
		
		elif((410000<=Gensenkeisan)and(Gensenkeisan<413000)and(self.Fuyo==1)):
			Gensen = 14250 
		
		elif((410000<=Gensenkeisan)and(Gensenkeisan<413000)and(self.Fuyo==2)):
			Gensen = 11020
		
		elif((410000<=Gensenkeisan)and(Gensenkeisan<413000)and(self.Fuyo==3)):
			Gensen = 8050
		
		elif((410000<=Gensenkeisan)and(Gensenkeisan<413000)and(self.Fuyo==4)):
			Gensen = 6420
		
		elif((410000<=Gensenkeisan)and(Gensenkeisan<413000)and(self.Fuyo==5)):
			Gensen = 4810
		
		elif((410000<=Gensenkeisan)and(Gensenkeisan<413000)and(self.Fuyo==6)):
			Gensen = 3200
		
		elif((410000<=Gensenkeisan)and(Gensenkeisan<413000)and(self.Fuyo==7)):
			Gensen = 1570
		
		#137
		elif((413000<=Gensenkeisan)and(Gensenkeisan<416000)and(self.Fuyo==0)): 
			Gensen = 17730   
		
		elif((413000<=Gensenkeisan)and(Gensenkeisan<416000)and(self.Fuyo==1)):
			Gensen = 14500 
		
		elif((413000<=Gensenkeisan)and(Gensenkeisan<416000)and(self.Fuyo==2)):
			Gensen = 11260
		
		elif((413000<=Gensenkeisan)and(Gensenkeisan<416000)and(self.Fuyo==3)):
			Gensen = 8170
		
		elif((413000<=Gensenkeisan)and(Gensenkeisan<416000)and(self.Fuyo==4)):
			Gensen = 6540
		
		elif((413000<=Gensenkeisan)and(Gensenkeisan<416000)and(self.Fuyo==5)):
			Gensen = 4930
		
		elif((413000<=Gensenkeisan)and(Gensenkeisan<416000)and(self.Fuyo==6)):
			Gensen = 3320
		
		elif((413000<=Gensenkeisan)and(Gensenkeisan<416000)and(self.Fuyo==7)):
			Gensen = 1690
		
		#138
		elif((416000<=Gensenkeisan)and(Gensenkeisan<419000)and(self.Fuyo==0)): 
			Gensen = 17980   
		
		elif((416000<=Gensenkeisan)and(Gensenkeisan<419000)and(self.Fuyo==1)):
			Gensen = 14740 
		
		elif((416000<=Gensenkeisan)and(Gensenkeisan<419000)and(self.Fuyo==2)):
			Gensen = 11510
		
		elif((416000<=Gensenkeisan)and(Gensenkeisan<419000)and(self.Fuyo==3)):
			Gensen = 8290
		
		elif((416000<=Gensenkeisan)and(Gensenkeisan<419000)and(self.Fuyo==4)):
			Gensen = 6670
		
		elif((416000<=Gensenkeisan)and(Gensenkeisan<419000)and(self.Fuyo==5)):
			Gensen = 5050
		
		elif((416000<=Gensenkeisan)and(Gensenkeisan<419000)and(self.Fuyo==6)):
			Gensen = 3440
		
		elif((416000<=Gensenkeisan)and(Gensenkeisan<419000)and(self.Fuyo==7)):
			Gensen = 1820
		
		#139
		elif((419000<=Gensenkeisan)and(Gensenkeisan<422000)and(self.Fuyo==0)): 
			Gensen = 18220   
		
		elif((419000<=Gensenkeisan)and(Gensenkeisan<422000)and(self.Fuyo==1)):
			Gensen = 14990 
		
		elif((419000<=Gensenkeisan)and(Gensenkeisan<422000)and(self.Fuyo==2)):
			Gensen = 11750
		
		elif((419000<=Gensenkeisan)and(Gensenkeisan<422000)and(self.Fuyo==3)):
			Gensen = 8530
		
		elif((419000<=Gensenkeisan)and(Gensenkeisan<422000)and(self.Fuyo==4)):
			Gensen = 6790
		
		elif((419000<=Gensenkeisan)and(Gensenkeisan<422000)and(self.Fuyo==5)):
			Gensen = 5180
		
		elif((419000<=Gensenkeisan)and(Gensenkeisan<422000)and(self.Fuyo==6)):
			Gensen = 3560
		
		elif((419000<=Gensenkeisan)and(Gensenkeisan<422000)and(self.Fuyo==7)):
			Gensen = 1940
		
		#140
		elif((422000<=Gensenkeisan)and(Gensenkeisan<425000)and(self.Fuyo==0)): 
			Gensen = 18470   
		
		elif((422000<=Gensenkeisan)and(Gensenkeisan<425000)and(self.Fuyo==1)):
			Gensen = 15230 
		
		elif((422000<=Gensenkeisan)and(Gensenkeisan<425000)and(self.Fuyo==2)):
			Gensen = 12000
		
		elif((422000<=Gensenkeisan)and(Gensenkeisan<425000)and(self.Fuyo==3)):
			Gensen = 8770
		
		elif((422000<=Gensenkeisan)and(Gensenkeisan<425000)and(self.Fuyo==4)):
			Gensen = 6910
		
		elif((422000<=Gensenkeisan)and(Gensenkeisan<425000)and(self.Fuyo==5)):
			Gensen = 5300
		
		elif((422000<=Gensenkeisan)and(Gensenkeisan<425000)and(self.Fuyo==6)):
			Gensen = 3690
		
		elif((422000<=Gensenkeisan)and(Gensenkeisan<425000)and(self.Fuyo==7)):
			Gensen = 2060
		
		#141
		elif((425000<=Gensenkeisan)and(Gensenkeisan<428000)and(self.Fuyo==0)): 
			Gensen = 18710   
		
		elif((425000<=Gensenkeisan)and(Gensenkeisan<428000)and(self.Fuyo==1)):
			Gensen = 15480 
		
		elif((425000<=Gensenkeisan)and(Gensenkeisan<428000)and(self.Fuyo==2)):
			Gensen = 12240
		
		elif((425000<=Gensenkeisan)and(Gensenkeisan<428000)and(self.Fuyo==3)):
			Gensen = 9020
		
		elif((425000<=Gensenkeisan)and(Gensenkeisan<428000)and(self.Fuyo==4)):
			Gensen = 7030
		
		elif((425000<=Gensenkeisan)and(Gensenkeisan<428000)and(self.Fuyo==5)):
			Gensen = 5420
		
		elif((425000<=Gensenkeisan)and(Gensenkeisan<428000)and(self.Fuyo==6)):
			Gensen = 3810
		
		elif((425000<=Gensenkeisan)and(Gensenkeisan<428000)and(self.Fuyo==7)):
			Gensen = 2180
		
		#142
		elif((428000<=Gensenkeisan)and(Gensenkeisan<431000)and(self.Fuyo==0)): 
			Gensen = 18960   
		
		elif((428000<=Gensenkeisan)and(Gensenkeisan<431000)and(self.Fuyo==1)):
			Gensen = 15720 
		
		elif((428000<=Gensenkeisan)and(Gensenkeisan<431000)and(self.Fuyo==2)):
			Gensen = 12490
		
		elif((428000<=Gensenkeisan)and(Gensenkeisan<431000)and(self.Fuyo==3)):
			Gensen = 9260
		
		elif((428000<=Gensenkeisan)and(Gensenkeisan<431000)and(self.Fuyo==4)):
			Gensen = 7160
		
		elif((428000<=Gensenkeisan)and(Gensenkeisan<431000)and(self.Fuyo==5)):
			Gensen = 5540
		
		elif((428000<=Gensenkeisan)and(Gensenkeisan<431000)and(self.Fuyo==6)):
			Gensen = 3930
		
		elif((428000<=Gensenkeisan)and(Gensenkeisan<431000)and(self.Fuyo==7)):
			Gensen = 2310
		
		#143
		elif((431000<=Gensenkeisan)and(Gensenkeisan<434000)and(self.Fuyo==0)): 
			Gensen = 19210   
		
		elif((431000<=Gensenkeisan)and(Gensenkeisan<434000)and(self.Fuyo==1)):
			Gensen = 15970 
		
		elif((431000<=Gensenkeisan)and(Gensenkeisan<434000)and(self.Fuyo==2)):
			Gensen = 12730
		
		elif((431000<=Gensenkeisan)and(Gensenkeisan<434000)and(self.Fuyo==3)):
			Gensen = 9510
		
		elif((431000<=Gensenkeisan)and(Gensenkeisan<434000)and(self.Fuyo==4)):
			Gensen = 7280
		
		elif((431000<=Gensenkeisan)and(Gensenkeisan<434000)and(self.Fuyo==5)):
			Gensen = 5670
		
		elif((431000<=Gensenkeisan)and(Gensenkeisan<434000)and(self.Fuyo==6)):
			Gensen = 4050
		
		elif((431000<=Gensenkeisan)and(Gensenkeisan<434000)and(self.Fuyo==7)):
			Gensen = 2430
		
		#144
		elif((434000<=Gensenkeisan)and(Gensenkeisan<437000)and(self.Fuyo==0)): 
			Gensen = 19450   
		
		elif((434000<=Gensenkeisan)and(Gensenkeisan<437000)and(self.Fuyo==1)):
			Gensen = 16210 
		
		elif((434000<=Gensenkeisan)and(Gensenkeisan<437000)and(self.Fuyo==2)):
			Gensen = 12980
		
		elif((434000<=Gensenkeisan)and(Gensenkeisan<437000)and(self.Fuyo==3)):
			Gensen = 9750
		
		elif((434000<=Gensenkeisan)and(Gensenkeisan<437000)and(self.Fuyo==4)):
			Gensen = 7400
		
		elif((434000<=Gensenkeisan)and(Gensenkeisan<437000)and(self.Fuyo==5)):
			Gensen = 5790
		
		elif((434000<=Gensenkeisan)and(Gensenkeisan<437000)and(self.Fuyo==6)):
			Gensen = 4180
		
		elif((434000<=Gensenkeisan)and(Gensenkeisan<437000)and(self.Fuyo==7)):
			Gensen = 2550
		
		#145
		elif((437000<=Gensenkeisan)and(Gensenkeisan<440000)and(self.Fuyo==0)): 
			Gensen = 19700   
		
		elif((437000<=Gensenkeisan)and(Gensenkeisan<440000)and(self.Fuyo==1)):
			Gensen = 16460 
		
		elif((437000<=Gensenkeisan)and(Gensenkeisan<440000)and(self.Fuyo==2)):
			Gensen = 13220
		
		elif((437000<=Gensenkeisan)and(Gensenkeisan<440000)and(self.Fuyo==3)):
			Gensen = 10000
		
		elif((437000<=Gensenkeisan)and(Gensenkeisan<440000)and(self.Fuyo==4)):
			Gensen = 7520
		
		elif((437000<=Gensenkeisan)and(Gensenkeisan<440000)and(self.Fuyo==5)):
			Gensen = 5910
		
		elif((437000<=Gensenkeisan)and(Gensenkeisan<440000)and(self.Fuyo==6)):
			Gensen = 4300
		
		elif((437000<=Gensenkeisan)and(Gensenkeisan<440000)and(self.Fuyo==7)):
			Gensen = 2680
		
		#146
		elif((440000<=Gensenkeisan)and(Gensenkeisan<443000)and(self.Fuyo==0)): 
			Gensen = 20090   
		
		elif((440000<=Gensenkeisan)and(Gensenkeisan<443000)and(self.Fuyo==1)):
			Gensen = 16700 
		
		elif((440000<=Gensenkeisan)and(Gensenkeisan<443000)and(self.Fuyo==2)):
			Gensen = 13470
		
		elif((440000<=Gensenkeisan)and(Gensenkeisan<443000)and(self.Fuyo==3)):
			Gensen = 10240
		
		elif((440000<=Gensenkeisan)and(Gensenkeisan<443000)and(self.Fuyo==4)):
			Gensen = 7650
		
		elif((440000<=Gensenkeisan)and(Gensenkeisan<443000)and(self.Fuyo==5)):
			Gensen = 6030
		
		elif((440000<=Gensenkeisan)and(Gensenkeisan<443000)and(self.Fuyo==6)):
			Gensen = 4420
		
		elif((440000<=Gensenkeisan)and(Gensenkeisan<443000)and(self.Fuyo==7)):
			Gensen = 2800
		
		#147
		elif((443000<=Gensenkeisan)and(Gensenkeisan<446000)and(self.Fuyo==0)): 
			Gensen = 20580   
		
		elif((443000<=Gensenkeisan)and(Gensenkeisan<446000)and(self.Fuyo==1)):
			Gensen = 16950 
		
		elif((443000<=Gensenkeisan)and(Gensenkeisan<446000)and(self.Fuyo==2)):
			Gensen = 13710
		
		elif((443000<=Gensenkeisan)and(Gensenkeisan<446000)and(self.Fuyo==3)):
			Gensen = 10490
		
		elif((443000<=Gensenkeisan)and(Gensenkeisan<446000)and(self.Fuyo==4)):
			Gensen = 7770
		
		elif((443000<=Gensenkeisan)and(Gensenkeisan<446000)and(self.Fuyo==5)):
			Gensen = 6160
		
		elif((443000<=Gensenkeisan)and(Gensenkeisan<446000)and(self.Fuyo==6)):
			Gensen = 4540
		
		elif((443000<=Gensenkeisan)and(Gensenkeisan<446000)and(self.Fuyo==7)):
			Gensen = 2920
		
		#148
		elif((446000<=Gensenkeisan)and(Gensenkeisan<449000)and(self.Fuyo==0)): 
			Gensen = 21070   
		
		elif((446000<=Gensenkeisan)and(Gensenkeisan<449000)and(self.Fuyo==1)):
			Gensen = 17190 
		
		elif((446000<=Gensenkeisan)and(Gensenkeisan<449000)and(self.Fuyo==2)):
			Gensen = 13960
		
		elif((446000<=Gensenkeisan)and(Gensenkeisan<449000)and(self.Fuyo==3)):
			Gensen = 10730
		
		elif((446000<=Gensenkeisan)and(Gensenkeisan<449000)and(self.Fuyo==4)):
			Gensen = 7890
		
		elif((446000<=Gensenkeisan)and(Gensenkeisan<449000)and(self.Fuyo==5)):
			Gensen = 6280
		
		elif((446000<=Gensenkeisan)and(Gensenkeisan<449000)and(self.Fuyo==6)):
			Gensen = 4670
		
		elif((446000<=Gensenkeisan)and(Gensenkeisan<449000)and(self.Fuyo==7)):
			Gensen = 3040
		
		#149
		elif((449000<=Gensenkeisan)and(Gensenkeisan<452000)and(self.Fuyo==0)): 
			Gensen = 21560   
		
		elif((449000<=Gensenkeisan)and(Gensenkeisan<452000)and(self.Fuyo==1)):
			Gensen = 17440 
		
		elif((449000<=Gensenkeisan)and(Gensenkeisan<452000)and(self.Fuyo==2)):
			Gensen = 14200
		
		elif((449000<=Gensenkeisan)and(Gensenkeisan<452000)and(self.Fuyo==3)):
			Gensen = 10980
		
		elif((449000<=Gensenkeisan)and(Gensenkeisan<452000)and(self.Fuyo==4)):
			Gensen = 8010
		
		elif((449000<=Gensenkeisan)and(Gensenkeisan<452000)and(self.Fuyo==5)):
			Gensen = 6400
		
		elif((449000<=Gensenkeisan)and(Gensenkeisan<452000)and(self.Fuyo==6)):
			Gensen = 4790
		
		elif((449000<=Gensenkeisan)and(Gensenkeisan<452000)and(self.Fuyo==7)):
			Gensen = 3170
		
		#150
		elif((452000<=Gensenkeisan)and(Gensenkeisan<455000)and(self.Fuyo==0)): 
			Gensen = 22050   
		
		elif((452000<=Gensenkeisan)and(Gensenkeisan<455000)and(self.Fuyo==1)):
			Gensen = 17680 
		
		elif((452000<=Gensenkeisan)and(Gensenkeisan<455000)and(self.Fuyo==2)):
			Gensen = 14450
		
		elif((452000<=Gensenkeisan)and(Gensenkeisan<455000)and(self.Fuyo==3)):
			Gensen = 11220
		
		elif((452000<=Gensenkeisan)and(Gensenkeisan<455000)and(self.Fuyo==4)):
			Gensen = 8140
		
		elif((452000<=Gensenkeisan)and(Gensenkeisan<455000)and(self.Fuyo==5)):
			Gensen = 6520
		
		elif((452000<=Gensenkeisan)and(Gensenkeisan<455000)and(self.Fuyo==6)):
			Gensen = 4910
		
		elif((452000<=Gensenkeisan)and(Gensenkeisan<455000)and(self.Fuyo==7)):
			Gensen = 3290
		
		#151
		elif((455000<=Gensenkeisan)and(Gensenkeisan<458000)and(self.Fuyo==0)): 
			Gensen = 22540   
		
		elif((455000<=Gensenkeisan)and(Gensenkeisan<458000)and(self.Fuyo==1)):
			Gensen = 17930 
		
		elif((455000<=Gensenkeisan)and(Gensenkeisan<458000)and(self.Fuyo==2)):
			Gensen = 14690
		
		elif((455000<=Gensenkeisan)and(Gensenkeisan<458000)and(self.Fuyo==3)):
			Gensen = 11470
		
		elif((455000<=Gensenkeisan)and(Gensenkeisan<458000)and(self.Fuyo==4)):
			Gensen = 8260
		
		elif((455000<=Gensenkeisan)and(Gensenkeisan<458000)and(self.Fuyo==5)):
			Gensen = 6650
		
		elif((455000<=Gensenkeisan)and(Gensenkeisan<458000)and(self.Fuyo==6)):
			Gensen = 5030
		
		elif((455000<=Gensenkeisan)and(Gensenkeisan<458000)and(self.Fuyo==7)):
			Gensen = 3410
		
		#152
		elif((458000<=Gensenkeisan)and(Gensenkeisan<461000)and(self.Fuyo==0)): 
			Gensen = 23030   
		
		elif((458000<=Gensenkeisan)and(Gensenkeisan<461000)and(self.Fuyo==1)):
			Gensen = 18170 
		
		elif((458000<=Gensenkeisan)and(Gensenkeisan<461000)and(self.Fuyo==2)):
			Gensen = 14940
		
		elif((458000<=Gensenkeisan)and(Gensenkeisan<461000)and(self.Fuyo==3)):
			Gensen = 11710
		
		elif((458000<=Gensenkeisan)and(Gensenkeisan<461000)and(self.Fuyo==4)):
			Gensen = 8470
		
		elif((458000<=Gensenkeisan)and(Gensenkeisan<461000)and(self.Fuyo==5)):
			Gensen = 6770
		
		elif((458000<=Gensenkeisan)and(Gensenkeisan<461000)and(self.Fuyo==6)):
			Gensen = 5160
		
		elif((458000<=Gensenkeisan)and(Gensenkeisan<461000)and(self.Fuyo==7)):
			Gensen = 3530
		
		#153
		elif((461000<=Gensenkeisan)and(Gensenkeisan<464000)and(self.Fuyo==0)): 
			Gensen = 23520   
		
		elif((461000<=Gensenkeisan)and(Gensenkeisan<464000)and(self.Fuyo==1)):
			Gensen = 18420 
		
		elif((461000<=Gensenkeisan)and(Gensenkeisan<464000)and(self.Fuyo==2)):
			Gensen = 15180
		
		elif((461000<=Gensenkeisan)and(Gensenkeisan<464000)and(self.Fuyo==3)):
			Gensen = 11960
		
		elif((461000<=Gensenkeisan)and(Gensenkeisan<464000)and(self.Fuyo==4)):
			Gensen = 8720
		
		elif((461000<=Gensenkeisan)and(Gensenkeisan<464000)and(self.Fuyo==5)):
			Gensen = 6890
		
		elif((461000<=Gensenkeisan)and(Gensenkeisan<464000)and(self.Fuyo==6)):
			Gensen = 5280
		
		elif((461000<=Gensenkeisan)and(Gensenkeisan<464000)and(self.Fuyo==7)):
			Gensen = 3660
		
		#154
		elif((464000<=Gensenkeisan)and(Gensenkeisan<467000)and(self.Fuyo==0)): 
			Gensen = 24010   
		
		elif((464000<=Gensenkeisan)and(Gensenkeisan<467000)and(self.Fuyo==1)):
			Gensen = 18660 
		
		elif((464000<=Gensenkeisan)and(Gensenkeisan<467000)and(self.Fuyo==2)):
			Gensen = 15430
		
		elif((464000<=Gensenkeisan)and(Gensenkeisan<467000)and(self.Fuyo==3)):
			Gensen = 12200
		
		elif((464000<=Gensenkeisan)and(Gensenkeisan<467000)and(self.Fuyo==4)):
			Gensen = 8960
		
		elif((464000<=Gensenkeisan)and(Gensenkeisan<467000)and(self.Fuyo==5)):
			Gensen = 7010
		
		elif((464000<=Gensenkeisan)and(Gensenkeisan<467000)and(self.Fuyo==6)):
			Gensen = 5400
		
		elif((464000<=Gensenkeisan)and(Gensenkeisan<467000)and(self.Fuyo==7)):
			Gensen = 3780
		
		#155
		elif((467000<=Gensenkeisan)and(Gensenkeisan<470000)and(self.Fuyo==0)): 
			Gensen = 24500   
		
		elif((467000<=Gensenkeisan)and(Gensenkeisan<470000)and(self.Fuyo==1)):
			Gensen = 18910 
		
		elif((467000<=Gensenkeisan)and(Gensenkeisan<470000)and(self.Fuyo==2)):
			Gensen = 15670
		
		elif((467000<=Gensenkeisan)and(Gensenkeisan<470000)and(self.Fuyo==3)):
			Gensen = 12450
		
		elif((467000<=Gensenkeisan)and(Gensenkeisan<470000)and(self.Fuyo==4)):
			Gensen = 9210
		
		elif((467000<=Gensenkeisan)and(Gensenkeisan<470000)and(self.Fuyo==5)):
			Gensen = 7140
		
		elif((467000<=Gensenkeisan)and(Gensenkeisan<470000)and(self.Fuyo==6)):
			Gensen = 5520
		
		elif((467000<=Gensenkeisan)and(Gensenkeisan<470000)and(self.Fuyo==7)):
			Gensen = 3900
		
		#156
		elif((470000<=Gensenkeisan)and(Gensenkeisan<473000)and(self.Fuyo==0)):
			Gensen = 24990 
		
		elif((470000<=Gensenkeisan)and(Gensenkeisan<473000)and(self.Fuyo==1)):
			Gensen = 19150 
		
		elif((470000<=Gensenkeisan)and(Gensenkeisan<473000)and(self.Fuyo==2)):
			Gensen = 15920 
		
		elif((470000<=Gensenkeisan)and(Gensenkeisan<473000)and(self.Fuyo==3)):
			Gensen = 12690 
		
		elif((470000<=Gensenkeisan)and(Gensenkeisan<473000)and(self.Fuyo==4)):
			Gensen = 9450 
		
		elif((470000<=Gensenkeisan)and(Gensenkeisan<473000)and(self.Fuyo==5)):
			Gensen = 7260 
		
		elif((470000<=Gensenkeisan)and(Gensenkeisan<473000)and(self.Fuyo==6)):
			Gensen = 5650 
		
		elif((470000<=Gensenkeisan)and(Gensenkeisan<473000)and(self.Fuyo==7)):
			Gensen = 4020 
		
		#157
		elif((473000<=Gensenkeisan)and(Gensenkeisan<476000)and(self.Fuyo==0)):
			Gensen = 25480 
		
		elif((473000<=Gensenkeisan)and(Gensenkeisan<476000)and(self.Fuyo==1)):
			Gensen = 19400 
		
		elif((473000<=Gensenkeisan)and(Gensenkeisan<476000)and(self.Fuyo==2)):
			Gensen = 16160 
		
		elif((473000<=Gensenkeisan)and(Gensenkeisan<476000)and(self.Fuyo==3)):
			Gensen = 12940 
		
		elif((473000<=Gensenkeisan)and(Gensenkeisan<476000)and(self.Fuyo==4)):
			Gensen = 9700 
		
		elif((473000<=Gensenkeisan)and(Gensenkeisan<476000)and(self.Fuyo==5)):
			Gensen = 7380 
		
		elif((473000<=Gensenkeisan)and(Gensenkeisan<476000)and(self.Fuyo==6)):
			Gensen = 5770 
		
		elif((473000<=Gensenkeisan)and(Gensenkeisan<476000)and(self.Fuyo==7)):
			Gensen = 4150 
		
		#158
		elif((476000<=Gensenkeisan)and(Gensenkeisan<479000)and(self.Fuyo==0)):
			Gensen = 25970 
		
		elif((476000<=Gensenkeisan)and(Gensenkeisan<479000)and(self.Fuyo==1)):
			Gensen = 19640 
		
		elif((476000<=Gensenkeisan)and(Gensenkeisan<479000)and(self.Fuyo==2)):
			Gensen = 16410 
		
		elif((476000<=Gensenkeisan)and(Gensenkeisan<479000)and(self.Fuyo==3)):
			Gensen = 13180 
		
		elif((476000<=Gensenkeisan)and(Gensenkeisan<479000)and(self.Fuyo==4)):
			Gensen = 9940 
		
		elif((476000<=Gensenkeisan)and(Gensenkeisan<479000)and(self.Fuyo==5)):
			Gensen = 7500 
		
		elif((476000<=Gensenkeisan)and(Gensenkeisan<479000)and(self.Fuyo==6)):
			Gensen = 5890 
		
		elif((476000<=Gensenkeisan)and(Gensenkeisan<479000)and(self.Fuyo==7)):
			Gensen = 4270 
		
		#159
		elif((479000<=Gensenkeisan)and(Gensenkeisan<482000)and(self.Fuyo==0)):
			Gensen = 26460 
		
		elif((479000<=Gensenkeisan)and(Gensenkeisan<482000)and(self.Fuyo==1)):
			Gensen = 20000 
		
		elif((479000<=Gensenkeisan)and(Gensenkeisan<482000)and(self.Fuyo==2)):
			Gensen = 16650 
		
		elif((479000<=Gensenkeisan)and(Gensenkeisan<482000)and(self.Fuyo==3)):
			Gensen = 13430 
		
		elif((479000<=Gensenkeisan)and(Gensenkeisan<482000)and(self.Fuyo==4)):
			Gensen = 10190 
		
		elif((479000<=Gensenkeisan)and(Gensenkeisan<482000)and(self.Fuyo==5)):
			Gensen = 7630 
		
		elif((479000<=Gensenkeisan)and(Gensenkeisan<482000)and(self.Fuyo==6)):
			Gensen = 6010 
		
		elif((479000<=Gensenkeisan)and(Gensenkeisan<482000)and(self.Fuyo==7)):
			Gensen = 4390 
		
		#160
		elif((482000<=Gensenkeisan)and(Gensenkeisan<485000)and(self.Fuyo==0)):
			Gensen = 26950 
		
		elif((482000<=Gensenkeisan)and(Gensenkeisan<485000)and(self.Fuyo==1)):
			Gensen = 20490 
		
		elif((482000<=Gensenkeisan)and(Gensenkeisan<485000)and(self.Fuyo==2)):
			Gensen = 16900 
		
		elif((482000<=Gensenkeisan)and(Gensenkeisan<485000)and(self.Fuyo==3)):
			Gensen = 13670 
		
		elif((482000<=Gensenkeisan)and(Gensenkeisan<485000)and(self.Fuyo==4)):
			Gensen = 10430 
		
		elif((482000<=Gensenkeisan)and(Gensenkeisan<485000)and(self.Fuyo==5)):
			Gensen = 7750 
		
		elif((482000<=Gensenkeisan)and(Gensenkeisan<485000)and(self.Fuyo==6)):
			Gensen = 6140 
		
		elif((482000<=Gensenkeisan)and(Gensenkeisan<485000)and(self.Fuyo==7)):
			Gensen = 4510 
		
		#161
		elif((485000<=Gensenkeisan)and(Gensenkeisan<488000)and(self.Fuyo==0)):
			Gensen = 27440 
		
		elif((485000<=Gensenkeisan)and(Gensenkeisan<488000)and(self.Fuyo==1)):
			Gensen = 20980 
		
		elif((485000<=Gensenkeisan)and(Gensenkeisan<488000)and(self.Fuyo==2)):
			Gensen = 17140 
		
		elif((485000<=Gensenkeisan)and(Gensenkeisan<488000)and(self.Fuyo==3)):
			Gensen = 13920 
		
		elif((485000<=Gensenkeisan)and(Gensenkeisan<488000)and(self.Fuyo==4)):
			Gensen = 10680 
		
		elif((485000<=Gensenkeisan)and(Gensenkeisan<488000)and(self.Fuyo==5)):
			Gensen = 7870 
		
		elif((485000<=Gensenkeisan)and(Gensenkeisan<488000)and(self.Fuyo==6)):
			Gensen = 6260 
		
		elif((485000<=Gensenkeisan)and(Gensenkeisan<488000)and(self.Fuyo==7)):
			Gensen = 4640 
		
		#162
		elif((488000<=Gensenkeisan)and(Gensenkeisan<491000)and(self.Fuyo==0)):
			Gensen = 27930 
		
		elif((488000<=Gensenkeisan)and(Gensenkeisan<491000)and(self.Fuyo==1)):
			Gensen = 21470 
		
		elif((488000<=Gensenkeisan)and(Gensenkeisan<491000)and(self.Fuyo==2)):
			Gensen = 17390 
		
		elif((488000<=Gensenkeisan)and(Gensenkeisan<491000)and(self.Fuyo==3)):
			Gensen = 14160 
		
		elif((488000<=Gensenkeisan)and(Gensenkeisan<491000)and(self.Fuyo==4)):
			Gensen = 10920 
		
		elif((488000<=Gensenkeisan)and(Gensenkeisan<491000)and(self.Fuyo==5)):
			Gensen = 7990 
		
		elif((488000<=Gensenkeisan)and(Gensenkeisan<491000)and(self.Fuyo==6)):
			Gensen = 6380 
		
		elif((488000<=Gensenkeisan)and(Gensenkeisan<491000)and(self.Fuyo==7)):
			Gensen = 4760 
		
		#163
		elif((491000<=Gensenkeisan)and(Gensenkeisan<494000)and(self.Fuyo==0)):
			Gensen = 28420 
		
		elif((491000<=Gensenkeisan)and(Gensenkeisan<494000)and(self.Fuyo==1)):
			Gensen = 21960 
		
		elif((491000<=Gensenkeisan)and(Gensenkeisan<494000)and(self.Fuyo==2)):
			Gensen = 17630 
		
		elif((491000<=Gensenkeisan)and(Gensenkeisan<494000)and(self.Fuyo==3)):
			Gensen = 14410 
		
		elif((491000<=Gensenkeisan)and(Gensenkeisan<494000)and(self.Fuyo==4)):
			Gensen = 11170 
		
		elif((491000<=Gensenkeisan)and(Gensenkeisan<494000)and(self.Fuyo==5)):
			Gensen = 8120 
		
		elif((491000<=Gensenkeisan)and(Gensenkeisan<494000)and(self.Fuyo==6)):
			Gensen = 6500 
		
		elif((491000<=Gensenkeisan)and(Gensenkeisan<494000)and(self.Fuyo==7)):
			Gensen = 4880 
		
		#164
		elif((494000<=Gensenkeisan)and(Gensenkeisan<497000)and(self.Fuyo==0)):
			Gensen = 28910 
		
		elif((494000<=Gensenkeisan)and(Gensenkeisan<497000)and(self.Fuyo==1)):
			Gensen = 22450 
		
		elif((494000<=Gensenkeisan)and(Gensenkeisan<497000)and(self.Fuyo==2)):
			Gensen = 17880 
		
		elif((494000<=Gensenkeisan)and(Gensenkeisan<497000)and(self.Fuyo==3)):
			Gensen = 14650 
		
		elif((494000<=Gensenkeisan)and(Gensenkeisan<497000)and(self.Fuyo==4)):
			Gensen = 11410 
		
		elif((494000<=Gensenkeisan)and(Gensenkeisan<497000)and(self.Fuyo==5)):
			Gensen = 8240 
		
		elif((494000<=Gensenkeisan)and(Gensenkeisan<497000)and(self.Fuyo==6)):
			Gensen = 6630 
		
		elif((494000<=Gensenkeisan)and(Gensenkeisan<497000)and(self.Fuyo==7)):
			Gensen = 5000 
		
		#165
		elif((497000<=Gensenkeisan)and(Gensenkeisan<500000)and(self.Fuyo==0)):
			Gensen = 29400 
		
		elif((497000<=Gensenkeisan)and(Gensenkeisan<500000)and(self.Fuyo==1)):
			Gensen = 22940 
		
		elif((497000<=Gensenkeisan)and(Gensenkeisan<500000)and(self.Fuyo==2)):
			Gensen = 18120 
		
		elif((497000<=Gensenkeisan)and(Gensenkeisan<500000)and(self.Fuyo==3)):
			Gensen = 14900 
		
		elif((497000<=Gensenkeisan)and(Gensenkeisan<500000)and(self.Fuyo==4)):
			Gensen = 11660 
		
		elif((497000<=Gensenkeisan)and(Gensenkeisan<500000)and(self.Fuyo==5)):
			Gensen = 8420 
		
		elif((497000<=Gensenkeisan)and(Gensenkeisan<500000)and(self.Fuyo==6)):
			Gensen = 6750 
		
		elif((497000<=Gensenkeisan)and(Gensenkeisan<500000)and(self.Fuyo==7)):
			Gensen = 5130 
		
		#166
		elif((500000<=Gensenkeisan)and(Gensenkeisan<503000)and(self.Fuyo==0)):
			Gensen = 29890 
		
		elif((500000<=Gensenkeisan)and(Gensenkeisan<503000)and(self.Fuyo==1)):
			Gensen = 23430 
		
		elif((500000<=Gensenkeisan)and(Gensenkeisan<503000)and(self.Fuyo==2)):
			Gensen = 18370 
		
		elif((500000<=Gensenkeisan)and(Gensenkeisan<503000)and(self.Fuyo==3)):
			Gensen = 15140 
		
		elif((500000<=Gensenkeisan)and(Gensenkeisan<503000)and(self.Fuyo==4)):
			Gensen = 11900 
		
		elif((500000<=Gensenkeisan)and(Gensenkeisan<503000)and(self.Fuyo==5)):
			Gensen = 8670 
		
		elif((500000<=Gensenkeisan)and(Gensenkeisan<503000)and(self.Fuyo==6)):
			Gensen = 6870 
		
		elif((500000<=Gensenkeisan)and(Gensenkeisan<503000)and(self.Fuyo==7)):
			Gensen = 5250 
		
		#167
		elif((503000<=Gensenkeisan)and(Gensenkeisan<506000)and(self.Fuyo==0)):
			Gensen = 30380 
		
		elif((503000<=Gensenkeisan)and(Gensenkeisan<506000)and(self.Fuyo==1)):
			Gensen = 23920 
		
		elif((503000<=Gensenkeisan)and(Gensenkeisan<506000)and(self.Fuyo==2)):
			Gensen = 18610 
		
		elif((503000<=Gensenkeisan)and(Gensenkeisan<506000)and(self.Fuyo==3)):
			Gensen = 15390 
		
		elif((503000<=Gensenkeisan)and(Gensenkeisan<506000)and(self.Fuyo==4)):
			Gensen = 12150 
		
		elif((503000<=Gensenkeisan)and(Gensenkeisan<506000)and(self.Fuyo==5)):
			Gensen = 8910 
		
		elif((503000<=Gensenkeisan)and(Gensenkeisan<506000)and(self.Fuyo==6)):
			Gensen = 6990 
		
		elif((503000<=Gensenkeisan)and(Gensenkeisan<506000)and(self.Fuyo==7)):
			Gensen = 5370 
		
		#168
		elif((506000<=Gensenkeisan)and(Gensenkeisan<509000)and(self.Fuyo==0)):
			Gensen = 30880 
		
		elif((506000<=Gensenkeisan)and(Gensenkeisan<509000)and(self.Fuyo==1)):
			Gensen = 24410 
		
		elif((506000<=Gensenkeisan)and(Gensenkeisan<509000)and(self.Fuyo==2)):
			Gensen = 18860 
		
		elif((506000<=Gensenkeisan)and(Gensenkeisan<509000)and(self.Fuyo==3)):
			Gensen = 15630 
		
		elif((506000<=Gensenkeisan)and(Gensenkeisan<509000)and(self.Fuyo==4)):
			Gensen = 12390 
		
		elif((506000<=Gensenkeisan)and(Gensenkeisan<509000)and(self.Fuyo==5)):
			Gensen = 9160 
		
		elif((506000<=Gensenkeisan)and(Gensenkeisan<509000)and(self.Fuyo==6)):
			Gensen = 7120 
		
		elif((506000<=Gensenkeisan)and(Gensenkeisan<509000)and(self.Fuyo==7)):
			Gensen = 5490 
		
		#169
		elif((509000<=Gensenkeisan)and(Gensenkeisan<512000)and(self.Fuyo==0)):
			Gensen = 31370 
		
		elif((509000<=Gensenkeisan)and(Gensenkeisan<512000)and(self.Fuyo==1)):
			Gensen = 24900 
		
		elif((509000<=Gensenkeisan)and(Gensenkeisan<512000)and(self.Fuyo==2)):
			Gensen = 19100 
		
		elif((509000<=Gensenkeisan)and(Gensenkeisan<512000)and(self.Fuyo==3)):
			Gensen = 15880 
		
		elif((509000<=Gensenkeisan)and(Gensenkeisan<512000)and(self.Fuyo==4)):
			Gensen = 12640 
		
		elif((509000<=Gensenkeisan)and(Gensenkeisan<512000)and(self.Fuyo==5)):
			Gensen = 9400 
		
		elif((509000<=Gensenkeisan)and(Gensenkeisan<512000)and(self.Fuyo==6)):
			Gensen = 7240 
		
		elif((509000<=Gensenkeisan)and(Gensenkeisan<512000)and(self.Fuyo==7)):
			Gensen = 5620 
		
		#170
		elif((512000<=Gensenkeisan)and(Gensenkeisan<515000)and(self.Fuyo==0)):
			Gensen = 31860 
		
		elif((512000<=Gensenkeisan)and(Gensenkeisan<515000)and(self.Fuyo==1)):
			Gensen = 25390 
		
		elif((512000<=Gensenkeisan)and(Gensenkeisan<515000)and(self.Fuyo==2)):
			Gensen = 19350 
		
		elif((512000<=Gensenkeisan)and(Gensenkeisan<515000)and(self.Fuyo==3)):
			Gensen = 16120 
		
		elif((512000<=Gensenkeisan)and(Gensenkeisan<515000)and(self.Fuyo==4)):
			Gensen = 12890 
		
		elif((512000<=Gensenkeisan)and(Gensenkeisan<515000)and(self.Fuyo==5)):
			Gensen = 9650 
		
		elif((512000<=Gensenkeisan)and(Gensenkeisan<515000)and(self.Fuyo==6)):
			Gensen = 7360 
		
		elif((512000<=Gensenkeisan)and(Gensenkeisan<515000)and(self.Fuyo==7)):
			Gensen = 5740 
		
		#171
		elif((515000<=Gensenkeisan)and(Gensenkeisan<518000)and(self.Fuyo==0)):
			Gensen = 32350 
		
		elif((515000<=Gensenkeisan)and(Gensenkeisan<518000)and(self.Fuyo==1)):
			Gensen = 25880 
		
		elif((515000<=Gensenkeisan)and(Gensenkeisan<518000)and(self.Fuyo==2)):
			Gensen = 19590 
		
		elif((515000<=Gensenkeisan)and(Gensenkeisan<518000)and(self.Fuyo==3)):
			Gensen = 16370 
		
		elif((515000<=Gensenkeisan)and(Gensenkeisan<518000)and(self.Fuyo==4)):
			Gensen = 13130 
		
		elif((515000<=Gensenkeisan)and(Gensenkeisan<518000)and(self.Fuyo==5)):
			Gensen = 9890 
		
		elif((515000<=Gensenkeisan)and(Gensenkeisan<518000)and(self.Fuyo==6)):
			Gensen = 7480 
		
		elif((515000<=Gensenkeisan)and(Gensenkeisan<518000)and(self.Fuyo==7)):
			Gensen = 5860 
		
		#172
		elif((518000<=Gensenkeisan)and(Gensenkeisan<521000)and(self.Fuyo==0)):
			Gensen = 32840 
		
		elif((518000<=Gensenkeisan)and(Gensenkeisan<521000)and(self.Fuyo==1)):
			Gensen = 26370 
		
		elif((518000<=Gensenkeisan)and(Gensenkeisan<521000)and(self.Fuyo==2)):
			Gensen = 19900 
		
		elif((518000<=Gensenkeisan)and(Gensenkeisan<521000)and(self.Fuyo==3)):
			Gensen = 16610 
		
		elif((518000<=Gensenkeisan)and(Gensenkeisan<521000)and(self.Fuyo==4)):
			Gensen = 13380 
		
		elif((518000<=Gensenkeisan)and(Gensenkeisan<521000)and(self.Fuyo==5)):
			Gensen = 10140 
		
		elif((518000<=Gensenkeisan)and(Gensenkeisan<521000)and(self.Fuyo==6)):
			Gensen = 7610 
		
		elif((518000<=Gensenkeisan)and(Gensenkeisan<521000)and(self.Fuyo==7)):
			Gensen = 5980 
		
		#173
		elif((521000<=Gensenkeisan)and(Gensenkeisan<524000)and(self.Fuyo==0)):
			Gensen = 33330 
		
		elif((521000<=Gensenkeisan)and(Gensenkeisan<524000)and(self.Fuyo==1)):
			Gensen = 26860 
		
		elif((521000<=Gensenkeisan)and(Gensenkeisan<524000)and(self.Fuyo==2)):
			Gensen = 20390 
		
		elif((521000<=Gensenkeisan)and(Gensenkeisan<524000)and(self.Fuyo==3)):
			Gensen = 16860 
		
		elif((521000<=Gensenkeisan)and(Gensenkeisan<524000)and(self.Fuyo==4)):
			Gensen = 13620 
		
		elif((521000<=Gensenkeisan)and(Gensenkeisan<524000)and(self.Fuyo==5)):
			Gensen = 10380 
		
		elif((521000<=Gensenkeisan)and(Gensenkeisan<524000)and(self.Fuyo==6)):
			Gensen = 7730 
		
		elif((521000<=Gensenkeisan)and(Gensenkeisan<524000)and(self.Fuyo==7)):
			Gensen = 6110 
		
		#174
		elif((524000<=Gensenkeisan)and(Gensenkeisan<527000)and(self.Fuyo==0)):
			Gensen = 33820 
		
		elif((524000<=Gensenkeisan)and(Gensenkeisan<527000)and(self.Fuyo==1)):
			Gensen = 27350 
		
		elif((524000<=Gensenkeisan)and(Gensenkeisan<527000)and(self.Fuyo==2)):
			Gensen = 20880 
		
		elif((524000<=Gensenkeisan)and(Gensenkeisan<527000)and(self.Fuyo==3)):
			Gensen = 17100 
		
		elif((524000<=Gensenkeisan)and(Gensenkeisan<527000)and(self.Fuyo==4)):
			Gensen = 13870 
		
		elif((524000<=Gensenkeisan)and(Gensenkeisan<527000)and(self.Fuyo==5)):
			Gensen = 10630 
		
		elif((524000<=Gensenkeisan)and(Gensenkeisan<527000)and(self.Fuyo==6)):
			Gensen = 7850 
		
		elif((524000<=Gensenkeisan)and(Gensenkeisan<527000)and(self.Fuyo==7)):
			Gensen = 6230 
		
		#175
		elif((527000<=Gensenkeisan)and(Gensenkeisan<530000)and(self.Fuyo==0)):
			Gensen = 34310 
		
		elif((527000<=Gensenkeisan)and(Gensenkeisan<530000)and(self.Fuyo==1)):
			Gensen = 27840 
		
		elif((527000<=Gensenkeisan)and(Gensenkeisan<530000)and(self.Fuyo==2)):
			Gensen = 21370 
		
		elif((527000<=Gensenkeisan)and(Gensenkeisan<530000)and(self.Fuyo==3)):
			Gensen = 17350 
		
		elif((527000<=Gensenkeisan)and(Gensenkeisan<530000)and(self.Fuyo==4)):
			Gensen = 14110 
		
		elif((527000<=Gensenkeisan)and(Gensenkeisan<530000)and(self.Fuyo==5)):
			Gensen = 10870 
		
		elif((527000<=Gensenkeisan)and(Gensenkeisan<530000)and(self.Fuyo==6)):
			Gensen = 7970 
		
		elif((527000<=Gensenkeisan)and(Gensenkeisan<530000)and(self.Fuyo==7)):
			Gensen = 6350 
		
		#176
		elif((530000<=Gensenkeisan)and(Gensenkeisan<533000)and(self.Fuyo==0)):
			Gensen = 34800 
		
		elif((530000<=Gensenkeisan)and(Gensenkeisan<533000)and(self.Fuyo==1)):
			Gensen = 28330 
		
		elif((530000<=Gensenkeisan)and(Gensenkeisan<533000)and(self.Fuyo==2)):
			Gensen = 21860 
		
		elif((530000<=Gensenkeisan)and(Gensenkeisan<533000)and(self.Fuyo==3)):
			Gensen = 17590 
		
		elif((530000<=Gensenkeisan)and(Gensenkeisan<533000)and(self.Fuyo==4)):
			Gensen = 14360 
		
		elif((530000<=Gensenkeisan)and(Gensenkeisan<533000)and(self.Fuyo==5)):
			Gensen = 11120 
		
		elif((530000<=Gensenkeisan)and(Gensenkeisan<533000)and(self.Fuyo==6)):
			Gensen = 8100 
		
		elif((530000<=Gensenkeisan)and(Gensenkeisan<533000)and(self.Fuyo==7)):
			Gensen = 6470 
		
		#177
		elif((533000<=Gensenkeisan)and(Gensenkeisan<536000)and(self.Fuyo==0)):
			Gensen = 35290 
		
		elif((533000<=Gensenkeisan)and(Gensenkeisan<536000)and(self.Fuyo==1)):
			Gensen = 28820 
		
		elif((533000<=Gensenkeisan)and(Gensenkeisan<536000)and(self.Fuyo==2)):
			Gensen = 22350 
		
		elif((533000<=Gensenkeisan)and(Gensenkeisan<536000)and(self.Fuyo==3)):
			Gensen = 17840 
		
		elif((533000<=Gensenkeisan)and(Gensenkeisan<536000)and(self.Fuyo==4)):
			Gensen = 14600 
		
		elif((533000<=Gensenkeisan)and(Gensenkeisan<536000)and(self.Fuyo==5)):
			Gensen = 11360 
		
		elif((533000<=Gensenkeisan)and(Gensenkeisan<536000)and(self.Fuyo==6)):
			Gensen = 8220 
		
		elif((533000<=Gensenkeisan)and(Gensenkeisan<536000)and(self.Fuyo==7)):
			Gensen = 6600 
		
		#178
		elif((536000<=Gensenkeisan)and(Gensenkeisan<539000)and(self.Fuyo==0)):
			Gensen = 35780 
		
		elif((536000<=Gensenkeisan)and(Gensenkeisan<539000)and(self.Fuyo==1)):
			Gensen = 29310 
		
		elif((536000<=Gensenkeisan)and(Gensenkeisan<539000)and(self.Fuyo==2)):
			Gensen = 22840 
		
		elif((536000<=Gensenkeisan)and(Gensenkeisan<539000)and(self.Fuyo==3)):
			Gensen = 18080 
		
		elif((536000<=Gensenkeisan)and(Gensenkeisan<539000)and(self.Fuyo==4)):
			Gensen = 14850 
		
		elif((536000<=Gensenkeisan)and(Gensenkeisan<539000)and(self.Fuyo==5)):
			Gensen = 11610 
		
		elif((536000<=Gensenkeisan)and(Gensenkeisan<539000)and(self.Fuyo==6)):
			Gensen = 8380 
		
		elif((536000<=Gensenkeisan)and(Gensenkeisan<539000)and(self.Fuyo==7)):
			Gensen = 6720 
		
		#179
		elif((539000<=Gensenkeisan)and(Gensenkeisan<542000)and(self.Fuyo==0)):
			Gensen = 36270 
		
		elif((539000<=Gensenkeisan)and(Gensenkeisan<542000)and(self.Fuyo==1)):
			Gensen = 29800 
		
		elif((539000<=Gensenkeisan)and(Gensenkeisan<542000)and(self.Fuyo==2)):
			Gensen = 23330 
		
		elif((539000<=Gensenkeisan)and(Gensenkeisan<542000)and(self.Fuyo==3)):
			Gensen = 18330 
		
		elif((539000<=Gensenkeisan)and(Gensenkeisan<542000)and(self.Fuyo==4)):
			Gensen = 15090 
		
		elif((539000<=Gensenkeisan)and(Gensenkeisan<542000)and(self.Fuyo==5)):
			Gensen = 11850 
		
		elif((539000<=Gensenkeisan)and(Gensenkeisan<542000)and(self.Fuyo==6)):
			Gensen = 8630 
		
		elif((539000<=Gensenkeisan)and(Gensenkeisan<542000)and(self.Fuyo==7)):
			Gensen = 6840 
		
		#180
		elif((542000<=Gensenkeisan)and(Gensenkeisan<545000)and(self.Fuyo==0)):
			Gensen = 36760 
		
		elif((542000<=Gensenkeisan)and(Gensenkeisan<545000)and(self.Fuyo==1)):
			Gensen = 30290 
		
		elif((542000<=Gensenkeisan)and(Gensenkeisan<545000)and(self.Fuyo==2)):
			Gensen = 23820 
		
		elif((542000<=Gensenkeisan)and(Gensenkeisan<545000)and(self.Fuyo==3)):
			Gensen = 18570 
		
		elif((542000<=Gensenkeisan)and(Gensenkeisan<545000)and(self.Fuyo==4)):
			Gensen = 15340 
		
		elif((542000<=Gensenkeisan)and(Gensenkeisan<545000)and(self.Fuyo==5)):
			Gensen = 12100 
		
		elif((542000<=Gensenkeisan)and(Gensenkeisan<545000)and(self.Fuyo==6)):
			Gensen = 8870 
		
		elif((542000<=Gensenkeisan)and(Gensenkeisan<545000)and(self.Fuyo==7)):
			Gensen = 6960 
		
		#181
		elif((545000<=Gensenkeisan)and(Gensenkeisan<548000)and(self.Fuyo==0)):
			Gensen = 37250 
		
		elif((545000<=Gensenkeisan)and(Gensenkeisan<548000)and(self.Fuyo==1)):
			Gensen = 30780 
		
		elif((545000<=Gensenkeisan)and(Gensenkeisan<548000)and(self.Fuyo==2)):
			Gensen = 24310 
		
		elif((545000<=Gensenkeisan)and(Gensenkeisan<548000)and(self.Fuyo==3)):
			Gensen = 18820 
		
		elif((545000<=Gensenkeisan)and(Gensenkeisan<548000)and(self.Fuyo==4)):
			Gensen = 15580 
		
		elif((545000<=Gensenkeisan)and(Gensenkeisan<548000)and(self.Fuyo==5)):
			Gensen = 12340 
		
		elif((545000<=Gensenkeisan)and(Gensenkeisan<548000)and(self.Fuyo==6)):
			Gensen = 9120 
		
		elif((545000<=Gensenkeisan)and(Gensenkeisan<548000)and(self.Fuyo==7)):
			Gensen = 7090 
		
		#182
		elif((548000<=Gensenkeisan)and(Gensenkeisan<551000)and(self.Fuyo==0)):
			Gensen = 37740 
		
		elif((548000<=Gensenkeisan)and(Gensenkeisan<551000)and(self.Fuyo==1)):
			Gensen = 31270 
		
		elif((548000<=Gensenkeisan)and(Gensenkeisan<551000)and(self.Fuyo==2)):
			Gensen = 24800 
		
		elif((548000<=Gensenkeisan)and(Gensenkeisan<551000)and(self.Fuyo==3)):
			Gensen = 19060 
		
		elif((548000<=Gensenkeisan)and(Gensenkeisan<551000)and(self.Fuyo==4)):
			Gensen = 15830 
		
		elif((548000<=Gensenkeisan)and(Gensenkeisan<551000)and(self.Fuyo==5)):
			Gensen = 12590 
		
		elif((548000<=Gensenkeisan)and(Gensenkeisan<551000)and(self.Fuyo==6)):
			Gensen = 9360 
		
		elif((548000<=Gensenkeisan)and(Gensenkeisan<551000)and(self.Fuyo==7)):
			Gensen = 7210 
		
		#183
		elif((551000<=Gensenkeisan)and(Gensenkeisan<554000)and(self.Fuyo==0)):
			Gensen = 38280 
		
		elif((551000<=Gensenkeisan)and(Gensenkeisan<554000)and(self.Fuyo==1)):
			Gensen = 31810 
		
		elif((551000<=Gensenkeisan)and(Gensenkeisan<554000)and(self.Fuyo==2)):
			Gensen = 25340 
		
		elif((551000<=Gensenkeisan)and(Gensenkeisan<554000)and(self.Fuyo==3)):
			Gensen = 19330 
		
		elif((551000<=Gensenkeisan)and(Gensenkeisan<554000)and(self.Fuyo==4)):
			Gensen = 16100 
		
		elif((551000<=Gensenkeisan)and(Gensenkeisan<554000)and(self.Fuyo==5)):
			Gensen = 12860 
		
		elif((551000<=Gensenkeisan)and(Gensenkeisan<554000)and(self.Fuyo==6)):
			Gensen = 9630 
		
		elif((551000<=Gensenkeisan)and(Gensenkeisan<554000)and(self.Fuyo==7)):
			Gensen = 7350 
		
		#184
		elif((554000<=Gensenkeisan)and(Gensenkeisan<557000)and(self.Fuyo==0)):
			Gensen = 38830 
		
		elif((554000<=Gensenkeisan)and(Gensenkeisan<557000)and(self.Fuyo==1)):
			Gensen = 32370 
		
		elif((554000<=Gensenkeisan)and(Gensenkeisan<557000)and(self.Fuyo==2)):
			Gensen = 25890 
		
		elif((554000<=Gensenkeisan)and(Gensenkeisan<557000)and(self.Fuyo==3)):
			Gensen = 19600 
		
		elif((554000<=Gensenkeisan)and(Gensenkeisan<557000)and(self.Fuyo==4)):
			Gensen = 16380 
		
		elif((554000<=Gensenkeisan)and(Gensenkeisan<557000)and(self.Fuyo==5)):
			Gensen = 13140 
		
		elif((554000<=Gensenkeisan)and(Gensenkeisan<557000)and(self.Fuyo==6)):
			Gensen = 9900 
		
		elif((554000<=Gensenkeisan)and(Gensenkeisan<557000)and(self.Fuyo==7)):
			Gensen = 7480 
		
		#185
		elif((557000<=Gensenkeisan)and(Gensenkeisan<560000)and(self.Fuyo==0)):
			Gensen = 39380 
		
		elif((557000<=Gensenkeisan)and(Gensenkeisan<560000)and(self.Fuyo==1)):
			Gensen = 32920 
		
		elif((557000<=Gensenkeisan)and(Gensenkeisan<560000)and(self.Fuyo==2)):
			Gensen = 26440 
		
		elif((557000<=Gensenkeisan)and(Gensenkeisan<560000)and(self.Fuyo==3)):
			Gensen = 19980 
		
		elif((557000<=Gensenkeisan)and(Gensenkeisan<560000)and(self.Fuyo==4)):
			Gensen = 16650 
		
		elif((557000<=Gensenkeisan)and(Gensenkeisan<560000)and(self.Fuyo==5)):
			Gensen = 13420 
		
		elif((557000<=Gensenkeisan)and(Gensenkeisan<560000)and(self.Fuyo==6)):
			Gensen = 10180 
		
		elif((557000<=Gensenkeisan)and(Gensenkeisan<560000)and(self.Fuyo==7)):
			Gensen = 7630 
		
		#186
		elif((560000<=Gensenkeisan)and(Gensenkeisan<563000)and(self.Fuyo==0)):
			Gensen = 39930 
		
		elif((560000<=Gensenkeisan)and(Gensenkeisan<563000)and(self.Fuyo==1)):
			Gensen = 33470 
		
		elif((560000<=Gensenkeisan)and(Gensenkeisan<563000)and(self.Fuyo==2)):
			Gensen = 27000 
		
		elif((560000<=Gensenkeisan)and(Gensenkeisan<563000)and(self.Fuyo==3)):
			Gensen = 20530 
		
		elif((560000<=Gensenkeisan)and(Gensenkeisan<563000)and(self.Fuyo==4)):
			Gensen = 16930 
		
		elif((560000<=Gensenkeisan)and(Gensenkeisan<563000)and(self.Fuyo==5)):
			Gensen = 13690 
		
		elif((560000<=Gensenkeisan)and(Gensenkeisan<563000)and(self.Fuyo==6)):
			Gensen = 10460 
		
		elif((560000<=Gensenkeisan)and(Gensenkeisan<563000)and(self.Fuyo==7)):
			Gensen = 7760 
		
		#187
		elif((563000<=Gensenkeisan)and(Gensenkeisan<566000)and(self.Fuyo==0)):
			Gensen = 40480 
		
		elif((563000<=Gensenkeisan)and(Gensenkeisan<566000)and(self.Fuyo==1)):
			Gensen = 34020 
		
		elif((563000<=Gensenkeisan)and(Gensenkeisan<566000)and(self.Fuyo==2)):
			Gensen = 27550 
		
		elif((563000<=Gensenkeisan)and(Gensenkeisan<566000)and(self.Fuyo==3)):
			Gensen = 21080 
		
		elif((563000<=Gensenkeisan)and(Gensenkeisan<566000)and(self.Fuyo==4)):
			Gensen = 17200 
		
		elif((563000<=Gensenkeisan)and(Gensenkeisan<566000)and(self.Fuyo==5)):
			Gensen = 13970 
		
		elif((563000<=Gensenkeisan)and(Gensenkeisan<566000)and(self.Fuyo==6)):
			Gensen = 10730 
		
		elif((563000<=Gensenkeisan)and(Gensenkeisan<566000)and(self.Fuyo==7)):
			Gensen = 7900 
		
		#188
		elif((566000<=Gensenkeisan)and(Gensenkeisan<569000)and(self.Fuyo==0)):
			Gensen = 41030 
		
		elif((566000<=Gensenkeisan)and(Gensenkeisan<569000)and(self.Fuyo==1)):
			Gensen = 34570 
		
		elif((566000<=Gensenkeisan)and(Gensenkeisan<569000)and(self.Fuyo==2)):
			Gensen = 28100 
		
		elif((566000<=Gensenkeisan)and(Gensenkeisan<569000)and(self.Fuyo==3)):
			Gensen = 21630 
		
		elif((566000<=Gensenkeisan)and(Gensenkeisan<569000)and(self.Fuyo==4)):
			Gensen = 17480 
		
		elif((566000<=Gensenkeisan)and(Gensenkeisan<569000)and(self.Fuyo==5)):
			Gensen = 14240 
		
		elif((566000<=Gensenkeisan)and(Gensenkeisan<569000)and(self.Fuyo==6)):
			Gensen = 11010 
		
		elif((566000<=Gensenkeisan)and(Gensenkeisan<569000)and(self.Fuyo==7)):
			Gensen = 8040 
		
		#189
		elif((569000<=Gensenkeisan)and(Gensenkeisan<572000)and(self.Fuyo==0)):
			Gensen = 41590 
		
		elif((569000<=Gensenkeisan)and(Gensenkeisan<572000)and(self.Fuyo==1)):
			Gensen = 35120 
		
		elif((569000<=Gensenkeisan)and(Gensenkeisan<572000)and(self.Fuyo==2)):
			Gensen = 28650 
		
		elif((569000<=Gensenkeisan)and(Gensenkeisan<572000)and(self.Fuyo==3)):
			Gensen = 22190 
		
		elif((569000<=Gensenkeisan)and(Gensenkeisan<572000)and(self.Fuyo==4)):
			Gensen = 17760 
		
		elif((569000<=Gensenkeisan)and(Gensenkeisan<572000)and(self.Fuyo==5)):
			Gensen = 14520 
		
		elif((569000<=Gensenkeisan)and(Gensenkeisan<572000)and(self.Fuyo==6)):
			Gensen = 11280 
		
		elif((569000<=Gensenkeisan)and(Gensenkeisan<572000)and(self.Fuyo==7)):
			Gensen = 8180 
		
		#190
		elif((572000<=Gensenkeisan)and(Gensenkeisan<575000)and(self.Fuyo==0)):
			Gensen = 42140 
		
		elif((572000<=Gensenkeisan)and(Gensenkeisan<575000)and(self.Fuyo==1)):
			Gensen = 35670 
		
		elif((572000<=Gensenkeisan)and(Gensenkeisan<575000)and(self.Fuyo==2)):
			Gensen = 29200 
		
		elif((572000<=Gensenkeisan)and(Gensenkeisan<575000)and(self.Fuyo==3)):
			Gensen = 22740 
		
		elif((572000<=Gensenkeisan)and(Gensenkeisan<575000)and(self.Fuyo==4)):
			Gensen = 18030 
		
		elif((572000<=Gensenkeisan)and(Gensenkeisan<575000)and(self.Fuyo==5)):
			Gensen = 14790 
		
		elif((572000<=Gensenkeisan)and(Gensenkeisan<575000)and(self.Fuyo==6)):
			Gensen = 11560 
		
		elif((572000<=Gensenkeisan)and(Gensenkeisan<575000)and(self.Fuyo==7)):
			Gensen = 8330 
		
		#191
		elif((575000<=Gensenkeisan)and(Gensenkeisan<578000)and(self.Fuyo==0)):
			Gensen = 42690 
		
		elif((575000<=Gensenkeisan)and(Gensenkeisan<578000)and(self.Fuyo==1)):
			Gensen = 36230 
		
		elif((575000<=Gensenkeisan)and(Gensenkeisan<578000)and(self.Fuyo==2)):
			Gensen = 29750 
		
		elif((575000<=Gensenkeisan)and(Gensenkeisan<578000)and(self.Fuyo==3)):
			Gensen = 23290 
		
		elif((575000<=Gensenkeisan)and(Gensenkeisan<578000)and(self.Fuyo==4)):
			Gensen = 18310 
		
		elif((575000<=Gensenkeisan)and(Gensenkeisan<578000)and(self.Fuyo==5)):
			Gensen = 15070 
		
		elif((575000<=Gensenkeisan)and(Gensenkeisan<578000)and(self.Fuyo==6)):
			Gensen = 11830 
		
		elif((575000<=Gensenkeisan)and(Gensenkeisan<578000)and(self.Fuyo==7)):
			Gensen = 8610 
		
		#192
		elif((578000<=Gensenkeisan)and(Gensenkeisan<581000)and(self.Fuyo==0)):
			Gensen = 43240 
		
		elif((578000<=Gensenkeisan)and(Gensenkeisan<581000)and(self.Fuyo==1)):
			Gensen = 36780 
		
		elif((578000<=Gensenkeisan)and(Gensenkeisan<581000)and(self.Fuyo==2)):
			Gensen = 30300 
		
		elif((578000<=Gensenkeisan)and(Gensenkeisan<581000)and(self.Fuyo==3)):
			Gensen = 23840 
		
		elif((578000<=Gensenkeisan)and(Gensenkeisan<581000)and(self.Fuyo==4)):
			Gensen = 18580 
		
		elif((578000<=Gensenkeisan)and(Gensenkeisan<581000)and(self.Fuyo==5)):
			Gensen = 15350 
		
		elif((578000<=Gensenkeisan)and(Gensenkeisan<581000)and(self.Fuyo==6)):
			Gensen = 12110 
		
		elif((578000<=Gensenkeisan)and(Gensenkeisan<581000)and(self.Fuyo==7)):
			Gensen = 8880 
		
		#193
		elif((581000<=Gensenkeisan)and(Gensenkeisan<584000)and(self.Fuyo==0)):
			Gensen = 43790 
		
		elif((581000<=Gensenkeisan)and(Gensenkeisan<584000)and(self.Fuyo==1)):
			Gensen = 37330 
		
		elif((581000<=Gensenkeisan)and(Gensenkeisan<584000)and(self.Fuyo==2)):
			Gensen = 30850 
		
		elif((581000<=Gensenkeisan)and(Gensenkeisan<584000)and(self.Fuyo==3)):
			Gensen = 24390 
		
		elif((581000<=Gensenkeisan)and(Gensenkeisan<584000)and(self.Fuyo==4)):
			Gensen = 18860 
		
		elif((581000<=Gensenkeisan)and(Gensenkeisan<584000)and(self.Fuyo==5)):
			Gensen = 15620 
		
		elif((581000<=Gensenkeisan)and(Gensenkeisan<584000)and(self.Fuyo==6)):
			Gensen = 12380 
		
		elif((581000<=Gensenkeisan)and(Gensenkeisan<584000)and(self.Fuyo==7)):
			Gensen = 9160 
		
		#194
		elif((584000<=Gensenkeisan)and(Gensenkeisan<587000)and(self.Fuyo==0)):
			Gensen = 44340 
		
		elif((584000<=Gensenkeisan)and(Gensenkeisan<587000)and(self.Fuyo==1)):
			Gensen = 37880 
		
		elif((584000<=Gensenkeisan)and(Gensenkeisan<587000)and(self.Fuyo==2)):
			Gensen = 31410 
		
		elif((584000<=Gensenkeisan)and(Gensenkeisan<587000)and(self.Fuyo==3)):
			Gensen = 24940 
		
		elif((584000<=Gensenkeisan)and(Gensenkeisan<587000)and(self.Fuyo==4)):
			Gensen = 19130 
		
		elif((584000<=Gensenkeisan)and(Gensenkeisan<587000)and(self.Fuyo==5)):
			Gensen = 15900 
		
		elif((584000<=Gensenkeisan)and(Gensenkeisan<587000)and(self.Fuyo==6)):
			Gensen = 12660 
		
		elif((584000<=Gensenkeisan)and(Gensenkeisan<587000)and(self.Fuyo==7)):
			Gensen = 9430 
		
		#195
		elif((587000<=Gensenkeisan)and(Gensenkeisan<590000)and(self.Fuyo==0)):
			Gensen = 44890 
		
		elif((587000<=Gensenkeisan)and(Gensenkeisan<590000)and(self.Fuyo==1)):
			Gensen = 38430 
		
		elif((587000<=Gensenkeisan)and(Gensenkeisan<590000)and(self.Fuyo==2)):
			Gensen = 31960 
		
		elif((587000<=Gensenkeisan)and(Gensenkeisan<590000)and(self.Fuyo==3)):
			Gensen = 25490 
		
		elif((587000<=Gensenkeisan)and(Gensenkeisan<590000)and(self.Fuyo==4)):
			Gensen = 19410 
		
		elif((587000<=Gensenkeisan)and(Gensenkeisan<590000)and(self.Fuyo==5)):
			Gensen = 16170 
		
		elif((587000<=Gensenkeisan)and(Gensenkeisan<590000)and(self.Fuyo==6)):
			Gensen = 12940 
		
		elif((587000<=Gensenkeisan)and(Gensenkeisan<590000)and(self.Fuyo==7)):
			Gensen = 9710 
		
		#196
		elif((590000<=Gensenkeisan)and(Gensenkeisan<593000)and(self.Fuyo==0)):
			Gensen = 45440 
		
		elif((590000<=Gensenkeisan)and(Gensenkeisan<593000)and(self.Fuyo==1)):
			Gensen = 38980 
		
		elif((590000<=Gensenkeisan)and(Gensenkeisan<593000)and(self.Fuyo==2)):
			Gensen = 32510 
		
		elif((590000<=Gensenkeisan)and(Gensenkeisan<593000)and(self.Fuyo==3)):
			Gensen = 26050 
		
		elif((590000<=Gensenkeisan)and(Gensenkeisan<593000)and(self.Fuyo==4)):
			Gensen = 19680 
		
		elif((590000<=Gensenkeisan)and(Gensenkeisan<593000)and(self.Fuyo==5)):
			Gensen = 16450 
		
		elif((590000<=Gensenkeisan)and(Gensenkeisan<593000)and(self.Fuyo==6)):
			Gensen = 13210 
		
		elif((590000<=Gensenkeisan)and(Gensenkeisan<593000)and(self.Fuyo==7)):
			Gensen = 9990 
		
		#197
		elif((593000<=Gensenkeisan)and(Gensenkeisan<596000)and(self.Fuyo==0)):
			Gensen = 46000 
		
		elif((593000<=Gensenkeisan)and(Gensenkeisan<596000)and(self.Fuyo==1)):
			Gensen = 39530 
		
		elif((593000<=Gensenkeisan)and(Gensenkeisan<596000)and(self.Fuyo==2)):
			Gensen = 33060 
		
		elif((593000<=Gensenkeisan)and(Gensenkeisan<596000)and(self.Fuyo==3)):
			Gensen = 26600 
		
		elif((593000<=Gensenkeisan)and(Gensenkeisan<596000)and(self.Fuyo==4)):
			Gensen = 20130 
		
		elif((593000<=Gensenkeisan)and(Gensenkeisan<596000)and(self.Fuyo==5)):
			Gensen = 16720 
		
		elif((593000<=Gensenkeisan)and(Gensenkeisan<596000)and(self.Fuyo==6)):
			Gensen = 13490 
		
		elif((593000<=Gensenkeisan)and(Gensenkeisan<596000)and(self.Fuyo==7)):
			Gensen = 10260 
		
		#198
		elif((596000<=Gensenkeisan)and(Gensenkeisan<599000)and(self.Fuyo==0)):
			Gensen = 46550 
		
		elif((596000<=Gensenkeisan)and(Gensenkeisan<599000)and(self.Fuyo==1)):
			Gensen = 40080 
		
		elif((596000<=Gensenkeisan)and(Gensenkeisan<599000)and(self.Fuyo==2)):
			Gensen = 33610 
		
		elif((596000<=Gensenkeisan)and(Gensenkeisan<599000)and(self.Fuyo==3)):
			Gensen = 27150 
		
		elif((596000<=Gensenkeisan)and(Gensenkeisan<599000)and(self.Fuyo==4)):
			Gensen = 20690 
		
		elif((596000<=Gensenkeisan)and(Gensenkeisan<599000)and(self.Fuyo==5)):
			Gensen = 17000 
		
		elif((596000<=Gensenkeisan)and(Gensenkeisan<599000)and(self.Fuyo==6)):
			Gensen = 13760 
		
		elif((596000<=Gensenkeisan)and(Gensenkeisan<599000)and(self.Fuyo==7)):
			Gensen = 10540 
		
		#199
		elif((599000<=Gensenkeisan)and(Gensenkeisan<602000)and(self.Fuyo==0)):
			Gensen = 47100 
		
		elif((599000<=Gensenkeisan)and(Gensenkeisan<602000)and(self.Fuyo==1)):
			Gensen = 40640 
		
		elif((599000<=Gensenkeisan)and(Gensenkeisan<602000)and(self.Fuyo==2)):
			Gensen = 34160 
		
		elif((599000<=Gensenkeisan)and(Gensenkeisan<602000)and(self.Fuyo==3)):
			Gensen = 27700 
		
		elif((599000<=Gensenkeisan)and(Gensenkeisan<602000)and(self.Fuyo==4)):
			Gensen = 21240 
		
		elif((599000<=Gensenkeisan)and(Gensenkeisan<602000)and(self.Fuyo==5)):
			Gensen = 17280 
		
		elif((599000<=Gensenkeisan)and(Gensenkeisan<602000)and(self.Fuyo==6)):
			Gensen = 14040 
		
		elif((599000<=Gensenkeisan)and(Gensenkeisan<602000)and(self.Fuyo==7)):
			Gensen = 10810
		
		#200
		elif((602000<=Gensenkeisan)and(Gensenkeisan<605000)and(self.Fuyo==0)):
			Gensen = 47650 
		
		elif((602000<=Gensenkeisan)and(Gensenkeisan<605000)and(self.Fuyo==1)):
			Gensen = 41190 
		
		elif((602000<=Gensenkeisan)and(Gensenkeisan<605000)and(self.Fuyo==2)):
			Gensen = 34710 
		
		elif((602000<=Gensenkeisan)and(Gensenkeisan<605000)and(self.Fuyo==3)):
			Gensen = 28250 
		
		elif((602000<=Gensenkeisan)and(Gensenkeisan<605000)and(self.Fuyo==4)):
			Gensen = 21790 
		
		elif((602000<=Gensenkeisan)and(Gensenkeisan<605000)and(self.Fuyo==5)):
			Gensen = 17550 
		
		elif((602000<=Gensenkeisan)and(Gensenkeisan<605000)and(self.Fuyo==6)):
			Gensen = 14310 
		
		elif((602000<=Gensenkeisan)and(Gensenkeisan<605000)and(self.Fuyo==7)):
			Gensen = 11090 
		
		#201
		elif((605000<=Gensenkeisan)and(Gensenkeisan<608000)and(self.Fuyo==0)):
			Gensen = 48200 
		
		elif((605000<=Gensenkeisan)and(Gensenkeisan<608000)and(self.Fuyo==1)):
			Gensen = 41740 
		
		elif((605000<=Gensenkeisan)and(Gensenkeisan<608000)and(self.Fuyo==2)):
			Gensen = 35270 
		
		elif((605000<=Gensenkeisan)and(Gensenkeisan<608000)and(self.Fuyo==3)):
			Gensen = 28800 
		
		elif((605000<=Gensenkeisan)and(Gensenkeisan<608000)and(self.Fuyo==4)):
			Gensen = 22340 
		
		elif((605000<=Gensenkeisan)and(Gensenkeisan<608000)and(self.Fuyo==5)):
			Gensen = 17830 
		
		elif((605000<=Gensenkeisan)and(Gensenkeisan<608000)and(self.Fuyo==6)):
			Gensen = 14590 
		
		elif((605000<=Gensenkeisan)and(Gensenkeisan<608000)and(self.Fuyo==7)):
			Gensen = 11360 
		
		#202
		elif((608000<=Gensenkeisan)and(Gensenkeisan<611000)and(self.Fuyo==0)):
			Gensen = 48750 
		
		elif((608000<=Gensenkeisan)and(Gensenkeisan<611000)and(self.Fuyo==1)):
			Gensen = 42290 
		
		elif((608000<=Gensenkeisan)and(Gensenkeisan<611000)and(self.Fuyo==2)):
			Gensen = 35820 
		
		elif((608000<=Gensenkeisan)and(Gensenkeisan<611000)and(self.Fuyo==3)):
			Gensen = 29350 
		
		elif((608000<=Gensenkeisan)and(Gensenkeisan<611000)and(self.Fuyo==4)):
			Gensen = 22890 
		
		elif((608000<=Gensenkeisan)and(Gensenkeisan<611000)and(self.Fuyo==5)):
			Gensen = 18100 
		
		elif((608000<=Gensenkeisan)and(Gensenkeisan<611000)and(self.Fuyo==6)):
			Gensen = 14870 
		
		elif((608000<=Gensenkeisan)and(Gensenkeisan<611000)and(self.Fuyo==7)):
			Gensen = 11640 
		
		#203
		elif((611000<=Gensenkeisan)and(Gensenkeisan<614000)and(self.Fuyo==0)):
			Gensen = 49300 
		
		elif((611000<=Gensenkeisan)and(Gensenkeisan<614000)and(self.Fuyo==1)):
			Gensen = 42840 
		
		elif((611000<=Gensenkeisan)and(Gensenkeisan<614000)and(self.Fuyo==2)):
			Gensen = 36370 
		
		elif((611000<=Gensenkeisan)and(Gensenkeisan<614000)and(self.Fuyo==3)):
			Gensen = 29910 
		
		elif((611000<=Gensenkeisan)and(Gensenkeisan<614000)and(self.Fuyo==4)):
			Gensen = 23440 
		
		elif((611000<=Gensenkeisan)and(Gensenkeisan<614000)and(self.Fuyo==5)):
			Gensen = 18380 
		
		elif((611000<=Gensenkeisan)and(Gensenkeisan<614000)and(self.Fuyo==6)):
			Gensen = 15140 
		
		elif((611000<=Gensenkeisan)and(Gensenkeisan<614000)and(self.Fuyo==7)):
			Gensen = 11920 
		
		#204
		elif((614000<=Gensenkeisan)and(Gensenkeisan<617000)and(self.Fuyo==0)):
			Gensen = 49860 
		
		elif((614000<=Gensenkeisan)and(Gensenkeisan<617000)and(self.Fuyo==1)):
			Gensen = 43390 
		
		elif((614000<=Gensenkeisan)and(Gensenkeisan<617000)and(self.Fuyo==2)):
			Gensen = 36920 
		
		elif((614000<=Gensenkeisan)and(Gensenkeisan<617000)and(self.Fuyo==3)):
			Gensen = 30460 
		
		elif((614000<=Gensenkeisan)and(Gensenkeisan<617000)and(self.Fuyo==4)):
			Gensen = 23990 
		
		elif((614000<=Gensenkeisan)and(Gensenkeisan<617000)and(self.Fuyo==5)):
			Gensen = 18650 
		
		elif((614000<=Gensenkeisan)and(Gensenkeisan<617000)and(self.Fuyo==6)):
			Gensen = 15420 
		
		elif((614000<=Gensenkeisan)and(Gensenkeisan<617000)and(self.Fuyo==7)):
			Gensen = 12190 
		
		#205
		elif((617000<=Gensenkeisan)and(Gensenkeisan<620000)and(self.Fuyo==0)):
			Gensen = 50410 
		
		elif((617000<=Gensenkeisan)and(Gensenkeisan<620000)and(self.Fuyo==1)):
			Gensen = 43940 
		
		elif((617000<=Gensenkeisan)and(Gensenkeisan<620000)and(self.Fuyo==2)):
			Gensen = 37470 
		
		elif((617000<=Gensenkeisan)and(Gensenkeisan<620000)and(self.Fuyo==3)):
			Gensen = 31010 
		
		elif((617000<=Gensenkeisan)and(Gensenkeisan<620000)and(self.Fuyo==4)):
			Gensen = 24540 
		
		elif((617000<=Gensenkeisan)and(Gensenkeisan<620000)and(self.Fuyo==5)):
			Gensen = 18930 
		
		elif((617000<=Gensenkeisan)and(Gensenkeisan<620000)and(self.Fuyo==6)):
			Gensen = 15690 
		
		elif((617000<=Gensenkeisan)and(Gensenkeisan<620000)and(self.Fuyo==7)):
			Gensen = 12470 
		
		#206
		elif((620000<=Gensenkeisan)and(Gensenkeisan<623000)and(self.Fuyo==0)):
			Gensen = 50960 
		
		elif((620000<=Gensenkeisan)and(Gensenkeisan<623000)and(self.Fuyo==1)):
			Gensen = 44500 
		
		elif((620000<=Gensenkeisan)and(Gensenkeisan<623000)and(self.Fuyo==2)):
			Gensen = 38020 
		
		elif((620000<=Gensenkeisan)and(Gensenkeisan<623000)and(self.Fuyo==3)):
			Gensen = 31560 
		
		elif((620000<=Gensenkeisan)and(Gensenkeisan<623000)and(self.Fuyo==4)):
			Gensen = 25100 
		
		elif((620000<=Gensenkeisan)and(Gensenkeisan<623000)and(self.Fuyo==5)):
			Gensen = 19210 
		
		elif((620000<=Gensenkeisan)and(Gensenkeisan<623000)and(self.Fuyo==6)):
			Gensen = 15970 
		
		elif((620000<=Gensenkeisan)and(Gensenkeisan<623000)and(self.Fuyo==7)):
			Gensen = 12740 
		
		#207
		elif((623000<=Gensenkeisan)and(Gensenkeisan<626000)and(self.Fuyo==0)):
			Gensen = 51510 
		
		elif((623000<=Gensenkeisan)and(Gensenkeisan<626000)and(self.Fuyo==1)):
			Gensen = 45050 
		
		elif((623000<=Gensenkeisan)and(Gensenkeisan<626000)and(self.Fuyo==2)):
			Gensen = 38570 
		
		elif((623000<=Gensenkeisan)and(Gensenkeisan<626000)and(self.Fuyo==3)):
			Gensen = 32110 
		
		elif((623000<=Gensenkeisan)and(Gensenkeisan<626000)and(self.Fuyo==4)):
			Gensen = 25650 
		
		elif((623000<=Gensenkeisan)and(Gensenkeisan<626000)and(self.Fuyo==5)):
			Gensen = 19480 
		
		elif((623000<=Gensenkeisan)and(Gensenkeisan<626000)and(self.Fuyo==6)):
			Gensen = 16240 
		
		elif((623000<=Gensenkeisan)and(Gensenkeisan<626000)and(self.Fuyo==7)):
			Gensen = 13020 
		
		#208
		elif((626000<=Gensenkeisan)and(Gensenkeisan<629000)and(self.Fuyo==0)):
			Gensen = 52060 
		
		elif((626000<=Gensenkeisan)and(Gensenkeisan<629000)and(self.Fuyo==1)):
			Gensen = 45600 
		
		elif((626000<=Gensenkeisan)and(Gensenkeisan<629000)and(self.Fuyo==2)):
			Gensen = 39120 
		
		elif((626000<=Gensenkeisan)and(Gensenkeisan<629000)and(self.Fuyo==3)):
			Gensen = 32660 
		
		elif((626000<=Gensenkeisan)and(Gensenkeisan<629000)and(self.Fuyo==4)):
			Gensen = 26200 
		
		elif((626000<=Gensenkeisan)and(Gensenkeisan<629000)and(self.Fuyo==5)):
			Gensen = 19760 
		
		elif((626000<=Gensenkeisan)and(Gensenkeisan<629000)and(self.Fuyo==6)):
			Gensen = 16520 
		
		elif((626000<=Gensenkeisan)and(Gensenkeisan<629000)and(self.Fuyo==7)):
			Gensen = 13290 
		
		#209
		elif((629000<=Gensenkeisan)and(Gensenkeisan<632000)and(self.Fuyo==0)):
			Gensen = 52610 
		
		elif((629000<=Gensenkeisan)and(Gensenkeisan<632000)and(self.Fuyo==1)):
			Gensen = 46150 
		
		elif((629000<=Gensenkeisan)and(Gensenkeisan<632000)and(self.Fuyo==2)):
			Gensen = 39680 
		
		elif((629000<=Gensenkeisan)and(Gensenkeisan<632000)and(self.Fuyo==3)):
			Gensen = 33210 
		
		elif((629000<=Gensenkeisan)and(Gensenkeisan<632000)and(self.Fuyo==4)):
			Gensen = 26750 
		
		elif((629000<=Gensenkeisan)and(Gensenkeisan<632000)and(self.Fuyo==5)):
			Gensen = 20280 
		
		elif((629000<=Gensenkeisan)and(Gensenkeisan<632000)and(self.Fuyo==6)):
			Gensen = 16800 
		
		elif((629000<=Gensenkeisan)and(Gensenkeisan<632000)and(self.Fuyo==7)):
			Gensen = 13570 
		
		#210
		elif((632000<=Gensenkeisan)and(Gensenkeisan<635000)and(self.Fuyo==0)):
			Gensen = 53160 
		
		elif((632000<=Gensenkeisan)and(Gensenkeisan<635000)and(self.Fuyo==1)):
			Gensen = 46700 
		
		elif((632000<=Gensenkeisan)and(Gensenkeisan<635000)and(self.Fuyo==2)):
			Gensen = 40230 
		
		elif((632000<=Gensenkeisan)and(Gensenkeisan<635000)and(self.Fuyo==3)):
			Gensen = 33760 
		
		elif((632000<=Gensenkeisan)and(Gensenkeisan<635000)and(self.Fuyo==4)):
			Gensen = 27300 
		
		elif((632000<=Gensenkeisan)and(Gensenkeisan<635000)and(self.Fuyo==5)):
			Gensen = 20830 
		
		elif((632000<=Gensenkeisan)and(Gensenkeisan<635000)and(self.Fuyo==6)):
			Gensen = 17070 
		
		elif((632000<=Gensenkeisan)and(Gensenkeisan<635000)and(self.Fuyo==7)):
			Gensen = 13840 
		
		#211
		elif((635000<=Gensenkeisan)and(Gensenkeisan<638000)and(self.Fuyo==0)):
			Gensen = 53710 
		
		elif((635000<=Gensenkeisan)and(Gensenkeisan<638000)and(self.Fuyo==1)):
			Gensen = 47250 
		
		elif((635000<=Gensenkeisan)and(Gensenkeisan<638000)and(self.Fuyo==2)):
			Gensen = 40780 
		
		elif((635000<=Gensenkeisan)and(Gensenkeisan<638000)and(self.Fuyo==3)):
			Gensen = 34320 
		
		elif((635000<=Gensenkeisan)and(Gensenkeisan<638000)and(self.Fuyo==4)):
			Gensen = 27850 
		
		elif((635000<=Gensenkeisan)and(Gensenkeisan<638000)and(self.Fuyo==5)):
			Gensen = 21380 
		
		elif((635000<=Gensenkeisan)and(Gensenkeisan<638000)and(self.Fuyo==6)):
			Gensen = 17350 
		
		elif((635000<=Gensenkeisan)and(Gensenkeisan<638000)and(self.Fuyo==7)):
			Gensen = 14120 
		
		#212
		elif((638000<=Gensenkeisan)and(Gensenkeisan<641000)and(self.Fuyo==0)):
			Gensen = 54270 
		
		elif((638000<=Gensenkeisan)and(Gensenkeisan<641000)and(self.Fuyo==1)):
			Gensen = 47800 
		
		elif((638000<=Gensenkeisan)and(Gensenkeisan<641000)and(self.Fuyo==2)):
			Gensen = 41330 
		
		elif((638000<=Gensenkeisan)and(Gensenkeisan<641000)and(self.Fuyo==3)):
			Gensen = 34870 
		
		elif((638000<=Gensenkeisan)and(Gensenkeisan<641000)and(self.Fuyo==4)):
			Gensen = 28400 
		
		elif((638000<=Gensenkeisan)and(Gensenkeisan<641000)and(self.Fuyo==5)):
			Gensen = 21930 
		
		elif((638000<=Gensenkeisan)and(Gensenkeisan<641000)and(self.Fuyo==6)):
			Gensen = 17620 
		
		elif((638000<=Gensenkeisan)and(Gensenkeisan<641000)and(self.Fuyo==7)):
			Gensen = 14400 
		
		#213
		elif((641000<=Gensenkeisan)and(Gensenkeisan<644000)and(self.Fuyo==0)):
			Gensen = 54820 
		
		elif((641000<=Gensenkeisan)and(Gensenkeisan<644000)and(self.Fuyo==1)):
			Gensen = 48350 
		
		elif((641000<=Gensenkeisan)and(Gensenkeisan<644000)and(self.Fuyo==2)):
			Gensen = 41880 
		
		elif((641000<=Gensenkeisan)and(Gensenkeisan<644000)and(self.Fuyo==3)):
			Gensen = 35420 
		
		elif((641000<=Gensenkeisan)and(Gensenkeisan<644000)and(self.Fuyo==4)):
			Gensen = 28960 
		
		elif((641000<=Gensenkeisan)and(Gensenkeisan<644000)and(self.Fuyo==5)):
			Gensen = 22480 
		
		elif((641000<=Gensenkeisan)and(Gensenkeisan<644000)and(self.Fuyo==6)):
			Gensen = 17900 
		
		elif((641000<=Gensenkeisan)and(Gensenkeisan<644000)and(self.Fuyo==7)):
			Gensen = 14670 
		
		#214
		elif((644000<=Gensenkeisan)and(Gensenkeisan<647000)and(self.Fuyo==0)):
			Gensen = 55370 
		
		elif((644000<=Gensenkeisan)and(Gensenkeisan<647000)and(self.Fuyo==1)):
			Gensen = 48910 
		
		elif((644000<=Gensenkeisan)and(Gensenkeisan<647000)and(self.Fuyo==2)):
			Gensen = 42430 
		
		elif((644000<=Gensenkeisan)and(Gensenkeisan<647000)and(self.Fuyo==3)):
			Gensen = 35970 
		
		elif((644000<=Gensenkeisan)and(Gensenkeisan<647000)and(self.Fuyo==4)):
			Gensen = 29510 
		
		elif((644000<=Gensenkeisan)and(Gensenkeisan<647000)and(self.Fuyo==5)):
			Gensen = 23030 
		
		elif((644000<=Gensenkeisan)and(Gensenkeisan<647000)and(self.Fuyo==6)):
			Gensen = 18170 
		
		elif((644000<=Gensenkeisan)and(Gensenkeisan<647000)and(self.Fuyo==7)):
			Gensen = 14950 
		
		#215
		elif((647000<=Gensenkeisan)and(Gensenkeisan<650000)and(self.Fuyo==0)):
			Gensen = 55920 
		
		elif((647000<=Gensenkeisan)and(Gensenkeisan<650000)and(self.Fuyo==1)):
			Gensen = 49460 
		
		elif((647000<=Gensenkeisan)and(Gensenkeisan<650000)and(self.Fuyo==2)):
			Gensen = 42980 
		
		elif((647000<=Gensenkeisan)and(Gensenkeisan<650000)and(self.Fuyo==3)):
			Gensen = 36520 
		
		elif((647000<=Gensenkeisan)and(Gensenkeisan<650000)and(self.Fuyo==4)):
			Gensen = 30060 
		
		elif((647000<=Gensenkeisan)and(Gensenkeisan<650000)and(self.Fuyo==5)):
			Gensen = 23590 
		
		elif((647000<=Gensenkeisan)and(Gensenkeisan<650000)and(self.Fuyo==6)):
			Gensen = 18450 
		
		elif((647000<=Gensenkeisan)and(Gensenkeisan<650000)and(self.Fuyo==7)):
			Gensen = 15220 
		
		#216
		elif((650000<=Gensenkeisan)and(Gensenkeisan<653000)and(self.Fuyo==0)):
			Gensen = 56470 
		
		elif((650000<=Gensenkeisan)and(Gensenkeisan<653000)and(self.Fuyo==1)):
			Gensen = 50010 
		
		elif((650000<=Gensenkeisan)and(Gensenkeisan<653000)and(self.Fuyo==2)):
			Gensen = 43540 
		
		elif((650000<=Gensenkeisan)and(Gensenkeisan<653000)and(self.Fuyo==3)):
			Gensen = 37070 
		
		elif((650000<=Gensenkeisan)and(Gensenkeisan<653000)and(self.Fuyo==4)):
			Gensen = 30610 
		
		elif((650000<=Gensenkeisan)and(Gensenkeisan<653000)and(self.Fuyo==5)):
			Gensen = 24140 
		
		elif((650000<=Gensenkeisan)and(Gensenkeisan<653000)and(self.Fuyo==6)):
			Gensen = 18730 
		
		elif((650000<=Gensenkeisan)and(Gensenkeisan<653000)and(self.Fuyo==7)):
			Gensen = 15500 
		
		#217
		elif((653000<=Gensenkeisan)and(Gensenkeisan<656000)and(self.Fuyo==0)):
			Gensen = 57020 
		
		elif((653000<=Gensenkeisan)and(Gensenkeisan<656000)and(self.Fuyo==1)):
			Gensen = 50560 
		
		elif((653000<=Gensenkeisan)and(Gensenkeisan<656000)and(self.Fuyo==2)):
			Gensen = 44090 
		
		elif((653000<=Gensenkeisan)and(Gensenkeisan<656000)and(self.Fuyo==3)):
			Gensen = 37620 
		
		elif((653000<=Gensenkeisan)and(Gensenkeisan<656000)and(self.Fuyo==4)):
			Gensen = 31160 
		
		elif((653000<=Gensenkeisan)and(Gensenkeisan<656000)and(self.Fuyo==5)):
			Gensen = 24690 
		
		elif((653000<=Gensenkeisan)and(Gensenkeisan<656000)and(self.Fuyo==6)):
			Gensen = 19000 
		
		elif((653000<=Gensenkeisan)and(Gensenkeisan<656000)and(self.Fuyo==7)):
			Gensen = 15770 
		
		#218
		elif((656000<=Gensenkeisan)and(Gensenkeisan<659000)and(self.Fuyo==0)):
			Gensen = 57570 
		
		elif((656000<=Gensenkeisan)and(Gensenkeisan<659000)and(self.Fuyo==1)):
			Gensen = 51110 
		
		elif((656000<=Gensenkeisan)and(Gensenkeisan<659000)and(self.Fuyo==2)):
			Gensen = 44640 
		
		elif((656000<=Gensenkeisan)and(Gensenkeisan<659000)and(self.Fuyo==3)):
			Gensen = 38180 
		
		elif((656000<=Gensenkeisan)and(Gensenkeisan<659000)and(self.Fuyo==4)):
			Gensen = 31710 
		
		elif((656000<=Gensenkeisan)and(Gensenkeisan<659000)and(self.Fuyo==5)):
			Gensen = 25240 
		
		elif((656000<=Gensenkeisan)and(Gensenkeisan<659000)and(self.Fuyo==6)):
			Gensen = 19280 
		
		elif((656000<=Gensenkeisan)and(Gensenkeisan<659000)and(self.Fuyo==7)):
			Gensen = 16050 
		
		#219
		elif((659000<=Gensenkeisan)and(Gensenkeisan<662000)and(self.Fuyo==0)):
			Gensen = 58130 
		
		elif((659000<=Gensenkeisan)and(Gensenkeisan<662000)and(self.Fuyo==1)):
			Gensen = 51660 
		
		elif((659000<=Gensenkeisan)and(Gensenkeisan<662000)and(self.Fuyo==2)):
			Gensen = 45190 
		
		elif((659000<=Gensenkeisan)and(Gensenkeisan<662000)and(self.Fuyo==3)):
			Gensen = 38730 
		
		elif((659000<=Gensenkeisan)and(Gensenkeisan<662000)and(self.Fuyo==4)):
			Gensen = 32260 
		
		elif((659000<=Gensenkeisan)and(Gensenkeisan<662000)and(self.Fuyo==5)):
			Gensen = 25790 
		
		elif((659000<=Gensenkeisan)and(Gensenkeisan<662000)and(self.Fuyo==6)):
			Gensen = 19550 
		
		elif((659000<=Gensenkeisan)and(Gensenkeisan<662000)and(self.Fuyo==7)):
			Gensen = 16330 
		
		#220
		elif((662000<=Gensenkeisan)and(Gensenkeisan<665000)and(self.Fuyo==0)):
			Gensen = 58680 
		
		elif((662000<=Gensenkeisan)and(Gensenkeisan<665000)and(self.Fuyo==1)):
			Gensen = 52210 
		
		elif((662000<=Gensenkeisan)and(Gensenkeisan<665000)and(self.Fuyo==2)):
			Gensen = 45740 
		
		elif((662000<=Gensenkeisan)and(Gensenkeisan<665000)and(self.Fuyo==3)):
			Gensen = 39280 
		
		elif((662000<=Gensenkeisan)and(Gensenkeisan<665000)and(self.Fuyo==4)):
			Gensen = 32810 
		
		elif((662000<=Gensenkeisan)and(Gensenkeisan<665000)and(self.Fuyo==5)):
			Gensen = 26340 
		
		elif((662000<=Gensenkeisan)and(Gensenkeisan<665000)and(self.Fuyo==6)):
			Gensen = 19880 
		
		elif((662000<=Gensenkeisan)and(Gensenkeisan<665000)and(self.Fuyo==7)):
			Gensen = 16600 
		
		#221
		elif((665000<=Gensenkeisan)and(Gensenkeisan<668000)and(self.Fuyo==0)):
			Gensen = 59230 
		
		elif((665000<=Gensenkeisan)and(Gensenkeisan<668000)and(self.Fuyo==1)):
			Gensen = 52770 
		
		elif((665000<=Gensenkeisan)and(Gensenkeisan<668000)and(self.Fuyo==2)):
			Gensen = 46290 
		
		elif((665000<=Gensenkeisan)and(Gensenkeisan<668000)and(self.Fuyo==3)):
			Gensen = 39830 
		
		elif((665000<=Gensenkeisan)and(Gensenkeisan<668000)and(self.Fuyo==4)):
			Gensen = 33370 
		
		elif((665000<=Gensenkeisan)and(Gensenkeisan<668000)and(self.Fuyo==5)):
			Gensen = 26890 
		
		elif((665000<=Gensenkeisan)and(Gensenkeisan<668000)and(self.Fuyo==6)):
			Gensen = 20430 
		
		elif((665000<=Gensenkeisan)and(Gensenkeisan<668000)and(self.Fuyo==7)):
			Gensen = 16880 
		
		#222
		elif((668000<=Gensenkeisan)and(Gensenkeisan<671000)and(self.Fuyo==0)):
			Gensen = 59780 
		
		elif((668000<=Gensenkeisan)and(Gensenkeisan<671000)and(self.Fuyo==1)):
			Gensen = 53320 
		
		elif((668000<=Gensenkeisan)and(Gensenkeisan<671000)and(self.Fuyo==2)):
			Gensen = 46840 
		
		elif((668000<=Gensenkeisan)and(Gensenkeisan<671000)and(self.Fuyo==3)):
			Gensen = 40380 
		
		elif((668000<=Gensenkeisan)and(Gensenkeisan<671000)and(self.Fuyo==4)):
			Gensen = 33920 
		
		elif((668000<=Gensenkeisan)and(Gensenkeisan<671000)and(self.Fuyo==5)):
			Gensen = 27440 
		
		elif((668000<=Gensenkeisan)and(Gensenkeisan<671000)and(self.Fuyo==6)):
			Gensen = 20980 
		
		elif((668000<=Gensenkeisan)and(Gensenkeisan<671000)and(self.Fuyo==7)):
			Gensen = 17150 
		
		#223
		elif((671000<=Gensenkeisan)and(Gensenkeisan<674000)and(self.Fuyo==0)):
			Gensen = 60330 
		
		elif((671000<=Gensenkeisan)and(Gensenkeisan<674000)and(self.Fuyo==1)):
			Gensen = 53870 
		
		elif((671000<=Gensenkeisan)and(Gensenkeisan<674000)and(self.Fuyo==2)):
			Gensen = 47390 
		
		elif((671000<=Gensenkeisan)and(Gensenkeisan<674000)and(self.Fuyo==3)):
			Gensen = 40930 
		
		elif((671000<=Gensenkeisan)and(Gensenkeisan<674000)and(self.Fuyo==4)):
			Gensen = 34470 
		
		elif((671000<=Gensenkeisan)and(Gensenkeisan<674000)and(self.Fuyo==5)):
			Gensen = 28000 
		
		elif((671000<=Gensenkeisan)and(Gensenkeisan<674000)and(self.Fuyo==6)):
			Gensen = 21530 
		
		elif((671000<=Gensenkeisan)and(Gensenkeisan<674000)and(self.Fuyo==7)):
			Gensen = 17430 
		
		#224
		elif((674000<=Gensenkeisan)and(Gensenkeisan<677000)and(self.Fuyo==0)):
			Gensen = 60880 
		
		elif((674000<=Gensenkeisan)and(Gensenkeisan<677000)and(self.Fuyo==1)):
			Gensen = 54420 
		
		elif((674000<=Gensenkeisan)and(Gensenkeisan<677000)and(self.Fuyo==2)):
			Gensen = 47950 
		
		elif((674000<=Gensenkeisan)and(Gensenkeisan<677000)and(self.Fuyo==3)):
			Gensen = 41480 
		
		elif((674000<=Gensenkeisan)and(Gensenkeisan<677000)and(self.Fuyo==4)):
			Gensen = 35020 
		
		elif((674000<=Gensenkeisan)and(Gensenkeisan<677000)and(self.Fuyo==5)):
			Gensen = 28550 
		
		elif((674000<=Gensenkeisan)and(Gensenkeisan<677000)and(self.Fuyo==6)):
			Gensen = 22080 
		
		elif((674000<=Gensenkeisan)and(Gensenkeisan<677000)and(self.Fuyo==7)):
			Gensen = 17700 
		
		#225
		elif((677000<=Gensenkeisan)and(Gensenkeisan<680000)and(self.Fuyo==0)):
			Gensen = 61430 
		
		elif((677000<=Gensenkeisan)and(Gensenkeisan<680000)and(self.Fuyo==1)):
			Gensen = 54970 
		
		elif((677000<=Gensenkeisan)and(Gensenkeisan<680000)and(self.Fuyo==2)):
			Gensen = 48500 
		
		elif((677000<=Gensenkeisan)and(Gensenkeisan<680000)and(self.Fuyo==3)):
			Gensen = 42030 
		
		elif((677000<=Gensenkeisan)and(Gensenkeisan<680000)and(self.Fuyo==4)):
			Gensen = 35570 
		
		elif((677000<=Gensenkeisan)and(Gensenkeisan<680000)and(self.Fuyo==5)):
			Gensen = 29100 
		
		elif((677000<=Gensenkeisan)and(Gensenkeisan<680000)and(self.Fuyo==6)):
			Gensen = 22640 
		
		elif((677000<=Gensenkeisan)and(Gensenkeisan<680000)and(self.Fuyo==7)):
			Gensen = 17980 
		
		#226
		elif((680000<=Gensenkeisan)and(Gensenkeisan<683000)and(self.Fuyo==0)):
			Gensen = 61980 
		
		elif((680000<=Gensenkeisan)and(Gensenkeisan<683000)and(self.Fuyo==1)):
			Gensen = 55520 
		
		elif((680000<=Gensenkeisan)and(Gensenkeisan<683000)and(self.Fuyo==2)):
			Gensen = 49050 
		
		elif((680000<=Gensenkeisan)and(Gensenkeisan<683000)and(self.Fuyo==3)):
			Gensen = 42590 
		
		elif((680000<=Gensenkeisan)and(Gensenkeisan<683000)and(self.Fuyo==4)):
			Gensen = 36120 
		
		elif((680000<=Gensenkeisan)and(Gensenkeisan<683000)and(self.Fuyo==5)):
			Gensen = 29650 
		
		elif((680000<=Gensenkeisan)and(Gensenkeisan<683000)and(self.Fuyo==6)):
			Gensen = 23190 
		
		elif((680000<=Gensenkeisan)and(Gensenkeisan<683000)and(self.Fuyo==7)):
			Gensen = 18260 
		
		#227
		elif((683000<=Gensenkeisan)and(Gensenkeisan<686000)and(self.Fuyo==0)):
			Gensen = 62540 
		
		elif((683000<=Gensenkeisan)and(Gensenkeisan<686000)and(self.Fuyo==1)):
			Gensen = 56070 
		
		elif((683000<=Gensenkeisan)and(Gensenkeisan<686000)and(self.Fuyo==2)):
			Gensen = 49600 
		
		elif((683000<=Gensenkeisan)and(Gensenkeisan<686000)and(self.Fuyo==3)):
			Gensen = 43140 
		
		elif((683000<=Gensenkeisan)and(Gensenkeisan<686000)and(self.Fuyo==4)):
			Gensen = 36670 
		
		elif((683000<=Gensenkeisan)and(Gensenkeisan<686000)and(self.Fuyo==5)):
			Gensen = 30200 
		
		elif((683000<=Gensenkeisan)and(Gensenkeisan<686000)and(self.Fuyo==6)):
			Gensen = 23740 
		
		elif((683000<=Gensenkeisan)and(Gensenkeisan<686000)and(self.Fuyo==7)):
			Gensen = 18530 
		
		#228
		elif((686000<=Gensenkeisan)and(Gensenkeisan<689000)and(self.Fuyo==0)):
			Gensen = 63090 
		
		elif((686000<=Gensenkeisan)and(Gensenkeisan<689000)and(self.Fuyo==1)):
			Gensen = 56620 
		
		elif((686000<=Gensenkeisan)and(Gensenkeisan<689000)and(self.Fuyo==2)):
			Gensen = 50150 
		
		elif((686000<=Gensenkeisan)and(Gensenkeisan<689000)and(self.Fuyo==3)):
			Gensen = 43690 
		
		elif((686000<=Gensenkeisan)and(Gensenkeisan<689000)and(self.Fuyo==4)):
			Gensen = 37230 
		
		elif((686000<=Gensenkeisan)and(Gensenkeisan<689000)and(self.Fuyo==5)):
			Gensen = 30750 
		
		elif((686000<=Gensenkeisan)and(Gensenkeisan<689000)and(self.Fuyo==6)):
			Gensen = 24290 
		
		elif((686000<=Gensenkeisan)and(Gensenkeisan<689000)and(self.Fuyo==7)):
			Gensen = 18810 
		
		#229
		elif((689000<=Gensenkeisan)and(Gensenkeisan<692000)and(self.Fuyo==0)):
			Gensen = 63640 
		
		elif((689000<=Gensenkeisan)and(Gensenkeisan<692000)and(self.Fuyo==1)):
			Gensen = 57180 
		
		elif((689000<=Gensenkeisan)and(Gensenkeisan<692000)and(self.Fuyo==2)):
			Gensen = 50700 
		
		elif((689000<=Gensenkeisan)and(Gensenkeisan<692000)and(self.Fuyo==3)):
			Gensen = 44240 
		
		elif((689000<=Gensenkeisan)and(Gensenkeisan<692000)and(self.Fuyo==4)):
			Gensen = 37780 
		
		elif((689000<=Gensenkeisan)and(Gensenkeisan<692000)and(self.Fuyo==5)):
			Gensen = 31300 
		
		elif((689000<=Gensenkeisan)and(Gensenkeisan<692000)and(self.Fuyo==6)):
			Gensen = 24840 
		
		elif((689000<=Gensenkeisan)and(Gensenkeisan<692000)and(self.Fuyo==7)):
			Gensen = 19080 
		
		#230
		elif((692000<=Gensenkeisan)and(Gensenkeisan<695000)and(self.Fuyo==0)):
			Gensen = 64190 
		
		elif((692000<=Gensenkeisan)and(Gensenkeisan<695000)and(self.Fuyo==1)):
			Gensen = 57730 
		
		elif((692000<=Gensenkeisan)and(Gensenkeisan<695000)and(self.Fuyo==2)):
			Gensen = 51250 
		
		elif((692000<=Gensenkeisan)and(Gensenkeisan<695000)and(self.Fuyo==3)):
			Gensen = 44790 
		
		elif((692000<=Gensenkeisan)and(Gensenkeisan<695000)and(self.Fuyo==4)):
			Gensen = 38330 
		
		elif((692000<=Gensenkeisan)and(Gensenkeisan<695000)and(self.Fuyo==5)):
			Gensen = 31860 
		
		elif((692000<=Gensenkeisan)and(Gensenkeisan<695000)and(self.Fuyo==6)):
			Gensen = 25390 
		
		elif((692000<=Gensenkeisan)and(Gensenkeisan<695000)and(self.Fuyo==7)):
			Gensen = 19360 
		
		#231
		elif((695000<=Gensenkeisan)and(Gensenkeisan<698000)and(self.Fuyo==0)):
			Gensen = 64740 
		
		elif((695000<=Gensenkeisan)and(Gensenkeisan<698000)and(self.Fuyo==1)):
			Gensen = 58280 
		
		elif((695000<=Gensenkeisan)and(Gensenkeisan<698000)and(self.Fuyo==2)):
			Gensen = 51810 
		
		elif((695000<=Gensenkeisan)and(Gensenkeisan<698000)and(self.Fuyo==3)):
			Gensen = 45340 
		
		elif((695000<=Gensenkeisan)and(Gensenkeisan<698000)and(self.Fuyo==4)):
			Gensen = 38880 
		
		elif((695000<=Gensenkeisan)and(Gensenkeisan<698000)and(self.Fuyo==5)):
			Gensen = 32410 
		
		elif((695000<=Gensenkeisan)and(Gensenkeisan<698000)and(self.Fuyo==6)):
			Gensen = 25940 
		
		elif((695000<=Gensenkeisan)and(Gensenkeisan<698000)and(self.Fuyo==7)):
			Gensen = 19630 
		
		#232
		elif((698000<=Gensenkeisan)and(Gensenkeisan<701000)and(self.Fuyo==0)):
			Gensen = 65290 
		
		elif((698000<=Gensenkeisan)and(Gensenkeisan<701000)and(self.Fuyo==1)):
			Gensen = 58830 
		
		elif((698000<=Gensenkeisan)and(Gensenkeisan<701000)and(self.Fuyo==2)):
			Gensen = 52360 
		
		elif((698000<=Gensenkeisan)and(Gensenkeisan<701000)and(self.Fuyo==3)):
			Gensen = 45890 
		
		elif((698000<=Gensenkeisan)and(Gensenkeisan<701000)and(self.Fuyo==4)):
			Gensen = 39430 
		
		elif((698000<=Gensenkeisan)and(Gensenkeisan<701000)and(self.Fuyo==5)):
			Gensen = 32960 
		
		elif((698000<=Gensenkeisan)and(Gensenkeisan<701000)and(self.Fuyo==6)):
			Gensen = 26490 
		
		elif((698000<=Gensenkeisan)and(Gensenkeisan<701000)and(self.Fuyo==7)):
			Gensen = 20030 
		
		#233
		elif((701000<=Gensenkeisan)and(Gensenkeisan<704000)and(self.Fuyo==0)):
			Gensen = 65840 
		
		elif((701000<=Gensenkeisan)and(Gensenkeisan<704000)and(self.Fuyo==1)):
			Gensen = 59380 
		
		elif((701000<=Gensenkeisan)and(Gensenkeisan<704000)and(self.Fuyo==2)):
			Gensen = 52910 
		
		elif((701000<=Gensenkeisan)and(Gensenkeisan<704000)and(self.Fuyo==3)):
			Gensen = 46450 
		
		elif((701000<=Gensenkeisan)and(Gensenkeisan<704000)and(self.Fuyo==4)):
			Gensen = 39980 
		
		elif((701000<=Gensenkeisan)and(Gensenkeisan<704000)and(self.Fuyo==5)):
			Gensen = 33510 
		
		elif((701000<=Gensenkeisan)and(Gensenkeisan<704000)and(self.Fuyo==6)):
			Gensen = 27050 
		
		elif((701000<=Gensenkeisan)and(Gensenkeisan<704000)and(self.Fuyo==7)):
			Gensen = 20580 
		
		#234
		elif((704000<=Gensenkeisan)and(Gensenkeisan<707000)and(self.Fuyo==0)):
			Gensen = 66400 
		
		elif((704000<=Gensenkeisan)and(Gensenkeisan<707000)and(self.Fuyo==1)):
			Gensen = 59930 
		
		elif((704000<=Gensenkeisan)and(Gensenkeisan<707000)and(self.Fuyo==2)):
			Gensen = 53460 
		
		elif((704000<=Gensenkeisan)and(Gensenkeisan<707000)and(self.Fuyo==3)):
			Gensen = 47000 
		
		elif((704000<=Gensenkeisan)and(Gensenkeisan<707000)and(self.Fuyo==4)):
			Gensen = 40530 
		
		elif((704000<=Gensenkeisan)and(Gensenkeisan<707000)and(self.Fuyo==5)):
			Gensen = 34060 
		
		elif((704000<=Gensenkeisan)and(Gensenkeisan<707000)and(self.Fuyo==6)):
			Gensen = 27600 
		
		elif((704000<=Gensenkeisan)and(Gensenkeisan<707000)and(self.Fuyo==7)):
			Gensen = 21130 
		
		#235
		elif((707000<=Gensenkeisan)and(Gensenkeisan<710000)and(self.Fuyo==0)):
			Gensen = 66960 
		
		elif((707000<=Gensenkeisan)and(Gensenkeisan<710000)and(self.Fuyo==1)):
			Gensen = 60480 
		
		elif((707000<=Gensenkeisan)and(Gensenkeisan<710000)and(self.Fuyo==2)):
			Gensen = 54020 
		
		elif((707000<=Gensenkeisan)and(Gensenkeisan<710000)and(self.Fuyo==3)):
			Gensen = 47550 
		
		elif((707000<=Gensenkeisan)and(Gensenkeisan<710000)and(self.Fuyo==4)):
			Gensen = 41090 
		
		elif((707000<=Gensenkeisan)and(Gensenkeisan<710000)and(self.Fuyo==5)):
			Gensen = 34620 
		
		elif((707000<=Gensenkeisan)and(Gensenkeisan<710000)and(self.Fuyo==6)):
			Gensen = 28150 
		
		elif((707000<=Gensenkeisan)and(Gensenkeisan<710000)and(self.Fuyo==7)):
			Gensen = 21690 
		
		#236
		elif((710000<=Gensenkeisan)and(Gensenkeisan<713000)and(self.Fuyo==0)):
			Gensen = 67570 
		
		elif((710000<=Gensenkeisan)and(Gensenkeisan<713000)and(self.Fuyo==1)):
			Gensen = 61100 
		
		elif((710000<=Gensenkeisan)and(Gensenkeisan<713000)and(self.Fuyo==2)):
			Gensen = 54630 
		
		elif((710000<=Gensenkeisan)and(Gensenkeisan<713000)and(self.Fuyo==3)):
			Gensen = 48160 
		
		elif((710000<=Gensenkeisan)and(Gensenkeisan<713000)and(self.Fuyo==4)):
			Gensen = 41700 
		
		elif((710000<=Gensenkeisan)and(Gensenkeisan<713000)and(self.Fuyo==5)):
			Gensen = 35230 
		
		elif((710000<=Gensenkeisan)and(Gensenkeisan<713000)and(self.Fuyo==6)):
			Gensen = 28760 
		
		elif((710000<=Gensenkeisan)and(Gensenkeisan<713000)and(self.Fuyo==7)):
			Gensen = 22300 
		
		#237
		elif((713000<=Gensenkeisan)and(Gensenkeisan<716000)and(self.Fuyo==0)):
			Gensen = 68180 
		
		elif((713000<=Gensenkeisan)and(Gensenkeisan<716000)and(self.Fuyo==1)):
			Gensen = 61710 
		
		elif((713000<=Gensenkeisan)and(Gensenkeisan<716000)and(self.Fuyo==2)):
			Gensen = 55250 
		
		elif((713000<=Gensenkeisan)and(Gensenkeisan<716000)and(self.Fuyo==3)):
			Gensen = 48770 
		
		elif((713000<=Gensenkeisan)and(Gensenkeisan<716000)and(self.Fuyo==4)):
			Gensen = 42310 
		
		elif((713000<=Gensenkeisan)and(Gensenkeisan<716000)and(self.Fuyo==5)):
			Gensen = 35850 
		
		elif((713000<=Gensenkeisan)and(Gensenkeisan<716000)and(self.Fuyo==6)):
			Gensen = 29370 
		
		elif((713000<=Gensenkeisan)and(Gensenkeisan<716000)and(self.Fuyo==7)):
			Gensen = 22910 
		
		#238
		elif((716000<=Gensenkeisan)and(Gensenkeisan<719000)and(self.Fuyo==0)):
			Gensen = 68790 
		
		elif((716000<=Gensenkeisan)and(Gensenkeisan<719000)and(self.Fuyo==1)):
			Gensen = 62320 
		
		elif((716000<=Gensenkeisan)and(Gensenkeisan<719000)and(self.Fuyo==2)):
			Gensen = 55860 
		
		elif((716000<=Gensenkeisan)and(Gensenkeisan<719000)and(self.Fuyo==3)):
			Gensen = 49390 
		
		elif((716000<=Gensenkeisan)and(Gensenkeisan<719000)and(self.Fuyo==4)):
			Gensen = 42920 
		
		elif((716000<=Gensenkeisan)and(Gensenkeisan<719000)and(self.Fuyo==5)):
			Gensen = 36460 
		
		elif((716000<=Gensenkeisan)and(Gensenkeisan<719000)and(self.Fuyo==6)):
			Gensen = 29990 
		
		elif((716000<=Gensenkeisan)and(Gensenkeisan<719000)and(self.Fuyo==7)):
			Gensen = 23520 
		
		#239
		elif((719000<=Gensenkeisan)and(Gensenkeisan<722000)and(self.Fuyo==0)):
			Gensen = 69410 
		
		elif((719000<=Gensenkeisan)and(Gensenkeisan<722000)and(self.Fuyo==1)):
			Gensen = 62930 
		
		elif((719000<=Gensenkeisan)and(Gensenkeisan<722000)and(self.Fuyo==2)):
			Gensen = 56470 
		
		elif((719000<=Gensenkeisan)and(Gensenkeisan<722000)and(self.Fuyo==3)):
			Gensen = 50000 
		
		elif((719000<=Gensenkeisan)and(Gensenkeisan<722000)and(self.Fuyo==4)):
			Gensen = 43540 
		
		elif((719000<=Gensenkeisan)and(Gensenkeisan<722000)and(self.Fuyo==5)):
			Gensen = 37070 
		
		elif((719000<=Gensenkeisan)and(Gensenkeisan<722000)and(self.Fuyo==6)):
			Gensen = 30600 
		
		elif((719000<=Gensenkeisan)and(Gensenkeisan<722000)and(self.Fuyo==7)):
			Gensen = 24140 
		
		#240
		elif((722000<=Gensenkeisan)and(Gensenkeisan<725000)and(self.Fuyo==0)):
			Gensen = 70020 
		
		elif((722000<=Gensenkeisan)and(Gensenkeisan<725000)and(self.Fuyo==1)):
			Gensen = 63550 
		
		elif((722000<=Gensenkeisan)and(Gensenkeisan<725000)and(self.Fuyo==2)):
			Gensen = 57080 
		
		elif((722000<=Gensenkeisan)and(Gensenkeisan<725000)and(self.Fuyo==3)):
			Gensen = 50610 
		
		elif((722000<=Gensenkeisan)and(Gensenkeisan<725000)and(self.Fuyo==4)):
			Gensen = 44150 
		
		elif((722000<=Gensenkeisan)and(Gensenkeisan<725000)and(self.Fuyo==5)):
			Gensen = 37690 
		
		elif((722000<=Gensenkeisan)and(Gensenkeisan<725000)and(self.Fuyo==6)):
			Gensen = 31210 
		
		elif((722000<=Gensenkeisan)and(Gensenkeisan<725000)and(self.Fuyo==7)):
			Gensen = 24750 
		
		#241
		elif((725000<=Gensenkeisan)and(Gensenkeisan<728000)and(self.Fuyo==0)):
			Gensen = 70630 
		
		elif((725000<=Gensenkeisan)and(Gensenkeisan<728000)and(self.Fuyo==1)):
			Gensen = 64160 
		
		elif((725000<=Gensenkeisan)and(Gensenkeisan<728000)and(self.Fuyo==2)):
			Gensen = 57700 
		
		elif((725000<=Gensenkeisan)and(Gensenkeisan<728000)and(self.Fuyo==3)):
			Gensen = 51220 
		
		elif((725000<=Gensenkeisan)and(Gensenkeisan<728000)and(self.Fuyo==4)):
			Gensen = 44760 
		
		elif((725000<=Gensenkeisan)and(Gensenkeisan<728000)and(self.Fuyo==5)):
			Gensen = 38300 
		
		elif((725000<=Gensenkeisan)and(Gensenkeisan<728000)and(self.Fuyo==6)):
			Gensen = 31820 
		
		elif((725000<=Gensenkeisan)and(Gensenkeisan<728000)and(self.Fuyo==7)):
			Gensen = 25360 
		
		#242
		elif((728000<=Gensenkeisan)and(Gensenkeisan<731000)and(self.Fuyo==0)):
			Gensen = 71250 
		
		elif((728000<=Gensenkeisan)and(Gensenkeisan<731000)and(self.Fuyo==1)):
			Gensen = 64770 
		
		elif((728000<=Gensenkeisan)and(Gensenkeisan<731000)and(self.Fuyo==2)):
			Gensen = 58310 
		
		elif((728000<=Gensenkeisan)and(Gensenkeisan<731000)and(self.Fuyo==3)):
			Gensen = 51840 
		
		elif((728000<=Gensenkeisan)and(Gensenkeisan<731000)and(self.Fuyo==4)):
			Gensen = 45370 
		
		elif((728000<=Gensenkeisan)and(Gensenkeisan<731000)and(self.Fuyo==5)):
			Gensen = 38910
		
		elif((728000<=Gensenkeisan)and(Gensenkeisan<731000)and(self.Fuyo==6)):
			Gensen = 32440 
		
		elif((728000<=Gensenkeisan)and(Gensenkeisan<731000)and(self.Fuyo==7)):
			Gensen = 25970 
		
		#243
		elif((731000<=Gensenkeisan)and(Gensenkeisan<734000)and(self.Fuyo==0)):
			Gensen = 71860 
		
		elif((731000<=Gensenkeisan)and(Gensenkeisan<734000)and(self.Fuyo==1)):
			Gensen = 65380 
		
		elif((731000<=Gensenkeisan)and(Gensenkeisan<734000)and(self.Fuyo==2)):
			Gensen = 58920 
		
		elif((731000<=Gensenkeisan)and(Gensenkeisan<734000)and(self.Fuyo==3)):
			Gensen = 52450 
		
		elif((731000<=Gensenkeisan)and(Gensenkeisan<734000)and(self.Fuyo==4)):
			Gensen = 45990 
		
		elif((731000<=Gensenkeisan)and(Gensenkeisan<734000)and(self.Fuyo==5)):
			Gensen = 39520 
		
		elif((731000<=Gensenkeisan)and(Gensenkeisan<734000)and(self.Fuyo==6)):
			Gensen = 33050 
		
		elif((731000<=Gensenkeisan)and(Gensenkeisan<734000)and(self.Fuyo==7)):
			Gensen = 26590 
		
		#244
		elif((734000<=Gensenkeisan)and(Gensenkeisan<737000)and(self.Fuyo==0)):
			Gensen = 72470 
		
		elif((734000<=Gensenkeisan)and(Gensenkeisan<737000)and(self.Fuyo==1)):
			Gensen = 66000 
		
		elif((734000<=Gensenkeisan)and(Gensenkeisan<737000)and(self.Fuyo==2)):
			Gensen = 59530 
		
		elif((734000<=Gensenkeisan)and(Gensenkeisan<737000)and(self.Fuyo==3)):
			Gensen = 53060 
		
		elif((734000<=Gensenkeisan)and(Gensenkeisan<737000)and(self.Fuyo==4)):
			Gensen = 46600 
		
		elif((734000<=Gensenkeisan)and(Gensenkeisan<737000)and(self.Fuyo==5)):
			Gensen = 40140 
		
		elif((734000<=Gensenkeisan)and(Gensenkeisan<737000)and(self.Fuyo==6)):
			Gensen = 33660 
		
		elif((734000<=Gensenkeisan)and(Gensenkeisan<737000)and(self.Fuyo==7)):
			Gensen = 27200 
		
		#245
		elif((737000<=Gensenkeisan)and(Gensenkeisan<740000)and(self.Fuyo==0)):
			Gensen = 73080 
		
		elif((737000<=Gensenkeisan)and(Gensenkeisan<740000)and(self.Fuyo==1)):
			Gensen = 66610 
		
		elif((737000<=Gensenkeisan)and(Gensenkeisan<740000)and(self.Fuyo==2)):
			Gensen = 60150 
		
		elif((737000<=Gensenkeisan)and(Gensenkeisan<740000)and(self.Fuyo==3)):
			Gensen = 53670 
		
		elif((737000<=Gensenkeisan)and(Gensenkeisan<740000)and(self.Fuyo==4)):
			Gensen = 47210 
		
		elif((737000<=Gensenkeisan)and(Gensenkeisan<740000)and(self.Fuyo==5)):
			Gensen = 40750 
		
		elif((737000<=Gensenkeisan)and(Gensenkeisan<740000)and(self.Fuyo==6)):
			Gensen = 34270 
		
		elif((737000<=Gensenkeisan)and(Gensenkeisan<740000)and(self.Fuyo==7)):
			Gensen = 27810 
		
		#740000
		elif((740000==Gensenkeisan)and(self.Fuyo==0)):
			Gensen = 73390
		
		elif((740000==Gensenkeisan)and(self.Fuyo==1)):
			Gensen = 66920
		
		elif((740000==Gensenkeisan)and(self.Fuyo==2)):
			Gensen = 60450
		
		elif((740000==Gensenkeisan)and(self.Fuyo==3)):
			Gensen = 53980
		
		elif((740000==Gensenkeisan)and(self.Fuyo==4)):
			Gensen = 47520
		
		elif((740000==Gensenkeisan)and(self.Fuyo==5)):
			Gensen = 41050
		
		elif((740000==Gensenkeisan)and(self.Fuyo==6)):
			Gensen = 34580
		
		elif((740000==Gensenkeisan)and(self.Fuyo==7)):
			Gensen = 28120
		

		#740000<Gensenkeisan<780000
		elif((740000<Gensenkeisan)and(Gensenkeisan<780000)and(self.Fuyo==0)):
			Gensen = ((Gensenkeisan-740000)*0.2042)+73390
		
		elif((740000<Gensenkeisan)and(Gensenkeisan<780000)and(self.Fuyo==1)):
			Gensen = ((Gensenkeisan-740000)*0.2042)+66920
		
		elif((740000<Gensenkeisan)and(Gensenkeisan<780000)and(self.Fuyo==2)):
			Gensen = ((Gensenkeisan-740000)*0.2042)+60450
		
		elif((740000<Gensenkeisan)and(Gensenkeisan<780000)and(self.Fuyo==3)):
			Gensen = ((Gensenkeisan-740000)*0.2042)+53980
		
		elif((740000<Gensenkeisan)and(Gensenkeisan<780000)and(self.Fuyo==4)):
			Gensen = ((Gensenkeisan-740000)*0.2042)+47520
		
		elif((740000<Gensenkeisan)and(Gensenkeisan<780000)and(self.Fuyo==5)):
			Gensen = ((Gensenkeisan-740000)*0.2042)+41050
		
		elif((740000<Gensenkeisan)and(Gensenkeisan<780000)and(self.Fuyo==6)):
			Gensen = ((Gensenkeisan-740000)*0.2042)+34580
		
		elif((740000<Gensenkeisan)and(Gensenkeisan<780000)and(self.Fuyo==7)):
			Gensen = ((Gensenkeisan-740000)*0.2042)+28120
		

		#780000
		elif((780000==Gensenkeisan)and(self.Fuyo==0)):
			Gensen = 81560
		
		elif((780000==Gensenkeisan)and(self.Fuyo==1)):
			Gensen = 75090
		
		elif((780000==Gensenkeisan)and(self.Fuyo==2)):
			Gensen = 68620
		
		elif((780000==Gensenkeisan)and(self.Fuyo==3)):
			Gensen = 62150
		
		elif((780000==Gensenkeisan)and(self.Fuyo==4)):
			Gensen = 55690
		
		elif((780000==Gensenkeisan)and(self.Fuyo==5)):
			Gensen = 49220
		
		elif((780000==Gensenkeisan)and(self.Fuyo==6)):
			Gensen = 42750
		
		elif((780000==Gensenkeisan)and(self.Fuyo==7)):
			Gensen = 36290
		

		#780000<Gensenkeisan<950000
		elif((780000<Gensenkeisan)and(Gensenkeisan<950000)and(self.Fuyo==0)):
			Gensen = ((Gensenkeisan-780000)*0.23483)+81560
		
		elif((780000<Gensenkeisan)and(Gensenkeisan<950000)and(self.Fuyo==1)):
			Gensen = ((Gensenkeisan-780000)*0.23483)+75090
		
		elif((780000<Gensenkeisan)and(Gensenkeisan<950000)and(self.Fuyo==2)):
			Gensen = ((Gensenkeisan-780000)*0.23483)+68620
		
		elif((780000<Gensenkeisan)and(Gensenkeisan<950000)and(self.Fuyo==3)):
			Gensen = ((Gensenkeisan-780000)*0.23483)+62150
		
		elif((780000<Gensenkeisan)and(Gensenkeisan<950000)and(self.Fuyo==4)):
			Gensen = ((Gensenkeisan-780000)*0.23483)+55690
		
		elif((780000<Gensenkeisan)and(Gensenkeisan<950000)and(self.Fuyo==5)):
			Gensen = ((Gensenkeisan-780000)*0.23483)+49220
		
		elif((780000<Gensenkeisan)and(Gensenkeisan<950000)and(self.Fuyo==6)):
			Gensen = ((Gensenkeisan-780000)*0.23483)+42750
		
		elif((780000<Gensenkeisan)and(Gensenkeisan<950000)and(self.Fuyo==7)):
			Gensen = ((Gensenkeisan-780000)*0.23483)+36290
		

		#950000
		elif((950000==Gensenkeisan)and(self.Fuyo==0)):
			Gensen = 121480
		
		elif((950000==Gensenkeisan)and(self.Fuyo==1)):
			Gensen = 115010
		
		elif((950000==Gensenkeisan)and(self.Fuyo==2)):
			Gensen = 108540
		
		elif((950000==Gensenkeisan)and(self.Fuyo==3)):
			Gensen = 102070
		
		elif((950000==Gensenkeisan)and(self.Fuyo==4)):
			Gensen = 95610
		
		elif((950000==Gensenkeisan)and(self.Fuyo==5)):
			Gensen = 89140
		
		elif((950000==Gensenkeisan)and(self.Fuyo==6)):
			Gensen = 82670
		
		elif((950000==Gensenkeisan)and(self.Fuyo==7)):
			Gensen = 76210
		
		#950000<Gensenkeisan< 1700000
		elif((950000<Gensenkeisan)and(Gensenkeisan<1700000)and(self.Fuyo==0)):
			Gensen = ((Gensenkeisan-950000)*0.33693)+121480
		
		elif((950000<Gensenkeisan)and(Gensenkeisan<1700000)and(self.Fuyo==1)):
			Gensen = ((Gensenkeisan-950000)*0.33693)+115010
		
		elif((950000<Gensenkeisan)and(Gensenkeisan<1700000)and(self.Fuyo==2)):
			Gensen = ((Gensenkeisan-950000)*0.33693)+108540
		
		elif((950000<Gensenkeisan)and(Gensenkeisan<1700000)and(self.Fuyo==3)):
			Gensen = ((Gensenkeisan-950000)*0.33693)+102070
		
		elif((950000<Gensenkeisan)and(Gensenkeisan<1700000)and(self.Fuyo==4)):
			Gensen = ((Gensenkeisan-950000)*0.33693)+95610
		
		elif((950000<Gensenkeisan)and(Gensenkeisan<1700000)and(self.Fuyo==5)):
			Gensen = ((Gensenkeisan-950000)*0.33693)+89140
		
		elif((950000<Gensenkeisan)and(Gensenkeisan<1700000)and(self.Fuyo==6)):
			Gensen = ((Gensenkeisan-950000)*0.33693)+82670
		
		elif((950000<Gensenkeisan)and(Gensenkeisan<1700000)and(self.Fuyo==7)):
			Gensen = ((Gensenkeisan-950000)*0.33693)+76210
		

		#1700000
		elif((1700000==Gensenkeisan)and(self.Fuyo==0)):
			Gensen = 374180
		
		elif((1700000==Gensenkeisan)and(self.Fuyo==1)):
			Gensen = 367710
		
		elif((1700000==Gensenkeisan)and(self.Fuyo==2)):
			Gensen = 361240
		
		elif((1700000==Gensenkeisan)and(self.Fuyo==3)):
			Gensen = 354770
		
		elif((1700000==Gensenkeisan)and(self.Fuyo==4)):
			Gensen = 348310
		
		elif((1700000==Gensenkeisan)and(self.Fuyo==5)):
			Gensen = 341840
		
		elif((1700000==Gensenkeisan)and(self.Fuyo==6)):
			Gensen = 335370
		
		elif((1700000==Gensenkeisan)and(self.Fuyo==7)):
			Gensen = 328910
		
		# 1700000<Gensenkeisan<  2170000
		elif((1700000<Gensenkeisan)and(Gensenkeisan<2170000)and(self.Fuyo==0)):
			Gensen = ((Gensenkeisan-1700000)*0.4084)+374180
		
		elif((1700000<Gensenkeisan)and(Gensenkeisan<2170000)and(self.Fuyo==1)):
			Gensen = ((Gensenkeisan-1700000)*0.4084)+367710
		
		elif((1700000<Gensenkeisan)and(Gensenkeisan<2170000)and(self.Fuyo==2)):
			Gensen = ((Gensenkeisan-1700000)*0.4084)+361240
		
		elif((1700000<Gensenkeisan)and(Gensenkeisan<2170000)and(self.Fuyo==3)):
			Gensen = ((Gensenkeisan-1700000)*0.4084)+354770
		
		elif((1700000<Gensenkeisan)and(Gensenkeisan<2170000)and(self.Fuyo==4)):
			Gensen = ((Gensenkeisan-1700000)*0.4084)+348310
		
		elif((1700000<Gensenkeisan)and(Gensenkeisan<2170000)and(self.Fuyo==5)):
			Gensen = ((Gensenkeisan-1700000)*0.4084)+341840
		
		elif((1700000<Gensenkeisan)and(Gensenkeisan<2170000)and(self.Fuyo==6)):
			Gensen = ((Gensenkeisan-1700000)*0.4084)+335370
		
		elif((1700000<Gensenkeisan)and(Gensenkeisan<2170000)and(self.Fuyo==7)):
			Gensen = ((Gensenkeisan-1700000)*0.4084)+328910
		

		#2170000
		elif((2170000==Gensenkeisan)and(self.Fuyo==0)):
			Gensen = 571570
		
		elif((2170000==Gensenkeisan)and(self.Fuyo==1)):
			Gensen = 565090
		
		elif((2170000==Gensenkeisan)and(self.Fuyo==2)):
			Gensen = 558630
		
		elif((2170000==Gensenkeisan)and(self.Fuyo==3)):
			Gensen = 552160
		
		elif((2170000==Gensenkeisan)and(self.Fuyo==4)):
			Gensen = 545690
		
		elif((2170000==Gensenkeisan)and(self.Fuyo==5)):
			Gensen = 539230
		
		elif((2170000==Gensenkeisan)and(self.Fuyo==6)):
			Gensen = 532760
		
		elif((2170000==Gensenkeisan)and(self.Fuyo==7)):
			Gensen = 526290
		
		# 2170000<Gensenkeisan< 2210000
		elif((2170000<Gensenkeisan)and(Gensenkeisan<2210000)and(self.Fuyo==0)):
			Gensen = ((Gensenkeisan-2170000)*0.4084)+571570
		
		elif((2170000<Gensenkeisan)and(Gensenkeisan<2210000)and(self.Fuyo==1)):
			Gensen = ((Gensenkeisan-2170000)*0.4084)+565090
		
		elif((2170000<Gensenkeisan)and(Gensenkeisan<2210000)and(self.Fuyo==2)):
			Gensen = ((Gensenkeisan-2170000)*0.4084)+558630
		
		elif((2170000<Gensenkeisan)and(Gensenkeisan<2210000)and(self.Fuyo==3)):
			Gensen = ((Gensenkeisan-2170000)*0.4084)+552160
		
		elif((2170000<Gensenkeisan)and(Gensenkeisan<2210000)and(self.Fuyo==4)):
			Gensen = ((Gensenkeisan-2170000)*0.4084)+545690
		
		elif((2170000<Gensenkeisan)and(Gensenkeisan<2210000)and(self.Fuyo==5)):
			Gensen = ((Gensenkeisan-2170000)*0.4084)+539230
		
		elif((2170000<Gensenkeisan)and(Gensenkeisan<2210000)and(self.Fuyo==6)):
			Gensen = ((Gensenkeisan-2170000)*0.4084)+532760
		
		elif((2170000<Gensenkeisan)and(Gensenkeisan<2210000)and(self.Fuyo==7)):
			Gensen = ((Gensenkeisan-2170000)*0.4084)+526290
		

		#2210000
		elif((2210000==Gensenkeisan)and(self.Fuyo==0)):
			Gensen = 593340
		
		elif((2210000==Gensenkeisan)and(self.Fuyo==1)):
			Gensen = 586870
		
		elif((2210000==Gensenkeisan)and(self.Fuyo==2)):
			Gensen = 580410
		
		elif((2210000==Gensenkeisan)and(self.Fuyo==3)):
			Gensen = 573930
		
		elif((2210000==Gensenkeisan)and(self.Fuyo==4)):
			Gensen = 567470
		
		elif((2210000==Gensenkeisan)and(self.Fuyo==5)):
			Gensen = 561010
		
		elif((2210000==Gensenkeisan)and(self.Fuyo==6)):
			Gensen = 554540
		
		elif((2210000==Gensenkeisan)and(self.Fuyo==7)):
			Gensen = 548070
		
		# 2210000<Gensenkeisan< 2250000
		elif((2210000<Gensenkeisan)and(Gensenkeisan<2250000)and(self.Fuyo==0)):
			Gensen = ((Gensenkeisan-2210000)*0.4084)+593340
		
		elif((2210000<Gensenkeisan)and(Gensenkeisan<2250000)and(self.Fuyo==1)):
			Gensen = ((Gensenkeisan-2210000)*0.4084)+586870
		
		elif((2210000<Gensenkeisan)and(Gensenkeisan<2250000)and(self.Fuyo==2)):
			Gensen = ((Gensenkeisan-2210000)*0.4084)+580410
		
		elif((2210000<Gensenkeisan)and(Gensenkeisan<2250000)and(self.Fuyo==3)):
			Gensen = ((Gensenkeisan-2210000)*0.4084)+573930
		
		elif((2210000<Gensenkeisan)and(Gensenkeisan<2250000)and(self.Fuyo==4)):
			Gensen = ((Gensenkeisan-2210000)*0.4084)+567470
		
		elif((2210000<Gensenkeisan)and(Gensenkeisan<2250000)and(self.Fuyo==5)):
			Gensen = ((Gensenkeisan-2210000)*0.4084)+561010
		
		elif((2210000<Gensenkeisan)and(Gensenkeisan<2250000)and(self.Fuyo==6)):
			Gensen = ((Gensenkeisan-2210000)*0.4084)+554540
		
		elif((2210000<Gensenkeisan)and(Gensenkeisan<2250000)and(self.Fuyo==7)):
			Gensen = ((Gensenkeisan-2210000)*0.4084)+548070
		

		#2250000
		elif((2250000==Gensenkeisan)and(self.Fuyo==0)):
			Gensen = 615120
		
		elif((2250000==Gensenkeisan)and(self.Fuyo==1)):
			Gensen = 608650
		
		elif((2250000==Gensenkeisan)and(self.Fuyo==2)):
			Gensen = 602190
		
		elif((2250000==Gensenkeisan)and(self.Fuyo==3)):
			Gensen = 595710
		
		elif((2250000==Gensenkeisan)and(self.Fuyo==4)):
			Gensen = 589250
		
		elif((2250000==Gensenkeisan)and(self.Fuyo==5)):
			Gensen = 582790
		
		elif((2250000==Gensenkeisan)and(self.Fuyo==6)):
			Gensen = 576310
		
		elif((2250000==Gensenkeisan)and(self.Fuyo==7)):
			Gensen = 569850
		
		# 2250000<Gensenkeisan< 3500000
		elif((2250000<Gensenkeisan)and(Gensenkeisan<3500000)and(self.Fuyo==0)):
			Gensen = ((Gensenkeisan-2250000)*0.4084)+615120
		
		elif((2250000<Gensenkeisan)and(Gensenkeisan<3500000)and(self.Fuyo==1)):
			Gensen = ((Gensenkeisan-2250000)*0.4084)+608650
		
		elif((2250000<Gensenkeisan)and(Gensenkeisan<3500000)and(self.Fuyo==2)):
			Gensen = ((Gensenkeisan-2250000)*0.4084)+602190
		
		elif((2250000<Gensenkeisan)and(Gensenkeisan<3500000)and(self.Fuyo==3)):
			Gensen = ((Gensenkeisan-2250000)*0.4084)+595710
		
		elif((2250000<Gensenkeisan)and(Gensenkeisan<3500000)and(self.Fuyo==4)):
			Gensen = ((Gensenkeisan-2250000)*0.4084)+589250
		
		elif((2250000<Gensenkeisan)and(Gensenkeisan<3500000)and(self.Fuyo==5)):
			Gensen = ((Gensenkeisan-2250000)*0.4084)+582790
		
		elif((2250000<Gensenkeisan)and(Gensenkeisan<3500000)and(self.Fuyo==6)):
			Gensen = ((Gensenkeisan-2250000)*0.4084)+576310
		
		elif((2250000<Gensenkeisan)and(Gensenkeisan<3500000)and(self.Fuyo==7)):
			Gensen = ((Gensenkeisan-2250000)*0.4084)+569850
		

		#3500000
		elif((3500000==Gensenkeisan)and(self.Fuyo==0)):
			Gensen = 1125620
		
		elif((3500000==Gensenkeisan)and(self.Fuyo==1)):
			Gensen = 1119150
		
		elif((3500000==Gensenkeisan)and(self.Fuyo==2)):
			Gensen = 1112690
		
		elif((3500000==Gensenkeisan)and(self.Fuyo==3)):
			Gensen = 1106210
		
		elif((3500000==Gensenkeisan)and(self.Fuyo==4)):
			Gensen = 1099750
		
		elif((3500000==Gensenkeisan)and(self.Fuyo==5)):
			Gensen = 1093290
		
		elif((3500000==Gensenkeisan)and(self.Fuyo==6)):
			Gensen = 1086810
		
		elif((3500000==Gensenkeisan)and(self.Fuyo==7)):
			Gensen = 1080350
		
		# <3500000
		elif((3500000<Gensenkeisan)and(self.Fuyo==0)):
			Gensen = ((Gensenkeisan-3500000)*0.45945)+1125620
		
		elif((3500000<Gensenkeisan)and(self.Fuyo==1)):
			Gensen = ((Gensenkeisan-3500000)*0.45945)+1119150
		
		elif((3500000<Gensenkeisan)and(self.Fuyo==2)):
			Gensen = ((Gensenkeisan-3500000)*0.45945)+1112690
		
		elif((3500000<Gensenkeisan)and(self.Fuyo==3)):
			Gensen = ((Gensenkeisan-3500000)*0.45945)+1106210
		
		elif((3500000<Gensenkeisan)and(self.Fuyo==4)):
			Gensen = ((Gensenkeisan-3500000)*0.45945)+1099750
		
		elif((3500000<Gensenkeisan)and(self.Fuyo==5)):
			Gensen = ((Gensenkeisan-3500000)*0.45945)+1093290
		
		elif((3500000<Gensenkeisan)and(self.Fuyo==6)):
			Gensen = ((Gensenkeisan-3500000)*0.45945)+1086810
		
		elif((3500000<Gensenkeisan)and(self.Fuyo==7)):
			Gensen = ((Gensenkeisan-3500000)*0.45945)+1080350

		return int(Gensen)

	def JuminVal(self):
		#源泉所得税額表
		nensyu = int((self.Kihonkyu) * 12)
		KSkojo = 0 #給与所得控除
		if nensyu <= 550999:
			KSkojo = nensyu
		elif nensyu <= 1625000:
			KSkojo = 550000
		elif nensyu <= 1800000:
			KSkojo = nensyu * 0.4 - 100000
		elif nensyu <= 3600000:
			KSkojo = nensyu * 0.3 + 80000
		elif nensyu <= 6600000:
			KSkojo = nensyu * 0.2 + 440000
		elif nensyu <= 8500000:
			KSkojo = nensyu * 0.1 + 1100000
		else:
			KSkojo = 1950000
		syotoku = nensyu - KSkojo
		kisokojo = 0
		if syotoku <= 24000000:
			kisokojo = 430000
		elif syotoku <= 24500000:
			kisokojo = 290000
		elif syotoku <= 25000000:
			kisokojyo = 150000

		fuyokojo = 0
		#ToDo 扶養控除等

		#課税総所得金額
		kazeisyotoku = syotoku - kisokojo - (self.Kenho + self.Kaiho + self.Nenkin + self.Koyo) - fuyokojo
		juminzei = kazeisyotoku * 0.1 + 5000
		return int(juminzei/12)

	
	def JidoteateVal(self):
		# 子ども・子育て拠出金
		Jidoteate = int((self.NenkinTokyu)*0.0036)
		return Jidoteate

	def TedoriVal(self):
		# 労働者手取り
		Tedori = int(self.Komi-self.Kenho - self.Nenkin - self.Gensen - self.Koyo - self.Kaiho - self.Jumin)
		return Tedori
	def KojoVal(self):
		# 労働者控除額合計
		Kojo = int(self.Kenho+self.Nenkin+self.Gensen+self.Koyo+self.Kaiho)		
		return Kojo
	def RosaiVal(self):
		# 事業主負担 労災
		Rosai = int(((self.Komi)*0.003)+0.49)
		return Rosai
	def JkoyoVal(self):
		# 事業主負担 雇用保険
		Jkoyo = int(((self.Komi)*0.006)+0.49)
		return Jkoyo
	def Jfutan(self):
		# 事業主負担額
		Jfutan = int(self.Komi+self.Kenho+self.Nenkin+self.Rosai+self.Jkoyo+self.Kaiho+self.Jidoteate)
		return Jfutan
	def Jkojo(self):
		# 事業主控除額合計
		Jkojo = int(self.Kenho+self.Nenkin+self.Rosai+self.Koyo+self.Kaiho+self.Jidoteate)
		return Jkojo

	def Ysyotoku(self):
		#総支給額[年収]
		nenSoushikyu = int(self.Komi*12)
		return nenSoushikyu
	def Ytedori(self):
		# 労働者手取り[年収]
		nenTedori = int((self.Komi-self.Kenho-self.Nenkin-self.Gensen-self.Koyo-self.Kaiho - self.Jumin)*12)
		return nenTedori
	def JYfutan(self):
		# 事業主負担額[年収]
		nenJfutan = int((self.Komi+self.Kenho+self.Nenkin+self.Rosai+self.Koyo+self.Kaiho+self.Jidoteate)*12)
		return nenJfutan
  

if __name__ == "__main__":
	ret = Cal(Kihonkyu=500000, Age=26, Pref="東京都", Kotsuhi=0, Zangyodai=0, Fuyo=0)
	print(vars(ret))
	print(ret.OutTedori())
