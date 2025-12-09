---
이름: "[Contents] Search Engines and Information Retreival in Practice"
출생: 2019-03-24
언어교환:
  - blog
---

1. search engines and information retrieval
2. architecture of a serarch engine
3. crawls and feeds
4. processing text
5. ranking with indexes
6. queries and interfaces

검색엔진의 구조를 알아본 후에 크롤링과 피드들이 어떻게 텍스트를 가져오는지, 가져온 텍스트들을 어떻게 가공하는지

가공된 텍스트들을 보여주기 위한 순서 정하는 방법

1. search engines and information retrieval
2. architecture of a serarch engine
    1. what is an architecture?
    2. basic building blocks
    3. breaking it down
        1. text acquisition
        2. text transformation
        3. index creation
        4. user interaction
        5. ranking
        6. evaluation
    4. how does it really work?
3. crawls and feeds
    1. deciding what to search
    2. crawling the web
        1. retrieving web pages
        2. the web crawler
        3. freshness
        4. focused crawling
        5. deep web
        6. sitemaps
        7. distributed crawling
    3. crawling documents and email
    4. document feeds
    5. the conversion problem
        1. character encodings
    6. scoring the documents
        1. using a database system
        2. random access
        3. compression and large files
        4. update
        5. bigtable
    7. detecting duplicates
    8. removing noise
4. processing text
    1. from words to terms
    2. text statistics
    3. document parsing
    4. document structure and markup
    5. information extraction
    6. internationalization
5. ranking with indexes
    1. overview
    2. abstract model of ranking
    3. inverted indexes
    4. compression
    5. auxiliary structures
    6. index construction
    7. query processing
6. queries and interfaces
    1. information needs and queries
    2. query transformation and refinement
        1. stopping and stemming revisted
        2. spell checking and suggestions
        3. query expansion
        4. relevance feedback
        5. context and presonlization
    3. showing the results
        1. result pages and snippets
        2. advertising and search
        3. clustering the results
    4. cross-language search

* * *

중요 용어 정리

pearson상관계수

similarity

mutual information

soundex code

noisy channel

delta encoding, compression

v-Byte encoding

Zipf, corpus

crawler, freshness

utf-8

pull 기반 프로토콜, http request, server

precision

query, recall 1

uri, rul

dynamic document

