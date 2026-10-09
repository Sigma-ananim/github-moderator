import os

def main():
    comment_text = os.getenv("COMMENT_BODY", "").lower()
    bad_words = ["stupid", "idiot", "trash", "garbage", "hate"]

    for word in bad_words:
        if word in comment_text:
            print(f"🚨 ОБНАРУЖЕН ТОКСИЧНЫЙ КОММЕНТАРИЙ! Найдено слово: '{word}'")
            exit(1) 

    print("🟢 Проверка пройдена. Комментарий вежливый!")

if __name__ == "__main__":
    main()
