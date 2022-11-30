# Military Letter Manager
![](/readme/main_screen.png "실행 화면")

---
## Introduction
매일 뉴스 타이틀을 크롤링하여, 육군 훈련병들에게 자동으로 인편을 보내주는 프로그램입니다.
더캠프 계정으로 로그인 및 이용이 가능합니다.

매일 오후 1시마다 인편이 전송됩니다.

---
## Requirements
Python 3.7 에서 작성된 코드입니다. 정상 동작을 위해 Python 3 버전 이상을 사용해주세요. 

필요한 라이브러리 및 패키지는 다음과 같습니다. 
```
beautifulsoup4
cryptography
Pillow
pycryptodome
PyQt5
pystray
requests
schedule
sqlite3
```

1920X1080 해상도에 최적화되어 있습니다

---
## Implementation
파이썬 숙련도가 부족한 상태로 급하게 만들다 보니 코드의 완성도가 좋지 않습니다 ㅠㅠ

##### 1. Client Package
더캠프 웹 서버와의 통신부입니다.
`TheCampClient` 클래스에 세션 프로퍼티와 포스트 함수를 만들어 두고, `LoginClient`와 `MainClient`에서 상속하여 사용합니다.

##### 2. Data Package
프로그램의 구현에 필요한 다양한 데이터 구조체입니다.

`LiveData`는 다른 구조체들과 결이 조금 다른데, data package 외에 마땅히 넣을 곳이 없어 그냥 넣어두었습니다.

*LiveData 클래스는 안드로이드의 LiveData에서 이름을 따 왔으나, 단순 Observable 오브젝트입니다*

*그냥 익숙한 이름으로 빠르게 개발하려고 대충 붙였습니다 ;ㅅ;*

##### 3. Database Package
DB 매니저와 레포지토리를 관리하는 패키지입니다.
초기 구상으로는 설정값을 관리하는 `SettingDatabaseManager`가 필요했기에 관리의 용이성을 위해 레포지토리를 만들었지만, 현재는 오버엔지니어링..입니다..

##### 4. Helper Package
비지니스 의존성이 낮은 기능들을 모아 놓은 패키지입니다.

##### 5. Manager Package
싱글턴 클래스들로, 하나의 인스턴스를 프로그램의 라이프타임동안 유지하며 사용해야 하는 클래스를 모아 놓은 패키지입니다.

##### 6. UI Package
레이아웃 구현체를 모아 놓은 패키지입니다.
내부 패키지로 `widgets`, `widgets/card` 패키지가 존재합니다.

`widgets package` : 레이아웃 구현에 필요한 각종 widget들을 구현해 둔 패키지

`widgets/card package` : widget 중 메인 화면에서 사용될 다양한 카드뷰를 구현해 둔 패키지

##### 7. Utils package
비지니스 의존성이 없다시피 한 기능들을 모아 놓은 패키지입니다.

##### 8. ViewModel Package
MVVM 구조를 위한 뷰모델을 구현해 둔 패키지입니다.

##### 9. res
리소스를 관리하는 패키지입니다.

---
## To-do
- 레이아웃 코드 구조 개선
- main client에서도 훈련병을 edu_seq으로 구분하도록 수정
- 해상도에 따른 폰트 크기 조정
- LiveData.. 이름.. 바꿔야..할까..?
- 막판에 급해서 뭉쳐넣은 커밋 나누기

---
## Contributors
- [Sanop](https://github.com/S4nop)
- [wjieun](https://github.com/wjieun)
- [mikeysw](https://github.com/mikeysw)
- [jun2017313149](https://github.com/jun2017313149)
