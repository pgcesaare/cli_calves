from modules.quick_analysis.averages.screens.avg_per_seller import avg_sellers_day, avg_sellers_month, avg_sellers_week

def sellers_controller(period):

    if period == "daily":
        avg_sellers_day()
    if period == "weekly":
        avg_sellers_week()
    if period == "monthly":
        avg_sellers_month()