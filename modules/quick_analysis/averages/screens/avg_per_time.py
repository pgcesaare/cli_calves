from modules.quick_analysis.averages.utils.template_runner import template_runner
from utils.get_avg import calves_day, calves_week, calves_month


def avg_per_day():
        
    template_runner(
        title="Avg. per Day",
        general_caption="Average per day",
        caption="Table - Avg. Per Day, data from last 2 weeks",
        dataframe=True,
        dataframe_caption="Table - Avg. Per Day, data from last 2 weeks",
        data_fn=calves_day,
        output_name="avg_per_day"
    )
            
def avg_per_week():
        
    template_runner(
        title="Avg. per Week",
        general_caption="Average per week",
        caption="Table - Avg. Per Week",
        dataframe=True,
        dataframe_caption="Table - Avg. Per Week",
        data_fn=calves_week,
        output_name="avg_per_week"
    )
            
def avg_per_month():
        
    template_runner(
        title="Avg. per Month",
        general_caption="Average per month",
        caption="Table - Avg. Per Month",
        dataframe=True,
        dataframe_caption="Table - Avg. Per Month",
        data_fn=calves_month,
        output_name="avg_per_month"
    )