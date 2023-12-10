---
layout: post
title: Companion
description: >
sitemap: false
permalink: /notes/UX/Companion
---

- this list will be replaced by the toc
{:toc .large-only}

## 사람과 상호작용하는 동반자


- 의사소통에 있어서 가장 자연스러운 것은 **음성 대화**
- 그럼에도 인간은 **시각적 채널에 굉장히 예민**하다 

**Chatbot에서의 소통**

- 주 정보: **텍스트**
- 맥락이 중요함 
- 때때로 radio button, checkbox 등으로 전환되지만 이는 효율적일지언정 **자연스럽지 않음**

1. 행동적 신호 (behavioral cues)
2. 준언어적 신호 (paralinguistic cues) `!!`, `??`, `^^`, `ㅋㅋㅋ`
3. 백채널링 신호 (back-channeling cues) `아하`, `정말?`, `응응`
    - 대화 끌어내기

## 추천 시스템 
---

### 필터링 문제점 🤔

1. **콜드 스타트 (cold start)**: 새로운 아이템이나 사용자에 대한 정보가 없는 경우 (참고 불가, 처리 어려움)
2. 사용자 집단 규모 커짐에 따른 **정보 과부하 (information overload)**: 계산 시간 복잡하며 비용이 많이 듦
3. **Long Tail**: 소수의 인기 있는 아이템이 대부분의 관심을 받고, 나머지는 관심이 없어서 추천이 어려움
4. 내용기반 필터링: 협업보다는 비교적 cold start 문제점에서 자유롭지만 item profile, user profile 둘 다 고려 필요 

### 필터링 종류 📚

1. 협업 필터링 (Collaborative Filtering)
    - 메모리 기반 협업 <fade>전통적 방법</fade>
        - **사용자 기반 협업 필터링 (User-based CF)**: **사용자간 유사성** 기반으로 추천 
            - <fade>내 취향과 비슷한 사람이 이걸 봤어요!</fade>

        - **아이템 기반 협업 필터링 (Item-based CF)**: **아이템간 유사성** 기반으로 추천
            - <fade>이 영화를 좋아하는 사람들은 이 영화도 좋아해요!</fade>
            - 표면적 선호도 
    - 모델 기반 협업 - more on netflix!

2. 내용 기반 필터링 (Content-based Filtering)
    - 표면적이 아닌, 아이템이 가지고 있는 **속성**을 기반으로 추천
    - 메모리 기반과 더불어 전통적인 추천시스템 방법

3. 하이브리드 필터링 (Hybrid Filtering)

### Netflix 추천 알고리즘 🎬

- 모델 기반 협업필터링 (통계, 머신러닝 기법 $$\rightarrow$$ 딥러닝)
    - <fade>사내 공모전에서 출발했다고 함</fade>
    - 데이터에 내재된 패턴을 찾아 동일 패턴을 보이는 군집 내 필터링 적용
    - **latent (잠재) 모델** 찾아내기 

**우연성 기반 추천 시스템** (Serendipity-based)
- 의도: 기존 시스템 너무 개인화되어 있음, 너무 안정적 
- **Filter Bubble** 🫧: 사용자를 자신의 세계에 갇히게 함, 새로운 영역 확장 or 나오기가 어려움
- 이러한 filter bubble을 pop, 새로운 취향과 경험을 제공함 
- 우연상 아이템은 맥락 / 특성에 영향을 많이 받아 알고리즘 일반화가 어려움
1. 참신한 (novel) 아이템 중 관련성이 있는,
2. 예상하지 못한 (unexpected) 
- $$\rightarrow$$ **예상하지 못한 가치**도출 목표

**Social Reommenation**의 역할도 크다
- (시청율 대부분을 차지하는 추천시스템) 알고리즘이 아닌 지인, 인터넷 통해 추천 받는 것
- 따라서 인플루언서 등 영향력 있는 사람들의 시청 이력에 더욱 가중치를 두는 전략도 있음 

TMI: 요즘 우연성 정도를 사용자가 직접 조작할 수 있게 하는 기능도 있다.

### 대화형 추천 시스템 💬
Conversation-based Recommendation System

- 우연성보다 보편적
- 일방향 상호작용 보완 $$\rightarrow$$ **양방향 상호작용**
- 목적지향적으로 여러 차례 대화를 통해 추천
- **_현재_**의 선호도 파악 가능, 추천에 대해 설명 제공 

