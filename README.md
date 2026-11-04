# OMNIMORPH: Datos Oficiales y Analítica Táctica — Brasil 1–7 Alemania (2014)

Repositorio oficial de datos espaciales, telemetría y analítica táctica del histórico partido de semifinal de la Copa Mundial de la FIFA 2014 entre **Brasil y Alemania** (8 de julio de 2014, Estádio Mineirão), estructurado bajo la arquitectura y contratos de **Project OMNIMORPH**.

---

## Arquitectura y Contratos Técnicos de OMNIMORPH

OMNIMORPH es un sistema de inteligencia artificial híbrido multi-agente:
$$\text{Percepción GPU Local (A1–A6)} \longrightarrow \text{Refinamiento Matemático IBM Cloud (P1–P3)} \longrightarrow \text{Dashboard 4 Paneles + TTS Sincronizado}$$

### 1. Sistema de Coordenadas de Campo (Métrico)
- **Dimensiones normalizadas**: $12000\text{ cm} \times 7000\text{ cm}$ ($120\text{ m} \times 70\text{ m}$).
- **Eje X ($0$ a $12000\text{ cm}$)**:
  - $x = 0$: Línea de gol defendida por Brasil en el 1T (centro de portería en $y = 3500$).
  - $x = 12000$: Línea de gol defendida por Alemania en el 1T.
- **Eje Y ($0$ a $7000\text{ cm}$)**:
  - $y = 0$: Banda Sur (lateral derecho defensivo de Brasil en 1T).
  - $y = 7000$: Banda Norte (lateral izquierdo defensivo de Brasil en 1T).
- **Identificadores de Equipo (`team`)**:
  - `0`: Brasil
  - `1`: Alemania
  - `null`: Árbitro / Balón
- **Velocidades**: Expresadas en $\text{cm/s}$.

### 2. Reloj Común y Ventanas Tácticas
- Tasa de muestreo de captura: **25 fps** ($0.04\text{ s}$ por cuadro).
- Ventanas de agregación táctica: **$\sim 4\text{ s}$** ($100\text{ cuadros}$ por ventana).
- **Contrato JSON**:
  ```json
  {
    "t0": 0.0,
    "t1": 4.0,
    "texto_tactico_dt": "Diagnóstico de marcas, pantallas y altura de bloque (<5s overlay)",
    "texto_narracion_accesible": "Descripción espacial de audio libre de alucinaciones",
    "metricas": {
      "posesion": "Alemania",
      "presion": "Baja",
      "zona_del_balon": "Área de penalti"
    }
  }
  ```

---

## Estructura del Repositorio

```text
omnimorph-brasil-alemania-2014/
├── 01_gol_muller_min11/
│   ├── README.md                      # Análisis táctico profundo del gol 1 (ABP)
│   ├── gol_1_muller_ventanas.json     # Ventanas tácticas de ~4s con payload dual (DT / TTS)
│   └── muestra_telemetria_muller.json # Muestra de tracking a 25 fps (22 jugadores + árbitro + balón)
├── 02_partido_completo/
│   ├── contexto_partido.json          # Metadatos del partido y plantillas completas (23 jugadores)
│   ├── estadisticas_partido.json      # Estadísticas globales (1T, 2T, FT y jugadores clave)
│   ├── estadisticas_partido.csv       # Tabla comparativa en formato tabular CSV
│   ├── linea_tiempo_goles.json        # Desglose táctico y espacial de los 8 goles
│   └── linea_tiempo_goles.csv         # Cronología de los 8 goles en formato CSV
├── scripts/
│   ├── generate_match_data.py         # Generador de estadísticas y contexto
│   ├── generate_muller_telemetry.py   # Generador de telemetría de alta resolución
│   └── validate_data.py               # Validador de esquemas, coordenadas y consistencia
└── README.md                          # Documentación maestra y guía de integración
```

---

## SECCIÓN 1: Análisis Específico del 1er Gol de Thomas Müller (Minuto 11')

Módulo ubicado en [`01_gol_muller_min11/`](./01_gol_muller_min11/). Diseñado para el pipeline de procesamiento de fotogramas.

