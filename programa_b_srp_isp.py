#PROGRAMA B
#aplicacion del srp+isp

from abc import ABC, abstractmethod

#isp-> Interfaces pequeñas y específicas
class Printer(ABC):
    @abstractmethod
    def print_doc(self, content: str):
        pass

class Scanner(ABC):
    @abstractmethod
    def scan_doc(self) -> str:
        pass

#srp-> clases con una responsabilidad
class SimplePrinter(Printer):
    def print_doc(self, content: str):
        print(f"🖨️ Imprimiendo: {content}")

class SimpleScanner(Scanner):
    def scan_doc(self) -> str:
        return "📄 Documento escaneado"

#isp-> el cliente solo va a usar lo que necesita 
class OfficeWorker:
    def __init__(self, printer: Printer):
        self.printer = printer

    def work(self):
        self.printer.print_doc("Informe semanal listo.")

if __name__ == "__main__":
    printer = SimplePrinter()
    worker = OfficeWorker(printer)
    worker.work()