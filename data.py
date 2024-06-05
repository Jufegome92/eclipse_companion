especies_hp = {
    "Naghii": 10, "Sauri": 12, "Zarnag": 10, "Drakkai": 13, "Rokhart": 9, "Loxod": 14,
    "Ceratox": 13, "Formix": 10, "Chelicer": 11, "Panin": 8, "Luphran": 11, "Ursari": 14,
    "Arakhel": 10, "Bufoni": 9, "Pteropido": 9, "Lepori": 8, "Gryllarch": 10, "Hystric": 9,
    "Talpi": 9, "Murin": 8
}

velocidades = {
    "Naghii": 10, "Sauri": 8, "Zarnag": 10, "Drakkai": 8, "Rokhart": 9, "Loxod": 8,
    "Ceratox": 8, "Formix": 10, "Chelicer": 10, "Panin": 12, "Luphran": 9, "Ursari": 8,
    "Arakhel": 11, "Bufoni": 9, "Pteropido": 9, "Lepori": 12, "Gryllarch": 11, "Hystric": 9,
    "Talpi": 9, "Murin": 12
}

disciplinas = {
    "Alma Ignea": {"inicial": 10, "avance": 8},
    "Poseido": {"inicial": 10, "avance": 8},
    "Caminante del Abismo": {"inicial": 8, "avance": 6},
    "Artillero": {"inicial": 8, "avance": 6},
    "Guardian": {"inicial": 12, "avance": 10},
    "Filo Danzante": {"inicial": 10, "avance": 8},
    "Destructor": {"inicial": 12, "avance": 10},
    "Tejedor": {"inicial": 8, "avance": 6},
    "Sombra": {"inicial": 8, "avance": 6},
    "Biogenetico": {"inicial": 8, "avance": 6},
    "Titiritero": {"inicial": 8, "avance": 6},
    "Primalista": {"inicial": 10, "avance": 8},
    "Pacifista": {"inicial": 12, "avance": 10}
}

lenguajes = {
    "Naghii": {"Común": "rango3", "Sssarith": "rango3"}, 
    "Sauri": {"Común": "rango3", "Zhirash": "rango3"}, 
    "Zarnag": {"Común": "rango3", "Zarnog": "rango3"}, 
    "Drakkai": {"Común": "rango3", "Drakar": "rango3"}, 
    "Rokhart": {"Común": "rango3", "Rokha": "rango3"}, 
    "Loxod": {"Común": "rango3", "Loxian": "rango3"},
    "Ceratox": {"Común": "rango3", "Ceratik": "rango3"}, 
    "Formix": {"Común": "rango3"}, 
    "Chelicer": {"Común": "rango3", "Chelí": "rango3"}, 
    "Panin": {"Común": "rango3", "Paní": "rango3"}, 
    "Luphran": {"Común": "rango3", "Lupino": "rango3"}, 
    "Ursari": {"Común": "rango3", "Ursal": "rango3"},
    "Arakhel": {"Común": "rango3", "Arakhi": "rango3"}, 
    "Bufoni": {"Común": "rango3", "Grog": "rango3"}, 
    "Pteropido": {"Común": "rango3", "Sangrath": "rango3"}, 
    "Lepori": {"Común": "rango3", "Lepori": "rango3"}, 
    "Gryllarch": {"Común": "rango3", "Gryllarch": "rango3"}, 
    "Hystric": {"Común": "rango3", "Hystric": "rango3"},
    "Talpi": {"Común": "rango3", "Talpi": "rango3"}, 
    "Murin": {"Común": "rango3", "Murin": "rango3"}
}


