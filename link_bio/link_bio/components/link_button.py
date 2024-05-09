import reflex as rx
import link_bio.styles.styles as st


def link_button(title, body, url, is_external=True) -> rx.Component:    #is external True para que por defecto te lleve a otra pagina
    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon(
                    tag='a_arrow_up',
                    width = st.Size.BIG.value,
                    height = st.Size.BIG.value,
                    margin = st.Size.MEDIUM.value,
                    ),
                rx.vstack(
                    rx.text(title, style=st.button_title_style),
                    rx.text(body, style=st.button_body_style),
                    spacing='1',
                    #spacing = st.Size.SMALL.value,
                    align_items = 'start',
                    padding_right = st.Size.SMALL.value,
                    ),
                    width='100%'  
                ),
            width= '100%',
            height= '100%',
            padding= st.Size.SMALL.value,
            border_radius=st.Size.DEFAULT.value,
            background_color= st.Color.CONTENT.value,
            white_space= 'normal',   #es una propiedad que ayuda a realizar los truncados de los textos
            text_align= 'start', 
            color= st.TextColor.HEADER.value,
            _hover= {
                'background_color': st.Color.SECONDARY.value,
            }
                
            ),
        href=url,
        is_external=is_external,    # lleva a una nueva pagina
        width='100%',
        
    )
