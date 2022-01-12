python -m portray as_html -o portraydocs --overwrite

cd portraydocs

git remote add origin https://github.com/paulablaza/discord-oauth2.git

git init

git checkout -b docs

git add .

git commit -m 'updated docs'

git push origin docs