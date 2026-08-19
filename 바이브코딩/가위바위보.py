import random

# 사용자가 입력할 수 있는 선택지
choices = ["가위", "바위", "보"]

print("=== 가위바위보 게임 ===")
print("종료하려면 '종료'를 입력하세요.")

while True:
    user_choice = input("가위, 바위, 보 중 하나를 입력하세요: ")

    # 종료 명령 확인
    if user_choice == "종료":
        print("게임을 종료합니다.")
        break

    # 올바른 입력인지 확인
    if user_choice not in choices:
        print("가위, 바위, 보 중에서 입력해 주세요.\n")
        continue

    # 컴퓨터가 세 가지 중 하나를 무작위로 선택
    computer_choice = random.choice(choices)

    print(f"사용자: {user_choice}")
    print(f"컴퓨터: {computer_choice}")

    # 두 선택이 같으면 무승부
    if user_choice == computer_choice:
        print("무승부입니다!")

    # 사용자가 이기는 경우를 직접 확인
    # 가위는 보를 이기고,
    # 바위는 가위를 이기고,
    # 보는 바위를 이깁니다.
    elif (
        (user_choice == "가위" and computer_choice == "보")
        or (user_choice == "바위" and computer_choice == "가위")
        or (user_choice == "보" and computer_choice == "바위")
    ):
        print("사용자가 이겼습니다!")

    # 위의 경우가 아니면 컴퓨터가 이긴 경우
    else:
        print("컴퓨터가 이겼습니다!")

    print()