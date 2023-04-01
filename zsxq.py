import requests

group_id = '15552545558282'
cookie = 'sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2248281551825888%22%2C%22first_id%22%3A%221870c143c6f10b3-0552622f9e3c428-26031951-2073600-1870c143c7011d2%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTg3MGMxNDNjNmYxMGIzLTA1NTI2MjJmOWUzYzQyOC0yNjAzMTk1MS0yMDczNjAwLTE4NzBjMTQzYzcwMTFkMiIsIiRpZGVudGl0eV9sb2dpbl9pZCI6IjQ4MjgxNTUxODI1ODg4In0%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%2248281551825888%22%7D%2C%22%24device_id%22%3A%221870c143c6f10b3-0552622f9e3c428-26031951-2073600-1870c143c7011d2%22%7D; UM_distinctid=1870c33fe3f7e9-0ba29ad83f5afa-26031951-1fa400-1870c33fe4046c; zsxqsessionid=0261a538542d9b12990ae4dc485b0b3b; zsxq_access_token=DE1BF64E-CC81-DFC4-C555-631028EBF90F_445E47E846A1FE31; __cuid=434a40f4f7174764a09ceb194738df9b; amp_fef1e8=9e1a1bab-4e47-40cf-8231-66ae67f31201R...1gssadlrs.1gssafbqb.n.1.o; abtest_env=beta'

# 访问知识星球API，获取问题列表
def get_questions():
    questions_url = f"https://api.zsxq.com/v2/groups/{group_id}/topics?scope=unanswered_questions&count=20"
    response = requests.get(questions_url, headers={"cookie": f"{cookie}"})
    if response.status_code == 200:
        questions_data = response.json()["resp_data"]["topics"]
        return questions_data
    else:
        print("Unable to get questions data.")
        return []

# 使用ChatGPT API，回答问题
def get_answer(question):
    chatgpt_api = "https://api.openai.com/v1/engines/davinci-codex/completions"
    prompt = f"Q: {question}\nA:"
    response = requests.post(chatgpt_api, headers={
        "Authorization": "Bearer YOUR_API_KEY_HERE",
        "Content-Type": "application/json"
    }, json={
        "prompt": prompt,
        "temperature": 0.7,
        "max_tokens": 1024
    })
    if response.status_code == 200:
        answer = response.json()["choices"][0]["text"]
        return answer
    else:
        print("Unable to get answer.")
        return ""

# 访问知识星球API，回答问题
def post_answer(access_token, question_id, answer):
    post_answer_url = f"https://api.zsxq.com/v2/topics/{question_id}/comments"
    response = requests.post(post_answer_url, headers={"Authorization": f"Bearer {access_token}"}, json={
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
        exit()

        # 发布答案
        post_answer(access_token, question_id, answer_text)

if __name__ == '__main__':
    main()
