import google.generativeai as genai

# আপনার API Key এখানে বসানো হয়েছে
API_KEY = "AIzaSyAEr-bY2XV2wuFWkUtCWS1jXYudiFMW7sg" 

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

def start_agent():
    print("AI Agent: Active. টাইপ করুন (বন্ধ করতে 'exit' লিখুন):")
    while True:
        user_input = input("User: ")
        
        if user_input.lower() == 'exit':
            break
        
        try:
            response = model.generate_content(user_input)
            print(f"AI: {response.text}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    start_agent()
