from enum import Enum
import reflex as rx
from .colors import Color as Color
from .colors import TextColor as TextColor
from .fonts import Font as Font

#Constants
MAX_WIDTH = '37.5em'

#Sizes
class Size(Enum):
    SMALL = '0.5em'
    MEDIUM = '0.8em'
    DEFAULT = '1em'
    LARGE = '1.5em'
    BIG = '2em'

#Styles
BASE_STYLE = {
    'font_family': Font.DEFAULT.value,
    'background_color': Color.BACKGROUND.value,
    
}
'''BASE_STYLE = {
    'font_family': Font.DEFAULT.value,
    'background_color': Color.BACKGROUND.value,
    rx.button: {
        'width': '100%',
        'height': '100%',
        'padding': Size.SMALL.value,
        'border_radius':Size.DEFAULT.value,
        'background_color': Color.CONTENT.value,
        'white_space': 'normal',   #es una propiedad que ayuda a realizar los truncados de los textos
        'text_align': 'start', 
        'color': TextColor.HEADER.value,
        '_hover': {
            'background_color': Color.SECONDARY.value,
        }
    },
    rx.link : {
        'text_decoratation': 'none',
        '_hover': {}
    }
}'''
'''BASE_STYLE = {
    'font_family': Font.DEFAULT.value,
    'background_color': Color.BACKGROUND.value,
    rx.button: {
        'width': '100%',
        'height': '100%',
        'padding': Size.SMALL.value,
        'border_radius':Size.DEFAULT.value,
        'background_color': Color.CONTENT.value,
        'white_space': 'normal',   #es una propiedad que ayuda a realizar los truncados de los textos
        'text_align': 'start', 
        'color': TextColor.HEADER.value,
        '_hover': {
            'background_color': Color.SECONDARY.value,
        }
    }
    }'''

navbar_title_style = dict (
    #font_family=Font.LOGO.value,
    font_size=Size.LARGE.value
)

title_style = dict (
    size = 'lg',    #en realidad size es una propiedad del componente rx.heading, por ende no afecta en nada que figure aca
    width = '100%',
    padding_top = Size.DEFAULT.value,
    color = TextColor.HEADER.value,
    font_family=Font.TITLE.value,
)

button_title_style = dict(
    font_size=Size.DEFAULT.value,
    color = TextColor.HEADER.value,
    font_family=Font.TITLE.value,
)

button_body_style = dict(
    font_size=Size.MEDIUM.value,
    color = TextColor.BODY.value,
    font_family=Font.DEFAULT.value,
)
