PORT = 3050

# name -> secret (32 hex chars)
USERS = {
    "tg":  "00000000000000000000000000000001",
    # "tg2": "0123456789abcdef0123456789abcdef",
}

MODES = {
    # Classic mode, easy to detect
    "classic": False,

    # Makes the proxy harder to detect
    # Can be incompatible with very old clients
    "secure": False,

    # Makes the proxy even more hard to detect
    # Can be incompatible with old clients
    "tls": True
}

# The domain for TLS mode, bad clients are proxied there
# Use random existing domain, proxy checks it on start
# TLS_DOMAIN = "www.google.com"

# Tag for advertising, obtainable from @MTProxybot
# AD_TAG = "3c09c680b76ee91a4c25ad51f742267d"

# Buffer size optimization for 8GB RAM server
# Adaptive buffer configuration: (low_buffer, user_threshold, high_buffer)
# When concurrent users < threshold, use high buffer; otherwise use low buffer
TO_CLT_BUFSIZE = (524288, 50, 2097152)  # (512KB, 50 users, 2MB)
TO_TG_BUFSIZE = (524288, 50, 2097152)   # (512KB, 50 users, 2MB)

# User TCP connection limits - set reasonable limits to prevent abuse
# Format: {"username": max_connections}
USER_MAX_TCP_CONNS = {
    "tg": 100,  # Allow up to 100 concurrent connections per user
}

# Performance optimization settings
CLIENT_KEEPALIVE = 20*60        # Keep connections alive for 20 minutes
CLIENT_HANDSHAKE_TIMEOUT = 30   # 30 seconds handshake timeout
CLIENT_ACK_TIMEOUT = 10*60      # 10 minutes ACK timeout
TG_CONNECT_TIMEOUT = 15         # 15 seconds Telegram connection timeout

# Performance monitoring and logging settings
ENABLE_STATS = True             # Enable connection statistics
STATS_PRINT_PERIOD = 600        # Print stats every 10 minutes
LOG_LEVEL = "INFO"              # Logging level: DEBUG, INFO, WARNING, ERROR
MAX_CONCURRENT_USERS = 200      # Maximum concurrent users (for monitoring)
MEMORY_USAGE_WARNING = 80       # Warning threshold for memory usage (percentage)
