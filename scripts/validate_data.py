"""
Validador de integridad para los datos de Brasil 1–7 Alemania 2014 (OMNIMORPH).
Verifica presencia de archivos, límites de cancha, consistencia JSON/CSV y contratos.
"""

import os
import json
import csv
import sys

def test_file_existence():
    required_files = [
        "01_primer_gol_muller/gol_muller_min11.json",
        "01_primer_gol_muller/muestra_telemetria_muller.json",
        "02_partido_completo/contexto_partido.json",
        "02_partido_completo/estadisticas_partido.json",
        "02_partido_completo/estadisticas_partido.csv",
        "02_partido_completo/cronologia_goles.json",
        "02_partido_completo/cronologia_goles.csv",
        "assets/mapa_8_goles.svg",
        "assets/radar_gol_muller.svg",
        "FUENTES.md",
        "README.md",
        ".gitignore"
    ]
    for rf in required_files:
        assert os.path.exists(rf), f"Falta archivo requerido: {rf}"
    print("✓ Todos los archivos requeridos están presentes.")

def test_muller_ventanas():
    with open("01_primer_gol_muller/gol_muller_min11.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    assert "metadatos_jugada" in data, "Falta 'metadatos_jugada'"
    assert "estadisticas_acumuladas_minuto_11" in data, "Falta 'estadisticas_acumuladas_minuto_11'"
    assert "ventanas_tacticas" in data, "Falta 'ventanas_tacticas'"
    assert len(data["ventanas_tacticas"]) == 2, "Deben existir exactamente 2 ventanas tácticas"
    for v in data["ventanas_tacticas"]:
        for key in ["t0", "t1", "texto", "texto_tactico", "texto_narracion", "metricas"]:
            assert key in v, f"Falta clave '{key}' en ventana {v.get('ventana_id')}"
    print("✓ gol_muller_min11.json cumple con el contrato OMNIMORPH y contiene stats al min 11.")

def test_muller_telemetry():
    with open("01_primer_gol_muller/muestra_telemetria_muller.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    frames = data.get("frames", [])
    assert len(frames) > 0, "No hay frames en telemetría"
    for frame in frames:
        for obj in frame.get("objetos", []):
            x = obj.get("pitch_x")
            y = obj.get("pitch_y")
            team = obj.get("team")
            assert 0.0 <= x <= 12000.0, f"Coordenada X fuera de límites: {x}"
            assert 0.0 <= y <= 7000.0, f"Coordenada Y fuera de límites: {y}"
            assert team in [0, 1, None], f"ID de equipo inválido: {team}"
    print("✓ muestra_telemetria_muller.json cumple con las coordenadas [0, 12000] x [0, 7000] cm.")

def test_goals_consistency():
    with open("02_partido_completo/cronologia_goles.json", "r", encoding="utf-8") as f:
        goles_json = json.load(f)
    assert len(goles_json) == 8, f"Se esperaban 8 goles en JSON, se encontraron {len(goles_json)}"
    
    with open("02_partido_completo/cronologia_goles.csv", "r", encoding="utf-8") as f:
        reader = list(csv.DictReader(f))
    assert len(reader) == 8, f"Se esperaban 8 goles en CSV, se encontraron {len(reader)}"

    for gj, gc in zip(goles_json, reader):
        assert gj["minuto"] == int(gc["Minuto"]), "Desalineación de minuto entre JSON y CSV"
        assert gj["marcador_momento"] == gc["Marcador"], "Desalineación de marcador entre JSON y CSV"
        assert gj["anotador"]["nombre"] == gc["Anotador"], "Desalineación de anotador entre JSON y CSV"
        x = gj["coordenadas_campo_cm"]["pitch_x"]
        y = gj["coordenadas_campo_cm"]["pitch_y"]
        assert 0 <= x <= 12000, f"Coordenada X de gol fuera de límites: {x}"
        assert 0 <= y <= 7000, f"Coordenada Y de gol fuera de límites: {y}"
    print("✓ Consistencia validada entre cronologia_goles.json y cronologia_goles.csv (8 goles).")

def test_context_and_stats():
    with open("02_partido_completo/contexto_partido.json", "r", encoding="utf-8") as f:
        ctx = json.load(f)
    assert ctx["equipos"]["brasil"]["team_id"] == 0
    assert ctx["equipos"]["alemania"]["team_id"] == 1
    assert len(ctx["equipos"]["brasil"]["plantilla"]) == 23, f"Brasil plantilla debe tener 23 jugadores, tiene {len(ctx['equipos']['brasil']['plantilla'])}"
    assert len(ctx["equipos"]["alemania"]["plantilla"]) == 23, f"Alemania plantilla debe tener 23 jugadores, tiene {len(ctx['equipos']['alemania']['plantilla'])}"

    with open("02_partido_completo/estadisticas_partido.json", "r", encoding="utf-8") as f:
        stats = json.load(f)
    assert stats["resumen_comparativo"]["tiempo_completo"]["marcador"] == "1-7"
    assert stats["resumen_comparativo"]["primer_tiempo"]["marcador"] == "0-5"
    assert stats["resumen_comparativo"]["segundo_tiempo"]["marcador"] == "1-2"
    print("✓ contexto_partido.json y estadisticas_partido.json validados con éxito.")

if __name__ == "__main__":
    try:
        test_file_existence()
        test_muller_ventanas()
        test_muller_telemetry()
        test_goals_consistency()
        test_context_and_stats()
        print("\n==========================================")
        print("✓ VALIDACIÓN COMPLETADA: TODOS LOS ARCHIVOS CUMPLEN CON EL ESTÁNDAR")
        print("==========================================")
    except Exception as e:
        print(f"Error de validación: {e}", file=sys.stderr)
        sys.exit(1)
