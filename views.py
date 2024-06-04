import flet as ft
from character_sheet import create_character_sheet

def create_view(view_name, show_menu, user_id, page, main_container):
    return ft.Column([
        ft.Text(f"Esta es la {view_name}", size=24),
        ft.ElevatedButton("Volver al menú principal", on_click=lambda e: show_menu(page, main_container, user_id))
    ], scroll=ft.ScrollMode.AUTO)

def show_menu(page, main_container, user_id):
    main_container.controls.clear()
    main_container.controls.append(ft.Column([
        ft.Text("Menú Principal", size=32),
        ft.ElevatedButton("Hoja de Personaje", on_click=lambda e: switch_to_character_sheet(page, main_container, show_menu, user_id)),
        ft.ElevatedButton("Hoja de Competencias", on_click=lambda e: switch_to_view("Hoja de Competencias", page, main_container, show_menu, user_id)),
        ft.ElevatedButton("Hoja de Equipo", on_click=lambda e: switch_to_view("Hoja de Equipo", page, main_container, show_menu, user_id)),
        ft.ElevatedButton("Hoja de Disciplina", on_click=lambda e: switch_to_view("Hoja de Disciplina", page, main_container, show_menu, user_id)),
    ], scroll=ft.ScrollMode.AUTO))
    page.update()

def switch_to_character_sheet(page, main_container, show_menu, user_id):
    main_container.controls.clear()
    create_character_sheet(page, main_container, show_menu, user_id)

def switch_to_view(view_name, page, main_container, show_menu, user_id):
    main_container.controls.clear()
    main_container.controls.append(create_view(view_name, show_menu, user_id, page, main_container))
    page.update()