armas = {
    "Armas de Asta": {
        "Lochaber": {
            "categoría_de_daño": "Cortante",
            "tipo": "Arma de Asta",
            "manos": 2,
            "daño": "d12",
            "alcance": "2 mts",
            "peso": 5.5,
            "característica": "Fuerza",
            "asignación": "Dominante",
            "potencia": None,
            "durabilidad": None,
            "descripción": "Una alabarda escocesa con una hoja ancha en forma de hacha y un gancho, utilizada para desmontar caballeros."
        },
        "Guja": {
            "categoría_de_daño": "Cortante o Perforante",
            "tipo": "Arma de Asta",
            "manos": 2,
            "daño": "d10",
            "alcance": "2 mts",
            "peso": 5.0,
            "característica": "Fuerza",
            "asignación": "Dominante",
            "potencia": None,
            "durabilidad": None,
            "descripción": "Lanza de origen indio con una hoja curva en el extremo, utilizada tanto para empujar como para cortar."
        },
        "Alabarda": {
            "categoría_de_daño": "Cortante o Perforante",
            "tipo": "Arma de Asta",
            "manos": 2,
            "daño": "d10",
            "alcance": "2 mts",
            "peso": 4.5,
            "característica": "Fuerza",
            "asignación": "Dominante",
            "potencia": None,
            "durabilidad": None,
            "descripción": "Arma medieval que combina características de un hacha y una lanza, ideal para enganchar y cortar."
        },
        "Naginata": {
            "categoría_de_daño": "Cortante",
            "tipo": "Arma de Asta",
            "manos": 2,
            "daño": "d12",
            "alcance": "2 mts",
            "peso": 4.5,
            "característica": "Fuerza",
            "asignación": "Dominante",
            "potencia": None,
            "durabilidad": None,
            "descripción": "Lanza japonesa con una larga hoja curvada, utilizada por la infantería para cortar a los enemigos a distancia."
        }
    },
    "Lanzas": {
        "Lancea": {
            "categoría_de_daño": "Perforante",
            "tipo": "Lanza",
            "manos": 2,
            "daño": "d12",
            "alcance": "2 mts",
            "peso": 4.0,
            "característica": "Fuerza",
            "asignación": "Dominante",
            "potencia": None,
            "durabilidad": None,
            "descripción": "Lanza ligera utilizada en la antigua Roma, diseñada para ser arrojada o utilizada en combate cuerpo a cuerpo."
        },
        "Partesana": {
            "categoría_de_daño": "Perforante o Cortante",
            "tipo": "Lanza",
            "manos": 2,
            "daño": "d10",
            "alcance": "2 mts",
            "peso": 4.5,
            "característica": "Fuerza",
            "asignación": "Dominante",
            "potencia": None,
            "durabilidad": None,
            "descripción": "Una lanza de origen europeo con una hoja ancha, utilizada tanto para cortar como para empujar."
        },
        "Kontos": {
            "categoría_de_daño": "Perforante",
            "tipo": "Lanza",
            "manos": 2,
            "daño": "d12",
            "alcance": "2 mts",
            "peso": 5.0,
            "característica": "Fuerza",
            "asignación": "Dominante",
            "potencia": None,
            "durabilidad": None,
            "descripción": "Larga lanza de caballería utilizada por los sármatas y los partos, diseñada para combate a distancia."
        },
        "Yari": {
            "categoría_de_daño": "Perforante",
            "tipo": "Lanza",
            "manos": 2,
            "daño": "d12",
            "alcance": "2 mts",
            "peso": 4.2,
            "característica": "Fuerza",
            "asignación": "Dominante",
            "potencia": None,
            "durabilidad": None,
            "descripción": "Lanza japonesa tradicional utilizada por los samuráis, conocida por su hoja extremadamente afilada."
        },
        "Hasta": {
            "categoría_de_daño": "Perforante",
            "tipo": "Lanza",
            "manos": 1,
            "daño": "d8",
            "alcance": "1 mt",
            "peso": 2.5,
            "característica": "Fuerza",
            "asignación": "Dominante",
            "potencia": None,
            "durabilidad": None,
            "descripción": "Una lanza corta de mano usada por la infantería romana para el combate cercano y ágil."
        },
        "Dory": {
            "categoría_de_daño": "Perforante",
            "tipo": "Lanza",
            "manos": 1,
            "daño": "d8",
            "alcance": "1 mt",
            "peso": 2.3,
            "característica": "Fuerza",
            "asignación": "Dominante",
            "potencia": None,
            "durabilidad": None,
            "descripción": "Lanza clásica de los hoplitas griegos, esencial en la formación de falange."
        }
    },
    "Hachas": {
        "Esparta": {
            "categoría_de_daño": "Cortante",
            "tipo": "Hacha",
            "manos": 2,
            "daño": "d10",
            "alcance": "2 mts",
            "peso": 4.0,
            "característica": "Tenacidad",
            "asignación": "Dominante",
            "potencia": None,
            "durabilidad": None,
            "descripción": "Un hacha grande con una hoja pesada, ideal para derribar escudos y armaduras enemigas."
        },
        "Sagaris": {
            "categoría_de_daño": "Cortante",
            "tipo": "Hacha",
            "manos": 1,
            "daño": "d8",
            "alcance": "1 mt",
            "peso": 2.0,
            "característica": "Fuerza",
            "asignación": "Dominante",
            "potencia": None,
            "durabilidad": None,
            "descripción": "Pequeño hacha de batalla originaria de Persia, ágil y efectiva para combate a corta distancia."
        },
        "Skeggøx": {
            "categoría_de_daño": "Cortante",
            "tipo": "Hacha",
            "manos": 1,
            "daño": "d8",
            "alcance": "1 mts",
            "peso": 2.0,
            "característica": "Fuerza",
            "asignación": "Dominante",
            "potencia": None,
            "durabilidad": None,
            "descripción": "Hacha vikinga utilizada tanto en combate como para tareas diarias por su versatilidad."
        },
        "Labrys": {
            "categoría_de_daño": "Cortante",
            "tipo": "Hacha",
            "manos": 2,
            "daño": "d12",
            "alcance": "2 mts",
            "peso": 3.5,
            "característica": "Tenacidad",
            "asignación": "Dominante",
            "potencia": None,
            "durabilidad": None,
            "descripción": "Doble hacha ceremonial de origen minoico, simboliza la autoridad y el poder."
        }
    },
    "Mazas": {
        "Morgenstern": {
            "categoría_de_daño": "Contundente",
            "tipo": "Maza",
            "manos": 1,
            "daño": "d8",
            "alcance": "1 mt",
            "peso": 2.0,
            "característica": "Fuerza",
            "asignación": "Dominante",
            "potencia": None,
            "durabilidad": None,
            "descripción": "Maza con cabeza esférica adornada con púas, eficaz contra armaduras de malla y placas."
        },
        "Nekhakha": {
            "categoría_de_daño": "Contundente",
            "tipo": "Maza",
            "manos": 1,
            "daño": "d8",
            "alcance": "1 mt",
            "peso": 2.0,
            "característica": "Fuerza",
            "asignación": "Dominante",
            "potencia": None,
            "durabilidad": None,
            "descripción": "Maza egipcia ligera utilizada por faraones como símbolo de poder y herramienta de guerra."
        },
        "Kanabo": {
            "categoría_de_daño": "Contundente",
            "tipo": "Maza",
            "manos": 2,
            "daño": "d10",
            "alcance": "2 mts",
            "peso": 5.0,
            "característica": "Fuerza",
            "asignación": "Dominante",
            "potencia": None,
            "durabilidad": None,
            "descripción": "Gran maza de madera reforzada con hierro usada por los samuráis para romper armaduras y escudos."
        }
    },
    "Hojas Largas": {
        "Katana": {
            "categoría_de_daño": "Cortante",
            "tipo": "Espada Larga",
            "manos": 1,
            "daño": "d8",
            "alcance": "1 mt",
            "peso": 1.2,
            "característica": "Agilidad",
            "asignación": "Dominante",
            "potencia": None,
            "durabilidad": None,
            "descripción": "Espada japonesa conocida por su hoja curva y afilada, símbolo de los samuráis."
        },
        "Spatha": {
            "categoría_de_daño": "Cortante",
            "tipo": "Espada Larga",
            "manos": 1,
            "daño": "d8",
            "alcance": "1 mt",
            "peso": 1.0,
            "característica": "Fuerza",
            "asignación": "Dominante",
            "potencia": None,
            "durabilidad": None,
            "descripción": "Espada larga usada por los soldados romanos y los guerreros germánicos, efectiva tanto a caballo como a pie."
        },
        "Khopesh": {
            "categoría_de_daño": "Cortante",
            "tipo": "Espada Larga",
            "manos": 1,
            "daño": "d8",
            "alcance": "1 mt",
            "peso": 1.5,
            "característica": "Fuerza",
            "asignación": "Dominante",
            "potencia": None,
            "durabilidad": None,
            "descripción": "Espada egipcia con hoja en forma de hoz, usada para atrapar armas del enemigo o desmontarlos."
        },
        "Shamshir": {
            "categoría_de_daño": "Cortante",
            "tipo": "Espada Larga",
            "manos": 1,
            "daño": "d8",
            "alcance": "1 mt",
            "peso": 1.0,
            "característica": "Agilidad",
            "asignación": "Dominante",
            "potencia": None,
            "durabilidad": None,
            "descripción": "Espada persa con una hoja curva pronunciada, optimizada para cortes de tajo."
        },
        "Claymore": {
            "categoría_de_daño": "Cortante",
            "tipo": "Espada Larga",
            "manos": 2,
            "daño": "d12",
            "alcance": "2 mts",
            "peso": 2.5,
            "característica": "Tenacidad",
            "asignación": "Dominante",
            "potencia": None,
            "durabilidad": None,
            "descripción": "Gran espada de dos manos originaria de Escocia, famosa por su uso en batallas formacionales y duelos."
        },
        "Mandoble": {
            "categoría_de_daño": "Cortante",
            "tipo": "Espada Larga",
            "manos": 2,
            "daño": "d10",
            "alcance": "2 mts",
            "peso": 2.0,
            "característica": "Tenacidad",
            "asignación": "Dominante",
            "potencia": None,
            "durabilidad": None,
            "descripción": "Espada de dos manos usada en Europa durante la Edad Media, capaz de infligir cortes devastadores."
        }
    },
    "Dagas": {
        "Sai": {
            "categoría_de_daño": "Perforante",
            "tipo": "Daga",
            "manos": 1,
            "daño": "d4",
            "alcance": "1 mt",
            "peso": 0.7,
            "característica": "Agilidad",
            "asignación": "Secundaria",
            "potencia": None,
            "durabilidad": None,
            "descripción": "Arma de origen japonés, usada principalmente para bloquear y atrapar otras armas en combate cuerpo a cuerpo."
        },
        "Jutte": {
            "categoría_de_daño": "Contundente",
            "tipo": "Daga",
            "manos": 1,
            "daño": "d4",
            "alcance": "1 mt",
            "peso": 0.6,
            "característica": "Astucia",
            "asignación": "Secundaria",
            "potencia": None,
            "durabilidad": None,
            "descripción": "Herramienta de ley tradicional japonesa, eficaz para desarmar y controlar sin causar lesiones severas."
        },
        "Scian": {
            "categoría_de_daño": "Perforante",
            "tipo": "Daga",
            "manos": 1,
            "daño": "d4",
            "alcance": "1 mt",
            "peso": 0.5,
            "característica": "Agilidad",
            "asignación": "Secundaria",
            "potencia": None,
            "durabilidad": None,
            "descripción": "Daga celta tradicional, comúnmente usada como arma secundaria y herramienta utilitaria."
        }
    },
    "Hojas Cortas": {
        "Wakizashi": {
            "categoría_de_daño": "Cortante",
            "tipo": "Espada Corta",
            "manos": 1,
            "daño": "d6",
            "alcance": "1 mt",
            "peso": 0.9,
            "característica": "Agilidad",
            "asignación": "Dominante",
            "potencia": None,
            "durabilidad": None,
            "descripción": "Espada japonesa más corta que la katana, tradicionalmente usada como arma secundaria por los samuráis."
        },
        "Tanto": {
            "categoría_de_daño": "Cortante",
            "tipo": "Espada Corta",
            "manos": 1,
            "daño": "d4",
            "alcance": "1 mt",
            "peso": 0.6,
            "característica": "Agilidad",
            "asignación": "Secundaria",
            "potencia": None,
            "durabilidad": None,
            "descripción": "Pequeña daga japonesa utilizada para apuñalar o como herramienta de último recurso."
        },
        "Kama": {
            "categoría_de_daño": "Cortante",
            "tipo": "Espada Corta",
            "manos": 1,
            "daño": "d6",
            "alcance": "1 mt",
            "peso": 0.7,
            "característica": "Agilidad",
            "asignación": "Dominante",
            "potencia": None,
            "durabilidad": None,
            "descripción": "Herramienta agrícola tradicional japonesa que también se usaba como arma, con una hoja curva similar a una hoz."
        },
        "Claideamh": {
            "categoría_de_daño": "Perforante",
            "tipo": "Espada Corta",
            "manos": 1,
            "daño": "d6",
            "alcance": "1 mt",
            "peso": 0.8,
            "característica": "Fuerza",
            "asignación": "Dominante",
            "potencia": None,
            "durabilidad": None,
            "descripción": "Espada corta tradicional celta, usada en batallas como arma secundaria y para ceremonias."
        },
        "Seax": {
            "categoría_de_daño": "Cortante",
            "tipo": "Espada Corta",
            "manos": 1,
            "daño": "d4",
            "alcance": "1 mt",
            "peso": 0.7,
            "característica": "Fuerza",
            "asignación": "Secundaria",
            "potencia": None,
            "durabilidad": None,
            "descripción": "Larga daga o cuchillo usado por los pueblos germánicos, famoso por su robustez y versatilidad."
        },
        "Cimitarra": {
            "categoría_de_daño": "Cortante",
            "tipo": "Espada Corta",
            "manos": 1,
            "daño": "d6",
            "alcance": "1 mt",
            "peso": 0.8,
            "característica": "Agilidad",
            "asignación": "Dominante",
            "potencia": None,
            "durabilidad": None,
            "descripción": "Espada corta y curva de origen persa, optimizada para cortes rápidos y precisos."
        },
        "Akinakes": {
            "categoría_de_daño": "Cortante",
            "tipo": "Espada Corta",
            "manos": 1,
            "daño": "d6",
            "alcance": "1 mt",
            "peso": 0.7,
            "característica": "Agilidad",
            "asignación": "Dominante",
            "potencia": None,
            "durabilidad": None,
            "descripción": "Daga corta usada por los persas antiguos, común tanto en la guerra como en rituales."
        },
        "Xiphos": {
            "categoría_de_daño": "Cortante",
            "tipo": "Espada Corta",
            "manos": 1,
            "daño": "d4",
            "alcance": "1 mt",
            "peso": 0.8,
            "característica": "Agilidad",
            "asignación": "Secundaria",
            "potencia": None,
            "durabilidad": None,
            "descripción": "Espada corta griega, equilibrada y eficaz, utilizada por los hoplitas como arma secundaria en la falange."
        }
    },
    "Arrojadizas": {
        "Kunai": {
            "categoría_de_daño": "Perforante",
            "tipo": "Arrojadiza",
            "manos": 1,
            "daño": "d4",
            "alcance": "10 mts",
            "peso": 0.3,
            "característica": "Agilidad",
            "asignación": "Secundaria",
            "potencia": None,
            "durabilidad": None,
            "descripción": "Herramienta multifuncional japonesa originalmente utilizada para la agricultura y adaptada como arma arrojadiza por los ninjas."
        },
        "Shuriken": {
            "categoría_de_daño": "Perforante",
            "tipo": "Arrojadiza",
            "manos": 1,
            "daño": "d4",
            "alcance": "10 mts",
            "peso": 0.2,
            "característica": "Agilidad",
            "asignación": "Secundaria",
            "potencia": None,
            "durabilidad": None,
            "descripción": "Pequeña arma estrella tradicional japonesa, conocida por su capacidad para ser lanzada con gran precisión."
        },
        "Pilum": {
            "categoría_de_daño": "Perforante",
            "tipo": "Lanza Arrojadiza",
            "manos": 1,
            "daño": "d6",
            "alcance": "10 mts",
            "peso": 1.5,
            "característica": "Fuerza",
            "asignación": "Dominante",
            "potencia": None,
            "durabilidad": None,
            "descripción": "Lanza arrojadiza pesada utilizada por los legionarios romanos, diseñada para doblarse al impacto para prevenir su reutilización."
        },
        "Francisca": {
            "categoría_de_daño": "Cortante",
            "tipo": "Hacha Arrojadiza",
            "manos": 1,
            "daño": "d6",
            "alcance": "10 mts",
            "peso": 1.4,
            "característica": "Fuerza",
            "asignación": "Dominante",
            "potencia": None,
            "durabilidad": None,
            "descripción": "Hacha arrojadiza diseñada por los francos, famosa por su vuelo inestable que dificultaba su esquiva."
        }
    },
    "Distancia": {
        "Yumi": {
            "categoría_de_daño": "Según Proyectil",
            "tipo": "Distancia",
            "manos": 2,
            "daño": "d8",
            "alcance": "30 mts",
            "peso": 1.0,
            "característica": "Agilidad",
            "asignación": "Dominante",
            "potencia": None,
            "durabilidad": None,
            "descripción": "Arco tradicional japonés largo, usado por los samuráis, conocido por su asimetría y alcance largo."
        },
        "Gakgung": {
            "categoría_de_daño": "Según Proyectil",
            "tipo": "Distancia",
            "manos": 2,
            "daño": "d6",
            "alcance": "20 mts",
            "peso": 1.0,
            "característica": "Agilidad",
            "asignación": "Dominante",
            "potencia": None,
            "durabilidad": None,
            "descripción": "Arco coreano compuesto, altamente eficiente y considerado uno de los arcos más potentes históricamente."
        },
        "Fukiya": {
            "categoría_de_daño": "Según Proyectil",
            "tipo": "Distancia",
            "manos": 1,
            "daño": "d4",
            "alcance": "20 mts",
            "peso": 0.5,
            "característica": "Agilidad",
            "asignación": "Dominante",
            "potencia": None,
            "durabilidad": None,
            "descripción": "Cerbatana japonesa, usada históricamente por los ninjas tanto para incapacitar como para eliminar sigilosamente."
        },
        "Scythian": {
            "categoría_de_daño": "Según Proyectil",
            "tipo": "Distancia (Sobre Montura)",
            "manos": 2,
            "daño": "d8",
            "alcance": "30 mts",
            "peso": 1.0,
            "característica": "Fuerza",
            "asignación": "Dominante",
            "potencia": None,
            "durabilidad": None,
            "descripción": "Arco compuesto usado por los escitas, diseñado para ser usado a caballo, permitiendo disparos rápidos y efectivos."
        },
        "Balearic": {
            "categoría_de_daño": "Según Proyectil",
            "tipo": "Distancia",
            "manos": 1,
            "daño": "d4",
            "alcance": "20 mts",
            "peso": 0.7,
            "característica": "Agilidad",
            "asignación": "Dominante",
            "potencia": None,
            "durabilidad": None,
            "descripción": "Honda usada por los honderos baleares, famosos en la antigüedad por su precisión y alcance."
        },
        "Sumpit": {
            "categoría_de_daño": "Según Proyectil",
            "tipo": "Distancia",
            "manos": 1,
            "daño": "d4",
            "alcance": "20 mts",
            "peso": 0.5,
            "característica": "Agilidad",
            "asignación": "Dominante",
            "potencia": None,
            "durabilidad": None,
            "descripción": "Cerbatana larga utilizada por las tribus indígenas de Borneo, capaz de lanzar dardos envenenados con gran precisión."
        }
    },
    "Flexibles": {
        "Kusarigama": {
            "categoría_de_daño": "Hoz(Cortante),Cadena(Contundente)",
            "tipo": "Flexible",
            "manos": 2,
            "daño": "Hoz(d6),Cadena(d4)",
            "alcance": "Hoz(1mt),Cadena(3mts)",
            "peso": 1.5,
            "característica": "Agilidad",
            "asignación": "Dominante",
            "potencia": None,
            "durabilidad": None,
            "descripción": "Arma japonesa que combina una hoz y una cadena con un peso al final, usada para atrapar o desarmar al enemigo."
        },
        "Scourge": {
            "categoría_de_daño": "Contundente",
            "tipo": "Flexible",
            "manos": 1,
            "daño": "d4",
            "alcance": "1-3 mts",
            "peso": 1.0,
            "característica": "Fuerza",
            "asignación": "Secundaria",
            "potencia": None,
            "durabilidad": None,
            "descripción": "Látigo con múltiples colas, cada una terminada en un nudo o gancho, utilizado para infligir dolor y heridas."
        },
        "Nekode": {
            "categoría_de_daño": "Cortante",
            "tipo": "Flexible",
            "manos": 1,
            "daño": "d4",
            "alcance": "1 mt",
            "peso": 0.5,
            "característica": "Agilidad",
            "asignación": "Secundaria",
            "potencia": None,
            "durabilidad": None,
            "descripción": "Garra de mano usada por los ninjas para escalar y como arma en combate cuerpo a cuerpo."
        },
        "Kusari Fundo": {
            "categoría_de_daño": "Contundente",
            "tipo": "Flexible",
            "manos": 2,
            "daño": "d6",
            "alcance": "1-3 mts",
            "peso": 1.2,
            "característica": "Astucia",
            "asignación": "Dominante",
            "potencia": None,
            "durabilidad": None,
            "descripción": "Cadena japonesa con pesos en ambos extremos, utilizada para inmovilizar o golpear a un oponente a distancia."
        },
        "Guantes de Araña": {
            "categoría_de_daño": "Cortante",
            "tipo": "Flexible",
            "manos": 1,
            "daño": "d4",
            "alcance": "1-3 mts",
            "peso": 0.4,
            "característica": "Agilidad",
            "asignación": "Secundaria",
            "potencia": None,
            "durabilidad": None,
            "descripción": "Guantes equipados con garras retráctiles hechas de seda Arakhel, permitiendo ataques rápidos y sorpresivos."
        }
    }
}

