# Survive in Berlin

A small text-based survival game about spending your first year in Berlin as a foreigner.

[한국어](#한국어)

## About

I live in Berlin, and I wanted to turn the things I went through as a foreigner here into a game.
Finding a flat, learning German, hunting for a minijob, sorting trash under the watchful eye of a German neighbor,
locking yourself out of your room — all of it is in here.

This project is built with [Claude Code](https://claude.com/claude-code), and the main language is **Python**.

## Gameplay

You arrive in Berlin with one goal: **survive 12 months without running out of money.**

- **Starting point**: 14,400–20,000 EUR, German level A1, living in a temporary residence.
- **Every month**: living costs (550 EUR, without rent) and rent are deducted.
- **Game over**: your money drops to 0 or below.

### Cost of living

The German blocked account (Sperrkonto) assumes **992 EUR per month** for living costs *including* rent
(11,904 EUR per year). That is a nationwide figure. Berlin is a big city, prices are higher, and rent in particular
is expensive — an average WG room alone costs about 650 EUR. Living in Berlin on 992 EUR is hard.

So the game assumes **at least 1,200 EUR per month**, which means you need **at least 14,400 EUR** for one year.
You start with a random amount between 14,400 EUR and, if you're lucky, 20,000 EUR.

| Item | EUR / month | Note |
| --- | --- | --- |
| Living costs (without rent) | 550 | food, insurance, transport, phone, ... |
| WG room | 650 | average asking rent in Berlin (MMI / WG-Gesucht, 2025) |
| Studio | 750 | estimate |
| Temporary residence | 800 | estimate for a furnished short-term flat |

The cheapest setup (living costs + WG) is exactly 1,200 EUR per month.

### Events

| Event | What happens |
| --- | --- |
| Find a home | While you're in a temporary residence (800 EUR/month), look for a WG (650 EUR) or a studio (750 EUR). WGs have more viewings and better odds. |
| German test | Take a German test every few months to level up from A1 toward C1. Higher levels get harder to pass. |
| Find a minijob | When your money runs low, apply for minijobs (556 EUR/month) in English or German. Better German means better odds for German jobs. |
| Lost key | You locked yourself out. Try it yourself, ask a neighbor, or call the Schlüsseldienst. |
| Trash sorting | Sort your trash into the blue, black, brown, and yellow bins. Get it wrong and a German grandma appears from behind the bins. |

## How to run

No external packages are needed for the text version. Python 3 is enough (developed with Python 3.14).

```bash
git clone <this-repo>
cd survive-in-Berlin
python3 main.py
```

## Project structure

```
main.py                 # game loop: 12 months, monthly costs, event schedule
player.py               # player creation, German levels, residence and rent
event_find_home.py      # house hunting event
event_find_job.py       # minijob hunting event and salary
event_lost_key.py       # lost key event
event_trash_sorting.py  # trash sorting minigame
utils.py                # small helpers
```

---

# 한국어

베를린에서 외국인으로 첫 1년을 버티는 텍스트 기반 생존 게임입니다.

## 소개

베를린에 살면서 외국인으로 겪었던 일들을 게임으로 만들어보고 싶어서 시작한 프로젝트입니다.
집 구하기, 독일어 공부, 미니잡 구하기, 독일 이웃의 감시 속에서 쓰레기 분리수거하기, 방 열쇠를 안에 두고 문 잠그기까지 독일에 살면서 겪을 수 있는 일들을 담아봤습니다.

이 프로젝트는 [Claude Code](https://claude.com/claude-code)를 사용해 제작했고, 메인 언어는 **Python**입니다.

## 게임 방법

베를린에 도착한 당신의 목표는 단 하나, **12개월을 버티는 것**입니다.

- **시작 상태**: 14,400–20,000 EUR, 독일어 A1, 임시 거처에서 생활
- **매달**: 생활비(월세 제외 550 EUR)와 월세가 빠져나갑니다.
- **게임 오버**: 돈이 0 이하가 되면 끝입니다.

### 생활비

독일 슈페어콘토(Sperrkonto, 독일 유학/체류용 보증 계좌)는 월세를 *포함한* 생활비를 **한 달 992 EUR**(연 11,904 EUR)로 잡습니다.
하지만 이건 독일 전국 기준입니다. 베를린은 대도시라 물가가 더 비싸고, 특히 월세가 비쌉니다.
WG 방 하나만 해도 평균 650 EUR 정도라서, 992 EUR로 베를린에서 생활하기는 어렵습니다.

그래서 이 게임에서는 **최소 한 달 1,200 EUR**가 든다고 보고, 1년을 버티려면 **최소 14,400 EUR**가 필요하다고 설정했습니다.
시작 금액은 14,400 EUR부터, 운이 좋으면 최대 20,000 EUR까지 랜덤으로 정해집니다.

| 항목 | 월 EUR | 비고 |
| --- | --- | --- |
| 생활비 (월세 제외) | 550 | 식비, 보험, 교통, 통신 등 |
| WG 방 | 650 | 베를린 평균 호가 (MMI / WG-Gesucht, 2025) |
| 원룸 | 750 | 추정치 |
| 임시 거처 | 800 | 가구 딸린 단기 숙소 추정치 |

가장 저렴한 조합(생활비 + WG)이 딱 한 달 1,200 EUR입니다.

### 이벤트

| 이벤트 | 내용 |
| --- | --- |
| 집 구하기 | 임시 거처(월 800 EUR)에 사는 동안 WG(650 EUR)나 원룸(750 EUR)을 구합니다. WG는 뷰잉 기회가 많고 성공 확률도 높습니다. |
| 독일어 시험 | 몇 달마다 독일어 시험을 봐서 A1부터 C1까지 레벨을 올립니다. 레벨이 높을수록 합격하기 어렵습니다. |
| 미니잡 구하기 | 돈이 부족해지면 영어 또는 독일어로 미니잡(월 556 EUR)에 지원합니다. 독일어 실력이 좋을수록 독일어 일자리 합격 확률이 올라갑니다. |
| 열쇠 분실 | 열쇠를 방 안에 두고 문을 잠갔습니다. 직접 열어보거나, 이웃에게 부탁하거나, 열쇠공(Schlüsseldienst)을 부릅니다. |
| 분리수거 | 쓰레기를 파랑, 검정, 갈색, 노랑 통에 나눠 버립니다. 틀리면 쓰레기통 뒤에서 독일 할머니가 나타납니다. |

## 실행 방법

텍스트 버전은 외부 패키지가 필요 없습니다. Python 3만 있으면 됩니다 (Python 3.14로 개발).

```bash
git clone <this-repo>
cd survive-in-Berlin
python3 main.py
```

## 프로젝트 구조

```
main.py                 # 게임 루프: 12개월, 매달 비용, 이벤트 일정
player.py               # 플레이어 생성, 독일어 레벨, 거주지와 월세
event_find_home.py      # 집 구하기 이벤트
event_find_job.py       # 미니잡 구하기 이벤트와 월급
event_lost_key.py       # 열쇠 분실 이벤트
event_trash_sorting.py  # 분리수거 미니게임
utils.py                # 작은 헬퍼 함수
```
