# Impossible Missions Force (IMF) Gadget API

## 🎯 Background
Your mission, should you choose to accept it…  
Welcome to the **Impossible Missions Force (IMF) Gadget API**, built for elite operatives to manage highly classified gadgets. 💼🛠️

---

## 🔧 Tech Stack
- **Backend:** Django REST Framework 
- **Auth:** JWT (SimpleJWT) 
- **DB:** PostgreSQL 
- **ORM:** Django ORM 
- **Deployed On:** Railway 

---

## 🔐 Authentication
All routes (except `/register/` and `/login/`) require a **JWT Access Token**.  
Use the following header for authentication:  
`Authorization: Bearer <token>` 🔑

---

## 📚 Endpoints Overview

### 👤 Auth Routes
- **POST api/v1/register/**  
  🔑 Register a new user.
  
- **POST /api/v1/login/**  
  🚪 Get JWT access & refresh tokens.
  
- **POST api/v1/logout/**  
  🔒 Revoke refresh token.

---

### 🎛️ Gadget Routes (Authenticated)
- **GET /api/v1/gadgets/**  
     List user's gadgets with mission success probability.

- **POST /api/v1/gadgets/**  
     Create a new gadget.

- **PATCH /api/v1/gadgets/{uuid}/**  
     Update gadget details.

- **DELETE /api/v1/gadgets/{uuid}/**  
     Mark gadget as "Decommissioned".

- **POST /api/v1/gadgets/{uuid}/self-destruct/**  
     Simulate self-destruct sequence.

- **GET /api/v1/gadgets/{uuid}/status/?status=**  
     Filter gadgets by status.

---

## 🌍 Base URL
`https://imf-api-7ik3.onrender.com/api/v1`  
   **Access the API** and start interacting with the gadgets right now!

---

## 📑 Refer Postman Documentation
For detailed API documentation and examples, you can view the Postman collection here -   
<a href="https://documenter.getpostman.com/view/37555239/2sB2cd4xoq#e5719b4f-ac99-4473-9091-53e8b0f9fea0">
    <img src="https://i.postimg.cc/L4kmQ1yF/postman-248x256.png" width="20" height="20">
</a>

---


## 📲 Try it Out!
Once you have the JWT Token, you can test out the API on your own:

1. **Login** to get your access token.
2. **Use Postman** to interact with the endpoints like `POST /api/gadgets/` to create new gadgets, or `GET /api/gadgets/` to list them. 

---

## 🛠️ Notes
- Ensure you are passing the JWT token in the `Authorization` header.
- All gadget-related routes are **authenticated** and require a valid JWT token.
- You can **filter gadgets** by status using the `GET /api/gadgets/{uuid}/status/?status=` route.
