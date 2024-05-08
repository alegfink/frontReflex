import reflex as rx
import link_bio_v2.styles.styles as st

def link_icon(url, alt) -> rx.Component:
    return rx.link(
        rx.icon(
            tag="link"
        ),
        href=url,
        is_external=True
    )