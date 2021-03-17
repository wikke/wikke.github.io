hugo -D
/Users/wikke/.pythonenv/default/bin/python scripts/fix_img_path.py
git add .
git commit -m 'update'
git push -f gitee master
echo "手动更新: https://gitee.com/wikke/wikke/pages"
echo "Gitee Pages已发布: https://wikke.gitee.io/"
