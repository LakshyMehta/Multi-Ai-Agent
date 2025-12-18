import os

os.environ["GEMINI_API_KEY"] = "AIzaSyACBmkGu5m0XX3BhKe7p0KVNCB_bnptXBU"

llm_config = {
    "temperature": 0.2,
    "config_list": [
        {
            "model": "gemini-2.5-flash",  # a supported model for generateContent
            "api_type": "google",
            "api_key": os.environ["GEMINI_API_KEY"]
        }
    ]
}