def calcular_bonificador_agilidad(agilidad, tipo, grado):
    factor = 1 if tipo == "Ligero" else 0.5 if tipo == "Intermedio" else 0
    return int(agilidad * factor)

def calcular_bonificador_evasion(evasion, tipo, grado):
    factor = 1 if tipo == "Ligero" else 0.5 if tipo == "Intermedio" else 0
    return int(evasion * factor)

def bonificador_base(tipo, grado):
    if tipo == "Ligero":
        return grado
    elif tipo == "Intermedio":
        return grado * 2
    elif tipo == "Pesado":
        return grado * 3
    
def bonificador_sigilo(grado):
    return grado  

def bonificador_acrobacias(grado):
    return grado  

def bonificador_vigor(grado):
    return grado 

def bonificador_destreza(grado):
    return grado 

def bonificador_resistencia(grado):
    return grado

def bonificador_velocidad(grado):
    return grado

def bonificador_equilibrio(grado):
    return grado

def penalizador_reacciones_instintivas(grado, tipo):
    if tipo == "Intermedio":
        return -grado  # Penalización igual al grado de la pieza
    elif tipo == "Pesado":
        return -(grado + 1)  # Penalización igual al grado de la pieza más uno
    return 0

def penalizador_agilidad_botas(grado, tipo):
    if tipo == "Intermedio":
        return -grado
    elif tipo == "Pesado":
        return -(grado + 1)
    return 0

