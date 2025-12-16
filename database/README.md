# Database

This directory contains code for working with databases.

## Structure

### models/

Contains data models for ORM (SQLAlchemy, Tortoise, MongoEngine, etc.).

**Model examples:**

**users.py** - user model:
```python
class User:
    - id
    - username
    - created_at
    - settings (JSON)
```

**messages.py** - message model:
```python
class Message:
    - id
    - user_id
    - content
    - role (user/assistant/system)
    - timestamp
    - conversation_id
```

**conversations.py** - conversation model:
```python
class Conversation:
    - id
    - user_id
    - title
    - created_at
    - updated_at
    - metadata (JSON)
```

### migrations/

Contains database schema migrations.

**Tools used:**
- Alembic (for SQLAlchemy)
- Django migrations
- Or custom migration scripts

## Database Connections

### PostgreSQL

Used for:
- Message history storage
- User data
- Metrics and analytics

### MongoDB

Used for:
- Document-oriented storage
- Flexible data schemas
- Large volumes of unstructured data

### Redis

Used for:
- Response caching
- Session management
- Rate limiting
- Temporary context storage

## Usage Example

```python
from database.models.users import User
from database.models.messages import Message

# Create user
user = User.create(username="john_doe")

# Save message
message = Message.create(
    user_id=user.id,
    content="Hello, AI!",
    role="user"
)

# Get history
history = Message.get_by_user(user.id, limit=10)
```

## Principles

1. **Abstraction** - using ORM for database independence
2. **Migrations** - all schema changes through migrations
3. **Indexing** - proper indexes for performance
4. **Normalization** - following database design principles
