---
title: "使用Hugo+Markdown创建个人博客，部署在Github/Gitee"
date: 2021-03-17T19:33:21+08:00
draft: true
---

## 安装

```bash
➜  ~ brew install hugo
...

➜  ~ hugo version
Hugo Static Site Generator v0.80.0/extended darwin/amd64 BuildDate: unknown
```

## 初始化

运行`hugo new site <your-blog-name>`初始化一个`hugo`工程

```bash
➜  ~ hugo new site blogs
Congratulations! Your new Hugo site is created in /Users/wikke/blogs.

Just a few more steps and you're ready to go:

1. Download a theme into the same-named folder.
   Choose a theme from https://themes.gohugo.io/ or
   create your own with the "hugo new theme <THEMENAME>" command.
2. Perhaps you want to add some content. You can add single files
   with "hugo new <SECTIONNAME>/<FILENAME>.<FORMAT>".
3. Start the built-in live server via "hugo server".

Visit https://gohugo.io/ for quickstart guide and full documentation.
```

初始化git仓库

```
➜  cd blogs

➜  blogs git init
Initialized empty Git repository in /Users/wikke/blogs/.git/

```

访问 [https://themes.gohugo.io/](https://themes.gohugo.io/) 挑选一个你喜欢的主题theme（这步是必须哦）

我挑选了一个[mainroad](https://themes.gohugo.io/mainroad/)的主题

把它的git项目作为**submoule**添加到blog仓库themes下

```bash

➜  blogs git:(master) ✗ git submodule add https://github.com/vimux/mainroad themes/mainroad
Cloning into '/Users/wikke/blogs/themes/mainroad'...
remote: Enumerating objects: 4, done.
remote: Counting objects: 100% (4/4), done.
remote: Compressing objects: 100% (4/4), done.
remote: Total 2033 (delta 0), reused 1 (delta 0), pack-reused 2029
Receiving objects: 100% (2033/2033), 1.17 MiB | 1.11 MiB/s, done.
Resolving deltas: 100% (1206/1206), done.
```

修改`config.toml`配置

- baseURL需要填写github博客的链接，这里`wikke`对应你的Github ID
- title即网站的标题
- theme填写你指定的theme。你可以clone多个theme的submodule，这里选择你想用的那个

![image-20210317174942476](blog-with-hugo.assets/image-20210317174942476.png)

通过Hugo命令创建post，`hugo new posts/blog-with-hugo.md`

- 这里需要增加`posts/`前缀，从而组织目录结构
- 文件后缀为`.md`，则hugo会使用markdown语法来解析生成HTML

然后你就可以使用你喜欢的Markdown编辑器来写博客啦。比如猩哥最喜欢的`Typora`编辑器，完美如图~

（我此刻正在写一篇“如何使用Hugo写博客”的博客，盗梦空间既视感）

![image-20210317175514552](blog-with-hugo.assets/image-20210317175514552.png)

## 本地预览效果

当你完成了markdown博客后，就可以本地预览效果

```bash
➜  blogs git:(master) ✗ hugo server -D
Start building sites …

                   | EN
-------------------+-----
  Pages            | 11
  Paginator pages  |  0
  Non-page files   |  7
  Static files     |  5
  Processed images |  0
  Aliases          |  4
  Sitemaps         |  1
  Cleaned          |  0

Built in 55 ms
Watching for changes in /Users/wikke/blogs/{archetypes,content,data,layouts,static,themes}
Watching for config changes in /Users/wikke/blogs/config.toml
Environment: "development"
Serving pages from memory
Running in Fast Render Mode. For full rebuilds on change: hugo server --disableFastRender
Web Server is available at http://localhost:1313/ (bind address 127.0.0.1)
Press Ctrl+C to stop
```

在`http://localhost:1313/`看效果。上图

![image-20210317180007125](blog-with-hugo.assets/image-20210317180007125.png)

值得一提的是，如果你的blog markdown内容发生了变更，比如又写了一部分博文，然后保存。这时候浏览器端是可以实时查看到改动效果的。不需要重新启动服务，甚至都不需要手动刷新浏览器！

# 上传在线博客

## Gitee Pages

- 创建一个和你用户名一样的repo
- 把博客项目上传到git仓库
- TODO：设置pages啥的，done！

## Github Pages

![截屏2021-03-17 15.21.00](blog-with-hugo.assets/截屏2021-03-17 15.21.00.png)

# Reference

1. [https://gohugo.io/getting-started/quick-start/](https://gohugo.io/getting-started/quick-start/)
2. [https://wikke.gitee.io/](https://wikke.gitee.io/)
3. [https://wikke.github.io/](https://wikke.github.io/)
4. [https://gohugo.io/hosting-and-deployment/hosting-on-github/](https://gohugo.io/hosting-and-deployment/hosting-on-github/)
5. [https://gitee.com/help/articles/4136](https://gitee.com/help/articles/4136)
6. [https://pages.github.com/](https://pages.github.com/)

