from django.shortcuts import render
from django.http import JsonResponse
import os
from pathlib import Path
from dotenv import load_dotenv
import openai
from openai import OpenAI


#1. 키 가져오기
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
load_dotenv(BASE_DIR / '.env')
api_key = os.getenv('open_ai_key')

client = OpenAI(api_key=api_key)

# 여행지 3곳의 소개글 (직접 전달 내용)
text = {
    "경주": "신라 천년의 수도로, 불국사와 석굴암, 첨성대, 대릉원 등 역사 유적이 도시 곳곳에 있는 곳이에요.",
    "내장산": "전북 정읍에 있는 국립공원으로, 우리나라 대표 단풍 명소예요. 내장사와 우화정, 케이블카가 유명해요.",
    "설악산": "강원도의 대표 국립공원으로 울산바위, 권금성, 비선대 계곡과 가을 단풍이 유명해요.",
}


def ajax_data(request):
    #html에서 들어온 입력데이터
    txt_input = request.POST.get('data', '').strip()
    print('입력데이터 : ', txt_input)

    #여행지 확인
    if txt_input not in text:
        context = {
            'intro': '경주, 내장산, 설악산 중에서 입력해 주세요.',
            'result': '',
        }
        return JsonResponse(context)

    #소개글
    intro = text[txt_input]

    #2. gpt 코스 요청
    result = ''
    try:
        response = client.responses.create(
            model='gpt-5.6',
            instructions=(
                "당신은 여행설계 전문가 입니다."
                "여행 일정을 1박2일 코스를 설계해 주세요."
                "[버스여행]으로 알려주세요."
                "여행자가 이해하기 쉽게 간략하게 답합니다."
                "[여행일정], [여행지], [숙소], [식사추천]으로 해주세요."
                "#, * 같은 마크다운 기호는 쓰지 않습니다."
            ),
            input=f'{txt_input}를 가지고 [1박2일 코스] - 버스여행, 여행지,숙소,식사 등을 제안해 주세요.',
            max_output_tokens=1000,
        )
        result = response.output_text.strip()
    except openai.APIConnectionError as error:
        print(f"인터넷연결,방화벽 문제 등 확인요망 :{error}")
        result = '인터넷연결,방화벽 문제 등 확인요망'hn
    except openai.RateLimitError as error:
        print(f"요청량 또는 프로젝트 사용한도 확인 :{error}")
        result = '요청량 또는 프로젝트 사용한도 확인'
    except openai.APIError as error:
        print(f"인증,권한 등 api 오류 확인 :{error}")
        result = '인증,권한 등 api 오류 확인'
    print(f'[{txt_input} 여행정보]')
    print(result)

    # 파일전달
    context = {
        'intro': intro,     #소개글
        'result': result,   #gpt 여행코스
    }
    return JsonResponse(context)


def tour(request):
    return render(request, 'tour.html')