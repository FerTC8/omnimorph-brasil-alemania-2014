"""
Generador de telemetría de alta precisión para el Gol 1 de Thomas Müller (Min 11)
Bajo especificación OMNIMORPH:
- Pitch: 12000 cm x 7000 cm
- fps: 25 (8 segundos = 200 frames)
- Jugadores: 22 + Árbitro + Balón
- Velocidades en cm/s
"""

import json
import math

def generate_telemetry():
    frames_data = []
    
    # 25 fps, 8 seconds = frames 0 to 200 (sampled every 10 frames = 0.4s interval: 21 keyframe snapshots)
    sample_frames = list(range(0, 201, 10))
    
    # Static or base coordinates for players not directly in the 6-yard cluster
    # Brazil defending left side (x=0 to 3000), Germany attacking towards x=0
    
    for f in sample_frames:
        t = round(f / 25.0, 2)
        progress_delivery = min(1.0, max(0.0, (t - 0.5) / 4.5)) if t >= 0.5 else 0.0
        progress_shot = min(1.0, max(0.0, (t - 5.0) / 1.5)) if t >= 5.0 else 0.0
        
        # Ball trajectory:
        # Corner flag at (35, 6965)
        # In flight towards Muller at (920, 4150)
        # Shot towards goal at (5, 3820)
        if t < 0.5:
            ball_x = 35.0
            ball_y = 6965.0
            ball_z = 0.0
            ball_speed = 0.0
        elif t <= 5.0:
            # Curved trajectory from corner to (920, 4150)
            u = (t - 0.5) / 4.5
            ball_x = 35.0 + u * (920.0 - 35.0)
            ball_y = 6965.0 + u * (4150.0 - 6965.0) + math.sin(u * math.pi) * 350.0 # slight outswing
            ball_speed = 2200.0 - u * 600.0 # deceleration in air cm/s
        else:
            # Shot from (920, 4150) to (5, 3820)
            u = min(1.0, (t - 5.0) / 1.5)
            ball_x = 920.0 - u * (920.0 - 5.0)
            ball_y = 4150.0 - u * (4150.0 - 3820.0)
            ball_speed = 2177.8 if u < 1.0 else 0.0

        # Player movements:
        # Kroos (#18 GER) - Corner taker
        kroos_x = 45.0 + (50.0 * min(1.0, t/3.0))
        kroos_y = 6950.0 - (40.0 * min(1.0, t/3.0))
        kroos_spd = 180.0 if t < 2.0 else 40.0
        
        # Muller (#13 GER) - Starts around (1350, 4700), makes looping run away from screen to (920, 4150)
        if t <= 5.0:
            u_m = t / 5.0
            muller_x = 1350.0 - u_m * 430.0
            muller_y = 4700.0 - u_m * 550.0
            muller_spd = 350.0 + u_m * 120.0 # accelerating cm/s (~4.7 m/s)
        else:
            muller_x = 920.0 + (t - 5.0) * 15.0
            muller_y = 4150.0 - (t - 5.0) * 20.0
            muller_spd = 80.0

        # David Luiz (#4 BRA) - Supposed to mark Muller, gets blocked by Klose/Howedes screen
        if t <= 2.5:
            # Follows initially
            u_dl = t / 2.5
            dl_x = 1280.0 - u_dl * 150.0
            dl_y = 4600.0 - u_dl * 120.0
            dl_spd = 280.0
        elif t <= 5.0:
            # Stuck in screen traffic around (1130, 4480)
            dl_x = 1130.0 + math.sin((t - 2.5) * 3) * 15.0
            dl_y = 4480.0 + math.cos((t - 2.5) * 3) * 10.0
            dl_spd = 65.0
        else:
            # Realizes Muller is free, desperate lunge
            dl_x = 1130.0 - (t - 5.0) * 80.0
            dl_y = 4480.0 - (t - 5.0) * 100.0
            dl_spd = 380.0

        # Klose (#11 GER) - Screening run into 6-yard box
        klose_x = 650.0 + math.sin(t * 0.5) * 30.0
        klose_y = 4300.0 + (t * 20.0)
        
        # Howedes (#4 GER) - Screening / decoy run
        howedes_x = 750.0 - math.cos(t * 0.6) * 20.0
        howedes_y = 4450.0 + (t * 15.0)
        
        # Dante (#13 BRA) - Central defender in 6-yard box
        dante_x = 520.0 + math.sin(t * 0.4) * 20.0
        dante_y = 3900.0 + (t * 10.0)

        # Julio Cesar (#12 BRA) - Goalkeeper inside 6-yard box
        if t < 5.0:
            jc_x = 180.0
            jc_y = 3550.0 + math.sin(t * 0.8) * 40.0
            jc_spd = 60.0
        else:
            # Reaction dive attempt
            jc_x = 180.0 - (t - 5.0) * 30.0
            jc_y = 3550.0 + (t - 5.0) * 85.0
            jc_spd = 140.0

        # Marcelo (#6 BRA) - Near post cover
        marcelo_x = 350.0 + math.cos(t * 0.5) * 15.0
        marcelo_y = 4850.0 - math.sin(t * 0.5) * 20.0

        # Maicon (#23 BRA) - Edge of box
        maicon_x = 1450.0 + math.sin(t * 0.3) * 30.0
        maicon_y = 5200.0

        # Fernandinho (#5 BRA) - Top of box
        fernandinho_x = 1550.0 + math.cos(t * 0.4) * 25.0
        fernandinho_y = 3600.0

        # Luiz Gustavo (#17 BRA) - Marking near edge
        luiz_gustavo_x = 880.0 + math.sin(t * 0.5) * 30.0
        luiz_gustavo_y = 3450.0

        # Oscar (#11 BRA) - Transition exit
        oscar_x = 2200.0 + math.cos(t * 0.2) * 50.0
        oscar_y = 4200.0

        # Hulk (#7 BRA) - Transition winger
        hulk_x = 2800.0 + math.sin(t * 0.2) * 60.0
        hulk_y = 5800.0

        # Bernard (#20 BRA) - Transition winger
        bernard_x = 2750.0 - math.cos(t * 0.2) * 40.0
        bernard_y = 1500.0

        # Fred (#9 BRA) - Target man on counter posture
        fred_x = 3600.0 + math.sin(t * 0.1) * 30.0
        fred_y = 3500.0

        # Germany players positioning
        # Hummels (#5 GER) - Far post target
        hummels_x = 720.0 + math.cos(t * 0.5) * 40.0
        hummels_y = 3200.0

        # Boateng (#20 GER) - Edge of box cover
        boateng_x = 1750.0 + math.sin(t * 0.3) * 30.0
        boateng_y = 4400.0

        # Lahm (#16 GER) - Rebound sweeper
        lahm_x = 2100.0 + math.cos(t * 0.3) * 40.0
        lahm_y = 5100.0

        # Khedira (#6 GER) - Central edge
        khedira_x = 1650.0 + math.sin(t * 0.4) * 50.0
        khedira_y = 3800.0

        # Schweinsteiger (#7 GER) - Rest defense midfield
        schweinsteiger_x = 2650.0 + math.cos(t * 0.2) * 30.0
        schweinsteiger_y = 3300.0

        # Ozil (#8 GER) - Short corner decoy
        ozil_x = 380.0 + math.sin(t * 0.6) * 40.0
        ozil_y = 6400.0 - (t * 30.0)

        # Neuer (#1 GER) - Sweeper-keeper near center circle
        neuer_x = 7800.0 + math.sin(t * 0.1) * 20.0
        neuer_y = 3500.0

        # Referee Marco Rodriguez (MEX)
        ref_x = 1850.0 + math.sin(t * 0.3) * 35.0
        ref_y = 2600.0 + (t * 15.0)

        objetos = [
            # Ball
            {
                "id": "ball",
                "team": None,
                "dorsal": None,
                "jugador": "Balon",
                "pitch_x": round(ball_x, 1),
                "pitch_y": round(ball_y, 1),
                "speed_cm_s": round(ball_speed, 1),
                "rol_jugada": "balon_en_juego"
            },
            # Germany key actors
            {
                "id": "ger_18",
                "team": 1,
                "dorsal": 18,
                "jugador": "Toni Kroos",
                "pitch_x": round(kroos_x, 1),
                "pitch_y": round(kroos_y, 1),
                "speed_cm_s": round(kroos_spd, 1),
                "rol_jugada": "ejecutor_corner"
            },
            {
                "id": "ger_13",
                "team": 1,
                "dorsal": 13,
                "jugador": "Thomas Müller",
                "pitch_x": round(muller_x, 1),
                "pitch_y": round(muller_y, 1),
                "speed_cm_s": round(muller_spd, 1),
                "rol_jugada": "rematador_desmarcado"
            },
            {
                "id": "ger_11",
                "team": 1,
                "dorsal": 11,
                "jugador": "Miroslav Klose",
                "pitch_x": round(klose_x, 1),
                "pitch_y": round(klose_y, 1),
                "speed_cm_s": 140.0,
                "rol_jugada": "bloqueador_pantalla"
            },
            {
                "id": "ger_4",
                "team": 1,
                "dorsal": 4,
                "jugador": "Benedikt Höwedes",
                "pitch_x": round(howedes_x, 1),
                "pitch_y": round(howedes_y, 1),
                "speed_cm_s": 125.0,
                "rol_jugada": "bloqueador_pantalla"
            },
            {
                "id": "ger_5",
                "team": 1,
                "dorsal": 5,
                "jugador": "Mats Hummels",
                "pitch_x": round(hummels_x, 1),
                "pitch_y": round(hummels_y, 1),
                "speed_cm_s": 110.0,
                "rol_jugada": "fijador_segundo_palo"
            },
            {
                "id": "ger_6",
                "team": 1,
                "dorsal": 6,
                "jugador": "Sami Khedira",
                "pitch_x": round(khedira_x, 1),
                "pitch_y": round(khedira_y, 1),
                "speed_cm_s": 130.0,
                "rol_jugada": "rebote_frontal"
            },
            {
                "id": "ger_8",
                "team": 1,
                "dorsal": 8,
                "jugador": "Mesut Özil",
                "pitch_x": round(ozil_x, 1),
                "pitch_y": round(ozil_y, 1),
                "speed_cm_s": 160.0,
                "rol_jugada": "distractor_corto"
            },
            {
                "id": "ger_16",
                "team": 1,
                "dorsal": 16,
                "jugador": "Philipp Lahm",
                "pitch_x": round(lahm_x, 1),
                "pitch_y": round(lahm_y, 1),
                "speed_cm_s": 95.0,
                "rol_jugada": "vigilancia_ofensiva"
            },
            {
                "id": "ger_20",
                "team": 1,
                "dorsal": 20,
                "jugador": "Jérôme Boateng",
                "pitch_x": round(boateng_x, 1),
                "pitch_y": round(boateng_y, 1),
                "speed_cm_s": 85.0,
                "rol_jugada": "vigilancia_ofensiva"
            },
            {
                "id": "ger_7",
                "team": 1,
                "dorsal": 7,
                "jugador": "Bastian Schweinsteiger",
                "pitch_x": round(schweinsteiger_x, 1),
                "pitch_y": round(schweinsteiger_y, 1),
                "speed_cm_s": 90.0,
                "rol_jugada": "equilibrio_medio"
            },
            {
                "id": "ger_1",
                "team": 1,
                "dorsal": 1,
                "jugador": "Manuel Neuer",
                "pitch_x": round(neuer_x, 1),
                "pitch_y": round(neuer_y, 1),
                "speed_cm_s": 40.0,
                "rol_jugada": "portero_libero"
            },
            # Brazil key actors
            {
                "id": "bra_12",
                "team": 0,
                "dorsal": 12,
                "jugador": "Júlio César",
                "pitch_x": round(jc_x, 1),
                "pitch_y": round(jc_y, 1),
                "speed_cm_s": round(jc_spd, 1),
                "rol_jugada": "portero"
            },
            {
                "id": "bra_4",
                "team": 0,
                "dorsal": 4,
                "jugador": "David Luiz",
                "pitch_x": round(dl_x, 1),
                "pitch_y": round(dl_y, 1),
                "speed_cm_s": round(dl_spd, 1),
                "rol_jugada": "marca_individual_bloqueada"
            },
            {
                "id": "bra_13",
                "team": 0,
                "dorsal": 13,
                "jugador": "Dante",
                "pitch_x": round(dante_x, 1),
                "pitch_y": round(dante_y, 1),
                "speed_cm_s": 95.0,
                "rol_jugada": "zona_central_chica"
            },
            {
                "id": "bra_6",
                "team": 0,
                "dorsal": 6,
                "jugador": "Marcelo",
                "pitch_x": round(marcelo_x, 1),
                "pitch_y": round(marcelo_y, 1),
                "speed_cm_s": 75.0,
                "rol_jugada": "primer_palo"
            },
            {
                "id": "bra_23",
                "team": 0,
                "dorsal": 23,
                "jugador": "Maicon",
                "pitch_x": round(maicon_x, 1),
                "pitch_y": round(maicon_y, 1),
                "speed_cm_s": 65.0,
                "rol_jugada": "zona_lateral"
            },
            {
                "id": "bra_17",
                "team": 0,
                "dorsal": 17,
                "jugador": "Luiz Gustavo",
                "pitch_x": round(luiz_gustavo_x, 1),
                "pitch_y": round(luiz_gustavo_y, 1),
                "speed_cm_s": 110.0,
                "rol_jugada": "marca_zonal_area"
            },
            {
                "id": "bra_5",
                "team": 0,
                "dorsal": 5,
                "jugador": "Fernandinho",
                "pitch_x": round(fernandinho_x, 1),
                "pitch_y": round(fernandinho_y, 1),
                "speed_cm_s": 105.0,
                "rol_jugada": "frontal_area"
            },
            {
                "id": "bra_11",
                "team": 0,
                "dorsal": 11,
                "jugador": "Oscar",
                "pitch_x": round(oscar_x, 1),
                "pitch_y": round(oscar_y, 1),
                "speed_cm_s": 80.0,
                "rol_jugada": "vigilancia_rebote"
            },
            {
                "id": "bra_7",
                "team": 0,
                "dorsal": 7,
                "jugador": "Hulk",
                "pitch_x": round(hulk_x, 1),
                "pitch_y": round(hulk_y, 1),
                "speed_cm_s": 70.0,
                "rol_jugada": "salida_contraataque"
            },
            {
                "id": "bra_20",
                "team": 0,
                "dorsal": 20,
                "jugador": "Bernard",
                "pitch_x": round(bernard_x, 1),
                "pitch_y": round(bernard_y, 1),
                "speed_cm_s": 60.0,
                "rol_jugada": "salida_contraataque"
            },
            {
                "id": "bra_9",
                "team": 0,
                "dorsal": 9,
                "jugador": "Fred",
                "pitch_x": round(fred_x, 1),
                "pitch_y": round(fred_y, 1),
                "speed_cm_s": 45.0,
                "rol_jugada": "descolgado"
            },
            # Referee
            {
                "id": "ref_1",
                "team": None,
                "dorsal": None,
                "jugador": "Marco Rodríguez (Árbitro)",
                "pitch_x": round(ref_x, 1),
                "pitch_y": round(ref_y, 1),
                "speed_cm_s": 85.0,
                "rol_jugada": "arbitro_posicionamiento"
            }
        ]

        frames_data.append({
            "frame": f,
            "timestamp_s": t,
            "ventana_activa": 1 if t <= 4.0 else 2,
            "total_objetos_detectados": len(objetos),
            "objetos": objetos
        })

    payload = {
        "metadata": {
            "version_schema": "OMNIMORPH-TELEMETRY-v2.0",
            "partido": "Brasil vs Alemania 2014",
            "evento": "Gol 1 - Thomas Müller (11')",
            "duracion_total_s": 8.0,
            "total_frames_analizados": 201,
            "intervalo_muestreo_frames": 10,
            "coordenadas_unidad": "centimetros (cm)",
            "dimensiones_campo_cm": {"largo_x": 12000, "ancho_y": 7000},
            "equipos": {
                "0": "Brasil (Defendiendo x=0)",
                "1": "Alemania (Atacando hacia x=0)"
            }
        },
        "frames": frames_data
    }
    
    with open("01_gol_muller_min11/muestra_telemetria_muller.json", "w", encoding="utf-8") as fp:
        json.dump(payload, fp, indent=2, ensure_ascii=False)
    print("muestra_telemetria_muller.json generado con exito.")

if __name__ == "__main__":
    generate_telemetry()