def penalizador_destreza(grado, tipo):
    if tipo == "Intermedio":
        return -grado  # Penalización igual al grado de la pieza
    elif tipo == "Pesado":
        return -(grado + 1)  # Penalización igual al grado de la pieza más uno
    return 0

def bonificador_reacciones_instintivas(grado):
    return grado  # Bonificador directo del grado de la pieza a la T.A durante reacciones instintivas

def bonificador_maniobra(grado):
    return grado  # Bonificador directo del grado de la pieza a la T.A en maniobras de disciplina y armas

def bonificador_escudos(grado):
    return grado 

def bonificador_preparacion(grado):
    return grado  # Bonificador directo del grado de la pieza a la Preparación

def bonificador_enfoque(grado):
    return grado  # Bonificador directo del grado de la pieza a las T.T de Enfoque

def penalizador_percepcion(grado, tipo):
    if tipo == "Intermedio":
        return -grado  # Penalización igual al grado de la pieza
    elif tipo == "Pesado":
        return -(grado + 1)  # Penalización igual al grado de la pieza más uno
    return 0

def bonificador_armadura(tipo, grado):
    if tipo == "Mediano":
        return grado  # Bonificación directa del grado de la pieza
    elif tipo == "Pesado":
        return grado * 2  # Bonificación multiplicada por dos del grado de la pieza
    return 0  # No hay bonificación de armadura para escudos livianos

