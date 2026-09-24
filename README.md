# Red Distribuida de Monitoreo Hídrico — Sabana Centro (Cundinamarca)

## Actividad de Refuerzo #2.3 — Conectividad en IoT

### Internet de las Cosas · Facultad de Ingeniería · Universidad de La Sabana · 2026-2

### Contexto

De un prototipo aislado a una red de vigilancia regional

El Challenge de monitoreo hídrico resuelve la medición en un punto crítico: un dispositivo que mide variables meteorológicas y de nivel, procesa la información localmente y alerta in situ a la comunidad. Pero la crisis hídrica de la Sabana de Bogotá no ocurre en un solo embalse.

La CAR ha identificado 20 municipios de Cundinamarca en riesgo extremo por desabastecimiento, y el sistema de embalses que regula el abastecimiento de la región —Neusa, Sisga, Tominé— está distribuido a lo largo de decenas de kilómetros. Un nodo aislado no permite comparar tendencias entre cuencas ni consolidar una visión regional para tomar decisiones de racionamiento.

El problema de esta actividad: ¿cómo se conectan múltiples nodos de monitoreo, dispersos geográficamente, a una plataforma central que las autoridades puedan consultar desde un solo tablero?

### Objetivo

Diseñar y validar el componente de conectividad de una red inalámbrica de sensores (WSN) que integre tres nodos de monitoreo hídrico ubicados en puntos críticos de Sabana Centro, empleando MQTT, un gateway y una plataforma IoT, y comprobar su funcionamiento mediante simulación en Cisco Packet Tracer.

### Solución implementada

Una red de tres nodos publicadores que reportan telemetría por MQTT 3.1.1 hacia un broker central, del cual un tablero suscriptor consume el estado consolidado de los tres puntos.

| Componentes del sistema | Implementación |
| :-- | :-- |
| Dispositivos | 3 nodos MCU-PT con módulo de conectividad celular |
| Gateway | Cell Tower + Central Office Server | 
| Conectividad | Backbone IP entre la central de operadora y el broker |
| Plataforma IoT | Broker MQTT 3.1.1 (puerto 1883) |
| Usuario final | Tablero: cliente MQTT suscrito a `sabanacentro/#` |

**Variables monitoreadas por nodo:** temperatura ambiente, humedad relativa, temperatura del agua, luz y presión atmosférica.

Hay nodos en Neusa, Cogua y Tominé.

## Roles e Integrantes del Equipo

| Integrante | Rol | Actividades y Contribuciones Clave |
| :-- | :-- | :-- |
| Carlos Andrés Vargas | Diseñador de la topología | Diseñó la topología y los protocolos de rd y aplicación en Packet Tracer, verificando servidores, paneles de control y nodos. |
| Karol Briyith Esquivel | Documentación | Realizó partes de la Wiki documentando procesos, troubleshooting y demás elementos dentro de la red. |
| David Santiago Murcia | Supervisión funcionamiento de MQTT | Supervisó el proceso hecho en Packet Tracer, verificando fuentes para saber si se estaba realizando correctamente. |
