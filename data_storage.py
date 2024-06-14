from data_definitions import Weapon, Armor, LegArmor, Boots, Bracers, Helmet, Shield, Jewelry
from data_definitions import Characteristics, Qualities, Health, Fatigue, Sanity, InstinctiveReactions, Specializations, Competences, Player, Species, calculate_load_capacity, predefined_specializations, specializations
from data_definitions import Technique, Maneuver, Gift, techniques, maneuvers, gifts
import json
import math

with open('techniques.json') as file:
    technique_data = json.load(file)
    for name, data in technique_data.items():
        techniques[name] = Technique(**data)

with open('maneuvers.json') as file:
    maneuver_data = json.load(file)
    for name, data in maneuver_data.items():
        maneuvers[name] = Maneuver(**data)

with open('gifts.json') as file:
    gift_data = json.load(file)
    for name, data in gift_data.items():
        gifts[name] = Gift(**data)

def get_techniques():
    return techniques

def get_maneuvers():
    return maneuvers

def get_gifts():
    return gifts

weapons = {
    "armas_de_asta": [
        Weapon("Lochaber", "Cortante", "Arma de Asta", 2, "d12", "2mts", 5.5, "strength", "Dominante","melee"),
        Weapon("Guja", "Cortante o Perforante", "Arma de Asta", 2, "d10", "2mts", 5, "strength", "Dominante","melee"),
        Weapon("Alabarda", "Cortante o Perforante", "Arma de Asta", 2, "d10", "2mts", 4.5, "strength", "Dominante","melee"),
        Weapon("Naginata", "Cortante", "Arma de Asta", 2, "d12", "2mts", 4.5, "strength", "Dominante","melee")
    ],
    "lanzas": [
        Weapon("Lancea", "Perforante", "Lanza", 2, "d12", "2mts", 4, "strength", "Dominante","melee"),
        Weapon("Partesana", "Perforante o Cortante", "Lanza", 2, "d10", "2mts", 4.5, "strength", "Dominante","melee"),
        Weapon("Kontos", "Perforante", "Lanza", 2, "d12", "2mts", 5, "strength", "Dominante","melee"),
        Weapon("Yari", "Perforante", "Lanza", 2, "d12", "2mts", 4.2, "strength", "Dominante","melee"),
        Weapon("Hasta", "Perforante", "Lanza", 1, "d8", "1mt", 2.5, "strength", "Dominante","melee"),
        Weapon("Dory", "Perforante", "Lanza", 1, "d8", "1mt", 2.3, "strength", "Dominante","melee")
    ],
    "hachas": [
        Weapon("Esparta", "Cortante", "Hacha", 2, "d10", "2mts", 4, "tenacity", "Dominante","melee"),
        Weapon("Sagaris", "Cortante", "Hacha", 1, "d8", "1mt", 2, "strength", "Dominante","melee"),
        Weapon("Skeggøx", "Cortante", "Hacha", 1, "d8", "1mts", 2, "strength", "Dominante","melee"),
        Weapon("Labrys", "Cortante", "Hacha", 2, "d12", "2mts", 3.5, "tenacity", "Dominante","melee")
    ],
    "mazas": [
        Weapon("Morgenstern", "Contundente", "Maza", 1, "d8", "1mt", 2, "strength", "Dominante","melee"),
        Weapon("Nekhakha", "Contundente", "Maza", 1, "d8", "1mt", 2, "strength", "Dominante","melee"),
        Weapon("Kanabo", "Contundente", "Maza", 2, "d10", "2mts", 5, "strength", "Dominante","melee")
    ],
    "hojas_largas": [
        Weapon("Katana", "Cortante", "Espada Larga", 1, "d8", "1mt", 1.2, "agility", "Dominante","melee"),
        Weapon("Spatha", "Cortante", "Espada Larga", 1, "d8", "1mt", 1, "strength", "Dominante","melee"),
        Weapon("Khopesh", "Cortante", "Espada Larga", 1, "d8", "1mt", 1.5, "strength", "Dominante","melee"),
        Weapon("Shamshir", "Cortante", "Espada Larga", 1, "d8", "1mt", 1, "agility", "Dominante","melee"),
        Weapon("Claymore", "Cortante", "Espada Larga", 2, "d12", "2mts", 2.5, "tenacity", "Dominante","melee"),
        Weapon("Mandoble", "Cortante", "Espada Larga", 2, "d10", "2mts", 2, "tenacity", "Dominante","melee")
    ],
    "dagas": [
        Weapon("Sai", "Perforante", "Daga", 1, "d4", "1mt", 0.7, "agility", "Secundaria","melee"),
        Weapon("Jutee", "Contundente", "Daga", 1, "d4", "1mt", 0.6, "cunning", "Secundaria","melee"),
        Weapon("Scian", "Perforante", "Daga", 1, "d4", "1mt", 0.5, "agility", "Secundaria","melee")
    ],
    "hojas_cortas": [
        Weapon("Wakizashi", "Cortante", "Espada Corta", 1, "d6", "1mt", 0.9, "agility", "Dominante","melee"),
        Weapon("Tanto", "Cortante", "Espada Corta", 1, "d4", "1mt", 0.6, "agility", "Secundaria","melee"),
        Weapon("Kama", "Cortante", "Espada Corta", 1, "d6", "1mt", 0.7, "agility", "Dominante","melee"),
        Weapon("Claideamh", "Perforante", "Espada Corta", 1, "d6", "1mt", 0.8, "strength", "Dominante","melee"),
        Weapon("Seax", "Cortante", "Espada Corta", 1, "d4", "1mt", 0.7, "strength", "Secundaria","melee"),
        Weapon("Cimitarra", "Cortante", "Espada Corta", 1, "d6", "1mt", 0.8, "agility", "Dominante","melee"),
        Weapon("Akinakes", "Cortante", "Espada Corta", 1, "d6", "1mt", 0.7, "agility", "Dominante","melee"),
        Weapon("Xiphos", "Cortante", "Espada Corta", 1, "d4", "1mt", 0.8, "agility", "Secundaria","melee")
    ],
    "armas_arrojadizas": [
        Weapon("Kunai", "Perforante", "Arrojadiza", 1, "d4", "10mts", 0.3, "agility", "Secundaria", "ranged"),
        Weapon("Shuriken", "Perforante", "Arrojadiza", 1, "d4", "10mts", 0.2, "agility", "Secundaria", "ranged"),
        Weapon("Pilum", "Perforante", "Lanza Arrojadiza", 1, "d6", "10mts", 1.5, "strength", "Dominante", "ranged"),
        Weapon("Francisca", "Cortante", "Hacha Arrojadiza", 1, "d6", "10mts", 1.4, "strength", "Dominante", "ranged")
    ],
    "armas_a_distancia": [
        Weapon("Yumi", "Según Proyectil", "Distancia", 2, "d8", "30mts", 1, "agility", "Dominante", "ranged"),
        Weapon("Gakgung", "Según Proyectil", "Distancia", 2, "d6", "20mts", 1, "agility", "Dominante", "ranged"),
        Weapon("Fukiya", "Según Proyectil", "Distancia", 1, "d4", "20mts", 0.5, "agility", "Dominante", "ranged"),
        Weapon("Scythian", "Según Proyectil", "Distancia (Sobre Montura)", 2, "d8", "30mts", 1, "strength", "Dominante", "ranged"),
        Weapon("Balearic", "Según Proyectil", "Distancia", 1, "d4", "20mts", 0.7, "agility", "Dominante", "ranged"),
        Weapon("Sumpit", "Según Proyectil", "Distancia", 1, "d4", "20mts", 0.5, "agility", "Dominante", "ranged")
    ],
    "armas_flexibles": [
        Weapon("Kusarigama", "Hoz(Cortante),Cadena(Contundente)", "Flexible", 2, "Hoz(d6),Cadena(d4)", "Hoz(1mt),Cadena(3mts)", 1.5, "agility", "Dominante","melee"),
        Weapon("Scourge", "Contundente", "Flexible", 1, "d4", "1-3mts", 1, "strength", "Secundaria","melee"),
        Weapon("Nekode", "Cortante", "Flexible", 1, "d4", "1mt", 0.5, "agility", "Secundaria","melee"),
        Weapon("Kusari Fundo", "Contundente", "Flexible", 2, "d6", "1-3mts", 1.2, "cunning", "Dominante","melee"),
        Weapon("Guantes de Araña", "Cortante", "Flexible", 1, "d4", "1-3mts", 0.4, "agility", "Secundaria","melee")
    ]
}

