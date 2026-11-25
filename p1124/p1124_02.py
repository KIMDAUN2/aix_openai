import os
from dotenv import load_dotenv
import openai
from openai import OpenAI

# 파일 불러오기
load_dotenv()
api_key = os.getenv('open_ai_key')
# print("확인 : ",api_key)

# 외부연결이기에 try-except
client = OpenAI(api_key=api_key)
# message1 = input('챗gpt검색을 시작합니다. 검색할 내용을 입력하세요.>>>')
try:
    # 챗gpt 연결
    response = client.responses.create(
        model = 'gpt-5.6',                                   # 사용할 모델
        instructions = "한국어로 친절하게 간결하게 답해줘요.",    # 지시사항,규칙
        #input = message1                                    # 전달메세지
        input = 'api 연결확인 환영문자를 짧게 작성해 주세요.'
    )
except openai.APIConnectionError as error :
    print(f'api 연결에러 : {error}')
except openai.RateLimitError as error :
    print(f'api 요청한도에러 : {error}')
except openai.APIError as error:
    print(f'api 요청실패 : {error}')

result = response.output_text.strip()
if not result:
    raise RuntimeError('api 응답에 표시할 텍스트가 없습니다.')
print('-'*40)
print(response)
print('-'*40)
print('[응답]',result)


# 응답내용
# Response(
# id='resp_0350c3303817591c006b04f0e18ef487d0b0c11a4c06c4c7ca', access_programs=None, 
# created_at=1795485922.0, 
# error=None, 
# incomplete_details=None, 
# instructions='한국어로 친절하게 간결하게 답해줘요.', metadata={}, model='gpt-5.6-sol',
#  object='response',
# output=[ResponseOutputMessage(id='msg0350c3303817591c006b04f0e2fec087d0b9d6440e345c8ea6', 
# content=[ResponseOutputText(annotations=[],
#  text='API 연결이 확인되었습니다. 환영합니다!',
#  type='output_text',
#  logprobs=[])],
#  role='assistant',
#  status='completed'
# , type='message', 
# phase='final_answer')],
#  parallel_tool_calls=True,
#  temperature=1.0,
#  tool_choice='auto',
#  tools=[], top_p=0.98,
#  background=False,
#  completed_at=1795485923.0, conversation=None, image=Image(context_compression='disabled'),
#  input_transformations=[],
#  max_output_tokens=None,
#  max_tool_calls=None, moderation=None,
#  previous_response_id=None, prompt=None,
#  prompt_cache_diagnostics=None, prompt_cache_key=None, prompt_cache_options=None,
#  prompt_cache_retention='24h',
#  reasoning=Reasoning(context='all_turns', effort='medium',  generate_summary=None,
#  mode='standard', summary=None),
#  safety_identifier=None,
#  service_tier='default',
#  status='completed', text=ResponseTextConfig(format=ResponseFormatText(type='text'), verbosity='medium'),  tool_usage=ToolUsage(image_gen=ToolUsageImageGen(input_tokens=0,  input_tokens_details=ToolUsageImageGenInputTokensDetails(image_tokens=0, text_tokens=0), 
# output_tokens=0,
#  total_tokens=0, 
# cached_tokens=None,
# cached_tokens_details=None, output_tokens_details=ToolUsageImageGenOutputTokensDetails(image_tokens=0,  text_tokens=0)), 
#  web_search=ToolUsageWebSearch(num_requests=0)),
#  top_logprobs=0,
#  truncation='disabled',
#  usage=ResponseUsage(input_tokens=39, input_tokens_details=InputTokensDetails(cache_write_tokens=0, cached_tokens=0, cache_write_tokens_details=InputTokensDetailsCacheWriteTokensDetails(ttl_ 12h_tokens=0, ttl_30m_tokens=0)),
#  output_tokens=14,    output_tokens_details=OutputTokensDetails(reasoning_tokens=0),
#  total_tokens=53), 
#  user=None, billing={'payer': 'developer'},
#  frequency_penalty=0.0,
#  presence_penalty=0.0,
#  store=True)