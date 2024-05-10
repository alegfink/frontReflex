import reflex as rx

config = rx.Config(
    app_name="link_bio",
    # esta es una manera de agregar url de back para que conecte con el front
    api_url='https://frontreflex-production.up.railway.app',  
    # cors es para tener mas seguridad sobre las conexiones entre urls
    cors_allowed_origins=[
        "http://localhost:3000",
        "https://frontreflex-production.up.railway.app"
    ]
)