# Modificadores para armaduras
def light_armor_bonus(characteristics, competencies, grade):
    return grade

def intermediate_armor_modifiers(characteristics, competencies, grade):
    agility = characteristics["agility"]
    evasive_competence = competencies["evasion"]
    return {
        "td_penalty": math.ceil(agility / 2),
        "te_penalty": math.ceil(evasive_competence / 2),
        "armor_bonus": grade * 2
    }

def heavy_armor_modifiers(characteristics, competencies, grade):
    return {
        "td_penalty": 0,
        "te_penalty": lambda characteristics, competencies, grade: (characteristics.agility + competencies.get_level("martial", "Evasion")) * -1,
        "armor_bonus": grade * 3
    }

# Modificadores para pantalones
def light_legs_bonus(characteristics, competencies, grade):
    competencies["Sigilo"] += grade
    return grade

def intermediate_legs_bonus(characteristics, competencies, grade):
    competencies["Acrobacias"] += grade
    competencies["Vigor"] += grade
    return grade

def heavy_legs_bonus(characteristics, competencies, grade):
    return grade

# Modificadores para botas
def light_boots_bonus(characteristics, competencies, qualities, grade):
    return grade

def intermediate_boots_bonus(characteristics, competencies, grade):
    return competencies["Equilibrio"] + grade

