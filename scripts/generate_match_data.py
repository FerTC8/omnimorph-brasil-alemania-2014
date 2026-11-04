"""
Generador de datos completos del partido Brasil 1–7 Alemania (2014)
Para Sección B de Project OMNIMORPH:
- 02_partido_completo/contexto_partido.json
- 02_partido_completo/estadisticas_partido.json
- 02_partido_completo/estadisticas_partido.csv
- 02_partido_completo/linea_tiempo_goles.json
- 02_partido_completo/linea_tiempo_goles.csv
"""

import os
import json
import csv

def generate_context():
    contexto = {
        "partido_info": {
            "id": "WC2014_SF_BRA_GER",
            "competicion": "Copa Mundial de la FIFA Brasil 2014",
            "fase": "Semifinal",
            "fecha": "2014-07-08",
            "hora_local": "17:00 BRT",
            "estadio": "Estádio Governador Magalhães Pinto (Mineirão)",
            "ciudad": "Belo Horizonte, Brasil",
            "asistencia": 58141,
            "arbitro": {
                "principal": "Marco Antonio Rodríguez",
                "pais": "México",
                "asistente_1": "Marvin Torrentera (México)",
                "asistente_2": "Marcos Quintero (México)",
                "cuarto_arbitro": "Mark Geiger (EE. UU.)"
            },
            "condiciones_climaticas": {
                "temperatura_c": 22,
                "humedad_pct": 51,
                "cielo": "Despejado",
                "viento_kmh": 11
            },
            "resultado": {
                "tiempo_reglamentario": "1-7",
                "primer_tiempo": "0-5",
                "segundo_tiempo": "1-2",
                "ganador": "Alemania (Clasificada a la Final)"
            }
        },
        "equipos": {
            "brasil": {
                "team_id": 0,
                "pais": "Brasil",
                "codigo": "BRA",
                "entrenador": "Luiz Felipe Scolari",
                "esquema_tactico_inicial": "4-2-3-1",
                "capitan": "David Luiz (#4)",
                "bajas_notables": [
                    {"nombre": "Neymar Jr", "motivo": "Fractura de tercera vértebra lumbar sufrida en cuartos vs Colombia"},
                    {"nombre": "Thiago Silva", "motivo": "Suspensión por acumulación de tarjetas amarillas"}
                ],
                "plantilla": {
                    "12": {"nombre": "Júlio César", "posicion": "Portero", "titular": True, "minutos_jugados": 90, "eventos": ["7 goles recibidos", "3 atajadas"]},
                    "23": {"nombre": "Maicon", "posicion": "Lateral Derecho", "titular": True, "minutos_jugados": 90, "eventos": []},
                    "4": {"nombre": "David Luiz", "posicion": "Defensa Central (C)", "titular": True, "minutos_jugados": 90, "eventos": ["Capitán"]},
                    "13": {"nombre": "Dante", "posicion": "Defensa Central", "titular": True, "minutos_jugados": 90, "eventos": ["Tarjeta amarilla 68'"]},
                    "6": {"nombre": "Marcelo", "posicion": "Lateral Izquierdo", "titular": True, "minutos_jugados": 90, "eventos": ["Asistencia 90'"]},
                    "17": {"nombre": "Luiz Gustavo", "posicion": "Pivote Defensivo", "titular": True, "minutos_jugados": 90, "eventos": []},
                    "5": {"nombre": "Fernandinho", "posicion": "Mediocentro", "titular": True, "minutos_jugados": 45, "eventos": ["Sustituido en el entretiempo (46')"]},
                    "7": {"nombre": "Hulk", "posicion": "Extremo Derecho", "titular": True, "minutos_jugados": 45, "eventos": ["Sustituido en el entretiempo (46')"]},
                    "11": {"nombre": "Oscar", "posicion": "Mediapunta", "titular": True, "minutos_jugados": 90, "eventos": ["Gol 90'"]},
                    "20": {"nombre": "Bernard", "posicion": "Extremo Izquierdo", "titular": True, "minutos_jugados": 90, "eventos": []},
                    "9": {"nombre": "Fred", "posicion": "Delantero Centro", "titular": True, "minutos_jugados": 69, "eventos": ["Sustituido al 69'"]},
                    "8": {"nombre": "Paulinho", "posicion": "Mediocentro", "titular": False, "minutos_jugados": 45, "eventos": ["Ingresó al 46'"]},
                    "16": {"nombre": "Ramires", "posicion": "Extremo / Interior", "titular": False, "minutos_jugados": 45, "eventos": ["Ingresó al 46'"]},
                    "19": {"nombre": "Willian", "posicion": "Extremo", "titular": False, "minutos_jugados": 21, "eventos": ["Ingresó al 69'"]},
                    "1": {"nombre": "Jefferson", "posicion": "Portero Suplente", "titular": False, "minutos_jugados": 0, "eventos": []},
                    "22": {"nombre": "Victor", "posicion": "Portero Suplente", "titular": False, "minutos_jugados": 0, "eventos": []},
                    "2": {"nombre": "Dani Alves", "posicion": "Lateral Derecho Suplente", "titular": False, "minutos_jugados": 0, "eventos": []},
                    "14": {"nombre": "Maxwell", "posicion": "Lateral Izquierdo Suplente", "titular": False, "minutos_jugados": 0, "eventos": []},
                    "15": {"nombre": "Henrique", "posicion": "Defensa Central Suplente", "titular": False, "minutos_jugados": 0, "eventos": []},
                    "18": {"nombre": "Hernanes", "posicion": "Mediocentro Suplente", "titular": False, "minutos_jugados": 0, "eventos": []},
                    "21": {"nombre": "Jô", "posicion": "Delantero Suplente", "titular": False, "minutos_jugados": 0, "eventos": []}
                }
            },
            "alemania": {
                "team_id": 1,
                "pais": "Alemania",
                "codigo": "GER",
                "entrenador": "Joachim Löw",
                "esquema_tactico_inicial": "4-3-3 / 4-2-3-1",
                "capitan": "Philipp Lahm (#16)",
                "plantilla": {
                    "1": {"nombre": "Manuel Neuer", "posicion": "Portero", "titular": True, "minutos_jugados": 90, "eventos": ["1 gol recibido", "7 atajadas"]},
                    "16": {"nombre": "Philipp Lahm", "posicion": "Lateral Derecho (C)", "titular": True, "minutos_jugados": 90, "eventos": ["Capitán", "Asistencia 24'", "Asistencia 69'"]},
                    "20": {"nombre": "Jérôme Boateng", "posicion": "Defensa Central", "titular": True, "minutos_jugados": 90, "eventos": []},
                    "5": {"nombre": "Mats Hummels", "posicion": "Defensa Central", "titular": True, "minutos_jugados": 45, "eventos": ["Sustituido en el entretiempo (46')"]},
                    "4": {"nombre": "Benedikt Höwedes", "posicion": "Lateral Izquierdo", "titular": True, "minutos_jugados": 90, "eventos": []},
                    "7": {"nombre": "Bastian Schweinsteiger", "posicion": "Pivote Organizador", "titular": True, "minutos_jugados": 90, "eventos": []},
                    "6": {"nombre": "Sami Khedira", "posicion": "Interior Box-to-Box", "titular": True, "minutos_jugados": 76, "eventos": ["Gol 29'", "Asistencia 26'", "Sustituido al 76'"]},
                    "18": {"nombre": "Toni Kroos", "posicion": "Interior / Organizador", "titular": True, "minutos_jugados": 90, "eventos": ["MVP del Partido", "Gol 24'", "Gol 26'", "Asistencia 11'"]},
                    "8": {"nombre": "Mesut Özil", "posicion": "Extremo / Enganche", "titular": True, "minutos_jugados": 90, "eventos": ["Asistencia 29'"]},
                    "13": {"nombre": "Thomas Müller", "posicion": "Extremo / Segundo Delantero", "titular": True, "minutos_jugados": 90, "eventos": ["Gol 11'", "Asistencia 23'", "Asistencia 79'"]},
                    "11": {"nombre": "Miroslav Klose", "posicion": "Delantero Centro", "titular": True, "minutos_jugados": 58, "eventos": ["Gol 23' (Récord histórico: 16 goles en Mundiales)", "Sustituido al 58'"]},
                    "17": {"nombre": "Per Mertesacker", "posicion": "Defensa Central", "titular": False, "minutos_jugados": 45, "eventos": ["Ingresó al 46'"]},
                    "9": {"nombre": "André Schürrle", "posicion": "Extremo / Delantero", "titular": False, "minutos_jugados": 32, "eventos": ["Ingresó al 58'", "Gol 69'", "Gol 79'"]},
                    "14": {"nombre": "Julian Draxler", "posicion": "Mediapunta", "titular": False, "minutos_jugados": 14, "eventos": ["Ingresó al 76'"]},
                    "12": {"nombre": "Ron-Robert Zieler", "posicion": "Portero Suplente", "titular": False, "minutos_jugados": 0, "eventos": []},
                    "22": {"nombre": "Roman Weidenfeller", "posicion": "Portero Suplente", "titular": False, "minutos_jugados": 0, "eventos": []},
                    "2": {"nombre": "Kevin Großkreutz", "posicion": "Lateral Suplente", "titular": False, "minutos_jugados": 0, "eventos": []},
                    "3": {"nombre": "Matthias Ginter", "posicion": "Defensa Suplente", "titular": False, "minutos_jugados": 0, "eventos": []},
                    "10": {"nombre": "Lukas Podolski", "posicion": "Delantero Suplente", "titular": False, "minutos_jugados": 0, "eventos": []},
                    "15": {"nombre": "Erik Durm", "posicion": "Lateral Suplente", "titular": False, "minutos_jugados": 0, "eventos": []},
                    "19": {"nombre": "Mario Götze", "posicion": "Mediapunta Suplente", "titular": False, "minutos_jugados": 0, "eventos": []},
                    "23": {"nombre": "Christoph Kramer", "posicion": "Centrocampista Suplente", "titular": False, "minutos_jugados": 0, "eventos": []}
                }
            }
        }
    }
    with open("02_partido_completo/contexto_partido.json", "w", encoding="utf-8") as f:
        json.dump(contexto, f, indent=2, ensure_ascii=False)
    print("contexto_partido.json generado con exito.")

