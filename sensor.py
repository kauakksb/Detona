from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

class ClassColorSensor:
    def __init__(self, port):
        self.sensor = ColorSensor(port) # Instanciando a classe de sensor
    
    # Obtendo o valor do sensor de cor com o tipo determinado
    def get_value(self, type):
        if type == 'color':
            return self.sensor.color()
        elif type == 'ambient':
            return self.sensor.ambient()
        elif type == 'reflection':
            return self.sensor.reflection()
        else:
            return self.sensor.rgb()

""" 

Dever no sensor de giro: 

- Criar a classe
- Definir a propriedade 'self.sensor' a partir do instanciamento da classe GyroSensor,
    junto com o parâmetro da porta

- Criação dos métodos
    - Retorne a velocidade angular
    - Retorne o ângulo atual
    - Reseta um ângulo a partir de um valor dado como parâmetro
"""