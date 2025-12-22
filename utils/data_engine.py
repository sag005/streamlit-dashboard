import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import numpy as np
from constants import METRIC_NAMES, CATEGORIES


@st.cache_data
def generate_timeseries_data(days_back: int, category: str, seed: int = 42) -> pd.DataFrame:
    """
    Generate mock time-series data for the tracking dashboard.

    Args:
        days_back: Number of days of history to generate (1-365)
        category: Category to generate data for ('macro', 'news', 'performance')
        seed: Random seed for reproducibility

    Returns:
        DataFrame with columns: date, metric_name, value (0-100%)
    """
    np.random.seed(seed + hash(category) % 1000)

    days_back = max(1, min(days_back, 365))
    category = category.lower()

    if category not in CATEGORIES:
        category = "news"

    # Generate date range
    end_date = datetime.now().date()
    start_date = end_date - timedelta(days=days_back - 1)
    dates = pd.date_range(start=start_date, end=end_date, freq='D').date

    # Generate data for 5 metrics
    data = []

    for metric_name in METRIC_NAMES:
        base_value = np.random.uniform(40, 80)

        # Category-specific variation
        if category == "macro":
            volatility = 0.08
            trend = 0.001
        elif category == "news":
            volatility = 0.12
            trend = -0.0005
        else:  # performance
            volatility = 0.06
            trend = 0.002

        # Generate values with trend and noise
        for i, date in enumerate(dates):
            noise = np.random.normal(0, volatility)
            trend_component = trend * i
            value = base_value + noise + trend_component
            value = max(0, min(100, value))

            data.append({
                "date": date,
                "metric_name": metric_name,
                "value": round(value, 2)
            })

    return pd.DataFrame(data)


@st.cache_data
def generate_case_data(date_str: str, category: str, seed: int = 42) -> dict:
    """
    Generate mock case data with metrics and response text.

    Args:
        date_str: Date as string (YYYY-MM-DD)
        category: Category ('macro', 'news', 'performance')
        seed: Random seed for reproducibility

    Returns:
        Dictionary with keys: date, category, response_text, metrics
    """
    np.random.seed(seed + hash(date_str + category) % 1000)

    category = category.lower()
    if category not in CATEGORIES:
        category = "news"

    try:
        case_date = datetime.strptime(date_str, "%Y-%m-%d").date()
    except:
        case_date = datetime.now().date()

    # Generate response text based on category
    response_texts = {
        "macro": "Overall system performance is stable with minor fluctuations in efficiency metrics. Water consumption remains within acceptable limits. Recommend continued monitoring of pressure levels to prevent potential issues.",
        "news": "Recent updates show mixed results across all metrics. System efficiency has improved by 3% compared to last week. Flow rate has stabilized after previous fluctuations. Continue monitoring temperature sensors.",
        "performance": "System is performing at peak levels with all metrics exceeding minimum thresholds. Efficiency has improved by 5.2% this month. Water usage optimization is on track. No immediate concerns identified."
    }

    response_text = response_texts.get(category, response_texts["news"])

    # Generate 3-5 metrics (max available is 5)
    num_metrics = np.random.randint(3, 6)
    metrics = []

    metric_configs = [
        ("Water Usage", 250, 350, "L/day", "Higher is worse"),
        ("System Efficiency", 75, 95, "%", "Higher is better"),
        ("Pressure Level", 45, 65, "PSI", "In range is better"),
        ("Temperature", 20, 30, "°C", "Normal range"),
        ("Flow Rate", 80, 120, "L/min", "Higher is better"),
    ]

    selected_metrics = np.random.choice(
        len(metric_configs),
        size=num_metrics,
        replace=False
    )

    for idx in selected_metrics:
        name, min_val, max_val, unit, description = metric_configs[idx]

        score = np.random.uniform(min_val, max_val)
        minimum_pass = (min_val + max_val) / 2
        is_pass = score >= minimum_pass

        if is_pass:
            reasons = [
                f"{name} is within acceptable range and performing as expected. The system has maintained stable metrics throughout the monitoring period. No immediate action is required, but continued monitoring is recommended to ensure sustained performance.",
                f"{name} performance is satisfactory with no immediate concerns identified. Current levels exceed minimum thresholds and show positive trends. The metric has remained consistent over the evaluation period with no significant fluctuations or anomalies detected.",
                f"{name} meets minimum requirements and shows positive trends across the evaluation period. Performance indicators are aligned with expected values and demonstrate system stability. Recommend continuing current operational parameters.",
                f"{name} shows good performance and is well-optimized for current conditions. The system is operating efficiently with minimal deviation from target values. All parameters are within acceptable ranges and the metric requires no immediate intervention.",
                f"{name} exceeds baseline expectations and maintains consistent quality throughout the monitoring period. Performance metrics indicate optimal system function with sustained high-quality results. This metric serves as a positive indicator for overall system health.",
            ]
        else:
            reasons = [
                f"{name} is slightly below target and requires monitoring over the next period. While not critical, gradual improvement is recommended. Review operational parameters and implement corrective measures if decline continues. Schedule follow-up assessment within the next review cycle.",
                f"{name} needs attention and optimization to reach acceptable levels. Current performance is below established thresholds and requires investigation. Identify root causes and develop improvement plan. Escalate to operations team if no improvement within specified timeframe.",
                f"{name} could be optimized further to meet performance standards. Performance has degraded compared to previous periods. Analyze recent changes and environmental factors that may have contributed to decline. Implement corrective actions and monitor closely.",
                f"{name} is currently below minimum threshold and requires immediate action to prevent further degradation. This metric requires urgent attention from the operations team. Implement immediate corrective measures and increase monitoring frequency. Escalate to management if unable to resolve.",
                f"{name} shows declining trend and should be reviewed for potential issues. Performance has consistently decreased over the monitoring period indicating systematic problems. Conduct root cause analysis and develop comprehensive action plan. Priority escalation recommended.",
            ]

        reason = np.random.choice(reasons)

        metrics.append({
            "name": name,
            "score": round(score, 2),
            "is_pass": bool(is_pass),
            "reason": reason,
            "minimum_pass": round(minimum_pass, 2),
            "unit": unit
        })

    return {
        "date": case_date.isoformat(),
        "category": category,
        "response_text": response_text,
        "metrics": metrics
    }