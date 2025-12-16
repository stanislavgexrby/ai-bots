# Utils

This directory contains helper functions and utilities used throughout the project.

## Utility Examples

### logging.py
Logging configuration for the project.

```python
def setup_logger(name: str, log_file: str, level: str):
    """Setup logger with file rotation"""
    pass

def log_api_call(provider: str, tokens: int, cost: float):
    """Log AI API calls"""
    pass
```

### validators.py
Input data validation.

```python
def validate_api_key(key: str) -> bool:
    """Validate API key format"""
    pass

def sanitize_user_input(text: str) -> str:
    """Sanitize user input"""
    pass
```

### formatters.py
Text and data formatting.

```python
def format_code_block(code: str, language: str) -> str:
    """Format code block for display"""
    pass

def truncate_text(text: str, max_length: int) -> str:
    """Truncate text while preserving meaning"""
    pass
```

### rate_limiter.py
Request rate management.

```python
class RateLimiter:
    def check_rate_limit(self, user_id: str) -> bool:
        """Check request rate limit"""
        pass

    def increment_usage(self, user_id: str):
        """Increment usage counter"""
        pass
```

### context_manager.py
Conversation context management.

```python
def build_context(messages: list, max_tokens: int) -> str:
    """Build context from message history"""
    pass

def summarize_context(messages: list) -> str:
    """Summarize long context"""
    pass
```

### crypto.py
Cryptographic functions.

```python
def hash_password(password: str) -> str:
    """Hash password"""
    pass

def encrypt_sensitive_data(data: str) -> str:
    """Encrypt sensitive data"""
    pass
```

## Principles

1. **DRY** - avoid code duplication
2. **Simplicity** - functions should do one thing well
3. **Reusability** - utilities should be universal
4. **Documentation** - every function should have a docstring
