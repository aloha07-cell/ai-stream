# Push to GitHub Instructions

To push this repository to GitHub, follow these steps:

## 1. Create a GitHub repository

Go to https://github.com/new and create a new repository:
- Repository name: `douyin-live-comment-voice`
- Description: `Douyin live stream comment processing with voice response`
- Visibility: Public or Private (your choice)

## 2. Add the remote repository

In your terminal, navigate to the project directory and run:

```bash
cd douyin-live-comment-voice
git remote add origin https://github.com/YOUR_USERNAME/douyin-live-comment-voice.git
```

Replace `YOUR_USERNAME` with your GitHub username.

## 3. Push the code

```bash
git push -u origin main
```

You may be prompted to enter your GitHub credentials or a personal access token.

## 4. Verify

Go to your GitHub repository to verify that the code has been pushed successfully.

## Alternative: Using GitHub CLI

If you prefer to use the GitHub CLI, run:

```bash
gh auth login
gh repo create douyin-live-comment-voice --public --description "Douyin live stream comment processing with voice response" --push
```

This will create the repository and push the code in one step.