def heavy_boots_bonus(characteristics, competencies, grade):
    return grade

# Modificadores para brazales
def light_bracers_bonus(characteristics, competencies, grade):
    return grade

def intermediate_bracers_bonus(characteristics, competencies, grade):
    return grade

def heavy_bracers_bonus(characteristics, competencies, grade):
    return grade

# Modificadores para cascos
def light_helmet_bonus(characteristics, competencies, grade):
    characteristics["preparation"] += grade
    return grade

def intermediate_helmet_bonus(characteristics, competencies, grade):
    competencies["Enfoque"] += grade
    return grade

def heavy_helmet_bonus(characteristics, competencies, grade):
    return grade

def pendant_bonus(characteristics, competencies, grade):
    return grade

def amulet_bonus(characteristics, competencies, grade, choice):
    print(f"Calculando bono del amuleto: choice {choice}, grade {grade}")  # Agregar esta línea
    if choice == "aguante":
        characteristics.endurance_bonus += grade
    elif choice == "cordura":
        characteristics.sanity_bonus += grade
    elif choice == "preparacion":
        characteristics.preparation_bonus += grade
    return grade

def badge_bonus(characteristics, competencies, grade):
    return grade

armors = {
    "armadura_ligera": Armor(
        name="Armadura Ligera",
        category="Ligero",
        base_armor_bonus=light_armor_bonus,
        td_penalty=None,
        te_penalty=None,
        weight=3,
        grade=1
    ),
    "armadura_intermedia": Armor(
        name="Armadura Intermedia",
        category="Intermedio",
        base_armor_bonus=lambda characteristics, competencies, grade: grade * 2,
        td_penalty=lambda characteristics, competencies, grade: math.ceil(characteristics.agility / 2),
        te_penalty=lambda characteristics, competencies, grade: math.ceil(competencies.get_bonus("martial", "Evasion") / 2),
        weight=6,
        grade=1,
        modifiers=[intermediate_armor_modifiers]
    ),
    "armadura_pesada": Armor(
        name="Armadura Pesada",
        category="Pesado",
        base_armor_bonus=lambda characteristics, competencies, grade: grade * 3,
        td_penalty=lambda characteristics, competencies, grade: 0,
        te_penalty=lambda characteristics, competencies, grade: 0,
        weight=9,
        grade=1,
        modifiers=[heavy_armor_modifiers]
    )
}

leg_armors = {
    "pantalones_ligeros": LegArmor(
        name="Pantalones Ligeros",
        category="Ligero",
        bonus=lambda characteristics, competencies, grade: grade,
        ta_penalty=None,
        weight=2,
        grade=1,
        descriptions=["Te mueves a velocidad normal a través de terreno difícil. Obtienes un bonificador de +{grade} para las tiradas de Sigilo."]
    ),
    "pantalones_intermedios": LegArmor(
        name="Pantalones Intermedios",
        category="Intermedio",
        bonus=lambda characteristics, competencies, grade, context: grade if context in ["acrobacias", "vigor"] else 0,
        ta_penalty=lambda grade: -grade,
        weight=4,
        grade=1,
        descriptions=["Penalizador de -{grade} a la tirada de ataque durante reacciones instintivas."]
    ),
    "pantalones_pesados": LegArmor(
        name="Pantalones Pesados",
        category="Pesado",
        bonus=lambda characteristics, competencies, grade: grade,
        ta_penalty=lambda grade: -(grade + 1),
        weight=6,
        grade=1,
        descriptions=["Bonificación a las tiradas de resistencia contra inmovilización y atrapado igual a {grade}.", 
                      "Penalizador de -{grade_plus_one} a la tirada de ataque durante reacciones instintivas."]
    )
}

