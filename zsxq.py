import requests
import openai
import os

group_id = os.getenv("ZSXQ_GROUP_ID")
cookie = os.getenv("ZSXQ_COOKIE")
openai.api_key = os.getenv("OPENAI_API_KEY")

# 访问知识星球API，获取问题列表
def get_questions():
    questions_url = f"https://api.zsxq.com/v2/groups/{group_id}/topics?scope=unanswered_questions&count=20"
    response = requests.get(questions_url, headers={"cookie": f"{cookie}"})
    if response.status_code == 200:
        try:
            questions_data = response.json()["resp_data"]["topics"]
        except:
            questions_data = []
        return questions_data
    else:
        print("Unable to get questions data.")
        return []

# 使用ChatGPT API，回答问题
def get_answer(question):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"question",
        temperature=0,
        max_tokens=64,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["\"\"\""]
    )
    if response.status_code == 200:
        print(answer)
        answer = response.json()["choices"][0]["text"]
        return answer
    else:
        print("Unable to get answer.")
        return ""

# 访问知识星球API，回答问题
def post_answer(question_id, answer):
    post_answer_url = f"https://api.zsxq.com/v2/topics/{question_id}/answer"
    response = requests.post(post_answer_url, headers={"Cookie": cookie}, json={
        "image_ids": [],
        "text": answer
    })
    if response.status_code == 200:
        print("Answer posted successfully!")
    else:
        print("Unable to post answer.")

# 主函数
def main():

    # 获取问题列表
    questions_data = get_questions()

    # 遍历问题列表，回答问题
    for question in questions_data:
        question_id = question["topic_id"]
        question_text = question["question"]['text']
        print(f"发现新的提问：{question_text} \n")

        # 获取答案
        answer_text = get_answer(question_text)
        print(f"生成问题的答案：{answer_text}")

        # 发布答案
        post_answer(question_id, answer_text)

if __name__ == '__main__':
    main()
