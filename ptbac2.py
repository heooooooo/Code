class Player:
	def __init__(self,name,age):
		self.name=name
		self.age=age
	@classmethod
	def chao(cls,s):
		 lst = s.split('-')
		 new_lst = [st.strip() for st in lst]
		 name,age=new_lst
		 return cls(name,age)
s='Hieu - 16'
ng1=Player.chao(s)
print(ng1.__dict__)