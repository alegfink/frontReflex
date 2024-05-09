import reflex as rx
from link_bio.components.link_button import link_button
from link_bio.components.title import title
from link_bio.styles.styles import Size as Size
from link_bio.routes import Route as Route

def courses_links() -> rx.Component:
    return rx.vstack(
        title('Cursos gratarolas'),
        link_button('primer curso','proba nomas', 'https://reflex.dev/docs/library/datadisplay'),
        link_button('segundo curso','aporta algo','https//reflex.dev/docs/library/datadisplay'),
        link_button('tercer curso','ya quisieras', 'https://reflex.dev/docs/library/datadisplay'),
        link_button('cuarto curso','no existe', 'https://reflex.dev/docs/library/datadisplay'),
        width = '100%',
        spacing='1'
        #spacing=Size.DEFAULT.value
    )