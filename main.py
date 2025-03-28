import streamlit as st
# from langchain_openai import ChatOpenAI
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from openai import OpenAI
from langchain.memory import ConversationBufferMemory
from gtts import gTTS
from dotenv import load_dotenv
import os

# 初始化 GPT 对话模型
load_dotenv()
llm = ChatOpenAI(model_name="gpt-4o", temperature=0.7, openai_api_key="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")

memory = ConversationBufferMemory()

# Streamlit 页面标题
st.title("AI语智")
st.subheader("——基于AI Agent的互动式多语言学习平台")

# =============== 语法分析 ===============
st.subheader("📖 AI 语法分析")

text_input = st.text_area("您可以输入中文、英文、西班牙文的文本内容，我将为您分析语法和结构", placeholder="输入一段文本，AI 将解析语法")
if st.button("分析文本"):
    if text_input:
        prompt = f"请分析以下文本的语法结构，并列出涉及的语法点和解释：{text_input}"
        response = llm.predict(text=prompt)
        st.write("📚 语法解析结果：")
        st.write(response)

# =============== 文字朗读 ===============
st.subheader("🔊 AI 语音朗读")

text_to_speak = st.text_area("我可以朗读中文/英文/西班牙，请输入需要朗读的内容", placeholder="输入文本，AI 将朗读")
if st.button("播放语音"):
    if text_to_speak:
        tts = gTTS(text=text_to_speak, lang="en")
        tts.save("output.mp3")
        st.audio("output.mp3", format="audio/mp3")

# =============== AI 角色扮演对话 ===============
st.subheader("🗣 AI 角色扮演对话")

# 创建对话链（带记忆）
conversation = ConversationChain(
    llm=llm,
    memory=memory,
    verbose=False  # 设为 True 可查看详细对话日志
)


user_input = st.text_input("你：", placeholder="输入你想和 AI 交谈的内容")
if st.button("发送"):
    if user_input:
        # response = llm.predict(text=user_input, memory=memory)
        response = conversation.predict(input=user_input)
        st.write(f"🤖 AI：{response}")