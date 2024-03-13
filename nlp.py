from llama_cpp import Llama
import os

# conda activate llama
# https://github.com/abetlen/llama-cpp-python

llm = Llama(
    model_path="./models/mistral-7b-openorca.Q4_K_M.gguf", n_gpu_layers=1, n_ctx=4096
)


print("\033c")


def saveTakling(user, bot):
    with open("talking.txt", "a") as f:
        f.write(f"User: {user}\n")
        f.write(f"Bot: {bot}\n")
        f.write("\n")


message = []


while True:

    user_input = input("User: ")
    message.append(f"User: {user_input}")
    output = llm.create_completion(
        f"""<|im_start|>system
    You are a helpful chatbot.
    <|im_end|>
    <|im_start|>give me answer with chat story {message}<|im_end|>
    <|im_start|>assistant""",
        max_tokens=500,
        stop=["<|im_end|>"],
        stream=True,
    )

    answer = ""

    for token in output:
        answer += token["choices"][0]["text"]

    print("Bot:", answer)

    print()

    message.append(f"User: {user_input}", f"Bot: {answer}")

    saveTakling(user_input, answer)

    if user_input == "exit":
        break


# def talk(user_input, conversation_history):
#     # Thêm đầu vào của người dùng vào lịch sử trò chuyện
#     conversation_history.append(f"User: {user_input}\n")

#     # Chuẩn bị đầu vào cho mô hình với lịch sử trò chuyện
#     model_input = (
#         "system\nYou are a helpful chatbot.\n"
#         + "".join(conversation_history)
#         + "assistant"
#     )

#     output = llm.create_completion(
#         model_input,
#         max_tokens=500,
#         stop=["assistant"],
#         stream=True,
#     )

#     answer = ""

#     for token in output:
#         answer += token["choices"][0]["text"]

#     conversation_history.append(f"Bot: {answer}\n")

#     return answer
