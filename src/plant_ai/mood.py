from plant_ai.plants import plants

def get_plant(plant):
    """Retourne le dictionnaire correspondant à la plante sélectionnée"""
    return plants[plant]

def build_mood_object(sensors, plant):
    """Construit l'objet contenant le mood en fonction des conditions environnementales"""
    issues = compare_sensors_to_needs(sensors, plant)
    mood_data = choose_primary_mood(issues, plant)

    return mood_data

def compare_sensors_to_needs(sensors, plant):
    """Compare les valeurs des capteurs aux besoins de la plante et retourne le mood de la plante"""
    issues = []

    for metric, value in sensors.items():
        if metric not in plant['needs']:
            continue

        tolerance = plant['tolerances'].get(metric, {})
        min_threshold = plant['needs'][metric]['min'] - tolerance.get('min', 0)
        max_threshold = plant['needs'][metric]['max'] + tolerance.get('max', 0)

        if value < min_threshold and 'too_low' in plant['emotional_triggers'].get(metric, {}):
            issues.append({
                'metric': metric,
                'trigger': plant['emotional_triggers'][metric]['too_low'],
                'source': metric,
                'reason': 'too_low'
            })
        elif value > max_threshold and 'too_high' in plant['emotional_triggers'].get(metric, {}):
            issues.append({
                'metric': metric,
                'trigger': plant['emotional_triggers'][metric]['too_high'],
                'source': metric,
                'reason': 'too_high'
            })

    return issues if issues else None

def choose_primary_mood(issues, plant):
    """Retourne le mood avec la plus grande sévérité ou le mood de base"""
    if not issues:
        base = plant['base_mood']
        result = {
            'internal_state': base['internal_state'],
            'expression': base['expression'],
            'severity': base['severity'],
            'source': 'none',
            'reason': 'stable_conditions'
        }
        return result
    else:
        primary_trigger = max(issues, key=lambda x: x['trigger']['severity'])
        result = {
            'internal_state': primary_trigger['trigger']['internal_state'],
            'expression': primary_trigger['trigger']['expression'],
            'severity': primary_trigger['trigger']['severity'],
            'source': primary_trigger['source'],
            'reason': primary_trigger['reason']
        }
        return result