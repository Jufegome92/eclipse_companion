import math

class Ability:
    def __init__(self, name, type, action_type, element, usage, action_points, range, area, duration, saving_throw, requirement, effect):
        self.name = name
        self.type = type 
        self.action_type = action_type  
        self.element = element 
        self.usage = usage  
        self.action_points = action_points  
        self.range = range  
        self.area = area  
        self.duration = duration  
        self.saving_throw = saving_throw  
        self.requirement = requirement  
        self.effect = effect  

class Technique(Ability):
    def __init__(self, name, type, action_type, element, usage, action_points, range, area, duration, saving_throw, requirement, effect, attack=None, impact=None, advancements=None):
        super().__init__(name, type, action_type, element, usage, action_points, range, area, duration, saving_throw, requirement, effect)
        self.attack = attack  
        self.impact = impact  
        self.advancements = advancements if advancements else {}  

class Maneuver(Ability):
    def __init__(self, name, type, action_type, element, usage, action_points, range, area, duration, saving_throw, requirement, effect, attack=None, impact=None):
        super().__init__(name, type, action_type, element, usage, action_points, range, area, duration, saving_throw, requirement, effect)
        self.attack = attack  
        self.impact = impact  

class Gift(Ability):
    def __init__(self, name, type, action_type, element, usage, action_points, range, area, duration, saving_throw, requirement, effect):
        super().__init__(name, type, action_type, element, usage, action_points, range, area, duration, saving_throw, requirement, effect)

techniques = {}
maneuvers = {}
gifts = {}

class Species:
    def __init__(self, name, size, base_health, movement_speed, characteristic_bonuses, languages):
        self.name = name
        self.size = size
        self.base_health = base_health
        self.movement_speed = movement_speed
        self.characteristic_bonuses = characteristic_bonuses
        self.languages = languages

class Weapon:
    def __init__(self, name, damage_category, weapon_type, hands, damage, range, weight, characteristic, assignment, weapon_range="melee"):
        self.name = name
        self.damage_category = damage_category
        self.weapon_type = weapon_type
        self.hands = hands
        self.damage = damage
        self.range = range
        self.weight = weight
        self.characteristic = characteristic
        self.assignment = assignment
        self.grade = 1
        self.weapon_range = weapon_range

class Armor:
    def __init__(self, name, category, base_armor_bonus, td_penalty, te_penalty, weight, grade, modifiers=None):
        self.name = name
        self.category = category
        self.base_armor_bonus = base_armor_bonus
        self.td_penalty = td_penalty
        self.te_penalty = te_penalty
        self.weight = weight
        self.grade = grade
        self.modifiers = modifiers if modifiers is not None else []

    def get_armor_bonus(self, characteristics, competencies):
        return self.base_armor_bonus(characteristics, competencies, self.grade)

    def get_te_penalty(self, characteristics, competencies):
        if self.te_penalty:
            if self.category == "Pesado":
                return (characteristics.agility + competencies.get_level("martial", "Evasion")) * -1
            return self.te_penalty(characteristics, competencies, self.grade)
        return 0

class LegArmor(Armor):
    def __init__(self, name, category, bonus, ta_penalty, weight, grade, modifiers=None, descriptions=None):
        super().__init__(name, category, None, None, None, weight, grade, modifiers)
        self.bonus = bonus
        self.ta_penalty = ta_penalty
        self.descriptions = descriptions if descriptions is not None else []

    def get_bonus(self, characteristics, competencies):
        return self.bonus(characteristics, competencies, self.grade)

    def get_ta_penalty(self):
        return self.ta_penalty(self.grade) if self.ta_penalty else 0

    def get_descriptions(self):
        return [desc.format(grade=self.grade, grade_plus_one=self.grade + 1) for desc in self.descriptions]

