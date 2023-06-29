from bs4 import BeautifulSoup

def extract_usernames(filename):
    with open(filename, 'r', encoding="utf-8") as f:
        contents = f.read()

    soup = BeautifulSoup(contents, 'html.parser')

    divs = soup.find_all('div', {'class': 'x9f619 xjbqb8w x1rg5ohu x168nmei x13lgxp2 x5pf9jr xo71vjh x1n2onr6 x1plvlek xryxfnj x1c4vz4f x2lah0s x1q0g3np xqjyukv x6s0dn4 x1oa3qoh x1nhvcw1'})
    return [div.text.replace("Verified", "") for div in divs]

# Replace these with the path to your actual files
following_file = 'following.txt'
followers_file = 'followers.txt'

following = set(extract_usernames(following_file))
followers = set(extract_usernames(followers_file))

not_following_back = following - followers


with open('not_following_back.txt', 'w', encoding="utf-8") as f:  # File to write URLs
    for user in not_following_back:
        f.write(f'https://www.instagram.com/{user}/\n')  # Write URL to file