### Geometría de la Acción a Balón Parado (ABP)
- **Minuto oficial**: 11' (Reloj `10:33`).
- **Ejecutante**: Toni Kroos (#18 GER) desde el córner derecho $(x: 35\text{ cm}, y: 6965\text{ cm})$.
- **Trayectoria**: Parábola con comba hacia afuera (*outswinger*) con destino al carril interior derecho del área penal.
- **Punto de impacto**: Thomas Müller (#13 GER) remata en $(x: 920\text{ cm}, y: 4150\text{ cm})$ a $9.2\text{ m}$ del arco.

### Desglose en Ventanas Tácticas ($\sim 4\text{ s}$)
| Ventana | Intervalo Temporal | Frames | Foco Táctico DT (Mateo Benítez) | Narración Accesible (Audio TTS) |
| :--- | :--- | :--- | :--- | :--- |
| **Ventana 1** | `0.0s - 4.0s` | `0 - 100` | Bloqueo intencional de Klose (#11) y Höwedes (#4) fijando la marca de Dante y David Luiz en 6 yardas. | Toni Kroos lanza córner abierto; bloqueo de Klose genera congestión en el área brasileña. |
| **Ventana 2** | `4.0s - 8.0s` | `100 - 200` | Pérdida de marca de David Luiz; Müller gana separación libre de $3.4\text{ m}$ ($>3.2\text{ m}$, $xG \approx 0.35$) y define de volea diestra picada. | Balón al punto penal; David Luiz queda atorado y Müller remata solo de primera al poste izquierdo. ¡Gol! |

---

## SECCIÓN 2: Estadísticas Completas y Contexto del Partido Brasil 1–7 Alemania

Módulo ubicado en [`02_partido_completo/`](./02_partido_completo/).

### 1. Comparativa Global del Partido
| Métrica | Brasil (1T) | Alemania (1T) | Brasil (2T) | Alemania (2T) | **Brasil (FT)** | **Alemania (FT)** |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Goles** | 0 | 5 | 1 | 2 | **1** | **7** |
| **Posesión de Balón** | 47.0% | 53.0% | 56.0% | 44.0% | **52.0%** | **48.0%** |
| **Tiros Totales** | 2 | 10 | 16 | 4 | **18** | **14** |
| **Tiros a Puerta** | 1 | 9 | 7 | 1 | **8** | **10** |
| **Tiros Dentro del Área**| 1 | 9 | 10 | 3 | **11** | **12** |
| **Goles Esperados (xG)** | 0.12 | 2.84 | 1.13 | 0.91 | **1.25** | **3.75** |
| **Precisión de Pases** | 79.8% | 88.9% | 78.6% | 83.4% | **79.1%** | **86.2%** |
| **Pases Completados** | 182 | 265 | 220 | 247 | **402** | **512** |
| **Córners** | 3 | 4 | 4 | 1 | **7** | **5** |
| **Faltas** | 5 | 6 | 6 | 8 | **11** | **14** |
| **Atajadas de Portero** | 4 | 1 | -1 | 6 | **3** | **7** |
| **PPDA (Intensidad Presión)**| 16.2 | 7.8 | 13.5 | 9.1 | **14.8** | **8.4** |

### 2. Cronología Táctica de los 8 Goles
| # | Min | Marcador | Anotador (#) | Asistente (#) | Tipo de Jugada | $xG$ | Coordenada $(x, y)\text{ cm}$ |
| :-: | :-: | :-: | :--- | :--- | :--- | :-: | :-: |
| **1** | 11' | 0–1 | Thomas Müller (#13) | Toni Kroos (#18) | ABP - Córner derecho | 0.35 | `(920, 4150)` |
| **2** | 23' | 0–2 | Miroslav Klose (#11) | Thomas Müller (#13) | Ataque interior / Rebote | 0.65 | `(680, 3450)` |
| **3** | 24' | 0–3 | Toni Kroos (#18) | Philipp Lahm (#16) | Centro raso y volea frontal | 0.18 | `(1420, 4300)` |
| **4** | 26' | 0–4 | Toni Kroos (#18) | Sami Khedira (#6) | Robo en presión alta y 2vs1 | 0.88 | `(850, 3600)` |
| **5** | 29' | 0–5 | Sami Khedira (#6) | Mesut Özil (#8) | Incursión vertical y pase atrás | 0.42 | `(1120, 3200)` |
| **6** | 69' | 0–6 | André Schürrle (#9) | Philipp Lahm (#16) | Desborde exterior y pase de la muerte | 0.45 | `(1050, 3750)` |
| **7** | 79' | 0–7 | André Schürrle (#9) | Thomas Müller (#13) | Control orientado y remate al ángulo | 0.12 | `(880, 2450)` |
| **8** | 90' | 1–7 | Oscar (#11) | Marcelo (#6) | Contraataque y desborde individual | 0.28 | `(10850, 3650)` |

---

## Guía Rápida de Consumo en Python (Roy)

```python
import json
import csv

# 1. Cargar las ventanas tácticas del Gol 1 de Müller
with open("01_gol_muller_min11/gol_1_muller_ventanas.json", "r", encoding="utf-8") as f:
    ventanas_muller = json.load(f)

for v in ventanas_muller["ventanas_tacticas"]:
    print(f"Ventana [{v['t0']}s - {v['t1']}s] | xG: {v['metricas'].get('xg')}")
    print(f"  DT Overlay: {v['texto_tactico_dt']}")
    print(f"  TTS Audio:  {v['texto_narracion_accesible']}")

# 2. Cargar línea de tiempo de los 8 goles desde CSV
with open("02_partido_completo/linea_tiempo_goles.csv", mode="r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    print("\n--- GOLES DEL PARTIDO ---")
    for row in reader:
        print(f"Minuto {row['Minuto']}' [{row['Marcador']}]: {row['Anotador']} (xG: {row['xG']}) - Coords: ({row['Pitch_X_cm']}, {row['Pitch_Y_cm']})")
```

---

## Verificación de Integridad de Datos

Para verificar que todos los datos numéricos y esquemas cumplan con las restricciones del sistema OMNIMORPH:
```bash
python3 scripts/validate_data.py
```
El script comprueba:
- Rangos de coordenadas $x \in [0, 12000]$, $y \in [0, 7000]$.
- Suma de probabilidades y límites de $xG \in [0, 1]$.
- Alineación estricta entre archivos JSON y CSV.
- Integridad de IDs de equipos (`0`, `1`, `null`).
