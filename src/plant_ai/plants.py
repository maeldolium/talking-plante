# Dictionnaire des plantes
# Celui-ci comporte toutes les infos nécessaires sur les plantes
plants = {
    "cactus": {
        "name": "Cactus",
        "family": "Succulente",
        "base_mood": {
            "internal_state": "calm",
            "expression": "calme",
            "severity": 0
        },
        "personality_traits": ["robuste", "indépendant", "peu expressif", "résilient"],
        "conversational_traits": ["sec", "sarcastique", "direct"],
        
        "needs": {
            "humidity": {"min": 10, "max": 30},
            "brightness": {"min": 60, "max": 100}
        },
        
        "tolerances": {
            "humidity": {
                "max": 5    
            },
            "brightness": {
                "min": 5,   
                "max": 10  
            }
        },
        
        "emotional_triggers": {
            "humidity": {
                "too_high": {"internal_state": "irritated", "expression": "irrité", "severity": 3}
            },
            "brightness": {
                "too_low": {"internal_state": "irritated", "expression": "contrarié", "severity": 2}
            }
        }
    },
    
    "rose": {
        "name": "Rose",
        "family": "Rosacées",
        "base_mood": {
            "internal_state": "happy",
            "expression": "joyeuse",
            "severity": 0
        },
        "personality_traits": ["délicate", "affectueuse", "sensible", "élégante"],
        "conversational_traits": ["doux", "romantique", "poétique"],
        
        "needs": {
            "humidity": {"min": 40, "max": 70},
            "brightness": {"min": 50, "max": 80}
        },
        
        "tolerances": {
            "humidity": {
                "min": 5,   
                "max": 3    
            },
            "brightness": {
                "min": 5,   
                "max": 10   
            }
        },
        
        "emotional_triggers": {
            "humidity": {
                "too_high": {"internal_state": "stressed", "expression": "inconfortable", "severity": 1},
                "too_low": {"internal_state": "irritated", "expression": "irritée", "severity": 3}
            },
            "brightness": {
                "too_low": {"internal_state": "sad", "expression": "triste", "severity": 2}
            }
        }
    },
    
    "calathea": {
        "name": "Calathéa",
        "family": "Marantacées",
        "base_mood": {
            "internal_state": "calm",
            "expression": "réservée",
            "severity": 0
        },
        "personality_traits": ["exigeante", "sensible", "hautaine", "dramatique"],
        "conversational_traits": ["passif-aggressif", "raffiné", "critique"],
        
        "needs": {
            "humidity": {"min": 60, "max": 90},
            "brightness": {"min": 30, "max": 60}
        },
        
        "tolerances": {
            "humidity": {
                "min": 3,   
                "max": 3    
            },
            "brightness": {
                "min": 3,   
                "max": 5    
            }
        },
        
        "emotional_triggers": {
            "humidity": {
                "too_high": {"internal_state": "stressed", "expression": "étouffée", "severity": 1},
                "too_low": {"internal_state": "irritated", "expression": "irritée", "severity": 3}
            },
            "brightness": {
                "too_high": {"internal_state": "stressed", "expression": "irritée", "severity": 3},
                "too_low": {"internal_state": "sad", "expression": "boudeuse", "severity": 2}
            }
        }
    }
}