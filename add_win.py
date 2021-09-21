import tkinter as tk
from tkinter import ttk
import player_manager

lst = ['Bulbasaur',
       'Ivysaur',
       'Venusaur',
       'Charmander',
       'Charmeleon',
       'Charizard',
       'Squirtle',
       'Wartortle',
       'Blastoise',
       'Caterpie',
       'Metapod',
       'Butterfree',
       'Weedle',
       'Kakuna',
       'Beedrill',
       'Pidgey',
       'Pidgeotto',
       'Pidgeot',
       'Rattata',
       'Raticate',
       'Spearow',
       'Fearow',
       'Ekans',
       'Arbok',
       'Pikachu',
       'Raichu',
       'Sandshrew',
       'Sandslash',
       'Nidoranf',
       'Nidorina',
       'Nidoqueen',
       'Nidoranm',
       'Nidorino',
       'Nidoking',
       'Clefairy',
       'Clefable',
       'Vulpix',
       'Ninetales',
       'Jigglypuff',
       'Wigglytuff',
       'Zubat',
       'Golbat',
       'Oddish',
       'Gloom',
       'Vileplume',
       'Paras',
       'Parasect',
       'Venonat',
       'Venomoth',
       'Diglett',
       'Dugtrio',
       'Meowth',
       'Persian',
       'Psyduck',
       'Golduck',
       'Mankey',
       'Primeape',
       'Growlithe',
       'Arcanine',
       'Poliwag',
       'Poliwhirl',
       'Poliwrath',
       'Abra',
       'Kadabra',
       'Alakazam',
       'Machop',
       'Machoke',
       'Machamp',
       'Bellsprout',
       'Weepinbell',
       'Victreebel',
       'Tentacool',
       'Tentacruel',
       'Geodude',
       'Graveler',
       'Golem',
       'Ponyta',
       'Rapidash',
       'Slowpoke',
       'Slowbro',
       'Magnemite',
       'Magneton',
       'Farfetch’d',
       'Doduo',
       'Dodrio',
       'Seel',
       'Dewgong',
       'Grimer',
       'Muk',
       'Shellder',
       'Cloyster',
       'Gastly',
       'Haunter',
       'Gengar',
       'Onix',
       'Drowzee',
       'Hypno',
       'Krabby',
       'Kingler',
       'Voltorb',
       'Electrode',
       'Exeggcute',
       'Exeggutor',
       'Cubone',
       'Marowak',
       'Hitmonlee',
       'Hitmonchan',
       'Lickitung',
       'Koffing',
       'Weezing',
       'Rhyhorn',
       'Rhydon',
       'Chansey',
       'Tangela',
       'Kangaskhan',
       'Horsea',
       'Seadra',
       'Goldeen',
       'Seaking',
       'Staryu',
       'Starmie',
       'Mr. Mime',
       'Scyther',
       'Jynx',
       'Electabuzz',
       'Magmar',
       'Pinsir',
       'Tauros',
       'Magikarp',
       'Gyarados',
       'Lapras',
       'Ditto',
       'Eevee',
       'Vaporeon',
       'Jolteon',
       'Flareon',
       'Porygon',
       'Omanyte',
       'Omastar',
       'Kabuto',
       'Kabutops',
       'Aerodactyl',
       'Snorlax',
       'Articuno',
       'Zapdos',
       'Moltres',
       'Dratini',
       'Dragonair',
       'Dragonite',
       'Mewtwo',
       'Mew',
       'Chikorita',
       'Bayleef',
       'Meganium',
       'Cyndaquil',
       'Quilava',
       'Typhlosion',
       'Totodile',
       'Croconaw',
       'Feraligatr',
       'Sentret',
       'Furret',
       'Hoothoot',
       'Noctowl',
       'Ledyba',
       'Ledian',
       'Spinarak',
       'Ariados',
       'Crobat',
       'Chinchou',
       'Lanturn',
       'Pichu',
       'Cleffa',
       'Igglybuff',
       'Togepi',
       'Togetic',
       'Natu',
       'Xatu',
       'Mareep',
       'Flaaffy',
       'Ampharos',
       'Bellossom',
       'Marill',
       'Azumarill',
       'Sudowoodo',
       'Politoed',
       'Hoppip',
       'Skiploom',
       'Jumpluff',
       'Aipom',
       'Sunkern',
       'Sunflora',
       'Yanma',
       'Wooper',
       'Quagsire',
       'Espeon',
       'Umbreon',
       'Murkrow',
       'Slowking',
       'Misdreavus',
       'Unown',
       'Wobbuffet',
       'Girafarig',
       'Pineco',
       'Forretress',
       'Dunsparce',
       'Gligar',
       'Steelix',
       'Snubbull',
       'Granbull',
       'Qwilfish',
       'Scizor',
       'Shuckle',
       'Heracross',
       'Sneasel',
       'Teddiursa',
       'Ursaring',
       'Slugma',
       'Magcargo',
       'Swinub',
       'Piloswine',
       'Corsola',
       'Remoraid',
       'Octillery',
       'Delibird',
       'Mantine',
       'Skarmory',
       'Houndour',
       'Houndoom',
       'Kingdra',
       'Phanpy',
       'Donphan',
       'Porygon2',
       'Stantler',
       'Smeargle',
       'Tyrogue',
       'Hitmontop',
       'Smoochum',
       'Elekid',
       'Magby',
       'Miltank',
       'Blissey',
       'Raikou',
       'Entei',
       'Suicune',
       'Larvitar',
       'Pupitar',
       'Tyranitar',
       'Lugia',
       'Ho-Oh',
       'Celebi',
       'Treecko',
       'Grovyle',
       'Sceptile',
       'Torchic',
       'Combusken',
       'Blaziken',
       'Mudkip',
       'Marshtomp',
       'Swampert',
       'Poochyena',
       'Mightyena',
       'Zigzagoon',
       'Linoone',
       'Wurmple',
       'Silcoon',
       'Beautifly',
       'Cascoon',
       'Dustox',
       'Lotad',
       'Lombre',
       'Ludicolo',
       'Seedot',
       'Nuzleaf',
       'Shiftry',
       'Taillow',
       'Swellow',
       'Wingull',
       'Pelipper',
       'Ralts',
       'Kirlia',
       'Gardevoir',
       'Surskit',
       'Masquerain',
       'Shroomish',
       'Breloom',
       'Slakoth',
       'Vigoroth',
       'Slaking',
       'Nincada',
       'Ninjask',
       'Shedinja',
       'Whismur',
       'Loudred',
       'Exploud',
       'Makuhita',
       'Hariyama',
       'Azurill',
       'Nosepass',
       'Skitty',
       'Delcatty',
       'Sableye',
       'Mawile',
       'Aron',
       'Lairon',
       'Aggron',
       'Meditite',
       'Medicham',
       'Electrike',
       'Manectric',
       'Plusle',
       'Minun',
       'Volbeat',
       'Illumise',
       'Roselia',
       'Gulpin',
       'Swalot',
       'Carvanha',
       'Sharpedo',
       'Wailmer',
       'Wailord',
       'Numel',
       'Camerupt',
       'Torkoal',
       'Spoink',
       'Grumpig',
       'Spinda',
       'Trapinch',
       'Vibrava',
       'Flygon',
       'Cacnea',
       'Cacturne',
       'Swablu',
       'Altaria',
       'Zangoose',
       'Seviper',
       'Lunatone',
       'Solrock',
       'Barboach',
       'Whiscash',
       'Corphish',
       'Crawdaunt',
       'Baltoy',
       'Claydol',
       'Lileep',
       'Cradily',
       'Anorith',
       'Armaldo',
       'Feebas',
       'Milotic',
       'Castform',
       'Kecleon',
       'Shuppet',
       'Banette',
       'Duskull',
       'Dusclops',
       'Tropius',
       'Chimecho',
       'Absol',
       'Wynaut',
       'Snorunt',
       'Glalie',
       'Spheal',
       'Sealeo',
       'Walrein',
       'Clamperl',
       'Huntail',
       'Gorebyss',
       'Relicanth',
       'Luvdisc',
       'Bagon',
       'Shelgon',
       'Salamence',
       'Beldum',
       'Metang',
       'Metagross',
       'Regirock',
       'Regice',
       'Registeel',
       'Latias',
       'Latios',
       'Kyogre',
       'Groudon',
       'Rayquaza',
       'Jirachi',
       'Deoxys',
       'Turtwig',
       'Grotle',
       'Torterra',
       'Chimchar',
       'Monferno',
       'Infernape',
       'Piplup',
       'Prinplup',
       'Empoleon',
       'Starly',
       'Staravia',
       'Staraptor',
       'Bidoof',
       'Bibarel',
       'Kricketot',
       'Kricketune',
       'Shinx',
       'Luxio',
       'Luxray',
       'Budew',
       'Roserade',
       'Cranidos',
       'Rampardos',
       'Shieldon',
       'Bastiodon',
       'Burmy',
       'Wormadam',
       'Mothim',
       'Combee',
       'Vespiquen',
       'Pachirisu',
       'Buizel',
       'Floatzel',
       'Cherubi',
       'Cherrim',
       'Shellos',
       'Gastrodon',
       'Ambipom',
       'Drifloon',
       'Drifblim',
       'Buneary',
       'Lopunny',
       'Mismagius',
       'Honchkrow',
       'Glameow',
       'Purugly',
       'Chingling',
       'Stunky',
       'Skuntank',
       'Bronzor',
       'Bronzong',
       'Bonsly',
       'Mime Jr.',
       'Happiny',
       'Chatot',
       'Spiritomb',
       'Gible',
       'Gabite',
       'Garchomp',
       'Munchlax',
       'Riolu',
       'Lucario',
       'Hippopotas',
       'Hippowdon',
       'Skorupi',
       'Drapion',
       'Croagunk',
       'Toxicroak',
       'Carnivine',
       'Finneon',
       'Lumineon',
       'Mantyke',
       'Snover',
       'Abomasnow',
       'Weavile',
       'Magnezone',
       'Lickilicky',
       'Rhyperior',
       'Tangrowth',
       'Electivire',
       'Magmortar',
       'Togekiss',
       'Yanmega',
       'Leafeon',
       'Glaceon',
       'Gliscor',
       'Mamoswine',
       'Porygon-Z',
       'Gallade',
       'Probopass',
       'Dusknoir',
       'Froslass',
       'Rotom',
       'Uxie',
       'Mesprit',
       'Azelf',
       'Dialga',
       'Palkia',
       'Heatran',
       'Regigigas',
       'Giratina',
       'Cresselia',
       'Phione',
       'Manaphy',
       'Darkrai',
       'Shaymin',
       'Arceus']
