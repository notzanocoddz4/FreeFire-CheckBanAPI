# FreeFire-CheckBanAPI

A Python Flask-based API designed to check the ban status of Garena FreeFire accounts using unique player IDs (UIDs).

---

## 📁 Project Structure

```text
FreeFire-CheckBanAPI/
│
├── app/
│   ├── routes/
│   │   ├── checkbanned.py
│   │   └── api.py
│   │
│   └── utils/
│       ├── garena_checkbanned.py
│       ├── get_headers.py
│       └── get_printColored.py
│
├── init.py
├── readme.md
└── requirements.txt
```

---

## 🛠️ Requirements

```text
flask
requests
gunicorn
```

---

## 🚀 Features

* **Real-time Ban Validation:** Instantly fetches the status of a specific FreeFire UID.
* **Flask Blueprint Architecture:** Modular layout makes it easy to scale and add more routes.
* **Graceful Error Handling:** Handlers for missing query parameters and invalid/non-existent user UIDs.

---

## 🛠️ Getting Started

### Prerequisites

Make sure you have Python 3.x installed on your machine.

### Installation

1. Clone the repository from GitHub:

```bash
git clone https://github.com/notzanocoddz4/FreeFire-CheckBanAPI.git

```

2. Navigate into the project root directory:

```bash
cd FreeFire-CheckBanAPI

```

3. Install the necessary dependencies:

```bash
pip install -r requirements.txt

```

---

### 🚀 Running the API

Start the Flask application using the main initialization script:

```bash
python init.py

```

---

## 🛣️ API Endpoints

### Check Account Ban Status

Queries the target Garena verification system to determine whether a player is banned.

* **Endpoint:** `/checkbanned`
* **Method:** `GET`
* **Query Parameters:**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `uid` | `string` | **Yes** | The unique Garena/FreeFire player ID to check. |

---

### 📥 Example Request

```http
GET /checkbanned?uid=123456789 HTTP/1.1
Host: localhost:5000

```

---

### 📤 Responses

#### 🟢 200 OK (Account is Banned)

Returned when the account exists and is currently banned.

```json
{
  "uid": "123456789",
  "is_banned": true,
  "status": "banned"
}

```

#### 🟢 200 OK (Account is Clean)

Returned when the account exists and has no active bans.

```json
{
  "uid": "123456789",
  "is_banned": false,
  "status": "clean"
}

```

#### 🟡 400 Bad Request

Returned when the `uid` parameter is missing from the query string.

```json
{
  "status": "error",
  "message": "Missing 'uid' query parameter."
}

```

#### 🔴 404 Not Found

Returned if the UID does not exist, or if the upstream verification service fails.

```json
{
  "status": "error",
  "message": "Could not verify UID '123456789'. It may not exist or the service is down."
}

```

---

## 👥 Credits

* **[notzanocoddz4](https://github.com/notzanocoddz4)** - Main developer