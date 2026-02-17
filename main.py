print("=== AI CỦA DŨNG v1 ===")

while True:
    user = input("Bạn: ")

    if user.lower() == "thoát":
        print("AI: Tạm biệt Dũng 👋")
        break

    elif "chào" in user.lower():
        print("AI: Chào Dũng 😎")

    elif "tên gì" in user.lower():
        print("AI: Tôi là AI riêng của Dũng.")

    elif "mấy giờ" in user.lower():
        print("AI: Tôi chưa xem được giờ nhưng sắp nâng cấp 😏")

    else:
        print("AI: Tôi đang học thêm... Dũng nói lại thử xem.")
