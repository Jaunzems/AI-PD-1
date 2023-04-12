# 1. Prakstiskais darbs


## Kā palaist
- Vajag Python3, pip un pygame
- Ja nav pygame:
```pip install -r requirements.txt```
- Lai palaistu:
```main.py```
## Pogas
- Pogas pa labi un pa kreisi kontrolē izvēlētās vērtības
- Vidus poga izvēlās
  - Izvēlētie skaitļi tiks pārvēsti par jaunajām vērtībām
- Player/Computer - Maina kas būs pretinieks
- tart/Restart - Ļauj sākt vai restartēt spēli
- Easy/Medium/Hard - Ļauj izvēlēties grūtības pakāpi un maina ciparu skaitu (easy = 6, medium = 8, hard = 10).

## Nosacījumi
 - Divus blakus esošus vienskaitļus var aizstāt ar 1 (11=1), un spēlētāja rezultātam tiek pieskaitīti 2 punkti;
 - Divus blakus esošus nulles skaitļus aizstāt ar 0 (00=0) un spēlētāja rezultātam pievienot 2 punktus;
 - Nomainot blakus esošās vieninieku un nulles ar 1 (10=1) un spēlētāja rezultātam pievienot 1 punktu;
 - Aaizstāt 0 un 1 blakus 0 (01=0) un pievienot 1 punktu spēlētāja rezultātam.
 - Spēle beidzas, kad skaitļu virknē ir palicis tikai viens skaitlis. Spēli uzvar spēlētājs ar lielāko punktu skaitu. Ja punktu skaits ir vienāds, spēle ir neizšķirta.

