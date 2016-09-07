#!/usr/bin/python3
from collections import OrderedDict
import sys

fin = open(sys.argv[1], 'r')
fout = open(sys.argv[1]+'roman', 'w')
d2r_dict=OrderedDict([
('क्','k'), 
('ख्','kh'), 
('ग्','g'), 
('घ्','gh'), 
('ङ्','ŋ'), 
('च्','ch'), 
('छ्','chh'), 
('ज्','j'), 
('झ्','jh'), 
('ञ्','ñ'), 
('ट्','t'), 
('ठ्','th'), 
('ड्','d'), 
('ढ्','dh'), 
('ण्','ṇ'), 
('त्','ṭ'), 
('थ्','ṭh'), 
('द्','ḍ'), 
('ध्','ḍh'), 
('न्','n'), 
('प्','p'), 
('फ्','ph'), 
('ब्','b'), 
('भ्','bh'), 
('म्','m'), 
('य्','y'), 
('र्','r'), 
('ल्','l'), 
('व्','w'), 
('श्','s'), 
('ष्','s'), 
('स्','s'), 
('ह्','h'), 
('ष','श'), 
('स','श'), 
('का','kaa'), 
('को','ko'),
('कौ','kau'),
('कि','ki'),
('की','ki'),
('कु','ku'),
('कू','ku'),
('के','ke'),
('कै','kai'),
('कं','kum'),
('खा','khaa'), 
('खो','kho'),
('खौ','khau'),
('खि','khi'),
('खी','khi'),
('खु','khu'),
('खू','khu'),
('खे','khe'),
('खै','khai'),
('खं','khum'),
('गा','gaa'), 
('गो','go'),
('गौ','gau'),
('गि','gi'),
('गी','gi'),
('गु','gu'),
('गू','gu'),
('गे','ge'),
('गै','gai'),
('गं','gum'),
('घा','ghaa'), 
('घो','gho'),
('घौ','ghau'),
('घि','ghi'),
('घी','ghi'),
('घु','ghu'),
('घू','ghu'),
('घे','ghe'),
('घै','ghai'),
('घं','ghum'),
('ङा','ŋaa'), 
('ङो','ŋo'),
('ङौ','ŋau'),
('ङि','ŋi'),
('ङी','ŋi'),
('ङु','ŋu'),
('ङू','ŋu'),
('ङे','ŋe'),
('ङै','ŋai'),
('ङं','ŋum'),
('चा','chaa'), 
('चो','cho'),
('चौ','chau'),
('चि','chi'),
('ची','chi'),
('चु','chu'),
('चू','chu'),
('चे','che'),
('चै','chai'),
('चं','chum'),
('छा','chhaa'), 
('छो','chho'),
('छौ','chhau'),
('छि','chhi'),
('छी','chhi'),
('छु','chhu'),
('छू','chhu'),
('छे','chhe'),
('छै','chhai'),
('छं','chhum'),
('जा','jaa'), 
('जो','jo'),
('जौ','jau'),
('जि','ji'),
('जी','ji'),
('जु','ju'),
('जू','ju'),
('जे','je'),
('जै','jai'),
('जं','jum'),
('झा','jhaa'), 
('झो','jho'),
('झौ','jhau'),
('झि','jhi'),
('झी','jhi'),
('झु','jhu'),
('झू','jhu'),
('झे','jhe'),
('झै','jhai'),
('झं','jhum'),
('ञा','ñaa'), 
('ञो','ño'),
('ञौ','ñau'),
('ञि','ñi'),
('ञी','ñi'),
('ञु','ñu'),
('ञू','ñu'),
('ञे','ñe'),
('ञै','ñai'),
('ञं','ñum'),
('टा','taa'), 
('टो','to'),
('टौ','tau'),
('टि','ti'),
('टी','ti'),
('टु','tu'),
('टू','tu'),
('टे','te'),
('टै','tai'),
('टं','tum'),
('ठा','thaa'), 
('ठो','tho'),
('ठौ','thau'),
('ठि','thi'),
('ठी','thi'),
('ठु','thu'),
('ठू','thu'),
('ठे','the'),
('ठै','thai'),
('ठं','thum'),
('डा','daa'), 
('डो','do'),
('डौ','dau'),
('डि','di'),
('डी','di'),
('डु','du'),
('डू','du'),
('डे','de'),
('डै','dai'),
('डं','dum'),
('ढा','dhaa'), 
('ढो','dho'),
('ढौ','dha'),
('ढि','dhi'),
('ढी','dhi'),
('ढु','dhu'),
('ढू','dhu'),
('ढे','dhe'),
('ढै','dhai'),
('ढं','dhum'),
('ता','ṭaa'), 
('तो','ṭo'),
('तौ','ṭau'),
('ति','ṭi'),
('ती','ṭi'),
('तु','ṭu'),
('तू','ṭu'),
('ते','ṭe'),
('तै','ṭai'),
('तं','ṭum'),
('था','ṭhaa'), 
('थो','ṭho'),
('थौ','ṭhau'),
('थि','ṭhi'),
('थी','ṭhi'),
('थु','ṭhu'),
('थू','ṭhu'),
('थे','ṭhe'),
('थै','ṭhai'),
('थं','ṭhum'),
('दा','daa'), 
('दो','do'),
('दौ','dau'),
('दि','di'),
('दी','di'),
('दु','du'),
('दू','du'),
('दे','de'),
('दै','dai'),
('दं','dum'),
('धा','dhaa'), 
('धो','dho'),
('धौ','dhau'),
('धि','dhi'),
('धी','dhi'),
('धु','dhu'),
('धू','dhu'),
('धे','dhe'),
('धै','dhai'),
('धं','dhum'),
('ना','naa'), 
('नो','no'),
('नौ','nau'),
('नि','ni'),
('नी','ni'),
('नु','nu'),
('नू','nu'),
('ने','ne'),
('नै','nai'),
('नं','num'),
('पा','paa'), 
('पो','po'),
('पौ','pau'),
('पि','pi'),
('पी','pi'),
('पु','pu'),
('पू','pu'),
('पे','pe'),
('पै','pai'),
('पं','pum'),
('फा','phaa'), 
('फो','pho'),
('फौ','phau'),
('फि','phi'),
('फी','phi'),
('फु','phu'),
('फू','phu'),
('फे','phe'),
('फै','phai'),
('फं','phum'),
('बा','baa'), 
('बो','bo'),
('बौ','bau'),
('बि','bi'),
('बी','bi'),
('बु','bu'),
('बू','bu'),
('बे','be'),
('बै','bai'),
('बं','bum'),
('भा','bhaa'), 
('भो','bho'),
('भौ','bhau'),
('भि','bhi'),
('भी','bhi'),
('भु','bhu'),
('भू','bhu'),
('भे','bhe'),
('भै','bhai'),
('भं','bhum'),
('मा','maa'), 
('मो','mo'),
('मौ','mau'),
('मि','mi'),
('मी','mi'),
('मु','mu'),
('मू','mu'),
('मे','me'),
('मै','mai'),
('मं','mum'),
('या','yaa'), 
('यो','yo'),
('यौ','yau'),
('यि','yi'),
('यी','yi'),
('यु','yu'),
('यू','yu'),
('ये','ye'),
('यै','yai'),
('यं','yum'),
('रा','raa'), 
('रो','ro'),
('रौ','rau'),
('रि','ri'),
('री','ri'),
('रु','ru'),
('रू','ru'),
('रे','re'),
('रै','rai'),
('रं','rum'),
('ला','laa'), 
('लो','lo'),
('लौ','lau'),
('लि','li'),
('ली','li'),
('लु','lu'),
('लू','lu'),
('ले','le'),
('लै','lai'),
('लं','lum'),
('वा','waa'), 
('वो','wo'),
('वौ','wau'),
('वि','wi'),
('वी','wi'),
('वु','wu'),
('वू','wu'),
('वे','we'),
('वै','wai'),
('वं','wum'),
('शा','saa'), 
('शो','so'),
('शौ','sau'),
('शि','si'),
('शी','si'),
('शु','su'),
('शू','su'),
('शे','se'),
('शै','sai'),
('शं','sum'),
('हा','haa'), 
('हो','ho'),
('हौ','hau'),
('हि','hi'),
('ही','hi'),
('हु','hu'),
('हू','hu'),
('हे','he'),
('है','hai'),
('हं','hum'),
('क','ka'), 
('ख','kha'), 
('ग','ga'), 
('घ','gha'), 
('ङ','ŋa'), 
('च','cha'), 
('छ','chha'), 
('ज','ja'), 
('झ','jha'), 
('ञ','ña'), 
('ट','ta'), 
('ठ','tha'), 
('ड','da'), 
('ढ','dha'), 
('ण','ṇa'), 
('त','ṭa'), 
('थ','ṭha'), 
('द','ḍa'), 
('ध','ḍha'), 
('न','na'), 
('प','pa'), 
('फ','pha'), 
('ब','ba'), 
('भ','bha'), 
('म','ma'), 
('य','ya'), 
('र','ra'), 
('ल','la'), 
('व','wa'), 
('श','sa'), 
('ष','श'), 
('स','श'), 
('ह','ha'),
('ँ','n'),
('ं','m'),
('ः','h'),
('अ','a'), 
('आ','ā'), 
('इ','i'), 
('ई','i'), 
('उ','u'), 
('ऊ','u'), 
('ऋ','ri'), 
('ए','e'), 
('ऐ','ai'), 
('ओ','o'), 
('औ','au'), 
('ा','ā'), 
('ि','i'), 
('ी','i'), 
('ु','u'), 
('ू','u'), 
('ृ','ri'), 
('े','e'), 
('ै','ai'), 
('ो','o'), 
('ौ','au')
])

def main():
  text=fin.read() 
  for key,value in d2r_dict.items():
  	text=text.replace(key,value)  
  fout.write(text)
  print(text)
  
if __name__ == '__main__':
  main()