hugo --destination ./docs --buildDrafts --cleanDestinationDir

/Users/wikke/.pythonenv/default/bin/python scripts/fix_img_path.py

git add .
git commit -m 'update'
git push gitee master
git push github master

echo "Github Pages: https://wikke.github.io/"
echo "Gitee Pagess: https://wikke.gitee.io/，手动更新: https://gitee.com/wikke/wikke/pages"
