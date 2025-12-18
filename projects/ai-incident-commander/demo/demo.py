from incident_generator.generator import generate_incident
import json

if __name__ == "__main__":
    incident = generate_incident()
    print("\n🚨 GENERATED INCIDENT\n")
    print(json.dumps(incident, indent=2))
