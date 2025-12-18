from incident_generator.generator import generate_incident

def test_generate_incident():
    incident = generate_incident()

    assert isinstance(incident, dict)
    assert "error" in incident
    assert "service" in incident
    assert "severity" in incident
    assert "timestamp" in incident

