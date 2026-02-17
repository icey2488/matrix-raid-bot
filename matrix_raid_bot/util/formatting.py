# Placeholder formatting utilities


def class_span(name: str, wow_class: str | None):
    return name

def format_signup_list(signups: list) -> str:
    # Placeholder implementation
    return ", ".join(f"{s['character_name']} ({s['status']})" for s in signups)