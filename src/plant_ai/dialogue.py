
INTENTS = {
    "greeting": {
        "salut",
        "bonjour",
        "hey"
    },
    "status_question": {
        "ça va",
        "comment",
        "comment vas-tu"
    },
    "generic": set(),
}

THEMES_BY_STATES = {
    ("humidity", "too_low"): "lack_of_water",
    ("humidity", "too_high"): "too_much_water",
    ("brightness", "too_low"): "lack_of_brightness",
    ("brightness", "too_high"): "too_much_brightness"
}

THEMES = {
    "lack_of_water": {
        "soif", "manque d'eau",
    },
    "too_much_water": {
        "trop d'eau", "noyé", "étouffé",
    },
    "lack_of_brightness": {
        "manque de lumière"
    },
    "too_much_brightness": {
        "trop de lumière"
    },
    "stable": {
        "bien-être", "stable"
    },
}

def normalize(text):
    """Normalize user text"""
    return text.strip().lower()

def detect_user_intent(user_text):
    """Return user intent depending on the words used"""
    text = normalize(user_text)
    for intent, keywords in INTENTS.items():
        if intent == "generic":
            print(intent)
            continue
        if text in keywords:
            print(intent)
            return intent
    return "generic"

def response_theme(mood_data):
    """Defined the theme of the plant's response"""
    source = mood_data['source']
    reason = mood_data['reason']
    key = (source, reason)
    return THEMES_BY_STATES.get(key, "stable")