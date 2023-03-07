import sys
# caution: path[0] is reserved for script path (or '' in REPL)
sys.path.insert(1, 'your path')
import keys 
!{sys.executable} -m pip install openai
import openai
openai.api_key = keys.get_openai_key()
# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
import openai

question = input()

print(question)
output = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "user", "content":question},
    ]
)
print(output)
