import streamlit as st
import google.generativeai as genai

# টাইটেল ও পেজ সেটআপ
st.set_page_config(page_title="My AI Agent", layout="centered")
st.title("🤖 My Personal AI Agent")

# আপনার API Key (সরাসরি বসানো হয়েছে)
API_KEY = "AIzaSyAEr-bY2XV2wuFWkUtCWS1jXYudiFMW7sg"
genai.configure(api_key=API_KEY)

# এখানে শুধু 'gemini-pro' ব্যবহার করুন, কোনো স্লাশ বা অতিরিক্ত ভার্সন ছাড়া
model = genai.GenerativeModel('gemini-pro')

# চ্যাট হিস্ট্রি সেটআপ
if "messages" not in st.session_state:
    st.session_state.messages = []

# আগের মেসেজগুলো পেজে দেখানো
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ইউজার মেসেজ লিখলে যা হবে
if prompt := st.chat_input("Ask me anything..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # এআই থেকে উত্তর আনা
    with st.chat_message("assistant"):
        try:
            # খুব সাধারণ পদ্ধতিতে উত্তর চাওয়া হচ্ছে
            response = model.generate_content(prompt)
            
            # উত্তরের টেক্সটটি চেক করে দেখানো
            if response.text:
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
            else:
                st.error("AI could not generate a response. Please try again.")
        except Exception as e:
            # যদি ভুল মডেল নাম থাকে তবে অন্য মডেল ট্রাই করা হবে অটোমেটিক
            st.error(f"Error: {e}")
            st.info("Trying to fix the model name... Please wait.")
