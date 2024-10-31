import emoji

def main():
    s = input()
    emo = emoji.emojize(s, language = "alias")
    print(emo)

if __name__ == "__main__":
    main()
#check50 cs50/problems/2022/python/emojize
