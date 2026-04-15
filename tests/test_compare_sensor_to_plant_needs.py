import sys
from pathlib import Path


# Permet d'importer mood.py directement (il importe plants.py comme module frère).
sys.path.append(str(Path(__file__).resolve().parents[1] / "src" / "plant_ai"))

from mood import build_mood_object, get_plant


def test_build_mood_object_with_trigger():
    """Test que build_mood_object retourne le trigger le plus sévère avec source/reason"""
    plant = get_plant("rose")
    sensors = {
        "humidity": 30,
        "brightness": 40,
    }

    mood = build_mood_object(sensors, plant)
    print(f"[CASE 1] plant={plant['name']} sensors={sensors}")
    print(f"  -> mood_object={mood}")

    # Rose a 2 triggers : humidity (severity 3) et brightness (severity 2)
    # Doit retourner humidity puisque c'est le plus sévère
    assert mood['source'] == 'humidity'
    assert mood['reason'] == 'too_low'
    assert mood['severity'] == 3
    assert mood['expression'] == 'irritée'


def test_build_mood_object_without_trigger():
    """Test que build_mood_object retourne base_mood quand aucun trigger n'est actif"""
    plant = get_plant("rose")
    sensors = {
        "humidity": 50,
        "brightness": 60,
    }

    mood = build_mood_object(sensors, plant)
    print(f"[CASE 2] plant={plant['name']} sensors={sensors}")
    print(f"  -> mood_object={mood}")

    # Aucun trigger, donc doit retourner base_mood
    assert mood['source'] == 'none'
    assert mood['reason'] == 'stable_conditions'
    assert mood['severity'] == 0
    assert mood['internal_state'] == 'happy'
    assert mood['expression'] == 'joyeuse'


def test_build_mood_object_value_exactly_on_min_is_stable():
    """Vérifie qu'une valeur exactement au minimum ne déclenche aucun trigger."""
    plant = get_plant("rose")
    sensors = {
        "humidity": 40,
        "brightness": 60,
    }

    mood = build_mood_object(sensors, plant)
    print(f"[MIN EXACT] plant={plant['name']} sensors={sensors} -> mood_object={mood}")

    assert mood['source'] == 'none'
    assert mood['reason'] == 'stable_conditions'


def test_build_mood_object_value_exactly_on_max_is_stable():
    """Vérifie qu'une valeur exactement au maximum ne déclenche aucun trigger."""
    plant = get_plant("rose")
    sensors = {
        "humidity": 70,
        "brightness": 60,
    }

    mood = build_mood_object(sensors, plant)
    print(f"[MAX EXACT] plant={plant['name']} sensors={sensors} -> mood_object={mood}")

    assert mood['source'] == 'none'
    assert mood['reason'] == 'stable_conditions'


def test_build_mood_object_value_exactly_on_min_minus_tolerance_is_stable():
    """Vérifie qu'une valeur exactement à min - tolérance reste stable."""
    plant = get_plant("rose")
    sensors = {
        "humidity": 35,
        "brightness": 60,
    }

    mood = build_mood_object(sensors, plant)
    print(f"[MIN-TOL EXACT] plant={plant['name']} sensors={sensors} -> mood_object={mood}")

    assert mood['source'] == 'none'
    assert mood['reason'] == 'stable_conditions'


def test_build_mood_object_value_exactly_on_max_plus_tolerance_is_stable():
    """Vérifie qu'une valeur exactement à max + tolérance reste stable."""
    plant = get_plant("rose")
    sensors = {
        "humidity": 73,
        "brightness": 60,
    }

    mood = build_mood_object(sensors, plant)
    print(f"[MAX+TOL EXACT] plant={plant['name']} sensors={sensors} -> mood_object={mood}")

    assert mood['source'] == 'none'
    assert mood['reason'] == 'stable_conditions'


def test_build_mood_object_two_problems_different_severity_returns_highest():
    """Vérifie que le mood final garde le trigger avec la plus forte sévérité."""
    plant = get_plant("rose")
    sensors = {
        "humidity": 30,
        "brightness": 40,
    }

    mood = build_mood_object(sensors, plant)
    print(f"[TWO PROBLEMS] plant={plant['name']} sensors={sensors} -> mood_object={mood}")

    assert mood['source'] == 'humidity'
    assert mood['reason'] == 'too_low'
    assert mood['severity'] == 3


def test_build_mood_object_problem_on_metric_without_defined_trigger_stays_stable():
    """Vérifie qu'un dépassement sans trigger défini ne change pas le base_mood."""
    plant = get_plant("rose")
    sensors = {
        "humidity": 50,
        "brightness": 200,
    }

    mood = build_mood_object(sensors, plant)
    print(f"[NO TRIGGER FOR METRIC] plant={plant['name']} sensors={sensors} -> mood_object={mood}")

    assert mood['source'] == 'none'
    assert mood['reason'] == 'stable_conditions'


def test_build_mood_object_cactus_very_low_humidity_stays_calm():
    """Vérifie qu'un cactus reste calme avec une humidité très basse."""
    plant = get_plant("cactus")
    sensors = {
        "humidity": 0,
        "brightness": 80,
    }

    mood = build_mood_object(sensors, plant)
    print(f"[CACTUS LOW HUMIDITY] plant={plant['name']} sensors={sensors} -> mood_object={mood}")

    assert mood['source'] == 'none'
    assert mood['reason'] == 'stable_conditions'
    assert mood['internal_state'] == 'calm'
    assert mood['expression'] == 'calme'