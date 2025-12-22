# Color Palette
COLORS = {
    "macro": "#6B46C1",      # Purple
    "news": "#0891B2",       # Teal
    "performance": "#EA580C", # Orange
    "success": "#10B981",    # Green
    "failure": "#EF4444",    # Red
    "neutral": "#9CA3AF",    # Gray
}

# Category definitions
CATEGORIES = ["macro", "news", "performance"]
DEFAULT_CATEGORY = "news"

# Time period settings
MIN_DAYS = 1
MAX_DAYS = 365
DEFAULT_DAYS = 7

# Metric names (for tracking dashboard)
METRIC_NAMES = [
    "Water Usage",
    "System Efficiency",
    "Pressure Level",
    "Temperature",
    "Flow Rate"
]

# Default units
UNITS = {
    "consumption": "L",      # Liters
    "efficiency": "%",       # Percentage
    "pressure": "PSI",       # Pounds per square inch
    "temperature": "°C",     # Celsius
    "flow": "L/min",         # Liters per minute
}

# Metric pass thresholds
METRIC_THRESHOLDS = {
    "water_usage": 300,      # Max liters per day
    "efficiency": 85,        # Min efficiency percentage
    "pressure": 50,          # Min PSI
    "temperature": 25,       # Max temperature
    "flow_rate": 100,        # Min flow rate
}

# Session state defaults
SESSION_STATE_DEFAULTS = {
    "days_back": DEFAULT_DAYS,
    "category": DEFAULT_CATEGORY,
    "case_date": None,
    "case_category": DEFAULT_CATEGORY,
}