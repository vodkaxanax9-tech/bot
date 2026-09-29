"""
Health check для Railway
"""
import os
import sys

def check_bot_token():
    """Проверяет что BOT_TOKEN установлен и валиден"""
    token = os.environ.get("BOT_TOKEN")
    if not token:
        print("ERROR: BOT_TOKEN not set in environment variables")
        return False
    
    if token == "your_bot_token_here":
        print("ERROR: BOT_TOKEN has default value, please set real token")
        return False
    
    # Проверяем валидность токена (длина)
    if len(token) < 20:
        print("ERROR: BOT_TOKEN seems too short to be valid")
        return False
    
    print(f"OK: BOT_TOKEN is set (length: {len(token)})")
    return True

def check_dependencies():
    """Проверяет что все зависимости установлены"""
    try:
        import telegram
        print(f"OK: python-telegram-bot version {telegram.__version__}")
    except ImportError:
        print("ERROR: python-telegram-bot not installed")
        return False
    
    try:
        import requests
        print(f"OK: requests version {requests.__version__}")
    except ImportError:
        print("ERROR: requests not installed")
        return False
    
    return True

if __name__ == "__main__":
    print("Running health checks...")
    
    checks = [
        ("BOT_TOKEN", check_bot_token),
        ("Dependencies", check_dependencies),
    ]
    
    all_passed = True
    for name, check_func in checks:
        print(f"\nChecking {name}:")
        if not check_func():
            all_passed = False
    
    if all_passed:
        print("\n✅ All health checks passed")
        sys.exit(0)
    else:
        print("\n❌ Some health checks failed")
        sys.exit(1)