- `NLU` (자연어 Understanding)
- `NLG` (자연어 Generation) 상호작용 이어가기 위한
- `Dialogue State Management`
- `Recommendation Engine` (추천 생성)
- `Explanation Engine` (사람들이 원하는 기능, 추천에 대한 설명)
- `Knowledge` (interaction data의 DB)

### Social Media 추천 시스템 📱

- Filter bubble과 인지편향 
    - 뉴스, 광고 등 내 관심사에만 노출되어 다른 영역 접근 점차 차단됨 
    - **Echo Chamber** (반향실 효과) 한 의견이 반복적으로 남겨져 이게 진실이라고 생각하게 됨
    - **Confirmation Bias** (인지편향) 내가 믿는 것만 믿게 됨 <fade>"거봐 내가 맞잖아"</fade>
    - 진실 외곡 위험성 $$\uparrow$$

- **Bandwagon 효과** :"모두가 YES" $$\leftrightarrow$$ Knob: "나 혼자 NO"
- **침묵의 나선 이론** (Spiral of Silence): 다수의 의견에 동조하고, 소수의 의견은 침묵하게 됨 (지배적 여론에 반대입장 표출 어려움)

- 거짓뉴스: 진실보다 6배 빠르게 퍼진다는 연구 결과, 자극, 감성이 극대화된 것들이 더욱 빠름 

- SNS에서의 주도적 의견 형성: 
    - chow test 결과 (꺾이는 point 찾기) 주로 초반에 (시간이 아닌, comment 수 많은 순서로) 의견 형성됨
    - 반대로 댓글이 없다면 휘발될 가능성 높음

## 설명 인터페이스
Explanation Interface
---

- 정보의 시각화, 강조점, 형태 $$\rightarrow$$ 정보 전달 

### 설명 방식 설계 📝

1. 대조적 설명 (Contrastive Explanation)
    - 왜 A의 반대인 A' 대신 A를 선택했는가?
2. 반사실적 설명 (Counterfactual Explanation)
    - 조건을 더하거나 빼서 `what if~`로 인과적 설명
3. 예제 기반 설명 (Example-based Explanation)
    - 규범적 (normative) 설명: A가 도출되는 여러 sample 보여주기
    - 비교 설명: 다른 결과 (B, C)가 도출되는 sample 보여주기
4. 귀인 설명 (attributive Explanation)
    - 사람들의 **특정 원인을 추론하는 귀인 과정을 반영**해 설명

**핀테크 결과설명 예시**: 
- 고객 대출가능여부 판단 AI가 대출불가를 판단했을 때, 이 내용을 ~~아주아주~~ 친절하게 설명해야 한다
- `why can't`, `how`, `what if` 등 원인, 결과, 그리고 가능하다면 대안을 제시해야 함

**자율주행 자동차 예시**:
- 현실화되는 중이지만 아직 불안감이 크다
- 1) 불확실성 <fade>~할수도 있다</fade>, 2) 심각성 <fade>~하기만 하더라도 정말 큰일난다</fade>, 통제권 이양 등 

- 위험수준 설명: 
    - 위험수준이 낮을 때 자세한 설명은 신뢰도를 향상 $$\rightarrow$$ 귀인 이론 입각한 설명 제공
    - 위험수준이 높을 때는 **너무 자세한 설명은 불안감 조성**. `Just say why`, 단순 상황만 보고할 것

## 메타버스 
---

현실과 상호작용 또는 현실을 확장하는 가상공간. 시간과 공간을 초월하며 디지털 자아들이 모여 사회활동을 하며, 경제활동으로 이어질 가능성이 높다.
온라인 개념의 확장

- `VR` (Virtual Reality): 가상현실 (100% aritificial), 완전 몰입
- `AR` (Augmented Reality): 증강현실 (실제 환경에 씌워진 가상 객체), 강화된 현실 세계
- `MR` (Mixed Reality): 혼합현실 (실제환경과 가상의 결합), 둘 다와 상호작용

- **Haptic Illusion**: 다른 감각 (예: 시각, 청각)을 통해 촉각을 느끼게 하는 것
    - 능동적 터치, 수동적 터치 

- `O2O`: online to offline, offline to online
    - 온라인에서의 행위 $$\rightarrow$$ 오프라인에서의 소비로 이루어지는 마케팅 기법 
    - <fade>ex: Hay Day</fade>
- `M2R`, `R2M`: metaverse to real world, real world to metaverse

- `NFT`, `Blockchain`, `Etherium`