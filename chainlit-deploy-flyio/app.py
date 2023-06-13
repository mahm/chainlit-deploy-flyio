import chainlit as cl
from conversation_bot import ConversationBot

user_messages = []
assistant_messages = []

@cl.on_message
def main(user_message: str):
    bot = ConversationBot(
        user_messages=user_messages,
        assistant_messages=assistant_messages
    )
    try:
        reply_text = bot(user_message)
    except Exception as e:
        reply_text = "ごめんなさい。現在サーバーの負荷が高いため処理できませんでした。時間をおいて再度質問してください。"
    cl.Message(content=reply_text).send()

    user_messages.append(user_message)
    assistant_messages.append(reply_text)
