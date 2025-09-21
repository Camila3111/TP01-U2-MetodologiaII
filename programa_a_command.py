#PROGRAMA A
#patron command asignado en el trabajo

from abc import ABC, abstractmethod

#Interfaz Command
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

#receptor
class Light:
    def on(self):
        print("💡 La luz está encendida")

    def off(self):
        print("💡 La luz está apagada")

#comandos
class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.on()

class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.off()

#invocador
class RemoteControl:
    def __init__(self):
        self._commands = []

    def add_command(self, command):
        self._commands.append(command)

    def run(self):
        for command in self._commands:
            command.execute()
        self._commands.clear()

#usO
if __name__ == "__main__":
    light = Light()
    remote = RemoteControl()

    remote.add_command(LightOnCommand(light))
    remote.add_command(LightOffCommand(light))
    remote.run()