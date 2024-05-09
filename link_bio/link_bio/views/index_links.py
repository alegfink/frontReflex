import reflex as rx
from link_bio.components.link_button import link_button
from link_bio.components.title import title
from link_bio.styles.styles import Size as Size
from link_bio.routes import Route as Route

def index_links() -> rx.Component:
    return rx.vstack(
        title('Comunidad'),
        link_button('cursos gratis','te lleva a la pagina cursos', Route.COURSES.value, is_external=False), #el external es lo que define si se abre una nueva pagina
        link_button('youtube','body youtube', 'https://reflex.dev/docs/library/datadisplay'),
        link_button('twich','body twich', 'https://reflex.dev/docs/library/datadisplay'),
        link_button('instagram','body instagram', 'https://reflex.dev/docs/library/datadisplay'),
        link_button('facebook','body facebook', 'https://reflex.dev/docs/library/datadisplay'),
        width = '100%',
        spacing='1'
        #spacing=Size.DEFAULT.value
    )