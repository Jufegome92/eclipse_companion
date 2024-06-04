import flet as ft
from data import especies_hp, velocidades, disciplinas, lenguajes
import math
from end_scene import handle_end_scene, save_character_data, load_character_data

def calculate_health(species, discipline, level, tenacity):
    base_health = especies_hp.get(species, 0)
    discipline_info = disciplinas.get(discipline, {"inicial": 0, "avance": 0})
    initial_health = discipline_info["inicial"]
    per_level_health = discipline_info["avance"]
    level_bonus = (level - 1) * per_level_health
    tenacity_bonus = tenacity * level
    max_health = base_health + initial_health + level_bonus + tenacity_bonus
    return max_health

def calculate_resilience(tenacity, wisdom, composure):
    return (tenacity + wisdom + composure) // 2

def calculate_preparation(agility, cunning, presence):
    return (agility + cunning + presence) // 2

def collect_character_data():
    return {
        "name": name_field.value,
        "species": species_dropdown.value,
        "discipline": discipline_dropdown.value,
        "level": player_level_field.value,
        "tenacity": tenacity_field.value,
        "wisdom": wisdom_field.value,
        "composure": composure_field.value,
        "agility": agility_field.value,
        "cunning": cunning_field.value,
        "presence": presence_field.value,
        "movement_speed": movement_speed.value,
        "max_health": max_health.value,
        "fatigue_level": fatigue_level.value,
        "instinctive_reactions": instinctive_reactions.value,
        "renewals": renewals.value,
        "resilience": resilience.value,
        "preparation": preparation.value,
        "sanity_level": sanity_level.value,
        "languages": lenguajes.get(species_dropdown.value, {})
    }

def populate_character_data(data):
    name_field.value = data.get("name", "")
    species_dropdown.value = data.get("species", "")
    discipline_dropdown.value = data.get("discipline", "")
    player_level_field.value = data.get("level", "1")
    tenacity_field.value = data.get("tenacity", "0")
    wisdom_field.value = data.get("wisdom", "0")
    composure_field.value = data.get("composure", "0")
    agility_field.value = data.get("agility", "0")
    cunning_field.value = data.get("cunning", "0")
    presence_field.value = data.get("presence", "0")
    movement_speed.value = data.get("movement_speed", "0")
    max_health.value = data.get("max_health", "0")
    fatigue_level.value = data.get("fatigue_level", "0")
    instinctive_reactions.value = data.get("instinctive_reactions", "0")
    renewals.value = data.get("renewals", "0")
    resilience.value = data.get("resilience", "0")
    preparation.value = data.get("preparation", "0")
    sanity_level.value = data.get("sanity_level", "0")

