# Rashid Hassan Ally — Portfolio Website

A Django-powered graphic-design portfolio. Projects, images, profile text, contact details, and social links are managed through Django Admin.

## Open this project on another Windows computer

This project currently includes its live portfolio database (`db.sqlite3`) and uploaded images (`media/`). Copy the complete `port 2` folder to the other computer; do not copy the `.venv` folder.

### 1. Install Python

Install Python 3.11 or newer from [python.org](https://www.python.org/downloads/). During installation, select **Add Python to PATH**.

### 2. Open the folder in VS Code

Open VS Code, select **File → Open Folder**, then choose the copied `port 2` folder. Open **Terminal → New Terminal**.

### 3. Create the local environment and install dependencies

Run these commands in the VS Code PowerShell terminal:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

### 4. Start the website

```powershell
.\.venv\Scripts\python.exe manage.py runserver 127.0.0.1:8017
```

Open http://127.0.0.1:8017/ in a browser.

### 5. Open the admin panel

Open http://127.0.0.1:8017/admin/ and sign in with the existing administrator account. Use the admin area to update the profile, social links, and project images.

If the project is copied with `db.sqlite3` and `media/`, all existing content will be present. If either is not copied, the portfolio data or uploaded images will be missing.

## Public sharing with ngrok

Keep Django running, open a second VS Code terminal, and run:

```powershell
ngrok http 8017
```

Share the HTTPS address ngrok gives you. The link works only while both terminals remain running.

## Generate the portfolio documents again

After changing portfolio details in the admin panel, regenerate the editable PowerPoint and PDF:

```powershell
.\.venv\Scripts\python.exe tools\build_portfolio_documents.py
```

The new files appear in `output/`.

## Important security note

The current project uses `DEBUG = True` and is intended for local development and temporary ngrok sharing. Do not use it unchanged as a permanent public deployment. Do not publish `db.sqlite3` in a public GitHub repository because it contains the admin account and your portfolio content. Use a **private** GitHub repository if you want GitHub to carry your current database and media files.

## Project layout

- `portfolio/` — models, admin configuration, and home view
- `templates/` — portfolio HTML
- `static/` — CSS and JavaScript
- `media/` — uploaded profile and project images
- `db.sqlite3` — current portfolio content
- `output/` — generated editable PowerPoint and PDF portfolio
- `tools/` — document generator