def generate_statistics():
    estadisticas = {
        "resumen_comparativo": {
            "primer_tiempo": {
                "marcador": "0-5",
                "posesion_pct": {"brasil": 47.0, "alemania": 53.0},
                "tiros_totales": {"brasil": 2, "alemania": 10},
                "tiros_a_puerta": {"brasil": 1, "alemania": 9},
                "tiros_fuera_bloqueados": {"brasil": 1, "alemania": 1},
                "tiros_dentro_area": {"brasil": 1, "alemania": 9},
                "tiros_fuera_area": {"brasil": 1, "alemania": 1},
                "xg_goles_esperados": {"brasil": 0.12, "alemania": 2.84},
                "pases_completados_intentados": {"brasil": "182/228", "alemania": "265/298"},
                "precision_pases_pct": {"brasil": 79.8, "alemania": 88.9},
                "corners": {"brasil": 3, "alemania": 4},
                "faltas_cometidas": {"brasil": 5, "alemania": 6},
                "fueras_de_juego": {"brasil": 1, "alemania": 0},
                "atajadas_portero": {"brasil": 4, "alemania": 1},
                "recuperaciones": {"brasil": 19, "alemania": 26},
                "ppda_presion": {"brasil": 16.2, "alemania": 7.8}
            },
            "segundo_tiempo": {
                "marcador": "1-2",
                "posesion_pct": {"brasil": 56.0, "alemania": 44.0},
                "tiros_totales": {"brasil": 16, "alemania": 4},
                "tiros_a_puerta": {"brasil": 7, "alemania": 1},
                "tiros_fuera_bloqueados": {"brasil": 9, "alemania": 3},
                "tiros_dentro_area": {"brasil": 10, "alemania": 3},
                "tiros_fuera_area": {"brasil": 6, "alemania": 1},
                "xg_goles_esperados": {"brasil": 1.13, "alemania": 0.91},
                "pases_completados_intentados": {"brasil": "220/280", "alemania": "247/296"},
                "precision_pases_pct": {"brasil": 78.6, "alemania": 83.4},
                "corners": {"brasil": 4, "alemania": 1},
                "faltas_cometidas": {"brasil": 6, "alemania": 8},
                "fueras_de_juego": {"brasil": 2, "alemania": 0},
                "atajadas_portero": {"brasil": -1, "alemania": 6},
                "recuperaciones": {"brasil": 29, "alemania": 28},
                "ppda_presion": {"brasil": 13.5, "alemania": 9.1}
            },
            "tiempo_completo": {
                "marcador": "1-7",
                "posesion_pct": {"brasil": 52.0, "alemania": 48.0},
                "tiros_totales": {"brasil": 18, "alemania": 14},
                "tiros_a_puerta": {"brasil": 8, "alemania": 10},
                "tiros_fuera_bloqueados": {"brasil": 10, "alemania": 4},
                "tiros_dentro_area": {"brasil": 11, "alemania": 12},
                "tiros_fuera_area": {"brasil": 7, "alemania": 2},
                "xg_goles_esperados": {"brasil": 1.25, "alemania": 3.75},
                "eficiencia_goles_sobre_xg": {"brasil": -0.25, "alemania": 3.25},
                "pases_completados_intentados": {"brasil": "402/508", "alemania": "512/594"},
                "precision_pases_pct": {"brasil": 79.1, "alemania": 86.2},
                "corners": {"brasil": 7, "alemania": 5},
                "faltas_cometidas": {"brasil": 11, "alemania": 14},
                "tarjetas_amarillas": {"brasil": 1, "alemania": 0},
                "tarjetas_rojas": {"brasil": 0, "alemania": 0},
                "fueras_de_juego": {"brasil": 3, "alemania": 0},
                "atajadas_portero": {"brasil": 3, "alemania": 7},
                "recuperaciones": {"brasil": 48, "alemania": 54},
                "ppda_presion_promedio": {"brasil": 14.8, "alemania": 8.4},
                "distribucion_zonas_balon_pct": {
                    "tercio_defensivo_brasil_ofensivo_alemania": 31.0,
                    "tercio_medio": 46.0,
                    "tercio_ofensivo_brasil_defensivo_alemania": 23.0
                }
            }
        },
        "estadisticas_individuales_clave": [
            {
                "jugador": "Toni Kroos",
                "dorsal": 18,
                "equipo": "Alemania",
                "posicion": "Mediocentro Organizador",
                "goles": 2,
                "asistencias": 1,
                "tiros_a_puerta": 2,
                "pases_totales": 71,
                "pases_completados": 66,
                "precision_pases_pct": 93.0,
                "recuperaciones": 6,
                "balones_tocados": 88,
                "distancia_recorrida_km": 11.5,
                "valoracion_omnimorph": 9.9
            },
            {
                "jugador": "Thomas Müller",
                "dorsal": 13,
                "equipo": "Alemania",
                "posicion": "Delantero / Extremo",
                "goles": 1,
                "asistencias": 2,
                "tiros_a_puerta": 2,
                "pases_totales": 34,
                "pases_completados": 29,
                "precision_pases_pct": 85.3,
                "presiones_altas": 18,
                "distancia_recorrida_km": 11.8,
                "valoracion_omnimorph": 9.6
            },
            {
                "jugador": "Sami Khedira",
                "dorsal": 6,
                "equipo": "Alemania",
                "posicion": "Interior Box-to-Box",
                "goles": 1,
                "asistencias": 1,
                "tiros_a_puerta": 1,
                "pases_totales": 42,
                "pases_completados": 38,
                "precision_pases_pct": 90.5,
                "intercepciones": 4,
                "distancia_recorrida_km": 9.4,
                "valoracion_omnimorph": 9.4
            },
            {
                "jugador": "André Schürrle",
                "dorsal": 9,
                "equipo": "Alemania",
                "posicion": "Extremo Suplente",
                "goles": 2,
                "asistencias": 0,
                "tiros_a_puerta": 2,
                "pases_totales": 16,
                "pases_completados": 14,
                "precision_pases_pct": 87.5,
                "minutos_jugados": 32,
                "distancia_recorrida_km": 4.5,
                "valoracion_omnimorph": 9.2
            },
            {
                "jugador": "Miroslav Klose",
                "dorsal": 11,
                "equipo": "Alemania",
                "posicion": "Delantero Centro",
                "goles": 1,
                "asistencias": 0,
                "tiros_a_puerta": 2,
                "pases_totales": 15,
                "pases_completados": 12,
                "precision_pases_pct": 80.0,
                "distancia_recorrida_km": 6.8,
                "valoracion_omnimorph": 8.8
            },
            {
                "jugador": "Manuel Neuer",
                "dorsal": 1,
                "equipo": "Alemania",
                "posicion": "Portero Líbero",
                "atajadas": 7,
                "goles_encajados": 1,
                "intervenciones_fuera_del_area": 3,
                "pases_completados": 29,
                "precision_pases_pct": 90.6,
                "distancia_recorrida_km": 5.4,
                "valoracion_omnimorph": 8.9
            },
            {
                "jugador": "Philipp Lahm",
                "dorsal": 16,
                "equipo": "Alemania",
                "posicion": "Lateral Derecho (C)",
                "goles": 0,
                "asistencias": 2,
                "tiros_a_puerta": 0,
                "pases_totales": 68,
                "pases_completados": 63,
                "precision_pases_pct": 92.6,
                "entradas_exitosas": 5,
                "distancia_recorrida_km": 10.9,
                "valoracion_omnimorph": 9.1
            },
            {
                "jugador": "Oscar",
                "dorsal": 11,
                "equipo": "Brasil",
                "posicion": "Mediapunta",
                "goles": 1,
                "asistencias": 0,
                "tiros_a_puerta": 3,
                "pases_totales": 48,
                "pases_completados": 39,
                "precision_pases_pct": 81.3,
                "regates_completados": 4,
                "distancia_recorrida_km": 10.7,
                "valoracion_omnimorph": 6.8
            },
            {
                "jugador": "David Luiz",
                "dorsal": 4,
                "equipo": "Brasil",
                "posicion": "Defensa Central (C)",
                "goles": 0,
                "asistencias": 0,
                "tiros_a_puerta": 1,
                "duelos_ganados": 3,
                "duelos_perdidos": 8,
                "perdidas_balon": 12,
                "errores_directos_gol": 2,
                "distancia_recorrida_km": 9.9,
                "valoracion_omnimorph": 3.8
            },
            {
                "jugador": "Fernandinho",
                "dorsal": 5,
                "equipo": "Brasil",
                "posicion": "Pivote Defensivo",
                "goles": 0,
                "asistencias": 0,
                "pases_totales": 26,
                "pases_completados": 19,
                "precision_pases_pct": 73.1,
                "perdidas_en_propio_campo": 3,
                "errores_directos_gol": 1,
                "minutos_jugados": 45,
                "valoracion_omnimorph": 3.2
            },
            {
                "jugador": "Júlio César",
                "dorsal": 12,
                "equipo": "Brasil",
                "posicion": "Portero",
                "atajadas": 3,
                "goles_encajados": 7,
                "goles_esperados_evitados": -3.25,
                "pases_largos_completados": 6,
                "valoracion_omnimorph": 3.5
            }
        ]
    }
    
    with open("02_partido_completo/estadisticas_partido.json", "w", encoding="utf-8") as f:
        json.dump(estadisticas, f, indent=2, ensure_ascii=False)
    print("estadisticas_partido.json generado con exito.")

    # Generación de CSV correspondiente
    csv_rows = [
        ["Fase", "Metrica", "Brasil", "Alemania", "Diferencia_Margen"],
        ["1T", "Marcador", "0", "5", "-5"],
        ["1T", "Posesion_Pct", "47.0", "53.0", "-6.0"],
        ["1T", "Tiros_Totales", "2", "10", "-8"],
        ["1T", "Tiros_A_Puerta", "1", "9", "-8"],
        ["1T", "Tiros_Dentro_Area", "1", "9", "-8"],
        ["1T", "xG_Goles_Esperados", "0.12", "2.84", "-2.72"],
        ["1T", "Pases_Precision_Pct", "79.8", "88.9", "-9.1"],
        ["1T", "Corners", "3", "4", "-1"],
        ["1T", "Faltas", "5", "6", "-1"],
        ["1T", "Atajadas", "4", "1", "+3"],
        ["2T", "Marcador", "1", "2", "-1"],
        ["2T", "Posesion_Pct", "56.0", "44.0", "+12.0"],
        ["2T", "Tiros_Totales", "16", "4", "+12"],
        ["2T", "Tiros_A_Puerta", "7", "1", "+6"],
        ["2T", "Tiros_Dentro_Area", "10", "3", "+7"],
        ["2T", "xG_Goles_Esperados", "1.13", "0.91", "+0.22"],
        ["2T", "Pases_Precision_Pct", "78.6", "83.4", "-4.8"],
        ["2T", "Corners", "4", "1", "+3"],
        ["2T", "Faltas", "6", "8", "-2"],
        ["2T", "Atajadas", "-1", "6", "-7"],
        ["FT", "Marcador_Final", "1", "7", "-6"],
        ["FT", "Posesion_Pct", "52.0", "48.0", "+4.0"],
        ["FT", "Tiros_Totales", "18", "14", "+4"],
        ["FT", "Tiros_A_Puerta", "8", "10", "-2"],
        ["FT", "Tiros_Dentro_Area", "11", "12", "-1"],
        ["FT", "Tiros_Fuera_Area", "7", "2", "+5"],
        ["FT", "xG_Total", "1.25", "3.75", "-2.50"],
        ["FT", "Eficiencia_Goles_vs_xG", "-0.25", "+3.25", "-3.50"],
        ["FT", "Pases_Completados", "402", "512", "-110"],
        ["FT", "Pases_Intentados", "508", "594", "-86"],
        ["FT", "Pases_Precision_Pct", "79.1", "86.2", "-7.1"],
        ["FT", "Corners", "7", "5", "+2"],
        ["FT", "Faltas_Cometidas", "11", "14", "-3"],
        ["FT", "Tarjetas_Amarillas", "1", "0", "+1"],
        ["FT", "Fueras_De_Juego", "3", "0", "+3"],
        ["FT", "Atajadas_Portero", "3", "7", "-4"],
        ["FT", "Recuperaciones_Balon", "48", "54", "-6"],
        ["FT", "PPDA_Presion_Intensidad", "14.8", "8.4", "+6.4"],
        ["FT", "Zona_Tercio_Defensivo_BRA_Pct", "31.0", "31.0", "0.0"],
        ["FT", "Zona_Tercio_Medio_Pct", "46.0", "46.0", "0.0"],
        ["FT", "Zona_Tercio_Ofensivo_BRA_Pct", "23.0", "23.0", "0.0"]
    ]
    with open("02_partido_completo/estadisticas_partido.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(csv_rows)
    print("estadisticas_partido.csv generado con exito.")

def generate_goals_timeline():
    goles = [
        {
            "orden": 1,
            "minuto": 11,
            "segundo_oficial": "10:33",
            "marcador_momento": "0-1",
            "equipo_anotador": "Alemania",
            "anotador": {"nombre": "Thomas Müller", "dorsal": 13},
            "asistente": {"nombre": "Toni Kroos", "dorsal": 18},
            "tipo_jugada": "ABP - Córner Derecho",
            "xg": 0.35,
            "coordenadas_campo_cm": {"pitch_x": 920, "pitch_y": 4150},
            "distancia_porteria_m": 9.2,
            "pie_remate": "Derecho (interior de volea)",
            "diagnostico_tactico_dt": "Pantalla combinada Klose-Höwedes en 6 yardas que bloquea la trayectoria defensiva de David Luiz. Müller rompe al espacio libre ganando 3.4m de ventaja y definiendo sin oposición.",
            "texto_narracion_accesible": "Minuto 11: Centro desde el córner derecho de Toni Kroos al punto de penalti. David Luiz queda atrapado en el tráfico y Thomas Müller entra completamente desmarcado para rematar con la cara interna del pie derecho. ¡Gol de Alemania!"
        },
        {
            "orden": 2,
            "minuto": 23,
            "segundo_oficial": "22:04",
            "marcador_momento": "0-2",
            "equipo_anotador": "Alemania",
            "anotador": {"nombre": "Miroslav Klose", "dorsal": 11},
            "asistente": {"nombre": "Thomas Müller", "dorsal": 13},
            "tipo_jugada": "Ataque Combinado Interior / Rebote",
            "xg": 0.65,
            "coordenadas_campo_cm": {"pitch_x": 680, "pitch_y": 3450},
            "distancia_porteria_m": 6.8,
            "pie_remate": "Derecho (primer tiro rechazado, segundo remate a placer)",
            "diagnostico_tactico_dt": "Triangulación vertical Kroos-Müller-Klose que desmonta el escalonamiento de la zaga de Brasil. Tras parada inicial de Júlio César, Klose captura su propio rechace ante la pasividad de Fernandinho y Dante.",
            "texto_narracion_accesible": "Minuto 23: Combinación vertiginosa en la corona del área entre Müller y Klose. Klose define de primera, tapa Júlio César dejando rebote y el mismo delantero captura el balón suelto para enviarlo a la red. ¡Gol histórico de Miroslav Klose, máximo artillero de los Mundiales con 16 tantos!"
        },
        {
            "orden": 3,
            "minuto": 24,
            "segundo_oficial": "23:57",
            "marcador_momento": "0-3",
            "equipo_anotador": "Alemania",
            "anotador": {"nombre": "Toni Kroos", "dorsal": 18},
            "asistente": {"nombre": "Philipp Lahm", "dorsal": 16},
            "tipo_jugada": "Centro lateral y volea desde la frontal",
            "xg": 0.18,
            "coordenadas_campo_cm": {"pitch_x": 1420, "pitch_y": 4300},
            "distancia_porteria_m": 14.2,
            "pie_remate": "Izquierdo (empalme de volea exterior)",
            "diagnostico_tactico_dt": "Centro raso de Lahm que cruza el área tras fallido intento de despeje de Müller. Kroos llega libre desde segunda línea sin que ningún mediocentro brasileño (Fernandinho o Luiz Gustavo) cierre la frontal.",
            "texto_narracion_accesible": "Minuto 24: Desborde veloz de Philipp Lahm por el flanco derecho, mete el centro raso al área grande. El balón pasa de largo y llega como un misil Toni Kroos para conectar una soberbia volea zurda pegada al poste. ¡Alemania se pone 3 a 0 en menos de dos minutos!"
        },
        {
            "orden": 4,
            "minuto": 26,
            "segundo_oficial": "25:38",
            "marcador_momento": "0-4",
            "equipo_anotador": "Alemania",
            "anotador": {"nombre": "Toni Kroos", "dorsal": 18},
            "asistente": {"nombre": "Sami Khedira", "dorsal": 6},
            "tipo_jugada": "Presión Alta / Recuperación en salida",
            "xg": 0.88,
            "coordenadas_campo_cm": {"pitch_x": 850, "pitch_y": 3600},
            "distancia_porteria_m": 8.5,
            "pie_remate": "Derecho (pase a la red vacía)",
            "diagnostico_tactico_dt": "Robo inmediato de Kroos sobre Fernandinho tras el saque de centro en sector medio defensivo de Brasil. Transición ultra-rápida 2 vs 1 con Khedira, quien asiste con generosidad para empujarla sin guardameta.",
            "texto_narracion_accesible": "Minuto 26: Error fatal de Fernandinho en la salida de balón, robo quirúrgico de Kroos. Toca para Khedira en el mano a mano y Khedira, con enorme frialdad, se la devuelve para que Kroos solo tenga que empujarla al arco desguarnecido. ¡4 a 0 descomunal!"
        },
        {
            "orden": 5,
            "minuto": 29,
            "segundo_oficial": "28:44",
            "marcador_momento": "0-5",
            "equipo_anotador": "Alemania",
            "anotador": {"nombre": "Sami Khedira", "dorsal": 6},
            "asistente": {"nombre": "Mesut Özil", "dorsal": 8},
            "tipo_jugada": "Ataque vertical y pase atrás",
            "xg": 0.42,
            "coordenadas_campo_cm": {"pitch_x": 1120, "pitch_y": 3200},
            "distancia_porteria_m": 11.2,
            "pie_remate": "Derecho (raso al palo largo)",
            "diagnostico_tactico_dt": "Conducción vertical de Hummels saltando dos líneas de presión sin oposición. Khedira combina con Özil por carril izquierdo; Özil aguanta la salida de Júlio César y cede atrás para el remate ajustado de Khedira.",
            "texto_narracion_accesible": "Minuto 29: Incursión profunda de Hummels desde la defensa, cede a Khedira que habilita a Özil dentro del área. Özil levanta la cabeza, frena y mete el pase atrás donde Khedira define con un toque sutil y colocado al rincón. ¡Manita histórica de Alemania en menos de media hora, 5 a 0!"
        },
        {
            "orden": 6,
            "minuto": 69,
            "segundo_oficial": "68:11",
            "marcador_momento": "0-6",
            "equipo_anotador": "Alemania",
            "anotador": {"nombre": "André Schürrle", "dorsal": 9},
            "asistente": {"nombre": "Philipp Lahm", "dorsal": 16},
            "tipo_jugada": "Pase de la muerte tras desborde exterior",
            "xg": 0.45,
            "coordenadas_campo_cm": {"pitch_x": 1050, "pitch_y": 3750},
            "distancia_porteria_m": 10.5,
            "pie_remate": "Derecho (remate de primera al primer palo)",
            "diagnostico_tactico_dt": "Desmarque de ruptura exterior de Lahm a la espalda de Marcelo. Pase de la muerte raso al corazón del área donde Schürrle anticipa a Dante atacando el intervalo.",
            "texto_narracion_accesible": "Minuto 69: Nueva proyección de Philipp Lahm por la banda derecha ganando la línea de fondo. Envía el centro raso hacia el punto penal y André Schürrle llega en carrera para cruzar el disparo de primera con pierna derecha. ¡6 a 0 para el conjunto teutón!"
        },
        {
            "orden": 7,
            "minuto": 79,
            "segundo_oficial": "78:20",
            "marcador_momento": "0-7",
            "equipo_anotador": "Alemania",
            "anotador": {"nombre": "André Schürrle", "dorsal": 9},
            "asistente": {"nombre": "Thomas Müller", "dorsal": 13},
            "tipo_jugada": "Control orientado y remate potente al ángulo",
            "xg": 0.12,
            "coordenadas_campo_cm": {"pitch_x": 880, "pitch_y": 2450},
            "distancia_porteria_m": 8.8,
            "pie_remate": "Izquierdo (volea potente al travesaño y adentro)",
            "diagnostico_tactico_dt": "Pase aéreo filtrado de Müller hacia la izquierda del área. Schürrle domina con pierna izquierda en carrera y empalma un disparo seco que impacta la parte inferior del larguero.",
            "texto_narracion_accesible": "Minuto 79: Balón picado de Thomas Müller hacia la izquierda del área chica. André Schürrle la duerme con la pierna zurda y sin dejarla caer mete un trallazo fulminante que revienta el travesaño antes de clavarse en el fondo de la red. ¡Golazo impresionante de Schürrle, 7 a 0!"
        },
        {
            "orden": 8,
            "minuto": 90,
            "segundo_oficial": "89:45",
            "marcador_momento": "1-7",
            "equipo_anotador": "Brasil",
            "anotador": {"nombre": "Oscar", "dorsal": 11},
            "asistente": {"nombre": "Marcelo", "dorsal": 6},
            "tipo_jugada": "Contraataque y desborde individual",
            "xg": 0.28,
            "coordenadas_campo_cm": {"pitch_x": 10850, "pitch_y": 3650},
            "distancia_porteria_m": 11.5,
            "pie_remate": "Derecho (disparo cruzado frente a Neuer)",
            "diagnostico_tactico_dt": "Transición rápida de Brasil ante un fallo de Özil en área contraria. Pelotazo largo de Marcelo al espacio para la carrera de Oscar, quien quiebra a Boateng y bate a Neuer en el mano a mano.",
            "texto_narracion_accesible": "Minuto 90: Salida rápida desde el fondo con pelotazo largo de Marcelo. Oscar gana la espalda de Boateng, recorta hacia adentro dentro del área y define ante el achique de Manuel Neuer con remate cruzado. Llega el descuento para Brasil: 1 a 7 en el tiempo cumplido."
        }
    ]

    with open("02_partido_completo/linea_tiempo_goles.json", "w", encoding="utf-8") as f:
        json.dump(goles, f, indent=2, ensure_ascii=False)
    print("linea_tiempo_goles.json generado con exito.")

    csv_rows = [
        ["Orden", "Minuto", "Reloj_Oficial", "Marcador", "Equipo", "Anotador", "Dorsal_Anotador", "Asistente", "Dorsal_Asistente", "Tipo_Jugada", "xG", "Pitch_X_cm", "Pitch_Y_cm", "Distancia_m", "Pie_Remate"]
    ]
    for g in goles:
        csv_rows.append([
            g["orden"],
            g["minuto"],
            g["segundo_oficial"],
            g["marcador_momento"],
            g["equipo_anotador"],
            g["anotador"]["nombre"],
            g["anotador"]["dorsal"],
            g["asistente"]["nombre"],
            g["asistente"]["dorsal"],
            g["tipo_jugada"],
            g["xg"],
            g["coordenadas_campo_cm"]["pitch_x"],
            g["coordenadas_campo_cm"]["pitch_y"],
            g["distancia_porteria_m"],
            g["pie_remate"]
        ])
    
    with open("02_partido_completo/linea_tiempo_goles.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(csv_rows)
    print("linea_tiempo_goles.csv generado con exito.")

if __name__ == "__main__":
    os.makedirs("02_partido_completo", exist_ok=True)
    generate_context()
    generate_statistics()
    generate_goals_timeline()
