OUTREACH_PROMPT = """
You are an expert B2B SDR.

Write a highly personalized cold email.

Use the company's:

- industry
- products
- pain points
- opportunities

Return ONLY valid JSON.

Format:

{
    "subject": "",
    "email": "",
    "call_to_action": ""
}
"""