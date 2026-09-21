# Push this project to GitHub

## Before you begin

Because this project includes `db.sqlite3` and the `media/` upload folder, create a **private** GitHub repository. A public repository would expose your site content and the administrator database.

## 1. Create a private repository on GitHub

1. Sign in at https://github.com.
2. Click **New repository**.
3. Name it, for example: `rashid-portfolio`.
4. Select **Private**.
5. Do not add a README, `.gitignore`, or license on GitHub—the project already has them.
6. Click **Create repository**.

## 2. Push from the VS Code terminal

Open the `port 2` folder in VS Code, then open **Terminal → New Terminal** and run:

```powershell
git init
git add .
git commit -m "Initial portfolio website"
git branch -M main
git remote add origin https://github.com/YOUR-GITHUB-USERNAME/rashid-portfolio.git
git push -u origin main
```

Replace `YOUR-GITHUB-USERNAME` with your actual GitHub username and use the repository name you selected.

When GitHub asks you to sign in, complete the browser sign-in flow. GitHub does not accept normal account passwords for command-line pushes; use the browser prompt, GitHub Desktop, or a personal access token if prompted.

## 3. Confirm the upload

Refresh the GitHub repository page. You should see folders such as `config`, `portfolio`, `media`, `static`, `templates`, plus `db.sqlite3`, `README.md`, and `requirements.txt`.

## 4. Open on another computer

1. Install Git, Python, and VS Code.
2. Clone the private repository:

```powershell
git clone https://github.com/YOUR-GITHUB-USERNAME/rashid-portfolio.git
cd rashid-portfolio
```

3. Follow the instructions in `README.md` to create `.venv`, install packages, and run the server.

## Later updates

After you edit the website or update content and want to save the latest version on GitHub:

```powershell
git add .
git commit -m "Update portfolio content"
git push
```