types = {
	'Bulbasaur': 'Grass',
	'Ivysaur': 'Grass',
	'Venusaur': 'Grass',
	'Charmander': 'Fire',
	'Charmeleon': 'Fire',
	'Charizard': 'Fire',
	'Squirtle': 'Water',
	'Wartortle': 'Water',
	'Blastoise': 'Water',
	'Caterpie': 'Bug',
	'Metapod': 'Bug',
	'Butterfree': 'Bug',
	'Weedle': 'Bug',
	'Kakuna': 'Bug',
	'Beedrill': 'Bug',
	'Pidgey': 'Normal',
	'Pidgeotto': 'Normal',
	'Pidgeot': 'Normal',
	'Rattata': 'Normal',
	'Raticate': 'Normal',
	'Spearow': 'Normal',
	'Fearow': 'Normal',
	'Ekans': 'Poison',
	'Arbok': 'Poison',
	'Pikachu': 'Electric',
	'Raichu': 'Electric',
	'Sandshrew': 'Ground',
	'Sandslash': 'Ground',
	'Nidoran♀': 'Poison',
	'Nidorina': 'Poison',
	'Nidoqueen': 'Poison',
	'Nidoran♂': 'Poison',
	'Nidorino': 'Poison',
	'Nidoking': 'Poison',
	'Clefairy': 'Normal',
	'Clefable': 'Normal',
	'Vulpix': 'Fire',
	'Ninetales': 'Fire',
	'Jigglypuff': 'Normal',
	'Wigglytuff': 'Normal',
	'Zubat': 'Poison',
	'Golbat': 'Poison',
	'Oddish': 'Grass',
	'Gloom': 'Grass',
	'Vileplume': 'Grass',
	'Paras': 'Bug',
	'Parasect': 'Bug',
	'Venonat': 'Bug',
	'Venomoth': 'Bug',
	'Diglett': 'Ground',
	'Dugtrio': 'Ground',
	'Meowth': 'Normal',
	'Persian': 'Normal',
	'Psyduck': 'Water',
	'Golduck': 'Water',
	'Mankey': 'Fighting',
	'Primeape': 'Fighting',
	'Growlithe': 'Fire',
	'Arcanine': 'Fire',
	'Poliwag': 'Water',
	'Poliwhirl': 'Water',
	'Poliwrath': 'Water',
	'Abra': 'Psychic',
	'Kadabra': 'Psychic',
	'Alakazam': 'Psychic',
	'Machop': 'Fighting',
	'Machoke': 'Fighting',
	'Machamp': 'Fighting',
	'Bellsprout': 'Grass',
	'Weepinbell': 'Grass',
	'Victreebel': 'Grass',
	'Tentacool': 'Water',
	'Tentacruel': 'Water',
	'Geodude': 'Rock',
	'Graveler': 'Rock',
	'Golem': 'Rock',
	'Ponyta': 'Fire',
	'Rapidash': 'Fire',
	'Slowpoke': 'Water',
	'Slowbro': 'Water',
	'Magnemite': 'Electric',
	'Magneton': 'Electric',
	'Farfetch’d': 'Normal',
	'Doduo': 'Normal',
	'Dodrio': 'Normal',
	'Seel': 'Water',
	'Dewgong': 'Water',
	'Grimer': 'Poison',
	'Muk': 'Poison',
	'Shellder': 'Water',
	'Cloyster': 'Water',
	'Gastly': 'Ghost',
	'Haunter': 'Ghost',
	'Gengar': 'Ghost',
	'Onix': 'Rock',
	'Drowzee': 'Psychic',
	'Hypno': 'Psychic',
	'Krabby': 'Water',
	'Kingler': 'Water',
	'Voltorb': 'Electric',
	'Electrode': 'Electric',
	'Exeggcute': 'Grass',
	'Exeggutor': 'Grass',
	'Cubone': 'Ground',
	'Marowak': 'Ground',
	'Hitmonlee': 'Fighting',
	'Hitmonchan': 'Fighting',
	'Lickitung': 'Normal',
	'Koffing': 'Poison',
	'Weezing': 'Poison',
	'Rhyhorn': 'Ground',
	'Rhydon': 'Ground',
	'Chansey': 'Normal',
	'Tangela': 'Grass',
	'Kangaskhan': 'Normal',
	'Horsea': 'Water',
	'Seadra': 'Water',
	'Goldeen': 'Water',
	'Seaking': 'Water',
	'Staryu': 'Water',
	'Starmie': 'Water',
	'Mr. Mime': 'Psychic',
	'Scyther': 'Bug',
	'Jynx': 'Ice',
	'Electabuzz': 'Electric',
	'Magmar': 'Fire',
	'Pinsir': 'Bug',
	'Tauros': 'Normal',
	'Magikarp': 'Water',
	'Gyarados': 'Water',
	'Lapras': 'Water',
	'Ditto': 'Normal',
	'Eevee': 'Normal',
	'Vaporeon': 'Water',
	'Jolteon': 'Electric',
	'Flareon': 'Fire',
	'Porygon': 'Normal',
	'Omanyte': 'Rock',
	'Omastar': 'Rock',
	'Kabuto': 'Rock',
	'Kabutops': 'Rock',
	'Aerodactyl': 'Rock',
	'Snorlax': 'Normal',
	'Articuno': 'Ice',
	'Zapdos': 'Electric',
	'Moltres': 'Fire',
	'Dratini': 'Dragon',
	'Dragonair': 'Dragon',
	'Dragonite': 'Dragon',
	'Mewtwo': 'Psychic',
	'Mew': 'Psychic',
	'Chikorita': 'Grass',
	'Bayleef': 'Grass',
	'Meganium': 'Grass',
	'Cyndaquil': 'Fire',
	'Quilava': 'Fire',
	'Typhlosion': 'Fire',
	'Totodile': 'Water',
	'Croconaw': 'Water',
	'Feraligatr': 'Water',
	'Sentret': 'Normal',
	'Furret': 'Normal',
	'Hoothoot': 'Normal',
	'Noctowl': 'Normal',
	'Ledyba': 'Bug',
	'Ledian': 'Bug',
	'Spinarak': 'Bug',
	'Ariados': 'Bug',
	'Crobat': 'Poison',
	'Chinchou': 'Water',
	'Lanturn': 'Water',
	'Pichu': 'Electric',
	'Cleffa': 'Normal',
	'Igglybuff': 'Normal',
	'Togepi': 'Normal',
	'Togetic': 'Normal',
	'Natu': 'Psychic',
	'Xatu': 'Psychic',
	'Mareep': 'Electric',
	'Flaaffy': 'Electric',
	'Ampharos': 'Electric',
	'Bellossom': 'Grass',
	'Marill': 'Water',
	'Azumarill': 'Water',
	'Sudowoodo': 'Rock',
	'Politoed': 'Water',
	'Hoppip': 'Grass',
	'Skiploom': 'Grass',
	'Jumpluff': 'Grass',
	'Aipom': 'Normal',
	'Sunkern': 'Grass',
	'Sunflora': 'Grass',
	'Yanma': 'Bug',
	'Wooper': 'Water',
	'Quagsire': 'Water',
	'Espeon': 'Psychic',
	'Umbreon': 'Dark',
	'Murkrow': 'Dark',
	'Slowking': 'Water',
	'Misdreavus': 'Ghost',
	'Unown': 'Psychic',
	'Wobbuffet': 'Psychic',
	'Girafarig': 'Normal',
	'Pineco': 'Bug',
	'Forretress': 'Bug',
	'Dunsparce': 'Normal',
	'Gligar': 'Ground',
	'Steelix': 'Steel',
	'Snubbull': 'Normal',
	'Granbull': 'Normal',
	'Qwilfish': 'Water',
	'Scizor': 'Bug',
	'Shuckle': 'Bug',
	'Heracross': 'Bug',
	'Sneasel': 'Dark',
	'Teddiursa': 'Normal',
	'Ursaring': 'Normal',
	'Slugma': 'Fire',
	'Magcargo': 'Fire',
	'Swinub': 'Ice',
	'Piloswine': 'Ice',
	'Corsola': 'Water',
	'Remoraid': 'Water',
	'Octillery': 'Water',
	'Delibird': 'Ice',
	'Mantine': 'Water',
	'Skarmory': 'Steel',
	'Houndour': 'Dark',
	'Houndoom': 'Dark',
	'Kingdra': 'Water',
	'Phanpy': 'Ground',
	'Donphan': 'Ground',
	'Porygon2': 'Normal',
	'Stantler': 'Normal',
	'Smeargle': 'Normal',
	'Tyrogue': 'Fighting',
	'Hitmontop': 'Fighting',
	'Smoochum': 'Ice',
	'Elekid': 'Electric',
	'Magby': 'Fire',
	'Miltank': 'Normal',
	'Blissey': 'Normal',
	'Raikou': 'Electric',
	'Entei': 'Fire',
	'Suicune': 'Water',
	'Larvitar': 'Rock',
	'Pupitar': 'Rock',
	'Tyranitar': 'Rock',
	'Lugia': 'Psychic',
	'Ho-Oh': 'Fire',
	'Celebi': 'Psychic',
	'Treecko': 'Grass',
	'Grovyle': 'Grass',
	'Sceptile': 'Grass',
	'Torchic': 'Fire',
	'Combusken': 'Fire',
	'Blaziken': 'Fire',
	'Mudkip': 'Water',
	'Marshtomp': 'Water',
	'Swampert': 'Water',
	'Poochyena': 'Dark',
	'Mightyena': 'Dark',
	'Zigzagoon': 'Normal',
	'Linoone': 'Normal',
	'Wurmple': 'Bug',
	'Silcoon': 'Bug',
	'Beautifly': 'Bug',
	'Cascoon': 'Bug',
	'Dustox': 'Bug',
	'Lotad': 'Water',
	'Lombre': 'Water',
	'Ludicolo': 'Water',
	'Seedot': 'Grass',
	'Nuzleaf': 'Grass',
	'Shiftry': 'Grass',
	'Taillow': 'Normal',
	'Swellow': 'Normal',
	'Wingull': 'Water',
	'Pelipper': 'Water',
	'Ralts': 'Psychic',
	'Kirlia': 'Psychic',
	'Gardevoir': 'Psychic',
	'Surskit': 'Bug',
	'Masquerain': 'Bug',
	'Shroomish': 'Grass',
	'Breloom': 'Grass',
	'Slakoth': 'Normal',
	'Vigoroth': 'Normal',
	'Slaking': 'Normal',
	'Nincada': 'Bug',
	'Ninjask': 'Bug',
	'Shedinja': 'Bug',
	'Whismur': 'Normal',
	'Loudred': 'Normal',
	'Exploud': 'Normal',
	'Makuhita': 'Fighting',
	'Hariyama': 'Fighting',
	'Azurill': 'Normal',
	'Nosepass': 'Rock',
	'Skitty': 'Normal',
	'Delcatty': 'Normal',
	'Sableye': 'Dark',
	'Mawile': 'Steel',
	'Aron': 'Steel',
	'Lairon': 'Steel',
	'Aggron': 'Steel',
	'Meditite': 'Fighting',
	'Medicham': 'Fighting',
	'Electrike': 'Electric',
	'Manectric': 'Electric',
	'Plusle': 'Electric',
	'Minun': 'Electric',
	'Volbeat': 'Bug',
	'Illumise': 'Bug',
	'Roselia': 'Grass',
	'Gulpin': 'Poison',
	'Swalot': 'Poison',
	'Carvanha': 'Water',
	'Sharpedo': 'Water',
	'Wailmer': 'Water',
	'Wailord': 'Water',
	'Numel': 'Fire',
	'Camerupt': 'Fire',
	'Torkoal': 'Fire',
	'Spoink': 'Psychic',
	'Grumpig': 'Psychic',
	'Spinda': 'Normal',
	'Trapinch': 'Ground',
	'Vibrava': 'Ground',
	'Flygon': 'Ground',
	'Cacnea': 'Grass',
	'Cacturne': 'Grass',
	'Swablu': 'Normal',
	'Altaria': 'Dragon',
	'Zangoose': 'Normal',
	'Seviper': 'Poison',
	'Lunatone': 'Rock',
	'Solrock': 'Rock',
	'Barboach': 'Water',
	'Whiscash': 'Water',
	'Corphish': 'Water',
	'Crawdaunt': 'Water',
	'Baltoy': 'Ground',
	'Claydol': 'Ground',
	'Lileep': 'Rock',
	'Cradily': 'Rock',
	'Anorith': 'Rock',
	'Armaldo': 'Rock',
	'Feebas': 'Water',
	'Milotic': 'Water',
	'Castform': 'Normal',
	'Kecleon': 'Normal',
	'Shuppet': 'Ghost',
	'Banette': 'Ghost',
	'Duskull': 'Ghost',
	'Dusclops': 'Ghost',
	'Tropius': 'Grass',
	'Chimecho': 'Psychic',
	'Absol': 'Dark',
	'Wynaut': 'Psychic',
	'Snorunt': 'Ice',
	'Glalie': 'Ice',
	'Spheal': 'Ice',
	'Sealeo': 'Ice',
	'Walrein': 'Ice',
	'Clamperl': 'Water',
	'Huntail': 'Water',
	'Gorebyss': 'Water',
	'Relicanth': 'Water',
	'Luvdisc': 'Water',
	'Bagon': 'Dragon',
	'Shelgon': 'Dragon',
	'Salamence': 'Dragon',
	'Beldum': 'Steel',
	'Metang': 'Steel',
	'Metagross': 'Steel',
	'Regirock': 'Rock',
	'Regice': 'Ice',
	'Registeel': 'Steel',
	'Latias': 'Dragon',
	'Latios': 'Dragon',
	'Kyogre': 'Water',
	'Groudon': 'Ground',
	'Rayquaza': 'Dragon',
	'Jirachi': 'Steel',
	'Deoxys': 'Psychic',
	'Turtwig': 'Grass',
	'Grotle': 'Grass',
	'Torterra': 'Grass',
	'Chimchar': 'Fire',
	'Monferno': 'Fire',
	'Infernape': 'Fire',
	'Piplup': 'Water',
	'Prinplup': 'Water',
	'Empoleon': 'Water',
	'Starly': 'Normal',
	'Staravia': 'Normal',
	'Staraptor': 'Normal',
	'Bidoof': 'Normal',
	'Bibarel': 'Normal',
	'Kricketot': 'Bug',
	'Kricketune': 'Bug',
	'Shinx': 'Electric',
	'Luxio': 'Electric',
	'Luxray': 'Electric',
	'Budew': 'Grass',
	'Roserade': 'Grass',
	'Cranidos': 'Rock',
	'Rampardos': 'Rock',
	'Shieldon': 'Rock',
	'Bastiodon': 'Rock',
	'Burmy': 'Bug',
	'Wormadam': 'Bug',
	'Mothim': 'Bug',
	'Combee': 'Bug',
	'Vespiquen': 'Bug',
	'Pachirisu': 'Electric',
	'Buizel': 'Water',
	'Floatzel': 'Water',
	'Cherubi': 'Grass',
	'Cherrim': 'Grass',
	'Shellos': 'Water',
	'Gastrodon': 'Water',
	'Ambipom': 'Normal',
	'Drifloon': 'Ghost',
	'Drifblim': 'Ghost',
	'Buneary': 'Normal',
	'Lopunny': 'Normal',
	'Mismagius': 'Ghost',
	'Honchkrow': 'Dark',
	'Glameow': 'Normal',
	'Purugly': 'Normal',
	'Chingling': 'Psychic',
	'Stunky': 'Poison',
	'Skuntank': 'Poison',
	'Bronzor': 'Steel',
	'Bronzong': 'Steel',
	'Bonsly': 'Rock',
	'Mime Jr.': 'Psychic',
	'Happiny': 'Normal',
	'Chatot': 'Normal',
	'Spiritomb': 'Ghost',
	'Gible': 'Dragon',
	'Gabite': 'Dragon',
	'Garchomp': 'Dragon',
	'Munchlax': 'Normal',
	'Riolu': 'Fighting',
	'Lucario': 'Fighting',
	'Hippopotas': 'Ground',
	'Hippowdon': 'Ground',
	'Skorupi': 'Poison',
	'Drapion': 'Poison',
	'Croagunk': 'Poison',
	'Toxicroak': 'Poison',
	'Carnivine': 'Grass',
	'Finneon': 'Water',
	'Lumineon': 'Water',
	'Mantyke': 'Water',
	'Snover': 'Grass',
	'Abomasnow': 'Grass',
	'Weavile': 'Dark',
	'Magnezone': 'Electric',
	'Lickilicky': 'Normal',
	'Rhyperior': 'Ground',
	'Tangrowth': 'Grass',
	'Electivire': 'Electric',
	'Magmortar': 'Fire',
	'Togekiss': 'Normal',
	'Yanmega': 'Bug',
	'Leafeon': 'Grass',
	'Glaceon': 'Ice',
	'Gliscor': 'Ground',
	'Mamoswine': 'Ice',
	'Porygon-Z': 'Normal',
	'Gallade': 'Psychic',
	'Probopass': 'Rock',
	'Dusknoir': 'Ghost',
	'Froslass': 'Ice',
	'Rotom': 'Electric',
	'Uxie': 'Psychic',
	'Mesprit': 'Psychic',
	'Azelf': 'Psychic',
	'Dialga': 'Steel',
	'Palkia': 'Water',
	'Heatran': 'Fire',
	'Regigigas': 'Normal',
	'Giratina': 'Ghost',
	'Cresselia': 'Psychic',
	'Phione': 'Water',
	'Manaphy': 'Water',
	'Darkrai': 'Dark',
	'Shaymin': 'Grass',
	'Arceus': 'Normal',
}

