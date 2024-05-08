import reflex as rx
from link_bio_v2.styles.styles import Size as Size
from link_bio_v2.styles.colors import TextColor as TextColor
from link_bio_v2.styles.colors import Color as Color

def info_text(title, body) -> rx.Component:
    return rx.box(
        rx.text(
            title,
            font_weight='bold',
            color=Color.PRIMARY.value,
            ),
        f' {body}', font_size=Size.MEDIUM.value,
        color=TextColor.BODY.value
    )