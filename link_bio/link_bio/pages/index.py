import reflex as rx
from link_bio.components.navbar import navbar
import link_bio.styles.styles as st
from link_bio.views.header import header
from link_bio.views.index_links import index_links
from link_bio.components.footer import footer
from link_bio.styles.colors import Color as Color
from link_bio.styles.colors import TextColor as TextColor
from link_bio.styles.fonts import Font as Font
import link_bio.views.utils as utils

@rx.page(
        title=utils.index_title,
        description=utils.index_description,
        image=utils.preview,
        meta=utils.index_meta
)    #todo lo que anotemos con page, automaticamente se convierte en una pagina

def index() -> rx.Component:    #index seria pagina de inicio
    '''return rx.text ('Hola reflex', color='blue') # con return indico que es lo que quiero devolver como parte grafica'''
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
            header(),
            index_links(),
            max_width=st.MAX_WIDTH,
            width='100%',
            marging_y=st.Size.BIG.value,
            )
        ),        
        footer()
    )

