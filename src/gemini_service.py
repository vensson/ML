import google.generativeai as genai


class GeminiService:

    def __init__(self):

        api_key = "AIzaSyA7DPcmA1uG_L5fAl89xlTqxwIJQ-88mvU"

        genai.configure(api_key=api_key)

        self.model = genai.GenerativeModel(
            'gemini-1.5-flash'
        )

    def improve_cv(self, cv_text):

        prompt = f"""
        Improve this CV professionally:

        {cv_text}
        """

        response = self.model.generate_content(prompt)

        return response.text