class AddWin:
	# player="p1" is temp
	def __init__(self):
		p2manager = player_manager.PlayerManager(player="p2")
		p3manager = player_manager.PlayerManager(player="p3")
		p1manager = player_manager.PlayerManager(player="p1")
		trio_win = tk.Toplevel()
		trio_win.geometry("500x300")
		trio_win.resizable(False, False)
		trio_win.title("Add a Trio")

		def check_input(event, input):
			value = event.widget.get()
			data = []
			for item in lst:
				if value.lower() in item.lower():
					data.append(item)
				input['values'] = data

		def update_pic(event, input, player):
			mon = event.widget.get()
			if mon not in lst:
				return
			mon = mon.lower()
			mon_image = f"{mon}.png"
			image = tk.PhotoImage(master=trio_win, file=f"./mons/{mon_image}")
			player.configure(image=image)
			player.image = image
		#TODO check if trio passes type limit on team, if so add to PC
		def addtrio():
			if p2_box.get() == "" or p1_box.get() == "" or p1_box.get() == "":
				# add an exception window here
				return
			p2manager.addMon(p2_box.get(), types[p2_box.get()], route_box.get())
			p3manager.addMon(p3_box.get(), types[p3_box.get()], route_box.get())
			p1manager.addMon(p1_box.get(), types[p1_box.get()], route_box.get())

		# creating Comp3ox
		p2 = ttk.Label(trio_win, text="p2")
		p2_box = ttk.Combobox(trio_win)
		p3 = ttk.Label(trio_win, text="p3")
		p3_box = ttk.Combobox(trio_win)
		p1 = ttk.Label(trio_win, text="p1by")
		p1_box = ttk.Combobox(trio_win)
		selecting = tk.PhotoImage(master=trio_win, file="./mons/default.png")
		p2_mon_img_label = ttk.Label(trio_win, image=selecting)
		p3_mon_img_label = ttk.Label(trio_win, image=selecting)
		p1_mon_img_label = ttk.Label(trio_win, image=selecting)
		p2_box['values'] = p3_box['values'] = p1_box['values'] = lst

		route_box = ttk.Entry(trio_win)
		route = ttk.Label(trio_win, text="route number")

		# update boxes after key presses to "search"
		p2_box.bind('<KeyRelease>', lambda event: check_input(event, p2_box))
		p3_box.bind('<KeyRelease>', lambda event: check_input(event, p3_box))
		p1_box.bind('<KeyRelease>', lambda event: check_input(event, p1_box))

		# update the picture of the selected pokemon above the box
		# might want to change the event check docs online
		p2_box.bind('<FocusOut>', lambda event: update_pic(event, p2_box, p2_mon_img_label))
		p3_box.bind('<FocusOut>', lambda event: update_pic(event, p3_box, p3_mon_img_label))
		p1_box.bind('<FocusOut>', lambda event: update_pic(event, p1_box, p1_mon_img_label))

		p2_mon_img_label.grid(row=0, column=0)
		p3_mon_img_label.grid(row=0, column=1)
		p1_mon_img_label.grid(row=0, column=2)
		p2_box.grid(row=1, column=0, padx=10, pady=(10, 0))
		p3_box.grid(row=1, column=1, padx=10, pady=(10, 0))
		p1_box.grid(row=1, column=2, padx=10, pady=(10, 0))
		p2.grid(row=2, column=0, padx=10)
		p3.grid(row=2, column=1, padx=10)
		p1.grid(row=2, column=2, padx=10)
		route_box.grid(row=3, column=1, pady=(50, 0))
		route.grid(row=4, column=1)

		add_button = tk.Button(trio_win, text="add", command=addtrio)
		add_button.grid(row=4, column=2)

		mon = p1_box.get()
		print(mon)

		trio_win.mainloop()