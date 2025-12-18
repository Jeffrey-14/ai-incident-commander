import json
from analysis.ai_analysis import chain

sample_incident = "Service X is down and users cannot log in."

def test_incident_analysis_output():
    result = chain.invoke({"incident_text": sample_incident})

    # LangChain returns an AIMessage
    data = json.loads(result.content)

    assert "root_cause" in data
    assert "impact" in data
    assert "recommended_fix" in data
    assert "severity_score" in data