class Boots(Armor):
    def __init__(self, name, category, bonus, tc_penalty, weight, grade, modifiers=None, description=None):
        super().__init__(name, category, None, None, None, weight, grade, modifiers)
        self.bonus = bonus
        self.tc_penalty = tc_penalty
        self.description = description if description is not None else ""

    def get_bonus(self, characteristics, competencies, qualities):
        return self.bonus(characteristics, competencies, qualities, self.grade)

    def get_tc_penalty(self):
        if self.tc_penalty:
            return self.tc_penalty(self.grade)
        return 0

    def get_resistance_bonus(self, context):
        if self.category == "Pesado" and context in ["Desplazado", "Derribado", "Desequilibrado"]:
            return self.grade
        return 0

class Bracers(Armor):
    def __init__(self, name, category, bonus, te_penalty, weight, grade, modifiers=None, description=None):
        super().__init__(name, category, None, None, None, weight, grade, modifiers)
        self.bonus = bonus
        self.te_penalty = te_penalty
        self.description = description if description is not None else ""

class Helmet(Armor):
    def __init__(self, name, category, bonus, te_penalty, weight, grade, modifiers=None, description=None):
        super().__init__(name, category, None, None, None, weight, grade, modifiers)
        self.bonus = bonus
        self.te_penalty = te_penalty
        self.description = description if description is not None else ""

    def get_bonus(self, characteristics, competences):
        return self.bonus(self.grade)

class Shield:
    def __init__(self, name, category, coverage_bonus, armor_bonus, movement_penalty, weight, grade=1):
        self.name = name 
        self.category = category
        self.coverage_bonus = coverage_bonus
        self.armor_bonus = armor_bonus
        self.movement_penalty = movement_penalty
        self.weight = weight
        self.grade = grade

    def get_armor_bonus(self, grade):
        if self.armor_bonus is None:
            return 0
        if callable(self.armor_bonus):
            return self.armor_bonus(grade)
        return self.armor_bonus

class Jewelry:
    def __init__(self, name, category, bonus, weight, grade=1, choice=None, description=None):
        self.name = name
        self.category = category
        self.bonus = bonus
        self.weight = weight
        self.grade = grade
        self.choice = choice
        self.description = description if description is not None else ""

    def apply_bonus(self, player, grade, choice=None):
        self.grade = grade
        self.choice = choice
        player.characteristics.amulet_bonus = 0
        if self.category == "Amuleto" and choice:
            if choice == "aguante":
                player.fatigue.amulet_bonus = grade
            elif choice == "cordura":
                player.sanity.amulet_bonus = grade
            elif choice == "preparacion":
                player.characteristics.amulet_bonus = grade
        elif self.category == "Insignia":
            player.characteristics.insignia_bonus = self.bonus(player.characteristics, player.competences, grade)
        return grade

class Characteristics:
    def __init__(self, strength, agility, tenacity, cunning, intellect, wisdom, charisma, composure, presence):
        self.strength = strength
        self.agility = agility
        self.tenacity = tenacity
        self.cunning = cunning
        self.intellect = intellect
        self.wisdom = wisdom
        self.charisma = charisma
        self.composure = composure
        self.presence = presence
        self.helmet_bonus = 0
        self.amulet_bonus = 0

    @property
    def preparation(self):
        return math.ceil((self.agility + self.cunning + self.presence) / 3) + self.helmet_bonus + self.amulet_bonus

    @property
    def resilience(self):
        return math.ceil((self.tenacity + self.wisdom + self.composure) / 3)

class Qualities:
    def __init__(self, player_level, age, size, height, weight, load_capacity, languages, movement_speed, heritage, legacies):
        self.player_level = player_level
        self.age = age
        self.size = size
        self.height = height
        self.weight = weight
        self.load_capacity = load_capacity
        self.languages = languages
        self.movement_speed = movement_speed
        self.heritage = heritage
        self.legacies = legacies

