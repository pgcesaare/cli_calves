from modules.quick_analysis.averages.screens.avg_per_time import avg_per_day, avg_per_week, avg_per_month

def average_controller(period):

    if period == "daily":
        avg_per_day()
    if period == "weekly":
        avg_per_week()
    if period == "monthly":
        avg_per_month()