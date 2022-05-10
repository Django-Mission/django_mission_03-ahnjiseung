# django_mission_02-ahnjiseung
> ## Basic Mission
1. 고객센터 앱과 FAQ 모델 만들기
2. 고객센터 앱 생성 -> "support"
3. FAQ 모델 생성
    - 모델명 : Faq
    - 필드 : 질문, 카테고리, 답변, 생성자, 생성일시, 최종 수정자, 최종 수정일시
4. Inquiry 모델 생성
    - 질문 제목, 카테고리, 생성 일시, 생성자, 이메일, 전화번호
5. Answer 모델 생성
    - 작성자, 내용, 생성일시
6. Admin 페이지 구성
    - 자주묻는질문(Faq)
    - 목록페이지 출력 필드 : 제목, 카테고리, 최종 수정 일시
    - 검색 필드 : 제목
    - 필터 필드 : 카테고리
    - 1:1문의(Inquiry)
    - 목록페이지 출력 필드 : 질문 제목, 카테고리, 생성 일시, 생성자
    - 검색 필드 : 제목, 이메일, 전화번호
    - 필터 필드 : 카테고리
    - 인라인모델 : 답변(`Answer`)
- 답변(`Answer`)
    - 1:1문의 모델에 인라인모델로 추가