import requests

#vars
day = 1
sessionCookie = '' # See Readme.md
puzzle_url = f"https://adventofcode.com/2022/day/${day}/input"
puzzle_cookie = f"${sessionCookie}"

def main():
    data = getter()
    return data

def getter():
    try:
        x = requests.get(puzzle_url, headers = {
            'Content-Type': 'plain/text',
            'cookie': puzzle_cookie
        })
        return x.text
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
        
print(main())
