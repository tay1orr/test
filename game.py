import streamlit as st
import random

# 첫 번째 게임 (숫자 야구 게임)
def generate_secret_number():
    digits = random.sample(range(10), 3)  # 0-9까지 중복 없이 3자리 선택
    return ''.join(map(str, digits))

def calculate_score(secret, guess):
    strikes = sum(1 for s, g in zip(secret, guess) if s == g)
    balls = len(set(secret) & set(guess)) - strikes
    return strikes, balls

def game1():
    st.title("⚾ 숫자 야구 게임 ⚾")

    # 게임 초기화
    if 'secret_number' not in st.session_state:
        st.session_state.secret_number = generate_secret_number()
        st.session_state.attempts = 0

    # 사용자 입력 받기
    user_guess = st.text_input("3자리 숫자를 추측하세요 (예: 123):")

    if st.button("제출"):
        if len(user_guess) != 3 or not user_guess.isdigit():
            st.warning("3자리 숫자를 입력하세요.")
        else:
            st.session_state.attempts += 1
            strikes, balls = calculate_score(st.session_state.secret_number, user_guess)

            if strikes == 3:
                st.success(f"축하합니다! 정답은 {st.session_state.secret_number}입니다. {st.session_state.attempts}번 만에 맞추셨습니다!")
                st.session_state.secret_number = generate_secret_number()  # 새로운 숫자 생성
                st.session_state.attempts = 0  # 시도 횟수 초기화
            else:
                st.info(f"{strikes} 스트라이크, {balls} 볼입니다.")

    # 초기화 버튼
    if st.button("게임 다시 시작"):
        st.session_state.secret_number = generate_secret_number()
        st.session_state.attempts = 0
        st.success("게임이 초기화되었습니다.")

# 두 번째 페이지 (로또 번호 생성기)
def generate_lotto_numbers():
    return sorted(random.sample(range(1, 46), 6))  # 1부터 45까지의 숫자 중 6개 선택

def game2():
    st.title("💰 로또 당첨 번호 시뮬레이션 💰")

    # 사용자가 입력한 로또 당첨 번호
    winning_numbers = generate_lotto_numbers()
    st.write("당첨 번호는 다음과 같습니다:")
    st.write(winning_numbers)

    # 시뮬레이션
    ticket_price = 5000  # 로또 1장 가격
    purchase_quantity = 50  # 한 번에 구매할 로또 장 수
    attempts = 0
    total_cost = 0
    success = False

    if st.button("시뮬레이션 시작하기"):
        # 당첨될 때까지 반복
        while not success:
            attempts += purchase_quantity
            total_cost += purchase_quantity * ticket_price

            # 여러 장의 로또 번호를 생성하여 체크
            for _ in range(purchase_quantity):
                generated_ticket = generate_lotto_numbers()
                if generated_ticket == winning_numbers:
                    success = True
                    break  # 성공 시 루프 종료

        st.success(f"축하합니다! 당첨되었습니다! 총 {attempts}장의 로또를 구매하셨습니다.")
        st.write(f"총 사용 금액은 {total_cost:,} 원입니다.")  # 사용 금액을 형식화하여 출력

    # 요약 메시지
    st.markdown("로또 번호는 1부터 45까지의 숫자로 이루어지며, 중복 없이 생성됩니다.")

# 사이드바 메뉴 설정
st.sidebar.title("메뉴")
selected_game = st.sidebar.radio("게임 선택", ("숫자 야구 게임", "로또 당첨 번호 시뮬레이션"))

# 선택된 게임에 따라 함수 호출
if selected_game == "숫자 야구 게임":
    game1()
elif selected_game == "로또 당첨 번호 시뮬레이션":
    game2()