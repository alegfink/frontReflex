"""Welcome to Reflex! This file outlines the steps to create a basic app."""
#from link_bio.rxconfig import config

import reflex as rx
import link_bio.styles.styles as st
from link_bio.pages.index import index
from link_bio.pages.courses import courses

'''docs_url = "https://reflex.dev/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"


class State(rx.State):
    """The app state."""

    pass


def index() -> rx.Component:
    return rx.fragment(
        rx.color_mode_button(rx.color_mode_icon(), float="right"),
        rx.vstack(
            rx.heading("Welcomeeeee to Reflex!", font_size="2em"),
            rx.box("Get started by editing ", rx.code(filename, font_size="1em")),
            rx.link(
                "Check out our docs!",
                href=docs_url,
                border="0.1em solid",
                padding="0.5em",
                border_radius="0.5em",
                _hover={
                    "color": rx.color_mode_cond(
                        light="rgb(107,99,246)",
                        dark="rgb(179, 175, 255)",
                    )
                },
            ),
            spacing="1.5em",
            font_size="2em",
            padding_top="10%",
        ),
    )


# Add state and page to the app.'''



class State(rx.State):      #sera la encargada de manejar los estados, con esto podemos evitar que sea estatica
    pass



'''app = rx.App(   #app es un componenete que va a generar la aplicacion con reflex
    style = st.BASE_STYLE   
)   #tira error'''
app = rx.App(
    style=st.BASE_STYLE
)



