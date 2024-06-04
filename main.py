import flet as ft
from views import show_menu
from auth import show_login_page
import asyncio

def main(page: ft.Page):
    main_container = ft.Column(scroll=ft.ScrollMode.AUTO, expand=True)
    page.add(main_container)
    show_login_page(page, main_container)

if __name__ == "__main__":
    # Si ya hay un bucle de eventos en ejecución, obténlo, de lo contrario crea uno nuevo.
    loop = asyncio.get_event_loop()
    if loop.is_running():
        print("El bucle de eventos ya está en ejecución.")
        loop.run_until_complete(ft.app_async(target=main))
    else:
        loop.run_until_complete(ft.app_async(target=main))
