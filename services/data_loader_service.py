def load_data():
    return {
        "summary": {
            "total_portfolio": 10,
            "avg_size_of_portfolio": 15000000,
            "avg_summaries_in_each_portfolio": 8
        },
        "run_configuration": {
            "model_setting": {
                "model_name": "claude-sonnet-4",
                "temperature": "0.7",
                "thinking": True,
                "prompt_version": "v2.0"
            },
            "news_setting": {
                "start_date": "2024-01-01",
                "end_date": "2024-12-31",
                "days": 365
            },
            "performance_setting": {
                "start_date": "2024-01-01",
                "end_date": "2024-12-31",
                "days": 365
            }
        },
        "portfolios": [
            {
                "holdings": {
                    "AAPL": {"movement_dollars": 1500, "movement_percentage": 2.5},
                    "GOOGL": {"movement_dollars": -800, "movement_percentage": -1.2},
                    "MSFT": {"movement_dollars": 2200, "movement_percentage": 3.1}
                },
                "ticker_summaries": {
                    "AAPL": ["Summary 1 for AAPL", "Summary 2 for AAPL", "Summary 3 for AAPL", "Summary 4 for AAPL"],
                    "GOOGL": ["Summary 1 for GOOGL", "Summary 2 for GOOGL", "Summary 3 for GOOGL", "Summary 4 for GOOGL"],
                    "MSFT": ["Summary 1 for MSFT", "Summary 2 for MSFT", "Summary 3 for MSFT", "Summary 4 for MSFT"]
                },
                "portfolio_insight": "This portfolio shows strong tech sector performance with positive momentum."
            },
            {
                "holdings": {
                    "TSLA": {"movement_dollars": -500, "movement_percentage": -0.8},
                    "NVDA": {"movement_dollars": 3000, "movement_percentage": 4.2}
                },
                "ticker_summaries": {
                    "TSLA": ["Summary 1 for TSLA", "Summary 2 for TSLA", "Summary 3 for TSLA", "Summary 4 for TSLA"],
                    "NVDA": ["Summary 1 for NVDA", "Summary 2 for NVDA", "Summary 3 for NVDA", "Summary 4 for NVDA"]
                },
                "portfolio_insight": "AI-focused portfolio with NVDA driving gains despite TSLA weakness."
            }
        ]
    }