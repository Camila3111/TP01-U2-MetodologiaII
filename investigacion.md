### Investigación: Patrones útiles para el Trabajo Integrador Final

Para el trabajo integrador final con Laravel 12 conviene aplicar algunos patrones clave en nuestro caso optamos por elegir la creacion de un sistema de inspecciones y registros de viviendas para el organismo publico IPV:

- **Repository:** separa la lógica de acceso a datos de los controladores, facilitando pruebas y cambios de motor de base sin romper el código.
- **Factory:** útil para crear entidades como Obras, Informes o Reclamos con valores iniciales estandarizados según el tipo de intervención.
- **Singleton:** aplicable a servicios compartidos como la generación de reportes PDF/Excel, evitando múltiples instancias pesadas.
- **Strategy:** permite calcular avances de obra de distintas formas (obra nueva vs. terminación vs. reacondicionamiento) sin condicionales gigantes.
- **Observer:** ideal para disparar eventos al actualizar un avance (ej. recalcular % total o generar notificaciones automáticas).

Estos patrones aportan mantenibilidad, flexibilidad y claridad en la arquitectura, fundamentales en un sistema público que puede crecer y requerir ajustes a largo plazo.