def calculate_load_capacity(strength, resilience, size):
    size_factors = {
        "Diminuto": 1,
        "Pequeño": 15,
        "Mediano": 35,
        "Grande": 80,
        "Enorme": 200,
        "Gigantesco": 800
    }
    if size not in size_factors:
        raise ValueError(f"Invalid size: {size}")
    return int(strength * resilience * size_factors[size])

class Health:
    def __init__(self, species_base_health, discipline_base_health, tenacity, discipline_health_per_level):
        self.damage_taken = 0
        self.species_base_health = species_base_health
        self.discipline_base_health = discipline_base_health
        self.tenacity = tenacity
        self.discipline_health_per_level = discipline_health_per_level
        self.current_health = self.calculate_health(1)

    def calculate_health(self, player_level):
        base_health = self.species_base_health + self.discipline_base_health
        additional_health = self.discipline_health_per_level * (player_level - 1)
        tenacity_health = self.tenacity * player_level
        return base_health + additional_health + tenacity_health

    def calculate_renewals(self, player):
        vigor_competence = player.competences.get_bonus("specialization", "Vigor")
        return self.tenacity + (vigor_competence // 2)

class Fatigue:
    def __init__(self, tenacity):
        self.tenacity = tenacity
        self.fatigue_accumulated = 0
        self.amulet_bonus = 0

    def calculate_endurance(self, player):
        vigor_competence = player.competences.get_bonus("specialization", "Vigor")
        return self.tenacity + (vigor_competence // 2) + self.amulet_bonus

    def calculate_fatigue(self, player):
        return max(0, self.fatigue_accumulated - self.calculate_endurance(player))

class InstinctiveReactions:
    def __init__(self, tenacity):
        self.tenacity = tenacity
        self.reactions_left = 0

    def calculate_reactions(self, player):
        vigor_competence = player.competences.get_bonus("specialization", "Vigor")
        return self.tenacity + (vigor_competence // 2)

    def update_reactions(self, player):
        self.reactions_left = self.calculate_reactions(player)

class Sanity:
    def __init__(self, composure):
        self.composure = composure
        self.disorders = 0
        self.amulet_bonus = 0

    @property
    def sanity(self):
        return self.composure * 2 + self.amulet_bonus

    def calculate_sanity(self):
        return max(0, self.disorders - self.sanity)

class Competence:
    def __init__(self, name, level=1):
        self.name = name
        self.level = level
        self.progress = 0
        self.rank = self.calculate_rank()

    def increase_progress(self):
        self.progress += 1
        if self.progress >= 10:
            self.progress = 0
            self.level_up()

    def level_up(self):
        self.level += 1
        self.rank = self.calculate_rank()

    def calculate_rank(self):
        if self.level >= 12:
            return 4
        elif self.level >= 8:
            return 3
        elif self.level >= 4:
            return 2
        elif self.level >= 1:
            return 1
        else:
            return 0

    def get_bonus(self):
        return self.level + self.rank

class Competences:
    def __init__(self):
        self.specializations = {}
        self.martial = {}
        self.resistances = {}

    def get_level(self, category, name):
        if category == "specialization" and name in self.specializations:
            return self.specializations[name].level
        elif category == "martial" and name in self.martial:
            return self.martial[name].level
        elif category == "resistance" and name in self.resistances:
            return self.resistances[name].level
        return 0

    def get_rank(self, category, name):
        if category == "specialization" and name in self.specializations:
            return self.specializations[name].rank
        elif category == "martial" and name in self.martial:
            return self.martial[name].rank
        elif category == "resistance" and name in self.resistances:
            return self.resistances[name].rank
        return 0

    def add_competence(self, category, name, level=1):
        if category == "specialization":
            self.specializations[name] = Competence(name, level)
        elif category == "martial":
            self.martial[name] = Competence(name, level)
        elif category == "resistance":
            self.resistances[name] = Competence(name, level)

    def get_bonus(self, category, name):
        if category == "specialization" and name in self.specializations:
            return self.specializations[name].get_bonus()
        elif category == "martial" and name in self.martial:
            return self.martial[name].get_bonus()
        elif category == "resistance" and name in self.resistances:
            return self.resistances[name].get_bonus()
        return 0

class Specialization:
    def __init__(self, name, category, characteristic):
        self.name = name
        self.category = category
        self.characteristic = characteristic

class Specializations:
    def __init__(self):
        self.specializations = {}

    def create_specialization(self, name, category, characteristic):
        self.specializations[name] = Specialization(name, category, characteristic)

    def get_specialization_characteristic(self, name):
        if name in self.specializations:
            return self.specializations[name].characteristic
        else:
            return None

predefined_specializations = [
    ("Acrobacias", "Habilidades Físicas", "agility"),
    ("Destreza", "Habilidades Físicas", "agility"),
    ("Equilibrio", "Habilidades Físicas", "composure"),
    ("Equitación", "Habilidades Físicas", "agility"),
    ("Vigor", "Habilidades Físicas", "strength"),
    ("Identificación", "Habilidades Mentales", "intellect"),
    ("Interpretación", "Habilidades Mentales", "intellect"),
    ("Lingüística", "Habilidades Mentales", "intellect"),
    ("Percepción", "Habilidades Mentales", "wisdom"),
    ("Supervivencia", "Habilidades Mentales", "wisdom"),
    ("Enfoque", "Habilidades Mentales", "composure"),
    ("Engaño", "Habilidades Mentales", "cunning"),
    ("Influencia", "Habilidades Sociales", "presence"),
    ("Sigilo", "Habilidades Sociales", "presence"),
    ("Domesticación", "Habilidades Sociales", "charisma"),
    ("Herrería", "Oficios y Artes", "strength"),
    ("Trampas", "Oficios y Artes", "cunning"),
    ("Carpintería", "Oficios y Artes", "strength"),
    ("Joyería", "Oficios y Artes", "dexterity"),
    ("Sastrería", "Oficios y Artes", "dexterity"),
    ("Minería", "Oficios y Artes", "strength"),
    ("Música", "Oficios y Artes", "dexterity"),
    ("Pintura", "Oficios y Artes", "dexterity"),
    ("Danza", "Oficios y Artes", "agility"),
    ("Alquimia", "Oficios y Artes", "intellect"),
    ("Medicina", "Saberes", "intellect"),
    ("Teología", "Saberes", "intellect"),
    ("Astronomía", "Saberes", "intellect"),
    ("Geografía", "Saberes", "intellect"),
    ("Anatomía", "Saberes", "intellect"),
    ("Botánica", "Saberes", "wisdom"),
    ("Historiografía", "Saberes", "intellect")
]

specializations = Specializations()
for name, category, characteristic in predefined_specializations:
    specializations.create_specialization(name, category, characteristic)

class Inventory:
    def __init__(self, player):
        self.player = player
        self.items = []
        self.equipped = {
            "left_hand": None,
            "right_hand": None,
            "armor": None,
            "pants": None,
            "boots": None,
            "bracers": None,
            "helmet": None,
            "shield": None,
            "amulet": None,
            "pendant": None,
            "badge": None
        }

    def add_item(self, item):
        self.items.append(item)

    def equip_item(self, item, slot, grade=None, choice=None):
        if slot in self.equipped:
            if grade is not None and hasattr(item, 'grade'):
                item.grade = grade
            if choice is not None and hasattr(item, 'choice'):
                item.choice = choice
            self.equipped[slot] = item
            if isinstance(item, Jewelry):
                item.apply_bonus(self.player, grade, choice)
            self.player.update_permanent_bonuses()
            self.player.calculate_movement_speed()

class Player:
    def __init__(self, name, species, characteristics, qualities, health, fatigue, sanity, instinctive_reactions, competences, resonance_level=1):
        self.name = name
        self.species = species
        self.characteristics = characteristics
        self.qualities = qualities
        self.health = health
        self.fatigue = fatigue
        self.sanity = sanity
        self.resonance_level = resonance_level
        self.instinctive_reactions = instinctive_reactions
        self.competences = competences
        self.specializations = Specializations()
        self.initialize_specializations()
        self.inventory = Inventory(self)
        self.update_permanent_bonuses()
        self.calculate_movement_speed()

    def initialize_specializations(self):
        for name, category, characteristic in predefined_specializations:
            self.specializations.create_specialization(name, category, characteristic)

    def update_amulet_bonus(self):
        amulet = self.inventory.equipped.get("amulet", None)
        if amulet and amulet.category == "Amuleto":
            self.characteristics.amulet_bonus = amulet.apply_bonus(self, amulet.grade, amulet.choice)
        else:
            self.characteristics.endurance_bonus = 0
            self.characteristics.sanity_bonus = 0
            self.characteristics.preparation_bonus = 0

    def update_level(self, new_level):
        self.qualities.player_level = new_level
        self.health.current_health = self.health.calculate_health(new_level)
        self.instinctive_reactions.update_reactions(self)
        self.fatigue.calculate_fatigue(self)
        self.qualities.load_capacity = calculate_load_capacity(
            self.characteristics.strength,
            self.characteristics.resilience,
            self.qualities.size
        )
        self.update_permanent_bonuses()
        self.calculate_movement_speed()

    def update_permanent_bonuses(self):
        self.update_amulet_bonus()
        self.update_helmet_bonus()
        self.reset_competence_bonuses()
        self.calculate_movement_speed()

    def reset_competence_bonuses(self):
        pass

    def calculate_total_bonus(self, base_value, bonuses):
        return base_value + sum(bonuses)

    def get_weapon_bonus(self, weapon_name, hand):
        weapon = self.inventory.equipped[hand]
        if weapon and weapon.name == weapon_name:
            characteristic_value = getattr(self.characteristics, weapon.characteristic)
            competence_level = self.competences.get_level("martial", weapon_name)
            return characteristic_value + competence_level
        return 0

    def calculate_attack_roll(self, weapon_name, context="normal"):
        right_hand_bonus = self.get_weapon_bonus(weapon_name, "right_hand")
        left_hand_bonus = self.get_weapon_bonus(weapon_name, "left_hand")

        weapon_bonus = right_hand_bonus if right_hand_bonus else left_hand_bonus
        penalty = 0
        if context == "reaccion_instintiva":
            penalty = self.get_leg_armor_penalty("ataque")
            bracer_bonus = self.get_bracer_bonus("ataque")
            total_bonus = weapon_bonus + penalty + bracer_bonus
        else:
            total_bonus = weapon_bonus + penalty
        roll_description = f"1d10 + {total_bonus}"
        return roll_description

    def get_bracer_bonus(self, context):
        bracers = self.inventory.equipped.get("bracers", None)
        if bracers and context == "ataque" and bracers.category == "Ligero":
            return bracers.bonus(self.characteristics, self.competences, bracers.grade)
        return 0

    def get_armor_bonus(self):
        armor = self.inventory.equipped["armor"]
        if armor:
            return armor.get_armor_bonus(self.characteristics, self.competences)
        return 0

    def get_evasion_penalty(self):
        armor = self.inventory.equipped["armor"]
        if armor:
            return armor.get_te_penalty(self.characteristics, self.competences)
        return 0

    def get_shield_bonus(self):
        shield = self.inventory.equipped["shield"]
        if shield:
            return shield.get_armor_bonus(shield.grade)
        return 0

    def get_shield_movement_penalty(self):
        shield = self.inventory.equipped["shield"]
        if shield and shield.movement_penalty:
            return shield.movement_penalty(shield.grade)
        return 0

    def calculate_movement_speed(self):
        base_speed = self.species.movement_speed
        shield_penalty = self.get_shield_movement_penalty()
        boot_bonus = self.get_boot_bonus()
        self.qualities.movement_speed = base_speed + shield_penalty + boot_bonus

    def get_boot_bonus(self):
        boots = self.inventory.equipped["boots"]
        if boots and boots.category == "Ligero":
            return boots.get_bonus(self.characteristics, self.competences, self.qualities)
        return 0

    def get_boot_tc_penalty(self):
        boots = self.inventory.equipped["boots"]
        if boots:
            return boots.get_tc_penalty()
        return 0

    def get_resistance_bonus(self, context):
        boots = self.inventory.equipped["boots"]
        if boots:
            return boots.get_resistance_bonus(context)
        return 0

    def get_specialization_bonus(self, specialization_name):
        specialization_bonus = 0
        if specialization_name == "Equilibrio":
            specialization_bonus = self.get_boot_equilibrium_bonus()
        elif specialization_name == "Equitación":
            specialization_bonus = self.get_boot_riding_bonus()
        return specialization_bonus

    def get_boot_equilibrium_bonus(self):
        boots = self.inventory.equipped["boots"]
        if boots and boots.category == "Intermedio":
            return boots.grade
        return 0

    def get_boot_riding_bonus(self):
        boots = self.inventory.equipped["boots"]
        if boots and boots.category == "Intermedio":
            return boots.grade
        return 0

    def calculate_defense_roll(self):
        agility = self.characteristics.agility
        evasion_competence = self.competences.get_level("martial", "Evasion")

        armor_bonus = self.get_armor_bonus()
        shield_bonus = self.get_shield_bonus()
        evasion_penalty = self.get_evasion_penalty()

        if evasion_penalty < 0:
            agility = 0
            evasion_competence = 0
        elif evasion_penalty > 0:
            agility = math.ceil(agility / 2)
            evasion_competence = math.ceil(evasion_competence / 2)

        total_bonus = agility + evasion_competence + armor_bonus + shield_bonus
        roll_description = f"1d10 + {total_bonus}"

        return roll_description

    def get_leg_armor_bonus(self, context):
        leg_armor = self.inventory.equipped["pants"]
        if not leg_armor:
            return 0

        if leg_armor.category == "Ligero" and context == "sigilo":
            return leg_armor.get_bonus(self.characteristics, self.competences)
        elif leg_armor.category == "Intermedio" and context in ["acrobacias", "vigor"]:
            return leg_armor.bonus(self.characteristics, self.competences, leg_armor.grade, context)
        elif leg_armor.category == "Pesado" and context == "resistencia":
            return leg_armor.get_bonus(self.characteristics, self.competences)
        return 0

    def get_leg_armor_penalty(self, context):
        leg_armor = self.inventory.equipped["pants"]
        if not leg_armor:
            return 0

        penalty = leg_armor.get_ta_penalty()
        if context == "ataque" and leg_armor.category in ["Intermedio", "Pesado"]:
            return penalty
        return 0

    def get_leg_armor_descriptions(self):
        leg_armor = self.inventory.equipped["pants"]
        if leg_armor:
            return leg_armor.get_descriptions()
        return []

    def get_boots_armor_descriptions(self):
        boot_armor = self.inventory.equipped["boots"]
        if boot_armor:
            return boot_armor.get_descriptions()
        return []
    
    def get_bracers_armor_descriptions(self):
        bracers_armor = self.inventory.equipped["bracers"]
        if bracers_armor:
            return bracers_armor.get_descriptions()
        return []
    
    def get_helmet_armor_descriptions(self):
        helmet_armor = self.inventory.equipped["helmet"]
        if helmet_armor:
            return helmet_armor.get_descriptions()
        return []
    
    def calculate_resistance_roll(self, agravio, context=None):
        if agravio in ["Veneno", "Infeccion"]:
            resistance_bonus = self.characteristics.tenacity
            competence_level = self.competences.get_level("resistance", agravio)
        elif agravio in ["Afliccion", "Maldicion"]:
            resistance_bonus = self.characteristics.composure
            competence_level = self.competences.get_level("resistance", agravio)
        elif agravio == "Alteracion":
            resistance_bonus = self.characteristics.resilience
            competence_level = self.competences.get_level("resistance", agravio)

            if context in ["Inmovilizado", "Atrapado"]:
                leg_armor = self.inventory.equipped["pants"]
                if leg_armor and leg_armor.category == "Pesado":
                    resistance_bonus += self.get_leg_armor_bonus("resistencia")

            if context in ["Desplazado", "Derribado", "Desequilibrado"]:
                resistance_bonus += self.get_resistance_bonus(context)

            if context in ["Conmocionado", "Cegado", "Aturdido"]:
                resistance_bonus += self.get_helmet_bonus(context)
        else:
            return f"Tipo de agravio desconocido: {agravio}"

        total_bonus = resistance_bonus + competence_level
        roll_description = f"1d10 + {total_bonus}"
        return roll_description

    def get_helmet_bonus(self, context):
        helmet = self.inventory.equipped.get("helmet", None)
        if helmet:
            if context == "focus" and helmet.category == "Intermedio":
                return helmet.get_bonus(self.characteristics, self.competences)
            elif context in ["Conmocionado", "Cegado", "Aturdido"] and helmet.category == "Pesado":
                return helmet.grade 
        return 0
    
    def get_helmet_perception_penalty(self):
        helmet = self.inventory.equipped.get("helmet", None)
        if helmet:
            if helmet.category == "Intermedio":
                return -helmet.grade
            elif helmet.category == "Pesado":
                return -(helmet.grade + 1)
        return 0
    
    def add_specialization(self, specialization_name, category="Oficios y Artes", characteristic="intellect"):
        if specialization_name not in self.specializations.specializations:
            # Encontrar la característica correcta para la especialización desde la lista predefinida
            predefined_spec = next((s for s in predefined_specializations if s[0] == specialization_name), None)
            if predefined_spec:
                category, characteristic = predefined_spec[1], predefined_spec[2]
            self.specializations.create_specialization(specialization_name, category, characteristic)
            self.competences.add_competence("specialization", specialization_name, level=0)
            print(f"Added new specialization: {specialization_name} with characteristic {characteristic}.")
        else:
            print(f"Specialization {specialization_name} already exists.")

    def increase_specialization_progress(self, specialization_name):
        if specialization_name in self.competences.specializations:
            self.competences.specializations[specialization_name].increase_progress()
            print(f"Increased progress for specialization: {specialization_name}.")
        else:
            print(f"Specialization {specialization_name} not found.")

    def update_helmet_bonus(self):
        helmet = self.inventory.equipped.get("helmet", None)
        if helmet and helmet.category == "Ligero":
            self.characteristics.helmet_bonus = helmet.get_bonus(self.characteristics, self.competences)
        else:
            self.characteristics.helmet_bonus = 0

    def calculate_specialization_roll(self, specialization_name):
        # Verificar si la especialización ya existe en la lista de competencias predefinida
        if specialization_name not in [name for name, category, characteristic in predefined_specializations]:
            self.add_specialization(specialization_name)

        # Acceder a los niveles y rangos de la especialización existente
        specialization_level = self.competences.get_level("specialization", specialization_name)
        specialization_rank = self.competences.get_rank("specialization", specialization_name)
        characteristic_name = self.specializations.get_specialization_characteristic(specialization_name)
        characteristic = getattr(self.characteristics, characteristic_name) if characteristic_name else 0
        # Calcular el bono total
        bonus = 0
        if specialization_name == "Sigilo":
            bonus = self.get_leg_armor_bonus("sigilo")
        elif specialization_name == "Acrobacias":
            bonus = self.get_leg_armor_bonus("acrobacias")
        elif specialization_name == "Vigor":
            bonus = self.get_leg_armor_bonus("vigor")
        elif specialization_name in ["Equilibrio", "Equitación"]:
            bonus = self.get_specialization_bonus(specialization_name)
        elif specialization_name == "Enfoque":
            bonus = self.get_helmet_bonus("focus")
        elif specialization_name == "Influencia":
            badge = self.inventory.equipped.get("pendant", None)
            if badge and badge.category == "Insignia":
                bonus = badge.bonus(self.characteristics, self.competences, badge.grade)

        
        helmet_penalty = self.get_helmet_perception_penalty() if specialization_name == "Percepción" else 0

        total_bonus = specialization_level + specialization_rank + characteristic + bonus + helmet_penalty
        roll_description = f"1d10 + {total_bonus}"
        return roll_description

    def calculate_characteristic_roll(self, characteristic_name):
        characteristic_value = getattr(self.characteristics, characteristic_name)
        level_bonus = self.qualities.player_level
        tc_penalty = self.get_boot_tc_penalty() if characteristic_name == "agility" else 0
        total_bonus = characteristic_value + level_bonus + tc_penalty
        roll_description = f"1d10 + {total_bonus}"
        return roll_description

    def calculate_impact_roll(self, weapon_name):
        weapon = self.inventory.equipped["right_hand"] if self.inventory.equipped["right_hand"] and self.inventory.equipped["right_hand"].name == weapon_name else self.inventory.equipped["left_hand"]
        if weapon and weapon.name == weapon_name:
            characteristic_value = getattr(self.characteristics, weapon.characteristic)
            competence_level = self.competences.get_level("martial", weapon_name)
            competence_rank = self.competences.get_rank("martial", weapon_name)
            if weapon.weapon_range == "melee":
                if competence_level == 0:
                    damage_roll = f"(1d{weapon.damage[1:]} + {weapon.grade * characteristic_value}) / 2"
                else:
                    damage_roll = f"{competence_rank}d{weapon.damage[1:]} + {weapon.grade * characteristic_value}"
            else:
                if competence_level == 0:
                    damage_roll = f"(1d{weapon.damage[1:]} + {weapon.grade}) / 2"
                else:
                    damage_roll = f"{competence_rank}d{weapon.damage[1:]} + {weapon.grade}"
            return damage_roll
        return "No weapon equipped"

    def calculate_personality_roll(self):
        level_bonus = self.qualities.player_level
        fixed_bonus = 5
        total_bonus = level_bonus + fixed_bonus
        roll_description = f"1d10 + {total_bonus}"
        return roll_description

    def get_equipment_bonus(self, category, name):
        return 0
    
    def list_specializations(self):
        for name, specialization in self.specializations.specializations.items():
            print(f"Specialization: {name}, Category: {specialization.category}, Characteristic: {specialization.characteristic}")

    def execute_technique(self, technique_name):
        technique = techniques.get(technique_name)
        if technique:
            print(f"Técnica {technique.name}: {technique.effect}")
            if self.resonance_level > 1:
                for level in range(2, self.resonance_level + 1):
                    if level in technique.advancements:
                        print(f"Avance Nivel {level}: {technique.advancements[level]}")
            # Aquí puedes añadir lógica para aplicar los efectos, coste de acción, etc.
        else:
            print(f"Técnica {technique_name} no encontrada.")

    def execute_maneuver(self, maneuver_name):
        maneuver = maneuvers.get(maneuver_name)
        if maneuver:
            print(f"Maniobra {maneuver.name}: {maneuver.effect}")
            # Aquí puedes añadir lógica para aplicar los efectos, coste de acción, etc.
        else:
            print(f"Maniobra {maneuver_name} no encontrada.")

    def apply_gift(self, gift_name):
        gift = gifts.get(gift_name)
        if gift:
            print(f"Don {gift.name} aplicado: {gift.effect}")
            # Aquí puedes añadir lógica para aplicar los efectos, etc.
        else:
            print(f"Don {gift_name} no encontrado.")

    def set_resonance_level(self, level):
        self.resonance_level = level