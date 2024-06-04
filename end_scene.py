from firebase_config import auth, db

def handle_end_scene(event, increment_fatigue, update_fatigue, update_instinctive_reactions, user_id, character_data):
    increment_fatigue(event)
    update_fatigue(event)
    update_instinctive_reactions(event)
    save_character_data(user_id, character_data)

def save_character_data(user_id, character_data):
    try:
        user = auth.current_user
        if user is not None:
            token = user['idToken']
            db.child("characters").child(user_id).set(character_data, token=token)
            print("Datos de personaje guardados exitosamente")
        else:
            print("No hay usuario autenticado.")
    except Exception as e:
        print(f"Error al guardar datos de personaje: {e}")

def load_character_data(user_id):
    try:
        user = auth.current_user
        if user is not None:
            token = user['idToken']
            character_data = db.child("characters").child(user_id).get(token=token).val()
            print("Datos de personaje cargados exitosamente")
            return character_data
        else:
            print("No hay usuario autenticado.")
            return None
    except Exception as e:
        print(f"Error al cargar datos de personaje: {e}")
        return None