boots = {
    "botas_ligeras": Boots(
        name="Botas Ligeras",
        category="Ligero",
        bonus=light_boots_bonus,
        tc_penalty=None,
        weight=1,
        grade=1
    ),
    "botas_intermedias": Boots(
        name="Botas Intermedias",
        category="Intermedio",
        bonus=lambda characteristics, competencies, qualities, grade: 0,
        tc_penalty=lambda grade: -grade,
        weight=2,
        grade=1
    ),
    "botas_pesadas": Boots(
        name="Botas Pesadas",
        category="Pesado",
        bonus=lambda characteristics, competencies, qualities, grade: 0,
        tc_penalty=lambda grade: -(grade + 1),
        weight=3,
        grade=1,
        description=["Bonificación a las T.R de alteraciones contra derribo, desplazamiento y desequilibrio igual al grado de la pieza."]
    )
}

bracers = {
    "brazales_ligeros": Bracers(
        name="Brazales Ligeros",
        category="Ligero",
        bonus=lambda characteristics, competencies, grade: grade,
        te_penalty=None,
        weight=2,
        grade=1,
        description=["Bonificación a la T.A durante las reacciones instintivas igual al grado de la pieza."]
    ),
    "brazales_intermedios": Bracers(
        name="Brazales Intermedios",
        category="Intermedio",
        bonus=lambda characteristics, competencies, grade: grade,
        te_penalty=lambda characteristics, competencies, grade: -grade,
        weight=3,
        grade=1,
        description=["Bonificación a la T.A al llevar a cabo maniobras de disciplina y armas igual al grado de la pieza."]
    ),
    "brazales_pesados": Bracers(
        name="Brazales Pesados",
        category="Pesado",
        bonus=lambda characteristics, competencies, grade: grade,
        te_penalty=lambda characteristics, competencies, grade: -(grade + 1),
        weight=4,
        grade=1,
        description=["Bonificación a la T.A o T.D al llevar a cabo maniobras de escudos igual al grado de la pieza."]
    )
}

helmets = {
    "casco_ligero": Helmet(
        name="Casco Ligero",
        category="Ligero",
        bonus=lambda grade: grade,
        te_penalty=None,
        weight=1,
        grade=1
    ),
    "casco_intermedio": Helmet(
        name="Casco Intermedio",
        category="Intermedio",
        bonus=lambda grade: grade,
        te_penalty=lambda grade: -grade,
        weight=2,
        grade=1
    ),
    "casco_pesado": Helmet(
        name="Casco Pesado",
        category="Pesado",
        bonus=lambda grade: grade,
        te_penalty=lambda grade: -(grade + 1),
        weight=3,
        grade=1,
        description=["Bonificación a las T.R de alteraciones contra conmoción, ceguera y aturdimiento igual al grado de la pieza."]
    )
}

shields = {
    "escudo_liviano": Shield(
        name="Escudo Liviano",
        category="Liviano",
        coverage_bonus=None,
        armor_bonus=None,
        movement_penalty=None,
        weight=2
    ),
    "escudo_mediano": Shield(
        name="Escudo Mediano",
        category="Mediano",
        coverage_bonus="Cobertura Ligera",
        armor_bonus=lambda grade: grade,
        movement_penalty=lambda grade: -(grade),
        weight=5
    ),
    "escudo_pesado": Shield(
        name="Escudo Pesado",
        category="Pesado",
        coverage_bonus="Cobertura Media",
        armor_bonus=lambda grade: grade * 2,
        movement_penalty=lambda grade: -(grade + 1),
        weight=10
    )
}

