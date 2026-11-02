# News Website App

A news website built with **Django 5.1**. Admin users publish news posts; registered users can read, like and comment on them. The project uses a custom user model, a full authentication flow (registration, login, logout, password reset), and ships with Dockerfiles and a Docker Compose setup.

## Features

- **Custom user model** with a role field (`Super User`, `Admin User`, `Site User`, `External User`) and a unique mobile number
- **Authentication** – registration, login, logout and the complete password-reset flow (emails are printed to the console in development)
- **News posts** – title, content, publication date and the admin user who published it; listed newest first
- **Likes and comments** – authenticated users can like and comment on any post
- **Latest news** page
- **Django admin** for managing users and content
- **Docker support** – separate containers for the accounting and news services

## Tech Stack

| Layer            | Technology                         |
| ---------------- | ---------------------------------- |
| Language         | Python 3.10                        |
| Framework        | Django 5.1                         |
| Database         | SQLite (default)                   |
| Templates        | Django Template Language           |
| Containerization | Docker, Docker Compose             |

## Project Structure

```
news-website-app/
├── accounting/        # CustomUser model, registration, login/logout, password reset
├── news/              # NewsPost, Comment and Like models, news views
├── interactions/      # Reserved for user-interaction features
├── news_website/      # Project settings and root URL configuration
├── templates/         # Shared HTML templates
├── docker-compose.yml # Multi-container setup
├── manage.py          # Django management entry point
└── requirements.txt   # Python dependencies
```

## Data Model

| Model        | Key fields                                                                                  |
| ------------ | ------------------------------------------------------------------------------------------- |
| `CustomUser` | extends `AbstractUser`; `user_type` (1–4, default 4), `mobile_number` (unique)              |
| `NewsPost`   | `title`, `content`, `publication_date`, `admin_user` (FK), `likes`, `comments_count`        |
| `Comment`    | `news_post` (FK), `user` (FK), `content`, `created_at`                                      |
| `Like`       | `news_post` (FK), `user` (FK), `created_at`                                                 |

## URL Routes

| URL                                  | Name                      | Description                  |
| ------------------------------------ | ------------------------- | ---------------------------- |
| `/`                                  | `home`                    | Home page                    |
| `/admin/`                            | –                         | Django admin                 |
| `/accounting/register/`              | `register`                | Create an account            |
| `/accounting/login/`                 | `login`                   | Log in                       |
| `/accounting/logout/`                | `logout`                  | Log out                      |
| `/accounting/password_reset/`        | `password_reset`          | Start a password reset       |
| `/accounting/reset/<uidb64>/<token>/`| `password_reset_confirm`  | Confirm a password reset     |
| `/news/`                             | `news_list`               | List all news posts          |
| `/news/<id>/`                        | `news_detail`             | View a single post           |
| `/news/<id>/add_comment/`            | `add_comment`             | Comment on a post            |
| `/news/<id>/like/`                   | `like_post`               | Like a post                  |
| `/news/latest/`                      | `latest_news`             | Latest news                  |

## Getting Started

### Prerequisites

- Python 3.10+
- pip
- (Optional) Docker and Docker Compose

### Run locally

```bash
# 1. Clone the repository
git clone https://github.com/ali-e-afshar/news-website-app.git
cd news-website-app

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Apply database migrations
python manage.py migrate

# 5. Create an admin account
python manage.py createsuperuser

# 6. Start the development server
python manage.py runserver
```

Open <http://127.0.0.1:8000/>. Log in to `/admin/` with the superuser to create news posts.

### Run with Docker

```bash
docker compose up --build
```

| Service  | Container    | Port |
| -------- | ------------ | ---- |
| Accounts | `accounting` | 8000 |
| News     | `news`       | 8001 |

Both containers use `python:3.10.1-slim`, run the Django development server, and read the `news_website.settings` module. Stop them with `docker compose down`.

## Configuration

Settings live in `news_website/settings.py`. The defaults are meant for development. Before deploying:

- Set `DEBUG = False` and configure `ALLOWED_HOSTS`
- Move `SECRET_KEY` out of the repository and load it from an environment variable
- Replace SQLite with a production database such as PostgreSQL
- Replace the console email backend with a real SMTP backend
- Serve the app with Gunicorn or uWSGI instead of `runserver`

## Roadmap

- [ ] REST API (Django REST Framework) with token/JWT authentication
- [ ] Automated tests
- [ ] PostgreSQL support
- [ ] Article categories, tags and search
- [ ] CI pipeline with GitHub Actions

## Contributing

Contributions are welcome. Fork the repository, create a feature branch, and open a pull request.

## Author

**Ali Afshar Degarsi** – [GitHub](https://github.com/ali-e-afshar)