def penalizador_velocidad(tipo, grado):
    if tipo == "Mediano":
        return -(grado + 1)  # Penalización incrementada en uno sobre el grado
    elif tipo == "Pesado":
        return -(grado + 2)  # Penalización incrementada en dos sobre el grado
    return 0 

def bonificador_cobertura(tipo, grado):
    if tipo == "Mediano":
        return "Cobertura Ligera"  # Bonificación estática de cobertura
    elif tipo == "Pesado":
        return "Cobertura Media"  # Bonificación estática más fuerte
    return None

def bonificador_amuleto(grado):
    return "+1 por Grado de la pieza al Aguante, Cordura o Preparación"

def bonificador_insignia(grado):
    return "+1 por Grado de la pieza a las T.T de Influencia relacionadas con Negociación y Liderazgo"


armaduras = {
    "Peto": {
        "Ligero": {
            "bonificador_base": lambda grado: bonificador_base("Ligero", grado),
            "penalizador_agilidad": lambda grado: 0,  # No hay penalización
            "peso": 3.0
        },
        "Intermedio": {
            "bonificador_base": lambda grado: bonificador_base("Intermedio", grado),
            "penalizador_agilidad": lambda grado: penalizador_agilidad_botas(grado, "Intermedio"),
            "peso": 6.0
        },
        "Pesado": {
            "bonificador_base": lambda grado: bonificador_base("Pesado", grado),
            "penalizador_agilidad": lambda grado: penalizador_agilidad_botas(grado, "Pesado"),
            "peso": 9.0
        }
    },
    "Pantalones":{
        "Ligero": {
            "bonificadores": {
                "sigilo": bonificador_sigilo
            },
            "penalizador_condicional": None,
            "peso": 2.0
        },
        "Intermedio": {
            "bonificadores": {
                "acrobacias": bonificador_acrobacias,
                "vigor": bonificador_vigor,
                "destreza": bonificador_destreza
            },
            "penalizador_condicional": penalizador_reacciones_instintivas,
            "hint_ta": f"Penalización en la T.A durante reacciones instintivas igual a {penalizador_reacciones_instintivas}.",
            "peso": 4.0
        },
        "Pesado": {
            "bonificadores": {
                "resistencia_inmovilizacion": bonificador_resistencia
            },
            "penalizador_condicional": penalizador_reacciones_instintivas,
            "hint_ta": f"Penalización en la T.A durante reacciones instintivas igual a {penalizador_reacciones_instintivas}.",
            "hint_tr": f"Bonificador en la T.R contra los efectos Inmovilizado y Atrapado igual a {bonificador_resistencia}",
            "peso": 6.0
        }
    },
    "Botas": {
        "Ligero": {
            "bonificadores": {
                "velocidad_movimiento": bonificador_velocidad
            },
            "penalizador_agilidad": None,  
            "peso": 1.0
        },
        "Intermedio": {
            "bonificadores": {
                "equilibrio": bonificador_equilibrio
            },
            "penalizador_agilidad": penalizador_agilidad_botas,
            "peso": 2.0
        },
        "Pesado": {
            "bonificadores": {
                "resistencia_desplazamiento": bonificador_resistencia
            },
            "penalizador_agilidad": penalizador_agilidad_botas,
            "hint_tr": f"Bonificador en la T.R contra los efectos Derribo, Desequilibrio y Desplazamiento igual a {bonificador_resistencia}",
            "peso": 3.0
        }
    },
    "Brazales": {
        "Ligero": {
            "bonificadores": {
                "reacciones_instintivas": bonificador_reacciones_instintivas
            },
            "penalizador_destreza_arte": None,  # No hay penalización para brazales ligeros
            "peso": 2.0
        },
        "Intermedio": {
            "bonificadores": {
                "disciplina_armas": bonificador_maniobra
            },
            "penalizador_destreza_arte": penalizador_destreza,
            "hint_te": f"Penalizador en la T.E de Destreza igual a {penalizador_destreza}",
            "peso": 3.0
        },
        "Pesado": {
            "bonificadores": {
                "escudos": bonificador_escudos
            },
            "penalizador_destreza_arte": penalizador_destreza,
            "hint_te": f"Penalizador en la T.E de Destreza igual a {penalizador_destreza}",
            "peso": 4.0
        }
    },
    "Casco": {
        "Ligero": {
            "bonificadores": {
                "preparacion": bonificador_preparacion
            },
            "penalizador_percepcion": None,  # No hay penalización para cascos ligeros
            "peso": 1.0
        },
        "Intermedio": {
            "bonificadores": {
                "enfoque": bonificador_enfoque
            },
            "penalizador_percepcion": penalizador_percepcion,
            "peso": 2.0
        },
        "Pesado": {
            "bonificadores": {
                "resistencia_conmocion": bonificador_resistencia
            },
            "penalizador_percepcion": penalizador_percepcion,  # Penalización incrementada por 1 sobre el grado de la pieza
            "hint_tr": f"Bonificador en la T.R contra los efectos de Conmosión igual a {bonificador_resistencia}",
            "hint_te": f"Penalizador en la T.E de Percepción igual a {penalizador_percepcion}",
            "peso": 3.0
        }
    },
    "Escudos":{
        "Liviano": {
            "bonificacion_cobertura": bonificador_cobertura("Liviano", 1),
            "bonificacion_armadura": bonificador_armadura("Liviano", 1),
            "penalizador_velocidad": penalizador_velocidad("Liviano", 1),
            "peso": 2.0
        },
        "Mediano": {
            "bonificacion_cobertura": bonificador_cobertura("Mediano", 1),
            "bonificacion_armadura": bonificador_armadura("Mediano", 1),
            "penalizador_velocidad": penalizador_velocidad("Mediano", 1),
            "peso": 5.0
        },
        "Pesado": {
            "bonificacion_cobertura": bonificador_cobertura("Pesado", 1),
            "bonificacion_armadura": bonificador_armadura("Pesado", 1),
            "penalizador_velocidad": penalizador_velocidad("Pesado", 1),
            "peso": 10.0
        }
    },
    "Joyas": {
        "Colgante": {
            "bonificador": "Permite utilizar objetos sin utilizar la acción Interactuar",
            "peso": 1.0
        },
        "Amuleto": {
            "bonificador": bonificador_amuleto,
            "peso": 0.1
        },
        "Insignia": {
            "bonificador": bonificador_insignia,
            "peso": 0.1
        }
    }
}


