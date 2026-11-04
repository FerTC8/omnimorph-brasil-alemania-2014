# Brasil 1–7 Alemania (Mundial 2014) — Datos Tácticos OMNIMORPH

Datos espaciales, métricas oficiales y desglose táctico del partido de semifinal del Mundial 2014 entre Brasil y Alemania (8 de julio de 2014, Estádio Mineirão), formateados para la integración en la aplicación de OMNIMORPH.

---

## Sistema de Referencia de la Cancha

- **Dimensiones normalizadas**: $12000\text{ cm} \times 7000\text{ cm}$ ($120\text{ m} \times 70\text{ m}$).
- **Eje X ($0$ a $12000\text{ cm}$)**:
  - $x = 0$: Línea de meta defendida por Brasil en el 1T (centro del arco en $y = 3500$).
  - $x = 12000$: Línea de meta defendida por Alemania en el 1T.
- **Eje Y ($0$ a $7000\text{ cm}$)**:
  - $y = 0$: Banda derecha defensiva de Brasil en el 1T.
  - $y = 7000$: Banda izquierda defensiva de Brasil en el 1T.
- **Identificadores de equipo**:
  - `0`: Brasil
  - `1`: Alemania
  - `null`: Árbitro o balón

---

## Contrato de Ventanas Tácticas (~4 s)

Para alimentar el monitor de 4 paneles (video con marcas, radar 2D, métricas y narración auditiva TTS), los eventos se estructuran en ventanas temporales:

```json
{
  "t0": 0.0,
  "t1": 4.0,
  "texto_tactico": "Análisis táctico para la visualización en pantalla",
  "texto_narracion": "Texto descriptivo para síntesis de voz",
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
├── 01_primer_gol_muller/
│   ├── gol_muller_min11.json           # Desglose del gol, ventanas 4s y stats acumuladas al min 11
│   └── muestra_telemetria_muller.json  # Telemetría de ejemplo a 25 fps en coordenadas de cancha
├── 02_partido_completo/
│   ├── contexto_partido.json           # Plantillas completas (23 jugadores), dorsales, árbitros y sede
│   ├── estadisticas_partido.json       # Estadísticas comparativas 1T, 2T y total en JSON
│   ├── estadisticas_partido.csv        # Mismas estadísticas tabuladas en CSV
│   ├── cronologia_goles.json           # Detalle de los 8 goles con minutos, xG, remate y nota táctica
│   └── cronologia_goles.csv            # Tabla CSV de los 8 goles
├── FUENTES.md                          # Detalle de fuentes oficiales (FIFA, Opta, FBref, StatsBomb)
├── fuentes.json                        # Registro estructurado de fuentes y enlaces
├── scripts/
│   └── validate_data.py                # Validador de esquemas, coordenadas y consistencia
└── README.md
```

---

## Detalle de Módulos

### 1. Primer Gol — Thomas Müller (`01_primer_gol_muller/`)
- **Minuto**: 11' (reloj `10:33`). Marcador: 0–0 $\rightarrow$ 0–1.
- **Jugada**: Saque de esquina por derecha cobrado por Toni Kroos (#18) con comba hacia afuera.
- **Acción táctica**: Pantalla en el área chica de Miroslav Klose (#11) y Benedikt Höwedes (#4) que obstaculiza la marca de David Luiz (#4). Thomas Müller (#13) se desmarca hacia el punto penal con una separación de $3.4\text{ m}$ y remata de primera con derecha a $9.2\text{ m}$ del arco.
- **Archivos**:
  - `gol_muller_min11.json`: Contrato con las dos ventanas de ~4 s, métricas de remate ($xG \approx 0.35$, velocidad $78.4\text{ km/h}$) y el bloque `estadisticas_acumuladas_minuto_11` con los números del partido previos y al momento del 0–1.
  - `muestra_telemetria_muller.json`: Registro de posiciones de los 22 jugadores, árbitro y balón a 25 fps.

### 2. Partido Completo (`02_partido_completo/`)
- **`contexto_partido.json`**: Metadatos de la sede (Mineirão, 58.141 personas), terna arbitral encabezada por Marco Rodríguez (México) y plantillas de 23 jugadores de Brasil y Alemania con dorsales, minutos jugados y eventos.
- **`estadisticas_partido.json` y `.csv`**: Comparativa oficial de Brasil vs. Alemania en tres cortes (1T `0-5`, 2T `1-2`, Total `1-7`): posesión, tiros totales, tiros al arco, tiros fuera/bloqueados, $xG$, tiros de esquina, pases completados/intentados (% acierto), recuperaciones, faltas, fueras de juego y distribución de zonas.
- **`cronologia_goles.json` y `.csv`**: Secuencia ordenada de los 8 goles del encuentro:
  1. 11' Thomas Müller (0–1)
  2. 23' Miroslav Klose (0–2)
  3. 24' Toni Kroos (0–3)
  4. 26' Toni Kroos (0–4)
  5. 29' Sami Khedira (0–5)
  6. 69' André Schürrle (0–6)
  7. 79' André Schürrle (0–7)
  8. 90' Oscar (1–7)

---

## Validación de Datos

Para verificar que todos los archivos existan, respeten los límites de cancha $[0, 12000] \times [0, 7000]\text{ cm}$ y mantengan consistencia entre JSON y CSV:

```bash
python3 scripts/validate_data.py
```