hmm, loen melon이라는 문장으로부터 상품명과 회사명을 추출, 각 state에서 가능한 출력은 loen, melon뿐이며, 출력확률은 p(loen|product = 0.1, p(loen|company) = 0.8

십진수로 표현된 역리스트를 델타 인코딩한 후, v-byte encoding, 최종결과는 이진수로 표현

5개의 web pages: page1은 page2,3에 대한 링크 생성, page 2는 1,3에 대한 링크 생성...

위 링크 관계를 그래프로 표현

random jump 확률이 0.2일때 5개 웹 페이지들의 page rank값 계산 위한 equation

아래 두 문서를 **indexing**한 후의 cosine similarity 계산 (and는 stopword,  stemming은 안 함)

D1 = five thousand five hundred and fifty five dollars, D2 = fifty six thousand five hundred sixty five dollars

주어진 문서 모음이 상수 c=0.1인 지프 법칙 따른다 가정시 가장 빈번히 출현한 상위 3개 단어들을 모두 지우면 **문서 모음에서 총 용어 발생횟수는 몇 % 감소**?

총 100만개의 문서로 구성된 문서모음이 있을 때, 아래 정보 이용해 다음 질문에 답

- 문서모음에서 단어 A가진 문서 수는 40만
- A가진 문서 10만 개 중 3만개가 단어 B가짐
- 문서모음에서 랜덤하게 선택된 문서 20만개 살펴본 결과, 그 중 5만개의 문서가 단어 C를 가지고 있었음
- 단어 C 5만개 중 1만개가 B가짐

A,B 모두 가진 문서수, A,C 모두 가진 문서 수, A,B,C 모두 가진 문서 수

 

두 단어의 co-occurrence

단어의 idf값

browser

http, statelessness, scalability

dns, web sever, browser, ip

스퀴드 웹 프락시에서는 만료 시점 이전에 get요청 보낼 수 없다

javascript pg은 동적 문서

웹 프락시는 브라우저에 대해 서버 역할 수행

정보검색 시스템에서 연관문서, 100% 재현율과 정확률

unicode symbol number encoding 3byte

checksum이 같은 문서는 완전히 중복된 문서

gentlemand, gentelman의 damerau-levenshtein거리는 1

스템 클래스에 다이스 계수 적용 목적은 **하나의 스템 클래스에 속한 단어들의 수를 늘리기** 위해

 

총 100만개 문서 있을 때 a,b,c,d 모두 포함하는 문서 개수 추정

a,b,c가 문서에서 함께 발생할 확률 + a,b가 문서에 있을때 d가 문서에 있을 확률 0.5

문서모음이 c=0.1인 지프법칙 따를때 전체 단어 출현빈도의 14%이상 차지하는 단어들의 최소 개수?

a는 b,c page, b는 c, c는 b에 대한 링크 생성 -> graph

무작위 점프 확률이 0.1: web page a,b,c의 pagerank값?

1. 5개의 web page - 크롤러가 a 페이지부터 크롤링 시작한다 하고, 이미 크롤된 페이지는 다시 크롤하지 않으며, 하나의 페이지에 존재하는 링크들에 대한 크롤링 순서는 위에 열거된 순서 따를때

크롤러가 넓이 우선 탐색, 깊이 우선 탐색할 때 크롤되는 페이지의 순서?

주어진 웹 그래프에 있어서 넓이 우선 탐색 vs 깊이 우선 탐색이 효과적?

문서 모음 가정 D1, D2, D3 중 단어 등장 순서

hidden markov model

markov chain, hmm의 공통점과 차이점?

문서를 입력으로 받아서 키워드를 추출하는 2개 상태로 구성된 hmm설계

 

2012

dns 서버 지정시 서버의 도메인 이름을 사용해 지정

질의어들을 모두 포함하는 검색결과 집합 크기 추정시 질의더 단어 중 가장 드물게 등장하는 단어 이용해 추정하는 이유는 검토할 표본의 크기를 늘리기 위해

스테밍은 검색 결과 개수의 향상에 기여

스테밍은 역색인의 크기를 줄이는 데 기여

idf는 문서별로 각각 계산되어야 함

html문서 이외의 다른 형태의 문서는 http로 전달될 수 없다

http메시지에는 http 메시지를 보낸 브라우저가 어디에 있는지가 기록되어 있다

프락시의 주요 목적은 브라우저가 해야할 일의 양을 줄이는 것

검색 시, 한 문서의 페이지랭크 점수는 주어진 질의어에 무관

익스텐트 리스트 사용할 경우, 이는 각 용어별로 하나씩 존재해야 함

문서에 대한 스테밍 규칙과 질의어에 대한 스테밍 규칙은 다르면 다를수록 좋다

일반적으로 검색모형의 성능은 **재현율**이 커질수록 **정확률**도 커진다

주어진 한정된 댓수의 컴퓨터로 크롤링할 때 커버리지가 커질수록 신선도는 떨어질 수밖에 없다

simhash값이 같아도 문서의 내용이 다를 수 있다

**컨텐트 블록 찾기 최적화 문제**는 선형계획법으로 풀 수 있다

 

질의어 a b c를 가지는 검색 결과 집합의 크기를 추정하고자 한다. a를 포함하는 문서가 총 N개, 이 중 S개 문서 분석 결과 a,b,c 모두 포함한 문서수가 m개. 검색결과 집합의 크기는 m/(s/n)로 추정할 수 있다. 이 방식의 추정은 어떠한 확률론적 근서를 가지는지, a,b,c와 관련된 확률값들을 이용해 증명

다음의 십진수들을 델타 인코딩한 후, v-byte encoding. 최종결과는 이진수로 표현

아래 hmm사용해 나는 서울대에 합격했다는 문장으로부터 기관명을 추출하고자 할 때, 서울대가 기관명으로 인식되는가? i는 시작 상태이며, 스테밍 결과를 나 서울대 합격하다로 가정한 후, 인식 여부와 근거제시

5.1 역리스트에 스킨 포인터를 정의하는 목적?

5.2 100개의 포스팅을 가지고 있는 역리스트가 있다고 할 때, 개별 포스팅에 각각 스킵 포인터를 정의해 총 100개의 스킵 포인터를 사용할 경우, 문제점?

5.3 100개 포스팅 가지는 역리스트에 10개의 스킵 포인터를 정의하고자 할때, 어떠한 포스팅에 스킵 포인터 정의하는 것이 최선?

1. 두 개의 검색 엔진 A, B가 있을 때 B의 색인 크기가 A의 몇 배인지를 추정. 실험 통해 다음과 같은 결과 얻었다 가정 시 B의 색인 크기는 A 색인 크기의 몇배인가?

A에 색인된 문서의 25%는 B에도 색인 + B에 색인된 문서의 40%는 A에도 색인

1. 다음과 같은 웹 페이지

A는 C, D에 대한 링크 생성, ...

무작위 점프의 확률이 0.5, B,E pagerank값이 0.2, 0.1일때 A의 pagerank값?

 

2011

in a trackback link used in blogs, link is directed from an old document to a new doc unlik hyperlinks

http: stateful protocol that records the state about a client at the server side?

cookie usually sotres entire session information about a user up to one year lng

proxies are necessarily locate closer to clents that to servers

jsp is a programming lang by which one can cerate a
