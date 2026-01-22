{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "16ea20da",
   "metadata": {},
   "outputs": [],
   "source": [
    "import bs4\n",
    "import requests\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "3bb852ea",
   "metadata": {},
   "outputs": [],
   "source": [
    "url = \"https://www.smu.ac.kr/kor/life/notice.do?srCampus=smu\"\n",
    "html = requests.get(url).text\n",
    "soup = bs4.BeautifulSoup(html, 'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "1f484a64",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "상명[학사]\n",
      "[교무처] 증명발급 서비스 일시 중단 안내\n",
      "서울[등록/장학]\n",
      "[학생복지팀] 26-1 면학장학금 신청 안내\n",
      "서울[등록/장학]\n",
      "[학생복지팀] 26-1학과수석, 학과차석, 다전공우수 장학금 선발 안내\n",
      "서울[일반]\n",
      "[교육혁신추진팀] 두레장학생(조교)채용 안내\n",
      "서울[일반]\n",
      "WIDEEP교육혁신원(교수학습혁신센터) 두레장학생 채용 공고\n",
      "상명[진로취업]\n",
      "[취업진로지원팀] 2026년도 전국 지역인재 7급 수습직원 선발시험 공고\n",
      "상명[학사]\n",
      "[HUSS 사회구조 컨소시엄] 공동체혁신융합전공 2026학년도 제1학기 수강신청 및 학사일정 안내\n",
      "서울[진로취업]\n",
      "[취업진로지원팀] 2026학년도 잡(JOB)서포터즈 모집(기간 연장)\n",
      "상명[진로취업]\n",
      "[취업진로지원팀] 1월 4주차 주간 채용(인턴) 정보\n",
      "상명[학사]\n",
      "[교무처] 2026학년도 제1학기 대상 캠퍼스 간 복수전공 신청 안내\n",
      "서울[등록/장학]\n",
      "[학생복지팀] 25-2 디딤돌(국가II) 장학금 지급 안내\n",
      "서울[학사]\n",
      "[학사운영팀] 2026학년도 제1학기 학점교류 안내(서울) (상명→타대)\n",
      "상명[학사]\n",
      "바이오헬스 혁신융합대학 2026학년도 1학기 수강신청 및 학사일정 안내\n",
      "상명[학사]\n",
      "2026학년도 제1학기 대상 휴학·복학 신청 안내\n",
      "상명[진로취업]\n",
      "[취업진로지원팀] 온라인 취업지원서비스(잡플래닛, 에듀스, 코멘토) 이용 안내(콘텐츠 업데이트)\n",
      "상명[진로취업]\n",
      "[취업진로지원팀] 상명대 대학일자리플러스센터 및 졸업생특화프로그램 리플렛\n",
      "상명[글로벌]\n",
      "[SJC] 2026학년도 2학기 파견 교환학생 일부 대학 설명회 안내\n",
      "상명[학생생활]\n",
      "[정보통신지원팀] Adobe 상명대학교 재학생 공동구매 프로모션 안내\n",
      "서울[학사]\n",
      "[학사운영팀] 2026년 제1차 평생교육사 자격증 발급 신청 안내\n",
      "상명[일반]\n",
      "해외직구 전자기기 중고거래 유의사항 안내\n",
      "서울[학사]\n",
      "[학사운영팀] 2026학년도 제1학기 서울캠퍼스 수강신청 일정 안내\n",
      "서울[일반]\n",
      "대학교 내 장애인 보조견 동반출입 관련 안내\n",
      "서울[학사]\n",
      "2025학년도 제2학기 학사경고자 면담 및 프로그램 시행 안내\n",
      "서울[학생생활]\n",
      "[학생상담센터(서울)] 25-2 학사경고자를 위한 개인상담 및 심리검사 안내\n",
      "상명[진로취업]\n",
      "[취업진로지원팀] 1월 3주차 주간 채용(인턴) 정보\n",
      "상명[학사]\n",
      "[교무처] 2025-2학기 (2026-1학기 대상) 다(부)전공, 마이크로전공, 전과, 캠퍼스 간 전과 승인 결과 조회 방법 안내\n"
     ]
    }
   ],
   "source": [
    "css_selector = 'div.board-name-thumb.board-wrap li td a'\n",
    "\n",
    "for tag in soup.select(css_selector):\n",
    "    print(tag.get_text(strip=True))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "63b168fe",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['상명[학사]', '서울[등록/장학]', '서울[등록/장학]', '서울[일반]', '서울[일반]', '상명[진로취업]', '상명[학사]', '서울[진로취업]', '상명[진로취업]', '상명[학사]', '서울[등록/장학]', '서울[학사]', '상명[학사]', '상명[학사]', '상명[진로취업]', '상명[진로취업]', '상명[글로벌]', '상명[학생생활]', '서울[학사]', '상명[일반]', '서울[학사]', '서울[일반]', '서울[학사]', '서울[학생생활]', '상명[진로취업]', '상명[학사]']\n"
     ]
    }
   ],
   "source": [
    "css_selector = 'div.board-name-thumb.board-wrap td:nth-child(2) a'\n",
    "\n",
    "labels = []\n",
    "\n",
    "for tag in soup.select(css_selector):\n",
    "    labels.append(tag.get_text(strip=True))\n",
    "\n",
    "print(labels)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "ae4313e2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['[교무처] 증명발급 서비스 일시 중단 안내', '[학생복지팀] 26-1 면학장학금 신청 안내', '[학생복지팀] 26-1학과수석, 학과차석, 다전공우수 장학금 선발 안내', '[교육혁신추진팀] 두레장학생(조교)채용 안내', 'WIDEEP교육혁신원(교수학습혁신센터) 두레장학생 채용 공고', '[취업진로지원팀] 2026년도 전국 지역인재 7급 수습직원 선발시험 공고', '[HUSS 사회구조 컨소시엄] 공동체혁신융합전공 2026학년도 제1학기 수강신청 및 학사일정 안내', '[취업진로지원팀] 2026학년도 잡(JOB)서포터즈 모집(기간 연장)', '[취업진로지원팀] 1월 4주차 주간 채용(인턴) 정보', '[교무처] 2026학년도 제1학기 대상 캠퍼스 간 복수전공 신청 안내', '[학생복지팀] 25-2 디딤돌(국가II) 장학금 지급 안내', '[학사운영팀] 2026학년도 제1학기 학점교류 안내(서울) (상명→타대)', '바이오헬스 혁신융합대학 2026학년도 1학기 수강신청 및 학사일정 안내', '2026학년도 제1학기 대상 휴학·복학 신청 안내', '[취업진로지원팀] 온라인 취업지원서비스(잡플래닛, 에듀스, 코멘토) 이용 안내(콘텐츠 업데이트)', '[취업진로지원팀] 상명대 대학일자리플러스센터 및 졸업생특화프로그램 리플렛', '[SJC] 2026학년도 2학기 파견 교환학생 일부 대학 설명회 안내', '[정보통신지원팀] Adobe 상명대학교 재학생 공동구매 프로모션 안내', '[학사운영팀] 2026년 제1차 평생교육사 자격증 발급 신청 안내', '해외직구 전자기기 중고거래 유의사항 안내', '[학사운영팀] 2026학년도 제1학기 서울캠퍼스 수강신청 일정 안내', '대학교 내 장애인 보조견 동반출입 관련 안내', '2025학년도 제2학기 학사경고자 면담 및 프로그램 시행 안내', '[학생상담센터(서울)] 25-2 학사경고자를 위한 개인상담 및 심리검사 안내', '[취업진로지원팀] 1월 3주차 주간 채용(인턴) 정보', '[교무처] 2025-2학기 (2026-1학기 대상) 다(부)전공, 마이크로전공, 전과, 캠퍼스 간 전과 승인 결과 조회 방법 안내']\n"
     ]
    }
   ],
   "source": [
    "css_selector = 'div.board-name-thumb.board-wrap td:nth-child(3) a'\n",
    "\n",
    "titles = []\n",
    "\n",
    "for tag in soup.select(css_selector):\n",
    "    titles.append(tag.get_text(strip=True))\n",
    "\n",
    "print(titles)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "e5997c58",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['2026-01-22', '2026-01-21', '2026-01-21', '2026-01-20', '2026-01-20', '2026-01-20', '2026-01-16', '2026-01-16', '2026-01-15', '2026-01-13', '2026-01-13', '2026-01-13', '2026-01-13', '2025-12-18', '2025-09-03', '2025-09-01', '2026-01-22', '2026-01-21', '2026-01-15', '2026-01-14', '2026-01-13', '2026-01-09', '2026-01-09', '2026-01-09', '2026-01-09', '2026-01-08']\n"
     ]
    }
   ],
   "source": [
    "css_selector = 'div.board-name-thumb.board-wrap li.board-thumb-content-date'\n",
    "\n",
    "dates = []\n",
    "\n",
    "for tag in soup.select(css_selector):\n",
    "    date_raw = tag.get_text(strip=True)\n",
    "    date = date_raw.replace('작성일', '')\n",
    "    dates.append(date)\n",
    "\n",
    "print(dates)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "dfa48b91",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.DataFrame({\n",
    "    \"date\": dates\n",
    "})\n",
    "\n",
    "df[\"date\"] = pd.to_datetime(df[\"date\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "be56b27c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['https://www.smu.ac.kr/kor/life/notice.do?mode=view&articleNo=762476&srCampus=smu&article.offset=0&articleLimit=10', 'https://www.smu.ac.kr/kor/life/notice.do?mode=view&articleNo=762440&srCampus=smu&article.offset=0&articleLimit=10', 'https://www.smu.ac.kr/kor/life/notice.do?mode=view&articleNo=762423&srCampus=smu&article.offset=0&articleLimit=10', 'https://www.smu.ac.kr/kor/life/notice.do?mode=view&articleNo=762416&srCampus=smu&article.offset=0&articleLimit=10', 'https://www.smu.ac.kr/kor/life/notice.do?mode=view&articleNo=762415&srCampus=smu&article.offset=0&articleLimit=10', 'https://www.smu.ac.kr/kor/life/notice.do?mode=view&articleNo=762409&srCampus=smu&article.offset=0&articleLimit=10', 'https://www.smu.ac.kr/kor/life/notice.do?mode=view&articleNo=762367&srCampus=smu&article.offset=0&articleLimit=10', 'https://www.smu.ac.kr/kor/life/notice.do?mode=view&articleNo=762364&srCampus=smu&article.offset=0&articleLimit=10', 'https://www.smu.ac.kr/kor/life/notice.do?mode=view&articleNo=762336&srCampus=smu&article.offset=0&articleLimit=10', 'https://www.smu.ac.kr/kor/life/notice.do?mode=view&articleNo=762237&srCampus=smu&article.offset=0&articleLimit=10', 'https://www.smu.ac.kr/kor/life/notice.do?mode=view&articleNo=762236&srCampus=smu&article.offset=0&articleLimit=10', 'https://www.smu.ac.kr/kor/life/notice.do?mode=view&articleNo=762234&srCampus=smu&article.offset=0&articleLimit=10', 'https://www.smu.ac.kr/kor/life/notice.do?mode=view&articleNo=762233&srCampus=smu&article.offset=0&articleLimit=10', 'https://www.smu.ac.kr/kor/life/notice.do?mode=view&articleNo=761872&srCampus=smu&article.offset=0&articleLimit=10', 'https://www.smu.ac.kr/kor/life/notice.do?mode=view&articleNo=759176&srCampus=smu&article.offset=0&articleLimit=10', 'https://www.smu.ac.kr/kor/life/notice.do?mode=view&articleNo=758963&srCampus=smu&article.offset=0&articleLimit=10', 'https://www.smu.ac.kr/kor/life/notice.do?mode=view&articleNo=762465&srCampus=smu&article.offset=0&articleLimit=10', 'https://www.smu.ac.kr/kor/life/notice.do?mode=view&articleNo=762454&srCampus=smu&article.offset=0&articleLimit=10', 'https://www.smu.ac.kr/kor/life/notice.do?mode=view&articleNo=762330&srCampus=smu&article.offset=0&articleLimit=10', 'https://www.smu.ac.kr/kor/life/notice.do?mode=view&articleNo=762314&srCampus=smu&article.offset=0&articleLimit=10', 'https://www.smu.ac.kr/kor/life/notice.do?mode=view&articleNo=762244&srCampus=smu&article.offset=0&articleLimit=10', 'https://www.smu.ac.kr/kor/life/notice.do?mode=view&articleNo=762193&srCampus=smu&article.offset=0&articleLimit=10', 'https://www.smu.ac.kr/kor/life/notice.do?mode=view&articleNo=762189&srCampus=smu&article.offset=0&articleLimit=10', 'https://www.smu.ac.kr/kor/life/notice.do?mode=view&articleNo=762183&srCampus=smu&article.offset=0&articleLimit=10', 'https://www.smu.ac.kr/kor/life/notice.do?mode=view&articleNo=762177&srCampus=smu&article.offset=0&articleLimit=10', 'https://www.smu.ac.kr/kor/life/notice.do?mode=view&articleNo=762166&srCampus=smu&article.offset=0&articleLimit=10']\n"
     ]
    }
   ],
   "source": [
    "base_url = \"https://www.smu.ac.kr/kor/life/notice.do\"\n",
    "css_selector = 'div.board-name-thumb.board-wrap td:nth-child(3) a'\n",
    "\n",
    "links = []\n",
    "\n",
    "for tag in soup.select(css_selector):\n",
    "    href = tag.get('href')\n",
    "    full_url = base_url + href\n",
    "    links.append(full_url)\n",
    "\n",
    "print(links)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "1ec72054",
   "metadata": {
    "vscode": {
     "languageId": "javascript"
    }
   },
   "outputs": [],
   "source": [
    "data = list(zip(labels,titles,dates,links))\n",
    "data = pd.DataFrame(data=data,columns=['labels','titles','date','links'])"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.14.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
