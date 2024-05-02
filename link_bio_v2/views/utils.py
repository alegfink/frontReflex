import reflex as rx

#comun

preview = 'https://ale.dev/preview.jpg'
'''def lang() -> rx.Component:
    return rx.script("document.documentElement.lang='es'")''' #no me termina de funcionar, es para definir el lenguaje
_meta=[
        {'name':'og:type','content':'website'},
        {'name':'og:image','content':preview},
        {'name':'twitter:card','content':'summary_large_image'},
        {'name':'twitter:site','content':'@afink'}
    ]

#index

index_title = 'Prueba index Ale'
index_description = 'Probando index'
index_meta=[
        {'name':'og:title', 'content':index_title},
        {'name':'og:description','content':index_description}
        ]
index_meta.extend(_meta)

#cursos

courses_title = 'Prueba cursos Ale'
courses_description = 'Probando cursos'
courses_meta=[
        {'name':'og:title', 'content':courses_title},
        {'name':'og:description','content':courses_description}
        ]
courses_meta.extend(_meta)