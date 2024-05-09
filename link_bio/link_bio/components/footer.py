import reflex as rx
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import TextColor as TextColor

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            src='/favicon.ico',
            height=Size.BIG.value,
            weight=Size.BIG.value,
            alt='Logotipo'  #TODAS LAS IMAGENES DEBEN TENER DEFINIDO TAMAÑO Y TEXTO ALTERNATIVO
            ),
        rx.link(
            'Este es un link del footer que lleva a youtube',
            href='https://www.youtube.com/',
            is_external=True,
            font_size = Size.MEDIUM.value
            ),
        rx.text(
            'Este es el footer',
            font_size = Size.MEDIUM.value
            ),
        margin_bottom=Size.BIG.value,
        color=TextColor.FOOTER.value,
        padding_bottom=Size.BIG.value,
        padding_x=Size.BIG.value,
        #spacing=Size.DEFAULT.value
        #spacing='4',
        align_items='center'
    )