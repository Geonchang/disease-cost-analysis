# disease-cost-analysis
공공데이터 공모전 준비

## What? 무엇을 하고자 하는가
동일한 질병군(Cluster) 내에서도 자기부담률이 높은 질병 식별
정부 및 보험기간의 의료 재정 사각지대 분석
본인 부담 격차 해소를 위한 기초 자료 제공

## Why? 왜 이 문제가 중요한가?
동일 질병군 내에서도 지원 격차가 존재할 가능성
정책적 지원에서 소외되는 질환들의 체계적 발견 필요
의료 형평성 제고와 사회보장 강화에 기여
데이터 기반 정책 수립의 근거 마련

## Installation

raptor 설치

```bash
git clone https://github.com/parthsarthi03/raptor.git
cd raptor
pip install -r requirements.txt

pip install huggingface_hub==0.19.4
pip install -U sentence-transformers
pip install --upgrade openai
```