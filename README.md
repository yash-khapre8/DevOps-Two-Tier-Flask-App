#  Two-Tier Flask Application (DevOps Project)

## 📌 Overview

This project demonstrates a **Two-Tier Architecture** using a Flask backend and a MySQL database deployed on AWS EC2 instances. It also includes **Docker containerization** and **CI/CD automation using GitHub Actions**.

---

## 🧠 Architecture

```
User → Nginx (optional) → Flask App (EC2) → MySQL Database (EC2)
```

* **Tier 1 (Application Layer):** Flask app running on EC2
* **Tier 2 (Database Layer):** MySQL (MariaDB) on separate EC2
* **CI/CD:** GitHub Actions for automated deployment
* **Containerization:** Docker + Docker Hub

---

## ⚙️ Tech Stack

* Python (Flask)
* MySQL (MariaDB)
* AWS EC2
* Docker
* GitHub Actions (CI/CD)
* Nginx (Reverse Proxy)

---

## ☁️ Infrastructure Setup

### 1️⃣ EC2 Instances

* **App Server:** Flask application
* **DB Server:** MySQL database

### 2️⃣ Security Groups

* App Server: Ports `22`, `5000`, `80`
* DB Server: Port `3306` (only accessible from App Server)

---

## 🗄️ Database Setup (MySQL)

```sql
CREATE DATABASE devopsdb;

USE devopsdb;

CREATE TABLE users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100)
);

INSERT INTO users (name) VALUES ('Yash'), ('DevOps');

CREATE USER 'appuser'@'%' IDENTIFIED BY 'StrongPass123';
GRANT ALL PRIVILEGES ON devopsdb.* TO 'appuser'@'%';
FLUSH PRIVILEGES;
```

---

## 🧑‍💻 Flask Application

* Connects to MySQL database using PyMySQL
* Fetches and displays user data

```python
app.run(host="0.0.0.0", port=5000)
```

---

## 🐳 Docker Setup

### Dockerfile

```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install flask pymysql

EXPOSE 5000

CMD ["python", "app.py"]
```

---

### Build & Run

```bash
docker build -t flask-app .
docker run -d -p 5000:5000 flask-app
```

---

## 🚀 Docker Hub

* Image pushed to Docker Hub:

```
yashkhapre/flask-app:latest
```

### Pull & Run

```bash
docker pull yashkhapre/flask-app:latest
docker run -d -p 5000:5000 yashkhapre/flask-app
```

---

## 🔁 CI/CD Pipeline (GitHub Actions)

* Automatically deploys application on EC2 when code is pushed

### Workflow File

```
.github/workflows/deploy.yml
```

### Key Steps:

* SSH into EC2
* Pull latest Docker image
* Stop old container
* Run new container

---

## 🌐 Nginx Setup (Reverse Proxy)

* Routes traffic from port `80` → `5000`

```nginx
location / {
    proxy_pass http://127.0.0.1:5000;
}
```

---

## 📡 Application Access

* Via Port:

```
http://<EC2-PUBLIC-IP>:5000
```

* Via Nginx:

```
http://<EC2-PUBLIC-IP>
```

---

## 🧪 Features

* Two-tier architecture (App + DB)
* Remote database connectivity
* Docker containerization
* CI/CD automation
* Reverse proxy with Nginx

---

## 💥 Challenges Faced & Solutions

| Issue                       | Solution                      |
| --------------------------- | ----------------------------- |
| GitHub authentication error | Used Personal Access Token    |
| SSH key issues in CI/CD     | Correct key formatting        |
| Docker push denied          | Created repo & proper tagging |
| CI/CD failing (SIGTERM)     | Fixed process handling        |
| Port access issues          | Updated Security Groups       |

---

## 📈 Future Improvements

* Use Gunicorn for production
* Add HTTPS with Let's Encrypt
* Use Docker Compose (Flask + MySQL)
* Deploy on Kubernetes
* Add monitoring (CloudWatch)

---

## 👨‍💻 Author

**Yash Khapre**

* GitHub: https://github.com/yash-khapre8
* LinkedIn: [www.linkedin.com/in/-yash](http://www.linkedin.com/in/-yash)

---

## ⭐ Conclusion

This project demonstrates practical knowledge of:

* Cloud deployment
* Backend development
* DevOps practices
* CI/CD pipelines
* Containerization

---

⭐ *If you found this useful, consider giving it a star!*
