# 推送到 GitHub 仓库的详细说明

由于认证问题，需要你手动完成推送。请按照以下步骤操作：

## 方法一：使用 GitHub CLI（推荐）

1. 首先认证 GitHub：
```bash
cd douyin-live-comment-voice
gh auth login
```

2. 然后推送代码：
```bash
gh repo set-default aloha07-cell/ai-stream
git remote add origin https://github.com/aloha07-cell/ai-stream.git
git branch -M main
git push -u origin main --force
```

## 方法二：使用个人访问令牌（PAT）

1. 在 GitHub 上创建个人访问令牌：
   - 访问 https://github.com/settings/tokens
   - 点击 "Generate new token" -> "Generate new token (classic)"
   - 选择 `repo` 权限
   - 生成并复制令牌

2. 使用令牌推送：
```bash
cd douyin-live-comment-voice
git remote add origin https://<你的令牌>@github.com/aloha07-cell/ai-stream.git
git branch -M main
git push -u origin main --force
```

将 `<你的令牌>` 替换为你刚才复制的令牌。

## 方法三：通过浏览器上传（最简单）

1. 访问 https://github.com/aloha07-cell/ai-stream
2. 点击 "Add file" -> "Upload files"
3. 将项目文件夹中的所有文件拖到上传区域
4. 提交更改

## 注意事项

- 使用 `--force` 选项会覆盖仓库中的现有内容，请谨慎使用
- 如果仓库已有内容，请先备份重要文件
- 建议先在本地测试代码，确保没有问题再推送
