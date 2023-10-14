# ARCHIVO CONFIGURACION:

# colores primarios del sistema aditivo red, green, bluee
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255) # sistema aditivo todos los led prendidos al maximo es color blanco
black = (0, 0, 0) # todos apagados es color negro
# Sistema sustractivo colores primarios cyan, magenta,yellow

cyan = (0, 255, 255)
magenta = (255, 0, 255)
yellow = (255, 255, 0)
custom = (255, 174, 201)

# la lista o tupla de tamaño de pantalla deberia estar en un archivo config.py para luego importarlo
width = 800
height = 600
size_screen = (width, height)
center_screen_x = width // 2
center_screen_y = height // 2
center_screen = (width // 2 , height // 2) # centro de pantalla

#ACTUALIZACION DE PANTALLA
FPS = 60
#VELOCIDAD DE DESPLAZAMIENTO EN PIXELES
SPEED = 100