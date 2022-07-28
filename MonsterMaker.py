import random
print('Welcome to the Subspecies Maker')
MonsterType=input('Choose a Monster Type: Flying Wyvern, Fanged Wyvern, Brute Wyvern, Snake Wyvern, Bird Wyvern, Piscine Wyvern, Leviathan, Fanged Beast, Amphibian, Carapaceon, Neopteron, Temnocerans, Other, Elder Dragon')
if(MonsterType in 'Flying Wyvern'):
    Monster = ['Rathian', 'Rathalos', 'Basrios', 'Gravios', 'Khezu', 'Nargacuga', 'Tigrex', 'Diablos', 'Monoblos', 'Barioth', 'Bazelgeuse', 'Legiana', 'Paolumu', 'Espinas', 'Astalos']
if(MonsterType in 'Fanged Wyvern'):
    Monster = ['Tobi-Kadachi', 'Great Jagras', 'Great Girros', 'Dodogama', 'Zinogre', 'Magnamalo', 'Lunagaron', 'Odogaron']
if(MonsterType in 'Brute Wyvern'):
    Monster = ['Barroth', 'Anjanath', 'Radobaan', 'Uragaan', 'Glavenus', 'Brachydios', 'Deviljho']
if(MonsterType in 'Snake Wyvern'):
    Monster = ['Narajala']
if(MonsterType in 'Bird Wyvern'):
    Monster = ['Velocidrome', 'Gendrome', 'Iodrome', 'Great Maccao', 'Great Izuchi', 'Great Jaggi', 'Great Baggi', 'Great Wroggi', 'Kulu-Ya-Ku', 'Yian-Kut-Ku', 'Gyperios', 'Aknosom', 'Qurupeco', 'Tzitzi-Ya-Ku', 'Pukei-Pukei', 'Malfestio', 'Yian Garuga']
if(MonsterType in 'Piscine Wyvern'):
    Monster = ['Plesioth', 'Beodotus', 'Lavasioth', 'Jyuratodus']
if(MonsterType in 'Leviathan'):
    Monster = ['Mizutsune', 'Somnacanth', 'Royal Ludroth', 'Lagiacrus', 'Agnaktor', 'Almudron']
if(MonsterType in 'Fanged Beast'):
    Monster = ['Bulldrome', 'Rajang', 'Congalala', 'Bishaten', 'Gammoth', 'Arzuros', 'Lagombi', 'Volvidon', 'Goss Harag', 'Garangolm']
if(MonsterType in 'Amphibian'):
    Monster = ['Tetradon', 'Tetscubra', 'Zamtrios']
if(MonsterType in 'Carapaceon'):
    Monster = ['Daimyo Hermitaur', 'Shogun Ceanataur', 'Shen Gaoren']
if(MonsterType in 'Neopteron'):
    Monster = ['Seltas', 'Seltas Queen', 'Ahtal-Ka']
if(MonsterType in 'Temnocerans'):
    Monster = ['Rakna-Kadaki', 'Nerscylla']
if(MonsterType in 'Other'):
    Monster = ['Gore Magala']
if(MonsterType in 'Elder Dragon'):
    Monster = ['Chameleos', 'Kushala Daora', 'Teostra', 'Lunastra', 'Kirin', 'Vaal Hazak', 'Namielle', 'Velkhana', 'Nergigante', 'Ibushi', 'Narwa', 'Valstrax', 'Shaguru Magala', 'Malzeno', 'Nakarkos', 'Lao-Shan Lung', 'Zorah Magdaros', 'Dalamadur', 'Xeno`jiiva', 'Safi`jiiva', 'Gogmazios', 'Kulve Taroth', 'Gaismagorm', 'Dire Miralis', 'Alatreon', 'Fatalis']
Elements = ['Fire', 'Ice', 'Water', 'Thunder', 'Dragon', 'Fire/Ice' , 'Fire/Water', 'Fire/Thunder', 'Fire/', 'Ice/Water' , 'Ice/Thunder' , 'Ice/Dragon', 'Water/Thunder', 'Water/Dragon', 'Thunder/Dragon','None']
Aliments = ['Poison', 'Paralysis', 'Sleep', 'Blastblight', 'Poison/Paralysis', 'Poison/Sleep', 'Poison/Blastblight', 'Poison/Bleed', 'Paralysis/Sleep', 'Paralysis/Blastblight', 'Paralysis/Bleed', 'Sleep/Blastblight', 'Sleep/Bleed', 'Blastblight/Bleed', 'Stench/Poison', 'Stench/Paralysis', 'Stench/Sleep', 'Stench/Blastblight', 'Stench/Bleed', 'Frenzy', 'Bleed', 'Stench', 'Fire-Blastblight', 'None']
Colors = ['Red', 'Blue', 'Purple', 'White', 'Black', 'Pink', 'Green', 'Yellow', 'Orange', 'Light Green', 'Teal', 'Brown', 'Dark Red', 'Navy Blue', 'Grey']
print('The New Species is a ' + random.choice(Colors) + 'Colored ' + random.choice(Monster) + ' with ' + random.choice(Elements) + ' and ' + random.choice(Aliments) + '.')