materiales = {
    "Hierro": {
        "Tipo": "Metal",
        "Costo": lambda grado: 10 * grado,
        "Durabilidad": 15,
        "Resistencia": 25
    },
    "Jade": {
        "Tipo": "Piedra Preciosa",
        "Costo": lambda grado: 50 * grado,
        "Durabilidad": 10,
        "Resistencia": 15
    },
    "Carbón": {
        "Tipo": "Roca",
        "Costo": lambda grado: 5 * grado,
        "Durabilidad": 5,
        "Resistencia": 10
    },
    "Lapislázuli": {
        "Tipo": "Piedra Preciosa",
        "Costo": lambda grado: 30 * grado,
        "Durabilidad": 8,
        "Resistencia": 14
    },
    "Oro": {
        "Tipo": "Metal",
        "Costo": lambda grado: 100 * grado,
        "Durabilidad": 10,
        "Resistencia": 20
    },
    "Estaño": {
        "Tipo": "Metal",
        "Costo": lambda grado: 20 * grado,
        "Durabilidad": 9,
        "Resistencia": 18
    },
    "Cobre": {
        "Tipo": "Metal",
        "Costo": lambda grado: 10 * grado,
        "Durabilidad": 10,
        "Resistencia": 20
    },
    "Cristales": {
        "Tipo": "Piedra Preciosa",
        "Costo": lambda grado: 30 * grado,
        "Durabilidad": 7,
        "Resistencia": 12
    },
    "Piedra": {
        "Tipo": "Roca",
        "Costo": lambda grado: 5 * grado,
        "Durabilidad": 8,
        "Resistencia": 16
    },
    "Roca": {
        "Tipo": "Roca",
        "Costo": lambda grado: 5 * grado,
        "Durabilidad": 9,
        "Resistencia": 18
    },
    "Obsidiana": {
        "Tipo": "Roca",
        "Costo": lambda grado: 30 * grado,
        "Durabilidad": 12,
        "Resistencia": 12
    },
    "Mithril": {
        "Tipo": "Metal",
        "Costo": lambda grado: 500 * grado,
        "Durabilidad": 28,
        "Resistencia": 45
    },
    "Adamantium": {
        "Tipo": "Metal",
        "Costo": lambda grado: 1000 * grado,
        "Durabilidad": 30,
        "Resistencia": 50
    },
    "Titanio": {
        "Tipo": "Metal",
        "Costo": lambda grado: 80 * grado,
        "Durabilidad": 22,
        "Resistencia": 35
    },
    "Plata": {
        "Tipo": "Metal",
        "Costo": lambda grado: 40 * grado,
        "Durabilidad": 16,
        "Resistencia": 28
    },
    "Platino": {
        "Tipo": "Metal",
        "Costo": lambda grado: 50 * grado,
        "Durabilidad": 17,
        "Resistencia": 29
    },
    "Cuarzo": {
        "Tipo": "Piedra Preciosa",
        "Costo": lambda grado: 20 * grado,
        "Durabilidad": 6,
        "Resistencia": 11
    },
    "Ámbar": {
        "Tipo": "Roca",
        "Costo": lambda grado: 20 * grado,
        "Durabilidad": 4,
        "Resistencia": 8
    },
    "Marfil": {
        "Tipo": "Piedra Preciosa",
        "Costo": lambda grado: 40 * grado,
        "Durabilidad": 7,
        "Resistencia": 13
    },
    "Coral": {
        "Tipo": "Roca",
        "Costo": lambda grado: 20 * grado,
        "Durabilidad": 6,
        "Resistencia": 10
    },
    "Ébano": {
        "Tipo": "Roca",
        "Costo": lambda grado: 20 * grado,
        "Durabilidad": 25,
        "Resistencia": 11
    },
    "Roble": {
        "Tipo": "Madera",
        "Costo": lambda grado: 10 * grado,
        "Durabilidad": 20,
        "Resistencia": 10
    },
    "Caoba": {
        "Tipo": "Madera",
        "Costo": lambda grado: 15 * grado,
        "Durabilidad": 22,
        "Resistencia": 12
    },
    "Pino": {
        "Tipo": "Madera",
        "Costo": lambda grado: 5 * grado,
        "Durabilidad": 15,
        "Resistencia": 7
    },
    "Arce": {
        "Tipo": "Madera",
        "Costo": lambda grado: 12 * grado,
        "Durabilidad": 18,
        "Resistencia": 8
    },
    "Secoya": {
        "Tipo": "Madera",
        "Costo": lambda grado: 25 * grado,
        "Durabilidad": 30,
        "Resistencia": 15
    },
    "Rubí": {
        "Tipo": "Piedra Preciosa",
        "Costo": lambda grado: 120 * grado,
        "Durabilidad": 16,
        "Resistencia": 9
    },
    "Esmeralda": {
        "Tipo": "Piedra Preciosa",
        "Costo": lambda grado: 140 * grado,
        "Durabilidad": 15,
        "Resistencia": 9
    },
    "Zafiro": {
        "Tipo": "Piedra Preciosa",
        "Costo": lambda grado: 110 * grado,
        "Durabilidad": 16,
        "Resistencia": 9
    },
    "Diamante": {
        "Tipo": "Piedra Preciosa",
        "Costo": lambda grado: 200 * grado,
        "Durabilidad": 18,
        "Resistencia": 10
    },
    "Topacio": {
        "Tipo": "Piedra Preciosa",
        "Costo": lambda grado: 90 * grado,
        "Durabilidad": 14,
        "Resistencia": 8
    },
    "Cromo": {
        "Tipo": "Metal",
        "Costo": lambda grado: 60 * grado,
        "Durabilidad": 20,
        "Resistencia": 27
    },
    "Plomo": {
        "Tipo": "Metal",
        "Costo": lambda grado: 15 * grado,
        "Durabilidad": 12,
        "Resistencia": 18
    },
    "Oricalco": {
        "Tipo": "Metal",
        "Costo": lambda grado: 800 * grado,
        "Durabilidad": 25,
        "Resistencia": 40
    },
    "Seda de Arakhel": {
        "Tipo": "Fibra",
        "Costo": lambda grado: 50 * grado,
        "Durabilidad": 18,
        "Resistencia": 18
    },
    "Lana": {
        "Tipo": "Fibra",
        "Costo": lambda grado: 50 * grado,
        "Durabilidad": 18,
        "Resistencia": 18
    },
    "Algodon": {
        "Tipo": "Fibra",
        "Costo": lambda grado: 50 * grado,
        "Durabilidad": 18,
        "Resistencia": 18
    },
    "Seda":{
        "Tipo": "Fibra",
        "Costo": lambda grado: 50 * grado,
        "Durabilidad": 18,
        "Resistencia": 18
    },
    "Yute": {
        "Tipo": "Fibra",
        "Costo": lambda grado: 50 * grado,
        "Durabilidad": 18,
        "Resistencia": 18
    },
    "Lino":{
        "Tipo": "Fibra",
        "Costo": lambda grado: 50 * grado,
        "Durabilidad": 18,
        "Resistencia": 18
    },
    "Nylon":{
        "Tipo": "Fibra",
        "Costo": lambda grado: 50 * grado,
        "Durabilidad": 18,
        "Resistencia": 18
    },
    "Poliester":{
        "Tipo": "Fibra",
        "Costo": lambda grado: 50 * grado,
        "Durabilidad": 18,
        "Resistencia": 18
    }
}
