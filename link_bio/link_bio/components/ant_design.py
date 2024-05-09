#aca pongo componentes de react con reflex, sacados de la pagina ant_design

import reflex as rx
from link_bio.styles.colors import Color

class FloatButton(rx.Component):
    library = 'antd'
    tag = 'FloatButton'
    '''icon = rx.Var[rx.Image]'''   #son propiedades propias de react en ant_design que se pueden usar aca
    '''href = rx.Var[str]'''   #las variables son para que vayan modificandose de manera dinamica segun necesidad, se completan desde navbar
    target = '_blank'
    badge = {'dot':True, 'color': Color.PRIMARY.value}

float_button = FloatButton.create   #todo componente tiene una funcion llamada create para crear este componente, dejamos asociado a una variable la ceracion del componente