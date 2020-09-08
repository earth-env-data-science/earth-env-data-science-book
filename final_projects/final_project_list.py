import pandas as pd

url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQZuGOVK_afpqjadVaI9wd29iXRC78Ofvp-hL3IQV7SbJN11LIW0SbcRtjhpdreHjqh6Efhh8UMlkqH/pub?gid=1496620424&single=true&output=csv'
df = pd.read_csv(url)
df

for idx, row in df.iterrows():
    repo = row['repo']
    repo_base = repo.replace('https://github.com/', '')
    github_badge = f'[![github](https://img.shields.io/badge/view-github-green?logo=github)]({repo})'
    
    binder_badge = f'[![Binder](https://mybinder.org/badge_logo.svg)]({row.binder})' if row.binder else ''
    name = row['name']
    
    print(f'- _{row.title.strip()}_ by {name}\n  {github_badge} {binder_badge}')
    