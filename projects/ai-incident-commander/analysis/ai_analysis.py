# analysis/ai_analysis.py

import json
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from analysis.severity import classify_severity


# Prompt template
template = """
Analyze the following incident.
Return JSON with keys:
root_cause, impact, recommended_fix, severity_score.

Incident:
{incident_text}
"""

prompt = PromptTemplate(
    input_variables=["incident_text"],
    template=template
)

# Initialize LLM
llm = ChatOpenAI(temperature=0)

# LCEL chain (modern LangChain)
chain = prompt | llm

incident_text = "Service X is down and users cannot log in."

# Invoke chain
result = chain.invoke({"incident_text": incident_text})

# Extract text
response_text = result.content

data = json.loads(response_text)

severity_level = classify_severity(data["severity_score"])

print("Root cause:", data["root_cause"])
print("Impact:", data["impact"])
print("Recommended fix:", data["recommended_fix"])
print("Severity score:", data["severity_score"])
print("Severity level:", severity_level)

