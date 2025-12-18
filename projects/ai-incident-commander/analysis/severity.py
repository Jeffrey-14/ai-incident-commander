# analysis/severity.py

def classify_severity(score: int) -> str:
    if score >= 9:
        return "SEV-1 (Critical)"
    elif score >= 7:
        return "SEV-2 (High)"
    elif score >= 4:
        return "SEV-3 (Medium)"
    else:
        return "SEV-4 (Low)"
