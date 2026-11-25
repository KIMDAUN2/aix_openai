import os
from pathlib import Path
from dotenv import load_dotenv
import openai
from openai import OpenAI

# 경제전문가입니다.
# 2027년도 주식시세가 어떻게 될지 알려주는 알려주는 프로그램을 구현하시오.
# 반도체주, 전력시설주, 우주항공주 
BASE_DIR= Path(__file__).resolve().parent.parent
envFile = BASE_DIR/'.env'
print(BASE_DIR)
print(envFile)
load_dotenv(envFile)
api_key = os.getenv('open_ai_key')

while True:
    txt_input = input('2027년 주식시세 보고싶은 종목을 입력하세요.>>> ')
    if txt_input:break
    print('입력하셔야 검색이 가능합니다.')
    print()

print('완료')

client = OpenAI(api_key=api_key)

try:
    response = client.responses.create(
        model ='gpt-5.6',
        instructions=(
            "당신은 주식 분석가 입니다."
            "2027년도 주식종목을 기반으로 전망를 알려주세요."
            "섹터, 성장요인,위험요인,대표종목으로 해주세요"
        ),
        input = f'{txt_input}을 가지고 [2027년도 종목별 주식시세] 제안',
        max_output_tokens=500,
    )
except openai.APIConnectionError as error:
    print(f"인터넷연결,봥화벽 문제 등 확인요망 :{error}")
except openai.RateLimitError as error:
    print(f"요청량 또는 프로젝트 사용한도 확인 :{error}")
except openai.APIError as error:
    print(f"인증,권한 등 api 오류 확인 :{error}")

result = response.output_text.strip()
if not result:
    raise RuntimeError('응답결과 내용이 없습니다.')
print('f[{txt_input} 2027년 종목별 주식시세]')
print(result)