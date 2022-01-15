docs=$(python -m pdoc discord_oauth2 -o docs --pdf)
longtext="
description: | API documentation for modules: discord_oauth2.

lang: en

classoption: oneside geometry: margin=1in papersize: a4

linkcolor: blue links-as-notes: true ...
"

echo $longtext

idreplacedocs=${docs//"{#id}"/""}
replacelongtext=${idreplacedocs//$longtext/""}
echo $replacelongtext > docs/API.md


