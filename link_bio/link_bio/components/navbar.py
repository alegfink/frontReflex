import reflex as rx
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import TextColor as TextColor
from link_bio.styles.colors import Color as Color
from link_bio.routes import Route as Route
from link_bio.components.ant_design import float_button

def navbar() -> rx.Component:
    return rx.hstack(  #con hstack tengo un componenete para meter cosas de forma horizontal
        rx.link(
            rx.text(
                'alegfink',
                color=Color.PRIMARY.value,  #color
                font_family='Comfortaa-Medium',  #fuente
                style=styles.navbar_title_style
            ),
            href=Route.INDEX.value
        ),
        float_button(
            '''icon = rx.Image(src='/favicon.ico'),''',
            '''href = 'https://reflex.dev/docs/library/datadisplay'''
        ),
        position='sticky',   #queda fijo
        bg=Color.CONTENT.value,   #color de fondo
        padding_x=Size.DEFAULT.value,
        padding_y=Size.SMALL.value,
        z_index='999',   #para asegurarme que siempre va a estar en la parte superior
        top='0', #con esto la barra siempre queda arriba
    ) 