jewelry = {
    "colgante": Jewelry(
        name="Colgante",
        category="Colgante",
        bonus=None,
        weight=1,
        description="Permite utilizar objetos sin utilizar la acción Interactuar."
    ),
    "amuleto": Jewelry(
        name="Amuleto",
        category="Amuleto",
        bonus=amulet_bonus,
        weight=0.1,
        description=["Bonificación a aguante, cordura o preparación igual al grado (elige uno)."]
    ),
    "insignia": Jewelry(
        name="Insignia",
        category="Insignia",
        bonus=badge_bonus,
        weight=0.1
    )
}

species_data = {
    "Naghii": Species(
        name="Naghii",
        size="Mediano",
        base_health=10,
        movement_speed=10,
        characteristic_bonuses={"agility": 1, "wisdom": 1, "presence": 1},
        languages={"Común": "rango3", "Sssarith": "rango3"}
    ),
    "Sauri": Species(
        name="Sauri",
        size="Grande",
        base_health=12,
        movement_speed=8,
        characteristic_bonuses={"strength": 1, "wisdom": 1, "composure": 1},
        languages={"Común": "rango3", "Zhirash": "rango3"}
    ),
    "Zarnag": Species(
        name="Zarnag",
        size="Mediano",
        base_health=10,
        movement_speed=10,
        characteristic_bonuses={"agility": 1, "cunning": 1, "presence": 1},
        languages={"Común": "rango3", "Zarnog": "rango3"}
    ),
    "Drakkai": Species(
        name="Drakkai",
        size="Grande",
        base_health=13,
        movement_speed=8,
        characteristic_bonuses={"tenacity": 1, "wisdom": 1, "presence": 1},
        languages={"Común": "rango3", "Drakar": "rango3"}
    ),
    "Rokhart": Species(
        name="Rokhart",
        size="Mediano",
        base_health=9,
        movement_speed=9,
        characteristic_bonuses={"agility": 1, "intellect": 1, "composure": 1},
        languages={"Común": "rango3", "Rokha": "rango3"}
    ),
    "Loxod": Species(
        name="Loxod",
        size="Grande",
        base_health=14,
        movement_speed=8,
        characteristic_bonuses={"tenacity": 1, "wisdom": 1, "composure": 1},
        languages={"Común": "rango3", "Loxian": "rango3"}
    ),
    "Ceratox": Species(
        name="Ceratox",
        size="Mediano",
        base_health=13,
        movement_speed=8,
        characteristic_bonuses={"strength": 1, "cunning": 1, "presence": 1},
        languages={"Común": "rango3", "Ceratik": "rango3"}
    ),
    "Formix": Species(
        name="Formix",
        size="Mediano",
        base_health=10,
        movement_speed=10,
        characteristic_bonuses={"agility": 1, "cunning": 1, "charisma": 1},
        languages={"Común": "rango3"}
    ),
    "Chelicer": Species(
        name="Chelicer",
        size="Mediano",
        base_health=11,
        movement_speed=10,
        characteristic_bonuses={"strength": 1, "wisdom": 1, "presence": 1},
        languages={"Común": "rango3", "Chelí": "rango3"}
    ),
    "Panin": Species(
        name="Panin",
        size="Pequeño",
        base_health=8,
        movement_speed=12,
        characteristic_bonuses={"agility": 1, "cunning": 1, "charisma": 1},
        languages={"Común": "rango3", "Paní": "rango3"}
    ),
    "Luphran": Species(
        name="Luphran",
        size="Mediano",
        base_health=11,
        movement_speed=9,
        characteristic_bonuses={"strength": 1, "wisdom": 1, "presence": 1},
        languages={"Común": "rango3", "Lupino": "rango3"}
    ),
    "Ursari": Species(
        name="Ursari",
        size="Grande",
        base_health=14,
        movement_speed=8,
        characteristic_bonuses={"tenacity": 1, "intellect": 1, "presence": 1},
        languages={"Común": "rango3", "Ursal": "rango3"}
    ),
    "Arakhel": Species(
        name="Arakhel",
        size="Mediano",
        base_health=10,
        movement_speed=11,
        characteristic_bonuses={"agility": 1, "cunning": 1, "composure": 1},
        languages={"Común": "rango3", "Arakhi": "rango3"}
    ),
    "Bufoni": Species(
        name="Bufoni",
        size="Pequeño",
        base_health=9,
        movement_speed=9,
        characteristic_bonuses={"agility": 1, "wisdom": 1, "composure": 1},
        languages={"Común": "rango3", "Grog": "rango3"}
    ),
    "Vesper": Species(
        name="Pteropido",
        size="Mediano",
        base_health=9,
        movement_speed=9,
        characteristic_bonuses={"strength": 1, "intellect": 1, "presence": 1},
        languages={"Común": "rango3", "Sangrath": "rango3"}
    ),
    "Lapinni": Species(
        name="Lapinni",
        size="Pequeño",
        base_health=8,
        movement_speed=12,
        characteristic_bonuses={"agility": 1, "cunning": 1, "charisma": 1},
        languages={"Común": "rango3", "Lepori": "rango3"}
    ),
    "Manto": Species(
        name="Manto",
        size="Mediano",
        base_health=10,
        movement_speed=11,
        characteristic_bonuses={"strength": 1, "wisdom": 1, "composure": 1},
        languages={"Común": "rango3", "Gryllarch": "rango3"}
    ),
    "Hystric": Species(
        name="Hystric",
        size="Mediano",
        base_health=9,
        movement_speed=9,
        characteristic_bonuses={"tenacity": 1, "intellect": 1, "charisma": 1},
        languages={"Común": "rango3", "Hystric": "rango3"}
    ),
    "Talpa": Species(
        name="Talpa",
        size="Mediano",
        base_health=9,
        movement_speed=9,
        characteristic_bonuses={"agility": 1, "cunning": 1, "composure": 1},
        languages={"Común": "rango3", "Talpi": "rango3"}
    ),
    "Myo": Species(
        name="Myo",
        size="Pequeño",
        base_health=8,
        movement_speed=12,
        characteristic_bonuses={"agility": 1, "cunning": 1, "charisma": 1},
        languages={"Común": "rango3", "Murin": "rango3"}
    )
}

