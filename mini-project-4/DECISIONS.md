# DECISIONS.md

## 1. Connection Management

I created a simple connection manager class to keep track of connected WebSocket clients. Every time a user opens the app, their WebSocket connection is added to the active connections list.

If a user closes the tab or disconnects during voting, the connection is removed from the list. I handled disconnects using try/except so the application does not crash when someone leaves unexpectedly.

---

## 2. State Storage

For this project, I stored the poll data in memory because it was simpler and enough for testing realtime communication.

The downside is that if the server restarts, all poll data and votes are lost. In a real production application, I would use a database like PostgreSQL so the data stays permanently stored.

---

## 3. Concurrency

If two people vote at the same time, FastAPI can process both requests asynchronously. In my current implementation I did not add extra protection for race conditions.

This means there could be small inconsistencies if many users vote at exactly the same moment. For a larger production system, database transactions or locks would probably be necessary.

---

## 4. REST vs WebSocket

The REST endpoint works with normal request-response communication. A client sends a vote request and receives a response once.

WebSocket is different because the connection stays open continuously. This allows the server to instantly broadcast vote updates to all connected users without refreshing the page.

I think REST is more useful for normal API operations, while WebSockets are much better for realtime features like live polls or chat applications.