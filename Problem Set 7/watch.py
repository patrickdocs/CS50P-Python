import re

def main():
    print(parse(input("HTML: ")))

def parse(s):
    pattern = r'src="https?://(?:www\.)?youtube\.com/embed/([a-z0-9_-]+)"'
    match = re.search(pattern, s, re.IGNORECASE)

    if not match:
        return None
    else:
        video_id = match.group(1)
        return f"https://youtu.be/{video_id}"

if __name__ == "__main__":
    main()