def create_player():
    species = species_data["Drakkai"]
    characteristics = Characteristics(
        strength=10 + species.characteristic_bonuses.get("strength", 0),
        agility=12 + species.characteristic_bonuses.get("agility", 0),
        tenacity=14 + species.characteristic_bonuses.get("tenacity", 0),
        cunning=13 + species.characteristic_bonuses.get("cunning", 0),
        intellect=15 + species.characteristic_bonuses.get("intellect", 0),
        wisdom=11 + species.characteristic_bonuses.get("wisdom", 0),
        charisma=9 + species.characteristic_bonuses.get("charisma", 0),
        composure=8 + species.characteristic_bonuses.get("composure", 0),
        presence=7 + species.characteristic_bonuses.get("presence", 0)
    )

    competences = Competences()
    competences.add_competence("specialization", "Vigor", 5)
    competences.add_competence("specialization", "Acrobacias", 3)
    competences.add_competence("specialization", "Equitación", 3)
    competences.add_competence("specialization", "Equilibrio", 3)
    competences.add_competence("specialization", "Enfoque", 3)
    competences.add_competence("martial", "Khopesh", 5)
    competences.add_competence("martial", "Evasion", 4)
    competences.add_competence("resistance", "Veneno", 3)
    competences.add_competence("resistance", "Infeccion", 2)
    competences.add_competence("resistance", "Afliccion", 4)
    competences.add_competence("resistance", "Maldicion", 1)
    competences.add_competence("resistance", "Alteracion", 5)

    load_capacity = calculate_load_capacity(characteristics.strength, characteristics.resilience, species.size)

    qualities = Qualities(
        player_level=1, age=25, size=species.size,
        height=180, weight=75, load_capacity=load_capacity,
        languages=species.languages, movement_speed=species.movement_speed,
        heritage="Herencia de especie", legacies=["Legado 1", "Legado 2", "Legado 3"]
    )

    health = Health(
        species_base_health=species.base_health, discipline_base_health=10, tenacity=characteristics.tenacity, discipline_health_per_level=8
    )

    fatigue = Fatigue(
        tenacity=characteristics.tenacity
    )

    sanity = Sanity(
        composure=characteristics.composure
    )

    instinctive_reactions = InstinctiveReactions(
        tenacity=characteristics.tenacity
    )

    player = Player(
        name="Aragorn",
        species=species,
        characteristics=characteristics,
        qualities=qualities,
        health=health,
        fatigue=fatigue,
        sanity=sanity,
        instinctive_reactions=instinctive_reactions,
        competences=competences
    )

    khopesh = weapons["hojas_largas"][2]
    kunai = weapons["armas_arrojadizas"][0]
    player.inventory.equip_item(khopesh, "right_hand", grade=2)
    player.inventory.equip_item(kunai, "left_hand", grade=2)

    intermediate_armor = armors["armadura_intermedia"]
    shield = shields["escudo_mediano"]
    intermediate_pants = leg_armors["pantalones_intermedios"]
    light_boots = boots["botas_intermedias"]
    light_bracers = bracers["brazales_ligeros"]
    light_helmet = helmets["casco_ligero"]
    amulet = jewelry["amuleto"]
    badge = jewelry["insignia"]
    player.inventory.equip_item(badge, "pendant", grade=2)
    player.inventory.equip_item(amulet, "amulet", grade=2, choice="aguante")
    player.inventory.equip_item(light_boots, "boots", grade=2)
    player.inventory.equip_item(intermediate_armor, "armor", grade=2)
    player.inventory.equip_item(shield, "shield", grade=2)
    player.inventory.equip_item(intermediate_pants, "pants", grade=2)
    player.inventory.equip_item(light_bracers, "bracers", grade=2)
    player.inventory.equip_item(light_helmet, "helmet", grade=2)
    player.update_permanent_bonuses()

    return player

