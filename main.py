{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "16ea20da",
   "metadata": {},
   "outputs": [],
   "source": [
    "import bs4\n",
    "import requests"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
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
   "execution_count": 60,
   "id": "1f484a64",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "상명[학사]\n",
      "[교무처] 2025-2학기 (2026-1학기 대상) 다(부)전공, 마이크로전공, 전과, 캠퍼스 간 전과 승인 결과 조회 방법 안내\n",
      "서울[진로취업]\n",
      "[현장실습·일경험지원팀(서울)] 2026학년도 1학기 현장실습학기제 참여자 모집 안내\n",
      "상명[학사]\n",
      "바이오헬스 혁신융합대학 2025학년도 동계 계절학기 성적공시 안내\n",
      "상명[비교과]\n",
      "[의사소통능력개발센터(서울)] 2025학년도 동계방학 독서특강 안내\n",
      "서울[학생생활]\n",
      "[창업지원센터] 창업 공간 이용 안내\n",
      "상명[진로취업]\n",
      "[현장실습·일경험지원센터] 2026년 서울영커리언스 인턴십(봄학기) 참여자 모집 안내\n",
      "서울[사회봉사]\n",
      "[상명소셜임팩트센터] 2026 서울런 멘토단 모집 안내\n",
      "서울[사회봉사]\n",
      "[상명사회봉사단] 서울디지털동행플라자 방문자 대상 입장 및 태블릿, 로봇커피 등 기기 이용 안내 모집\n",
      "서울[비교과]\n",
      "[의사소통능력개발센터(서울)] 2025학년도 2학기 에세이경진대회 수상자 발표\n",
      "상명[진로취업]\n",
      "[취업진로지원팀] 1월 2주차 주간 채용(인턴) 정보\n",
      "서울[사회봉사]\n",
      "[상명사회봉사단] 지역사회 아동복지 서비스를 위한 멘토링 봉사활동 모집 안내\n",
      "서울[진로취업]\n",
      "[취업진로지원팀] 2026학년도 잡(JOB)서포터즈 모집\n",
      "상명[진로취업]\n",
      "[상명대학교 국제개발평가센터(천안)] KOICA 2026년 상반기 ODA YP(Young Professional) 채용 공고(접수: 2025.12.29~2026.1.6)\n",
      "상명[진로취업]\n",
      "[취업진로지원팀] 온라인 취업지원서비스(잡플래닛, 에듀스, 코멘토) 이용 안내(콘텐츠 업데이트)\n",
      "상명[진로취업]\n",
      "[취업진로지원팀] 상명대 대학일자리플러스센터 및 졸업생특화프로그램 리플렛\n",
      "서울[등록/장학]\n",
      "2026년 1학기 농촌출신대학(원)생 학자금대출(무이자) 지원 안내\n",
      "서울[등록/장학]\n",
      "2026년 상반기 울산광역시 대학(원)생 학자금대출 이자지원사업 안내\n",
      "서울[일반]\n",
      "[상명대학교박물관] 두레장학생(조교) 채용 안내\n",
      "서울[일반]\n",
      "[상명대학교박물관] 교육조교 채용 안내\n",
      "서울[등록/장학]\n",
      "2026학년도 1학기 학자금 대출 안내\n",
      "상명[일반]\n",
      "[천안캠퍼스] 상명대학교 창업지원센터(창업보육팀) 입주기업 모집\n",
      "상명[글로벌]\n",
      "[국립국제교육원] 2026년 브루나이 정부초청(BDGS) 장학생 선발 안내\n",
      "서울[비교과]\n",
      "[교수학습혁신센터(서울)] 2025학년도 학생 디지털 역량강화 교육_2차 특강\n",
      "상명[일반]\n",
      "2026년 수뭉이 새해 인사말 카드 이미지 2종 안내\n",
      "상명[진로취업]\n",
      "[창업지원센터] 한경대_2026년 제5회 장애/비장애 대학생 창업경진대회\n"
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
   "execution_count": 61,
   "id": "63b168fe",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['상명[학사]', '서울[진로취업]', '상명[학사]', '상명[비교과]', '서울[학생생활]', '상명[진로취업]', '서울[사회봉사]', '서울[사회봉사]', '서울[비교과]', '상명[진로취업]', '서울[사회봉사]', '서울[진로취업]', '상명[진로취업]', '상명[진로취업]', '상명[진로취업]', '서울[등록/장학]', '서울[등록/장학]', '서울[일반]', '서울[일반]', '서울[등록/장학]', '상명[일반]', '상명[글로벌]', '서울[비교과]', '상명[일반]', '상명[진로취업]']\n"
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
   "execution_count": 62,
   "id": "ae4313e2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['[교무처] 2025-2학기 (2026-1학기 대상) 다(부)전공, 마이크로전공, 전과, 캠퍼스 간 전과 승인 결과 조회 방법 안내', '[현장실습·일경험지원팀(서울)] 2026학년도 1학기 현장실습학기제 참여자 모집 안내', '바이오헬스 혁신융합대학 2025학년도 동계 계절학기 성적공시 안내', '[의사소통능력개발센터(서울)] 2025학년도 동계방학 독서특강 안내', '[창업지원센터] 창업 공간 이용 안내', '[현장실습·일경험지원센터] 2026년 서울영커리언스 인턴십(봄학기) 참여자 모집 안내', '[상명소셜임팩트센터] 2026 서울런 멘토단 모집 안내', '[상명사회봉사단] 서울디지털동행플라자 방문자 대상 입장 및 태블릿, 로봇커피 등 기기 이용 안내 모집', '[의사소통능력개발센터(서울)] 2025학년도 2학기 에세이경진대회 수상자 발표', '[취업진로지원팀] 1월 2주차 주간 채용(인턴) 정보', '[상명사회봉사단] 지역사회 아동복지 서비스를 위한 멘토링 봉사활동 모집 안내', '[취업진로지원팀] 2026학년도 잡(JOB)서포터즈 모집', '[상명대학교 국제개발평가센터(천안)] KOICA 2026년 상반기 ODA YP(Young Professional) 채용 공고(접수: 2025.12.29~2026.1.6)', '[취업진로지원팀] 온라인 취업지원서비스(잡플래닛, 에듀스, 코멘토) 이용 안내(콘텐츠 업데이트)', '[취업진로지원팀] 상명대 대학일자리플러스센터 및 졸업생특화프로그램 리플렛', '2026년 1학기 농촌출신대학(원)생 학자금대출(무이자) 지원 안내', '2026년 상반기 울산광역시 대학(원)생 학자금대출 이자지원사업 안내', '[상명대학교박물관] 두레장학생(조교) 채용 안내', '[상명대학교박물관] 교육조교 채용 안내', '2026학년도 1학기 학자금 대출 안내', '[천안캠퍼스] 상명대학교 창업지원센터(창업보육팀) 입주기업 모집', '[국립국제교육원] 2026년 브루나이 정부초청(BDGS) 장학생 선발 안내', '[교수학습혁신센터(서울)] 2025학년도 학생 디지털 역량강화 교육_2차 특강', '2026년 수뭉이 새해 인사말 카드 이미지 2종 안내', '[창업지원센터] 한경대_2026년 제5회 장애/비장애 대학생 창업경진대회']\n"
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
   "execution_count": 57,
   "id": "e5997c58",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['작성일2026-01-08', '작성일2026-01-08', '작성일2026-01-08', '작성일2026-01-07', '작성일2026-01-06', '작성일2026-01-06', '작성일2026-01-06', '작성일2026-01-05', '작성일2025-12-31', '작성일2025-12-31', '작성일2025-12-29', '작성일2025-12-29', '작성일2025-12-18', '작성일2025-09-03', '작성일2025-09-01', '작성일2026-01-08', '작성일2026-01-08', '작성일2026-01-06', '작성일2026-01-06', '작성일2026-01-06', '작성일2026-01-05', '작성일2026-01-05', '작성일2026-01-02', '작성일2025-12-31', '작성일2025-12-29']\n"
     ]
    }
   ],
   "source": [
    "css_selector = 'div.board-name-thumb.board-wrap li.board-thumb-content-date'\n",
    "\n",
    "dates = []\n",
    "\n",
    "for tag in soup.select(css_selector):\n",
    "    dates.append(tag.get_text(strip=True))\n",
    "\n",
    "print(dates)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "id": "be56b27c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['https://www.smu.ac.kr/kor/life/notice.do?mode=view&articleNo=762166&srCampus=smu&article.offset=0&articleLimit=10', 'https://www.smu.ac.kr/kor/life/notice.do?mode=view&articleNo=762164&srCampus=smu&article.offset=0&articleLimit=10', 'https://www.smu.ac.kr/kor/life/notice.do?mode=view&articleNo=762158&srCampus=smu&article.offset=0&articleLimit=10', 'https://www.smu.ac.kr/kor/life/notice.do?mode=view&articleNo=762150&srCampus=smu&article.offset=0&articleLimit=10', 'https://www.smu.ac.kr/kor/life/notice.do?mode=view&articleNo=762138&srCampus=smu&article.offset=0&articleLimit=10', 'https://www.smu.ac.kr/kor/life/notice.do?mode=view&articleNo=762131&srCampus=smu&article.offset=0&articleLimit=10', 'https://www.smu.ac.kr/kor/life/notice.do?mode=view&articleNo=762125&srCampus=smu&article.offset=0&articleLimit=10', 'https://www.smu.ac.kr/kor/life/notice.do?mode=view&articleNo=762111&srCampus=smu&article.offset=0&articleLimit=10', 'https://www.smu.ac.kr/kor/life/notice.do?mode=view&articleNo=762075&srCampus=smu&article.offset=0&articleLimit=10', 'https://www.smu.ac.kr/kor/life/notice.do?mode=view&articleNo=762071&srCampus=smu&article.offset=0&articleLimit=10', 'https://www.smu.ac.kr/kor/life/notice.do?mode=view&articleNo=762022&srCampus=smu&article.offset=0&articleLimit=10', 'https://www.smu.ac.kr/kor/life/notice.do?mode=view&articleNo=762016&srCampus=smu&article.offset=0&articleLimit=10', 'https://www.smu.ac.kr/kor/life/notice.do?mode=view&articleNo=761866&srCampus=smu&article.offset=0&articleLimit=10', 'https://www.smu.ac.kr/kor/life/notice.do?mode=view&articleNo=759176&srCampus=smu&article.offset=0&articleLimit=10', 'https://www.smu.ac.kr/kor/life/notice.do?mode=view&articleNo=758963&srCampus=smu&article.offset=0&articleLimit=10', 'https://www.smu.ac.kr/kor/life/notice.do?mode=view&articleNo=762159&srCampus=smu&article.offset=0&articleLimit=10', 'https://www.smu.ac.kr/kor/life/notice.do?mode=view&articleNo=762156&srCampus=smu&article.offset=0&articleLimit=10', 'https://www.smu.ac.kr/kor/life/notice.do?mode=view&articleNo=762135&srCampus=smu&article.offset=0&articleLimit=10', 'https://www.smu.ac.kr/kor/life/notice.do?mode=view&articleNo=762134&srCampus=smu&article.offset=0&articleLimit=10', 'https://www.smu.ac.kr/kor/life/notice.do?mode=view&articleNo=762123&srCampus=smu&article.offset=0&articleLimit=10', 'https://www.smu.ac.kr/kor/life/notice.do?mode=view&articleNo=762116&srCampus=smu&article.offset=0&articleLimit=10', 'https://www.smu.ac.kr/kor/life/notice.do?mode=view&articleNo=762112&srCampus=smu&article.offset=0&articleLimit=10', 'https://www.smu.ac.kr/kor/life/notice.do?mode=view&articleNo=762096&srCampus=smu&article.offset=0&articleLimit=10', 'https://www.smu.ac.kr/kor/life/notice.do?mode=view&articleNo=762080&srCampus=smu&article.offset=0&articleLimit=10', 'https://www.smu.ac.kr/kor/life/notice.do?mode=view&articleNo=762019&srCampus=smu&article.offset=0&articleLimit=10']\n"
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
   "execution_count": 70,
   "id": "1ec72054",
   "metadata": {
    "vscode": {
     "languageId": "javascript"
    }
   },
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "\n",
    "data = list(zip(labels,titles,dates,links))\n",
    "data = pd.DataFrame(data=data,columns=['labels','titles','dates','links'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c4d8770a",
   "metadata": {
    "vscode": {
     "languageId": "javascript"
    }
   },
   "outputs": [
    {
     "ename": "PermissionError",
     "evalue": "[Errno 13] Permission denied: 'C:\\\\Users\\\\jaena\\\\OneDrive\\\\Desktop\\\\data.csv'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mPermissionError\u001b[39m                           Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[74]\u001b[39m\u001b[32m, line 1\u001b[39m\n\u001b[32m----> \u001b[39m\u001b[32m1\u001b[39m \u001b[43mdata\u001b[49m\u001b[43m.\u001b[49m\u001b[43mto_csv\u001b[49m\u001b[43m(\u001b[49m\u001b[33;43m\"\u001b[39;49m\u001b[33;43mC:\u001b[39;49m\u001b[38;5;130;43;01m\\\\\u001b[39;49;00m\u001b[33;43mUsers\u001b[39;49m\u001b[38;5;130;43;01m\\\\\u001b[39;49;00m\u001b[33;43mjaena\u001b[39;49m\u001b[38;5;130;43;01m\\\\\u001b[39;49;00m\u001b[33;43mOneDrive\u001b[39;49m\u001b[38;5;130;43;01m\\\\\u001b[39;49;00m\u001b[33;43mDesktop\u001b[39;49m\u001b[38;5;130;43;01m\\\\\u001b[39;49;00m\u001b[33;43mdata.csv\u001b[39;49m\u001b[33;43m\"\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mindex\u001b[49m\u001b[43m=\u001b[49m\u001b[38;5;28;43;01mFalse\u001b[39;49;00m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mencoding\u001b[49m\u001b[43m=\u001b[49m\u001b[33;43m\"\u001b[39;49m\u001b[33;43mutf-8-sig\u001b[39;49m\u001b[33;43m\"\u001b[39;49m\u001b[43m)\u001b[49m\n",
      "\u001b[36mFile \u001b[39m\u001b[32mc:\\Users\\jaena\\AppData\\Local\\Python\\pythoncore-3.14-64\\Lib\\site-packages\\pandas\\util\\_decorators.py:333\u001b[39m, in \u001b[36mdeprecate_nonkeyword_arguments.<locals>.decorate.<locals>.wrapper\u001b[39m\u001b[34m(*args, **kwargs)\u001b[39m\n\u001b[32m    327\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28mlen\u001b[39m(args) > num_allow_args:\n\u001b[32m    328\u001b[39m     warnings.warn(\n\u001b[32m    329\u001b[39m         msg.format(arguments=_format_argument_list(allow_args)),\n\u001b[32m    330\u001b[39m         \u001b[38;5;167;01mFutureWarning\u001b[39;00m,\n\u001b[32m    331\u001b[39m         stacklevel=find_stack_level(),\n\u001b[32m    332\u001b[39m     )\n\u001b[32m--> \u001b[39m\u001b[32m333\u001b[39m \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[43mfunc\u001b[49m\u001b[43m(\u001b[49m\u001b[43m*\u001b[49m\u001b[43margs\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43m*\u001b[49m\u001b[43m*\u001b[49m\u001b[43mkwargs\u001b[49m\u001b[43m)\u001b[49m\n",
      "\u001b[36mFile \u001b[39m\u001b[32mc:\\Users\\jaena\\AppData\\Local\\Python\\pythoncore-3.14-64\\Lib\\site-packages\\pandas\\core\\generic.py:3989\u001b[39m, in \u001b[36mNDFrame.to_csv\u001b[39m\u001b[34m(self, path_or_buf, sep, na_rep, float_format, columns, header, index, index_label, mode, encoding, compression, quoting, quotechar, lineterminator, chunksize, date_format, doublequote, escapechar, decimal, errors, storage_options)\u001b[39m\n\u001b[32m   3978\u001b[39m df = \u001b[38;5;28mself\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28misinstance\u001b[39m(\u001b[38;5;28mself\u001b[39m, ABCDataFrame) \u001b[38;5;28;01melse\u001b[39;00m \u001b[38;5;28mself\u001b[39m.to_frame()\n\u001b[32m   3980\u001b[39m formatter = DataFrameFormatter(\n\u001b[32m   3981\u001b[39m     frame=df,\n\u001b[32m   3982\u001b[39m     header=header,\n\u001b[32m   (...)\u001b[39m\u001b[32m   3986\u001b[39m     decimal=decimal,\n\u001b[32m   3987\u001b[39m )\n\u001b[32m-> \u001b[39m\u001b[32m3989\u001b[39m \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[43mDataFrameRenderer\u001b[49m\u001b[43m(\u001b[49m\u001b[43mformatter\u001b[49m\u001b[43m)\u001b[49m\u001b[43m.\u001b[49m\u001b[43mto_csv\u001b[49m\u001b[43m(\u001b[49m\n\u001b[32m   3990\u001b[39m \u001b[43m    \u001b[49m\u001b[43mpath_or_buf\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m   3991\u001b[39m \u001b[43m    \u001b[49m\u001b[43mlineterminator\u001b[49m\u001b[43m=\u001b[49m\u001b[43mlineterminator\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m   3992\u001b[39m \u001b[43m    \u001b[49m\u001b[43msep\u001b[49m\u001b[43m=\u001b[49m\u001b[43msep\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m   3993\u001b[39m \u001b[43m    \u001b[49m\u001b[43mencoding\u001b[49m\u001b[43m=\u001b[49m\u001b[43mencoding\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m   3994\u001b[39m \u001b[43m    \u001b[49m\u001b[43merrors\u001b[49m\u001b[43m=\u001b[49m\u001b[43merrors\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m   3995\u001b[39m \u001b[43m    \u001b[49m\u001b[43mcompression\u001b[49m\u001b[43m=\u001b[49m\u001b[43mcompression\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m   3996\u001b[39m \u001b[43m    \u001b[49m\u001b[43mquoting\u001b[49m\u001b[43m=\u001b[49m\u001b[43mquoting\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m   3997\u001b[39m \u001b[43m    \u001b[49m\u001b[43mcolumns\u001b[49m\u001b[43m=\u001b[49m\u001b[43mcolumns\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m   3998\u001b[39m \u001b[43m    \u001b[49m\u001b[43mindex_label\u001b[49m\u001b[43m=\u001b[49m\u001b[43mindex_label\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m   3999\u001b[39m \u001b[43m    \u001b[49m\u001b[43mmode\u001b[49m\u001b[43m=\u001b[49m\u001b[43mmode\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m   4000\u001b[39m \u001b[43m    \u001b[49m\u001b[43mchunksize\u001b[49m\u001b[43m=\u001b[49m\u001b[43mchunksize\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m   4001\u001b[39m \u001b[43m    \u001b[49m\u001b[43mquotechar\u001b[49m\u001b[43m=\u001b[49m\u001b[43mquotechar\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m   4002\u001b[39m \u001b[43m    \u001b[49m\u001b[43mdate_format\u001b[49m\u001b[43m=\u001b[49m\u001b[43mdate_format\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m   4003\u001b[39m \u001b[43m    \u001b[49m\u001b[43mdoublequote\u001b[49m\u001b[43m=\u001b[49m\u001b[43mdoublequote\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m   4004\u001b[39m \u001b[43m    \u001b[49m\u001b[43mescapechar\u001b[49m\u001b[43m=\u001b[49m\u001b[43mescapechar\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m   4005\u001b[39m \u001b[43m    \u001b[49m\u001b[43mstorage_options\u001b[49m\u001b[43m=\u001b[49m\u001b[43mstorage_options\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m   4006\u001b[39m \u001b[43m\u001b[49m\u001b[43m)\u001b[49m\n",
      "\u001b[36mFile \u001b[39m\u001b[32mc:\\Users\\jaena\\AppData\\Local\\Python\\pythoncore-3.14-64\\Lib\\site-packages\\pandas\\io\\formats\\format.py:1014\u001b[39m, in \u001b[36mDataFrameRenderer.to_csv\u001b[39m\u001b[34m(self, path_or_buf, encoding, sep, columns, index_label, mode, compression, quoting, quotechar, lineterminator, chunksize, date_format, doublequote, escapechar, errors, storage_options)\u001b[39m\n\u001b[32m    993\u001b[39m     created_buffer = \u001b[38;5;28;01mFalse\u001b[39;00m\n\u001b[32m    995\u001b[39m csv_formatter = CSVFormatter(\n\u001b[32m    996\u001b[39m     path_or_buf=path_or_buf,\n\u001b[32m    997\u001b[39m     lineterminator=lineterminator,\n\u001b[32m   (...)\u001b[39m\u001b[32m   1012\u001b[39m     formatter=\u001b[38;5;28mself\u001b[39m.fmt,\n\u001b[32m   1013\u001b[39m )\n\u001b[32m-> \u001b[39m\u001b[32m1014\u001b[39m \u001b[43mcsv_formatter\u001b[49m\u001b[43m.\u001b[49m\u001b[43msave\u001b[49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\n\u001b[32m   1016\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m created_buffer:\n\u001b[32m   1017\u001b[39m     \u001b[38;5;28;01massert\u001b[39;00m \u001b[38;5;28misinstance\u001b[39m(path_or_buf, StringIO)\n",
      "\u001b[36mFile \u001b[39m\u001b[32mc:\\Users\\jaena\\AppData\\Local\\Python\\pythoncore-3.14-64\\Lib\\site-packages\\pandas\\io\\formats\\csvs.py:251\u001b[39m, in \u001b[36mCSVFormatter.save\u001b[39m\u001b[34m(self)\u001b[39m\n\u001b[32m    247\u001b[39m \u001b[38;5;250m\u001b[39m\u001b[33;03m\"\"\"\u001b[39;00m\n\u001b[32m    248\u001b[39m \u001b[33;03mCreate the writer & save.\u001b[39;00m\n\u001b[32m    249\u001b[39m \u001b[33;03m\"\"\"\u001b[39;00m\n\u001b[32m    250\u001b[39m \u001b[38;5;66;03m# apply compression and byte/text conversion\u001b[39;00m\n\u001b[32m--> \u001b[39m\u001b[32m251\u001b[39m \u001b[38;5;28;01mwith\u001b[39;00m \u001b[43mget_handle\u001b[49m\u001b[43m(\u001b[49m\n\u001b[32m    252\u001b[39m \u001b[43m    \u001b[49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43mfilepath_or_buffer\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m    253\u001b[39m \u001b[43m    \u001b[49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43mmode\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m    254\u001b[39m \u001b[43m    \u001b[49m\u001b[43mencoding\u001b[49m\u001b[43m=\u001b[49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43mencoding\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m    255\u001b[39m \u001b[43m    \u001b[49m\u001b[43merrors\u001b[49m\u001b[43m=\u001b[49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43merrors\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m    256\u001b[39m \u001b[43m    \u001b[49m\u001b[43mcompression\u001b[49m\u001b[43m=\u001b[49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43mcompression\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m    257\u001b[39m \u001b[43m    \u001b[49m\u001b[43mstorage_options\u001b[49m\u001b[43m=\u001b[49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43mstorage_options\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m    258\u001b[39m \u001b[43m\u001b[49m\u001b[43m)\u001b[49m \u001b[38;5;28;01mas\u001b[39;00m handles:\n\u001b[32m    259\u001b[39m     \u001b[38;5;66;03m# Note: self.encoding is irrelevant here\u001b[39;00m\n\u001b[32m    260\u001b[39m     \u001b[38;5;28mself\u001b[39m.writer = csvlib.writer(\n\u001b[32m    261\u001b[39m         handles.handle,\n\u001b[32m    262\u001b[39m         lineterminator=\u001b[38;5;28mself\u001b[39m.lineterminator,\n\u001b[32m   (...)\u001b[39m\u001b[32m    267\u001b[39m         quotechar=\u001b[38;5;28mself\u001b[39m.quotechar,\n\u001b[32m    268\u001b[39m     )\n\u001b[32m    270\u001b[39m     \u001b[38;5;28mself\u001b[39m._save()\n",
      "\u001b[36mFile \u001b[39m\u001b[32mc:\\Users\\jaena\\AppData\\Local\\Python\\pythoncore-3.14-64\\Lib\\site-packages\\pandas\\io\\common.py:873\u001b[39m, in \u001b[36mget_handle\u001b[39m\u001b[34m(path_or_buf, mode, encoding, compression, memory_map, is_text, errors, storage_options)\u001b[39m\n\u001b[32m    868\u001b[39m \u001b[38;5;28;01melif\u001b[39;00m \u001b[38;5;28misinstance\u001b[39m(handle, \u001b[38;5;28mstr\u001b[39m):\n\u001b[32m    869\u001b[39m     \u001b[38;5;66;03m# Check whether the filename is to be opened in binary mode.\u001b[39;00m\n\u001b[32m    870\u001b[39m     \u001b[38;5;66;03m# Binary mode does not support 'encoding' and 'newline'.\u001b[39;00m\n\u001b[32m    871\u001b[39m     \u001b[38;5;28;01mif\u001b[39;00m ioargs.encoding \u001b[38;5;129;01mand\u001b[39;00m \u001b[33m\"\u001b[39m\u001b[33mb\u001b[39m\u001b[33m\"\u001b[39m \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;129;01min\u001b[39;00m ioargs.mode:\n\u001b[32m    872\u001b[39m         \u001b[38;5;66;03m# Encoding\u001b[39;00m\n\u001b[32m--> \u001b[39m\u001b[32m873\u001b[39m         handle = \u001b[38;5;28;43mopen\u001b[39;49m\u001b[43m(\u001b[49m\n\u001b[32m    874\u001b[39m \u001b[43m            \u001b[49m\u001b[43mhandle\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m    875\u001b[39m \u001b[43m            \u001b[49m\u001b[43mioargs\u001b[49m\u001b[43m.\u001b[49m\u001b[43mmode\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m    876\u001b[39m \u001b[43m            \u001b[49m\u001b[43mencoding\u001b[49m\u001b[43m=\u001b[49m\u001b[43mioargs\u001b[49m\u001b[43m.\u001b[49m\u001b[43mencoding\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m    877\u001b[39m \u001b[43m            \u001b[49m\u001b[43merrors\u001b[49m\u001b[43m=\u001b[49m\u001b[43merrors\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m    878\u001b[39m \u001b[43m            \u001b[49m\u001b[43mnewline\u001b[49m\u001b[43m=\u001b[49m\u001b[33;43m\"\u001b[39;49m\u001b[33;43m\"\u001b[39;49m\u001b[43m,\u001b[49m\n\u001b[32m    879\u001b[39m \u001b[43m        \u001b[49m\u001b[43m)\u001b[49m\n\u001b[32m    880\u001b[39m     \u001b[38;5;28;01melse\u001b[39;00m:\n\u001b[32m    881\u001b[39m         \u001b[38;5;66;03m# Binary mode\u001b[39;00m\n\u001b[32m    882\u001b[39m         handle = \u001b[38;5;28mopen\u001b[39m(handle, ioargs.mode)\n",
      "\u001b[31mPermissionError\u001b[39m: [Errno 13] Permission denied: 'C:\\\\Users\\\\jaena\\\\OneDrive\\\\Desktop\\\\data.csv'"
     ]
    }
   ],
   "source": [
    "data.to_csv(\"data.csv\", index=False, encoding=\"utf-8-sig\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "id": "dfa664fe",
   "metadata": {
    "vscode": {
     "languageId": "javascript"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "WindowsPath('C:/Users/jaena/AppData/Local/Programs/Microsoft VS Code')"
      ]
     },
     "execution_count": 73,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pathlib\n",
    "\n",
    "pathlib.Path().resolve()"
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
