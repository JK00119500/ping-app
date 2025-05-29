
# 🏓 Ping App – Dockerized Python HTTP Server

This is a minimal HTTP server built with Python's built-in `http.server`, containerized using Docker, and ready to deploy on an EC2 instance.

---

## 🌐 What It Does

When you visit:

```
http://13.232.34.40:8085/ping
```

You will see:

```
Pong
```

---

## 📁 Files

- `server.py` – A simple Python HTTP server
- `Dockerfile` – Docker instructions
- `README.md` – You are here

---

## 🧰 Requirements

- Docker installed locally
- A Docker Hub account
- An EC2 instance with Docker installed (Ubuntu recommended)
- Port **8085** open in EC2 security group

---

## 🚀 Deployment Steps

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/ping-app.git
cd ping-app
```

---

### 2. Build the Docker Image

```bash
docker build -t YOUR_DOCKERHUB_USERNAME/ping-app:latest .
```

---

### 3. Push to Docker Hub

```bash
docker login
docker push YOUR_DOCKERHUB_USERNAME/ping-app:latest
```

---

### 4. SSH into Your EC2 Instance

```bash
ssh ubuntu@your-ec2-ip
```

Make sure Docker is installed. If not:

```bash
sudo apt update
sudo apt install docker.io -y
sudo systemctl start docker
sudo systemctl enable docker
```

---

### 5. Pull and Run the Docker Container

```bash
docker pull YOUR_DOCKERHUB_USERNAME/ping-app:latest
docker run -d -p 8085:8085 YOUR_DOCKERHUB_USERNAME/ping-app:latest
```

---

### 6. Test It!

Open your browser and go to:

```
http://<your-ec2-ip>:8085/ping
```

You should see: `Pong`

---

## ✅ Done!

This should take **under 5 minutes** to deploy if Docker is already set up.

