from utils.get_avg import sellers_day, sellers_week, sellers_month
from modules.quick_analysis.averages.utils.template_runner import template_runner

def avg_sellers_day():
        
    template_runner(
        title="Avg. per Seller",
        general_caption="Average per seller",
        caption="Table - Avg. Per Seller",
        dataframe=False,
        dataframe_caption=None,
        data_fn=sellers_day,
        output_name="avg_per_seller_per_day"
    )

def avg_sellers_week():
        
    template_runner(
        title="Avg. per Seller Per Week",
        general_caption="Average per seller per week",
        caption="Table - Avg. Per Seller Per Week, data from last 2 weeks",
        dataframe=False,
        dataframe_caption=None,
        data_fn=sellers_week,
        output_name="avg_per_seller_per_week"
    )

def avg_sellers_month():
        
    template_runner(
        title="Avg. per Seller Per Month",
        general_caption="Average per seller per month",
        caption="Table - Avg. Per Seller Per Month",
        dataframe=False,
        dataframe_caption=None,
        data_fn=sellers_month,
        output_name="avg_per_seller_per_month"
    )