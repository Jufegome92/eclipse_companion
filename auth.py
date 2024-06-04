import flet as ft
from firebase_config import auth, db
from views import show_menu

def show_login_page(page, main_container):
    def register_user(e):
        email = email_field.value
        password = password_field.value
        try:
            user = auth.create_user_with_email_and_password(email, password)
            user_id = user['localId']
            auth.current_user = user  # Actualiza el usuario actual
            # Opcional: guarda información adicional en la base de datos
            db.child("users").child(user_id).set({"email": email})
            show_menu(page, main_container, user_id)  # Ir al menú principal después del registro
        except Exception as ex:
            error_message = str(ex)
            if 'email-already-in-use' in error_message:
                error_message = "El correo electrónico ya está en uso."
            elif 'invalid-email' in error_message:
                error_message = "El correo electrónico no es válido."
            elif 'weak-password' in error_message:
                error_message = "La contraseña es demasiado débil."
            else:
                error_message = f"Error desconocido: {error_message}"
            print(error_message)  # Imprimir el mensaje de error para depuración
            error_label.value = error_message
            page.update()

    def login_user(e):
        email = email_field.value
        password = password_field.value
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            user_id = user['localId']
            auth.current_user = user  # Actualiza el usuario actual
            show_menu(page, main_container, user_id)  # Ir al menú principal después del inicio de sesión
        except Exception as ex:
            error_message = str(ex)
            if 'invalid-email' in error_message:
                error_message = "El correo electrónico no es válido."
            elif 'wrong-password' in error_message:
                error_message = "La contraseña es incorrecta."
            elif 'user-not-found' in error_message:
                error_message = "No se encontró un usuario con este correo electrónico."
            else:
                error_message = f"Error desconocido: {error_message}"
            print(error_message)  # Imprimir el mensaje de error para depuración
            error_label.value = error_message
            page.update()

    email_field = ft.TextField(label="Correo Electrónico", width=200)
    password_field = ft.TextField(label="Contraseña", width=200, password=True)
    error_label = ft.Text(value="", color="red")

    login_button = ft.ElevatedButton("Iniciar Sesión", on_click=login_user)
    register_button = ft.ElevatedButton("Registrarse", on_click=register_user)

    main_container.controls.clear()
    main_container.controls.append(
        ft.Column(
            [
                ft.Text("Iniciar Sesión / Registrarse", size=24),
                email_field,
                password_field,
                login_button,
                register_button,
                error_label
            ],
            scroll=ft.ScrollMode.AUTO
        )
    )
    page.update()
