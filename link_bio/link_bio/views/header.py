import reflex as rx
from link_bio.components.link_icon import link_icon
from link_bio.components.info_text import info_text
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import TextColor as TextColor
from link_bio.styles.fonts import Font as Font
from link_bio.styles.colors import Color as Color

def header(details=True) -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                fallback='AF', 
                size='4',
                color=TextColor.BODY.value,
                bg=Color.CONTENT.value,
                # src = 'avatar.jpg,    para poner una imagen
                padding='2px',
                boder='4px',
                border_color=Color.PRIMARY.value
                ),
            rx.vstack(
                rx.heading(
                    'ALEJANDRO FINKKK',
                    size='3',
                    color=TextColor.HEADER.value,
                    font_family = Font.TITLE.value
                    ),
                rx.text(
                    '@alegfink',
                    margin_top='0px !important',
                    color=TextColor.BODY.value
                    ),
                rx.hstack(
                    link_icon('https://reflex.dev/docs/library/datadisplay', 'instagram'),
                    link_icon('https://reflex.dev/docs/library/datadisplay', 'youtube'),
                    link_icon('https://reflex.dev/docs/library/datadisplay', 'facebook')
        ),
                width = '100%',
                align_items = 'start',
                #spacing=Size.DEFAULT.value
                spacing='1'
            )
        ),
        rx.cond(
            details,
            rx.vstack(
                rx.flex(
                    info_text('+13', 'años de experiencia'),
                    rx.spacer(),
                    info_text('+13', 'años de experiencia'),
                    rx.spacer(),
                    info_text('+13', 'años de experiencia'),
                    width='100%',
                    #color=TextColor.HEADER.value
                        ),
                rx.text(
                    'sadkjashsdkakhdakja',
                    font_size=Size.MEDIUM.value,
                    color=TextColor.BODY.value
                    )
            ), 
        
        ),
        #spacing=Size.BIG.value,
        spacing='4',
        align_items = 'start'
    )