player = create_player()

# Actualizar el nivel del jugador
player.update_level(5)

# Comprobar los valores
print(player.health.current_health)
print(player.health.calculate_renewals(player))
print(player.qualities.load_capacity)
print(player.instinctive_reactions.reactions_left)
print(player.fatigue.calculate_fatigue(player))
print(player.qualities.movement_speed)

# Ejemplo de tirada de ataque
print(player.calculate_attack_roll("Khopesh"))

# Ejemplo de tirada de defensa
print(player.calculate_defense_roll())

# Ejemplo de tirada de resistencia
print(player.calculate_resistance_roll("Veneno"))
print(player.calculate_resistance_roll("Infeccion"))
print(player.calculate_resistance_roll("Afliccion"))
print(player.calculate_resistance_roll("Maldicion"))
print(player.calculate_resistance_roll("Alteracion"))
print(player.calculate_resistance_roll("Alteracion", context="Inmovilizado"))
print(player.calculate_resistance_roll("Alteracion", context="Derribado"))
print(player.calculate_resistance_roll("Alteracion", context="Desplazado"))
print(player.calculate_resistance_roll("Alteracion", context="Desequilibrado"))

# Ejemplo de tirada de ataque durante una reacción instintiva
print(player.calculate_attack_roll("Khopesh", context="reaccion_instintiva"))

# Obtener descripciones específicas de los pantalones equipados
for description in player.get_leg_armor_descriptions():
    print(description)

for characteristic in ["strength", "agility", "tenacity", "cunning", "intellect", "wisdom", "charisma", "composure", "presence"]:
    print(f"{characteristic.capitalize()} Roll: {player.calculate_characteristic_roll(characteristic)}")

print(player.calculate_impact_roll("Khopesh"))
print(player.calculate_impact_roll("Kunai"))
print(player.calculate_specialization_roll("Vigor"))
print(player.calculate_specialization_roll("Acrobacias"))
print(player.calculate_specialization_roll("Minería"))
print(player.calculate_specialization_roll("Titiritero"))
print(player.calculate_characteristic_roll("agility"))
print(player.calculate_specialization_roll("Equilibrio"))
print(player.calculate_specialization_roll("Equitación"))
print(player.calculate_specialization_roll("Sigilo"))
print(player.calculate_specialization_roll("Enfoque"))
print(player.calculate_specialization_roll("Percepción"))
print(player.calculate_specialization_roll("Influencia"))

# Listar todas las especializaciones para verificar su creación
player.list_specializations()
player.execute_technique("Visión Elemental")
player.execute_maneuver("Guardia Elemental")
player.apply_gift("Visiones Reveladoras")
print(player.calculate_resistance_roll("Alteracion", context="Conmocionado"))
print(player.calculate_resistance_roll("Alteracion", context="Cegado"))
print(player.calculate_resistance_roll("Alteracion", context="Aturdido"))
print(f"Aguante: {player.fatigue.calculate_endurance(player)}")
print(f"Cordura: {player.sanity.sanity}")
print(f"Preparación: {player.characteristics.preparation}")