def create_character_sheet(page, main_container, show_menu, user_id):
    global name_field, species_dropdown, discipline_dropdown, player_level_field, tenacity_field, wisdom_field, composure_field
    global agility_field, cunning_field, presence_field, movement_speed, max_health, fatigue_level, fatigue_accumulated
    global endurance_field, instinctive_reactions, renewals, resilience, preparation, sanity_level, disorders, languages_section

    def calculate_roll(characteristic_value, player_level, bonus_value):
        return f"1d10 + {player_level + characteristic_value + bonus_value}"

    def update_roll(characteristic_value, roll_label, player_level, bonus_value):
        try:
            characteristic_value = int(characteristic_value.value)
            player_level = int(player_level.value)
            bonus_value = int(bonus_value.value) if bonus_value.value else 0
            if characteristic_value > 5:
                characteristic_value = 5
                characteristic_value.value = "5"
            if player_level > 12:
                player_level = 12
                player_level.value = "12"
            roll_label.value = calculate_roll(characteristic_value, player_level, bonus_value)
        except ValueError:
            roll_label.value = "Valor inválido"
        page.update()

    def create_on_change(characteristic_value, roll_label, player_level, bonus_value):
        return lambda e: update_roll(characteristic_value, roll_label, player_level, bonus_value)

    def create_characteristic_fields(characteristics, player_level):
        fields = []
        for characteristic in characteristics:
            characteristic_value = ft.TextField(value="1", width=40)
            bonus_value = ft.TextField(value="0", width=40)
            roll_label = ft.Text(value=calculate_roll(int(characteristic_value.value), int(player_level.value), int(bonus_value.value)), size=18)
            characteristic_value.on_change = create_on_change(characteristic_value, roll_label, player_level, bonus_value)
            bonus_value.on_change = create_on_change(characteristic_value, roll_label, player_level, bonus_value)
            fields.append(ft.Row([
                ft.Text(characteristic, size=16),
                characteristic_value,
                ft.Text("Bonificador:"),
                bonus_value,
                ft.Text("Tirada:"),
                roll_label
            ], scroll='auto'))
            if characteristic == "Tenacidad":
                global tenacity_field
                tenacity_field = characteristic_value
                tenacity_field.on_change = lambda e: update_health_and_fatigue()
            if characteristic == "Sabiduría":
                global wisdom_field
                wisdom_field = characteristic_value
                wisdom_field.on_change = lambda e: update_resilience_preparation()
            if characteristic == "Compostura":
                global composure_field
                composure_field = characteristic_value
                composure_field.on_change = lambda e: update_resilience_preparation()
            if characteristic == "Agilidad":
                global agility_field
                agility_field = characteristic_value
                agility_field.on_change = lambda e: update_resilience_preparation()
            if characteristic == "Astucia":
                global cunning_field
                cunning_field = characteristic_value
                cunning_field.on_change = lambda e: update_resilience_preparation()
            if characteristic == "Presencia":
                global presence_field
                presence_field = characteristic_value
                presence_field.on_change = lambda e: update_resilience_preparation()
        return ft.Column(fields, scroll='auto')

    def update_movement_speed(e):
        species = species_dropdown.value
        if species in velocidades:
            movement_speed.value = str(velocidades[species])
        else:
            movement_speed.value = "0"
        update_health()
        update_languages()
        page.update()

    def update_health(e=None):
        species = species_dropdown.value
        discipline = discipline_dropdown.value
        level = int(player_level_field.value) if player_level_field.value else 1
        tenacity = int(tenacity_field.value) if tenacity_field.value else 0
        max_health.value = str(calculate_health(species, discipline, level, tenacity))
        page.update()

    def update_fatigue(e=None):
        tenacity = int(tenacity_field.value) if tenacity_field.value else 0
        vigor = int(endurance_field.value) if endurance_field.value else 0
        accumulated = int(fatigue_accumulated.value) if fatigue_accumulated.value else 0
        endurance = math.ceil(vigor / 2) + tenacity
        fatigue_level.value = str(max(0, accumulated - endurance))
        update_instinctive_reactions()
        update_renewals()
        page.update()

    def update_instinctive_reactions(e=None):
        tenacity = int(tenacity_field.value) if tenacity_field.value else 0
        vigor = int(endurance_field.value) if endurance_field.value else 0
        endurance = math.ceil(vigor / 2) + tenacity
        instinctive_reactions.value = str(max(0, endurance - int(fatigue_level.value)))
        page.update()

    def update_renewals(e=None):
        tenacity = int(tenacity_field.value) if tenacity_field.value else 0
        vigor = int(endurance_field.value) if endurance_field.value else 0
        endurance = math.ceil(vigor / 2) + tenacity
        renewals.value = str(endurance)
        page.update()

    def update_resilience_preparation(e=None):
        tenacity = int(tenacity_field.value) if tenacity_field.value else 0
        wisdom = int(wisdom_field.value) if wisdom_field.value else 0
        composure = int(composure_field.value) if composure_field.value else 0
        agility = int(agility_field.value) if agility_field.value else 0
        cunning = int(cunning_field.value) if cunning_field.value else 0
        presence = int(presence_field.value) if presence_field.value else 0
        resilience.value = str(calculate_resilience(tenacity, wisdom, composure))
        preparation.value = str(calculate_preparation(agility, cunning, presence))
        page.update()

    def update_health_and_fatigue(e=None):
        update_health()
        update_fatigue()
        update_resilience_preparation()

    def increment_fatigue(e):
        accumulated = int(fatigue_accumulated.value) if fatigue_accumulated.value else 0
        fatigue_accumulated.value = str(accumulated + 1)
        update_fatigue()

    def decrement_fatigue(e):
        accumulated = int(fatigue_accumulated.value) if fatigue_accumulated.value else 0
        fatigue_accumulated.value = str(max(0, accumulated - 1))
        update_fatigue()

    def decrement_instinctive_reactions(e):
        current_value = int(instinctive_reactions.value) if instinctive_reactions.value else 0
        instinctive_reactions.value = str(max(0, current_value - 1))
        page.update()

    def decrement_renewals(e):
        current_value = int(renewals.value) if renewals.value else 0
        renewals.value = str(max(0, current_value - 1))
        page.update()

    def update_sanity(e=None):
        composure = int(composure_field.value) if composure_field.value else 0
        sanity = composure * 2
        disorders_value = int(disorders.value) if disorders.value else 0
        sanity_level.value = str(max(0, disorders_value - sanity))
        page.update()

    def update_languages(e=None):
        species = species_dropdown.value
        if species in lenguajes:
            languages_section.controls.clear()
            for language, rank in lenguajes[species].items():
                languages_section.controls.append(ft.Text(f"{language}: {rank}"))
        else:
            languages_section.controls.clear()
            languages_section.controls.append(ft.Text("No hay lenguajes disponibles"))
        page.update()

    def toggle_help_text(e):
        help_text.visible = not help_text.visible
        page.update()

    def toggle_add_language_section(e):
        add_language_section.visible = not add_language_section.visible
        page.update()

    def add_language(e):
        new_language = new_language_dropdown.value
        new_rank = int(new_language_rank.value)
        languages_section.controls.append(ft.Text(f"{new_language}: Rango {new_rank}"))
        page.update()

    def save_character_data_to_db(e):
        character_data = collect_character_data()
        save_character_data(user_id, character_data)

    def load_character_data_from_db(e):
        character_data = load_character_data(user_id)
        if character_data:
            populate_character_data(character_data)
        page.update()

    name_field = ft.TextField(label="Nombre", width=200)
    global species_dropdown
    species_dropdown = ft.Dropdown(label="Especie", options=[ft.dropdown.Option(species) for species in especies_hp.keys()], on_change=update_movement_speed)
    global discipline_dropdown
    discipline_dropdown = ft.Dropdown(label="Disciplina", options=[ft.dropdown.Option(discipline) for discipline in disciplinas.keys()], on_change=update_health_and_fatigue)
    global movement_speed
    movement_speed = ft.TextField(label="Velocidad de Movimiento", value="0", width=200, read_only=True)
    gender_field = ft.TextField(label="Género", width=100)
    weight_field = ft.TextField(label="Peso", width=100)
    age_field = ft.TextField(label="Edad", width=100)
    global player_level_field
    player_level_field = ft.TextField(value="1", width=40, on_change=update_health_and_fatigue)
    global max_health
    max_health = ft.TextField(label="Puntos de Salud", value="0", width=200, read_only=True)
    damage_received = ft.TextField(label="Daño Recibido", width=200)

    global fatigue_level, fatigue_accumulated, endurance_field
    fatigue_accumulated = ft.TextField(label="Fatiga Acumulada", value="0", width=200, read_only=True)
    endurance_field = ft.TextField(label="Aguante", value="1", width=200)
    fatigue_level = ft.TextField(label="Nivel de Fatiga", value="0", width=200, read_only=True)
    end_scene_button = ft.ElevatedButton("Fin de Escena", on_click=lambda e: handle_end_scene(e, increment_fatigue, update_fatigue, update_instinctive_reactions, user_id, collect_character_data()))
    increase_fatigue_button = ft.ElevatedButton("Incrementar Fatiga", on_click=increment_fatigue)
    decrease_fatigue_button = ft.ElevatedButton("Disminuir Fatiga", on_click=decrement_fatigue)

    global instinctive_reactions, renewals
    instinctive_reactions = ft.TextField(label="Reacciones Instintivas", value="0", width=200, read_only=True)
    renewals = ft.TextField(label="Renovaciones", value="0", width=200, read_only=True)
    decrease_instinctive_reactions_button = ft.ElevatedButton("Disminuir Reacciones Instintivas", on_click=decrement_instinctive_reactions)
    decrease_renewals_button = ft.ElevatedButton("Disminuir Renovaciones", on_click=decrement_renewals)

    global resilience, preparation
    resilience = ft.TextField(label="Resiliencia", value="0", width=200, read_only=True)
    preparation = ft.TextField(label="Preparación", value="0", width=200, read_only=True)

    global sanity_level, disorders
    sanity_level = ft.TextField(label="Sanidad", value="0", width=200, read_only=True)
    disorders = ft.TextField(label="Trastornos", value="0", width=200, on_change=update_sanity)

    global languages_section
    languages_section = ft.Column([])

    help_icon = ft.Icon(name="help_outline", size=20, color="blue")
    help_text = ft.Text("Rango 1: Comprender frases básicas, no sabes leer ni escribir\n"
                        "Rango 2: Mantener conversaciones, leer y escribir frases básicas\n"
                        "Rango 3: Hablar, leer y escribir con fluidez", visible=False)
    help_button = ft.Container(
        content=help_icon,
        on_click=toggle_help_text,
    )

    new_language_dropdown = ft.Dropdown(
        label="Nuevo Lenguaje",
        options=[ft.dropdown.Option(lang) for lang in lenguajes.keys()]
    )
    new_language_rank = ft.TextField(label="Rango", width=100)
    add_language_button = ft.ElevatedButton("Agregar Lenguaje", on_click=add_language)

    add_language_section = ft.Column(
        controls=[
            ft.Row([
                new_language_dropdown,
                new_language_rank,
                add_language_button
            ], scroll='auto')
        ],
        visible=False
    )

    add_language_icon = ft.Icon(name="add", size=20, color="green")
    add_language_button = ft.Container(
        content=add_language_icon,
        on_click=toggle_add_language_section,
    )

    physical_characteristics = create_characteristic_fields(["Fuerza", "Agilidad", "Tenacidad"], player_level_field)
    mental_characteristics = create_characteristic_fields(["Sabiduría", "Intelecto", "Astucia"], player_level_field)
    social_characteristics = create_characteristic_fields(["Carisma", "Presencia", "Compostura"], player_level_field)

    def update_all_rolls():
        for section in [physical_characteristics, mental_characteristics, social_characteristics]:
            for row in section.controls:
                characteristic_value = row.controls[1]
                bonus_value = row.controls[3]
                roll_label = row.controls[5]
                update_roll(characteristic_value, roll_label, player_level_field, bonus_value)
        update_health_and_fatigue()
        update_sanity()

    def toggle_visibility(e, section):
        section.visible = not section.visible
        page.update()

    player_level_section = ft.Column([player_level_field], visible=False)
    physical_section = ft.Column([physical_characteristics], visible=False)
    mental_section = ft.Column([mental_characteristics], visible=False)
    social_section = ft.Column([social_characteristics], visible=False)
    languages_section = ft.Column([], visible=False)

    items = [
        ft.Row([
            ft.ElevatedButton("Nivel del Jugador", on_click=lambda e: toggle_visibility(e, player_level_section)),
            end_scene_button
        ], scroll='auto'),
        player_level_section,
        ft.Row([name_field, gender_field, weight_field, age_field], scroll='auto'),
        ft.Row([species_dropdown, discipline_dropdown, movement_speed], scroll='auto'),
        ft.Row([max_health, damage_received], scroll='auto'),
        ft.Row([fatigue_level, increase_fatigue_button, decrease_fatigue_button], scroll='auto'),
        ft.Row([instinctive_reactions, decrease_instinctive_reactions_button], scroll='auto'),
        ft.Row([renewals, decrease_renewals_button], scroll='auto'),
        ft.Row([resilience, preparation], scroll='auto'),
        ft.Row([sanity_level, disorders], scroll='auto'),
        ft.Row([
            ft.Column([
                ft.ElevatedButton("Características Físicas", on_click=lambda e: toggle_visibility(e, physical_section)),
                physical_section
            ]),
            ft.Column([
                ft.ElevatedButton("Características Mentales", on_click=lambda e: toggle_visibility(e, mental_section)),
                mental_section
            ]),
            ft.Column([
                ft.ElevatedButton("Características Sociales", on_click=lambda e: toggle_visibility(e, social_section)),
                social_section
            ])
        ], scroll='auto'),
        ft.Row([
            ft.ElevatedButton("Lenguajes", on_click=lambda e: toggle_visibility(e, languages_section)),
            languages_section,
            add_language_button,
            add_language_section,
            help_button,
            help_text
        ], scroll='auto'),
        ft.Row([
            ft.ElevatedButton("Guardar Personaje", on_click=save_character_data_to_db),
            ft.ElevatedButton("Cargar Personaje", on_click=load_character_data_from_db)
        ], scroll='auto'),
        ft.ElevatedButton("Volver al menú principal", on_click=lambda e: show_menu(page, main_container, user_id))
    ]

    scrollable = ft.Container(
        content=ft.Column(
            controls=items,
            scroll=ft.ScrollMode.AUTO
        ),
        expand=True
    )

    main_container.controls.append(scrollable)
    page.update()
