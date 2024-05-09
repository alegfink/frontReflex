import reflex as rx
import link_bio.styles.styles as st

def title(text) -> rx.Component:
    return rx.heading(
        text,
        size='2',
        style = st.title_style
    )