import pandas as pd
from dash import Dash, Input, Output, dcc, html
import requests
import plotly.express as px
import seaborn as sns
import plotly.graph_objects as go
from plotly.data import tips
import plotly.figure_factory as ff
import numpy as np
import sys

# Making an HTTP request to the web api that is locally run
api_url = "http://127.0.0.1:5000/api/v1/resources/salaries/all"
response = requests.get(api_url)

# Reading the response into a dataframe
data = pd.read_json(response.json())

# Creating a new column called work type to differentiate among non-remote, partially remote, and fully remote work.
data.loc[data["remote_ratio"]==0, 'work_type'] =  'Non-Remote Work (<20%)'
data.loc[data["remote_ratio"]==50, 'work_type'] =  'Partially remote (~50%)'
data.loc[data["remote_ratio"]==100, 'work_type'] =  'Fully remote (>80%)'
data.reset_index()

# Creating a new column called country based on the country codes in the existing column comany_location
data.loc[data["company_location"]=='AE', 'country'] =  'United Arab Emirates'
data.loc[data["company_location"]=='AL', 'country'] =  'Albania'
data.loc[data["company_location"]=='AM', 'country'] =  'Armenia'
data.loc[data["company_location"]=='AR', 'country'] =  'Argentina'
data.loc[data["company_location"]=='AS', 'country'] =  'American Samoa'
data.loc[data["company_location"]=='AT', 'country'] =  'Austria'
data.loc[data["company_location"]=='AU', 'country'] =  'Australia'
data.loc[data["company_location"]=='BA', 'country'] =  'Bosnia and Herzegovina'
data.loc[data["company_location"]=='BE', 'country'] =  'Belgium'
data.loc[data["company_location"]=='BO', 'country'] =  'Bolivia'
data.loc[data["company_location"]=='BR', 'country'] =  'Brazil'
data.loc[data["company_location"]=='BS', 'country'] =  'Bahamas'
data.loc[data["company_location"]=='CA', 'country'] =  'Canada'
data.loc[data["company_location"]=='CF', 'country'] =  'Central African Republic'
data.loc[data["company_location"]=='CH', 'country'] =  'Switzerland'
data.loc[data["company_location"]=='CL', 'country'] =  'Chile'
data.loc[data["company_location"]=='CN', 'country'] =  'China'
data.loc[data["company_location"]=='CO', 'country'] =  'Colombia'
data.loc[data["company_location"]=='CR', 'country'] =  'Costa Rica'
data.loc[data["company_location"]=='CZ', 'country'] =  'Czechia'
data.loc[data["company_location"]=='DE', 'country'] =  'Germany'
data.loc[data["company_location"]=='DK', 'country'] =  'Denmark'
data.loc[data["company_location"]=='DZ', 'country'] =  'Algeria'
data.loc[data["company_location"]=='EE', 'country'] =  'Estonia'
data.loc[data["company_location"]=='EG', 'country'] =  'Egypt'
data.loc[data["company_location"]=='ES', 'country'] =  'Spain'
data.loc[data["company_location"]=='FI', 'country'] =  'Finland'
data.loc[data["company_location"]=='FR', 'country'] =  'France'
data.loc[data["company_location"]=='GB', 'country'] =  'United Kingdom'
data.loc[data["company_location"]=='GH', 'country'] =  'Ghana'
data.loc[data["company_location"]=='GR', 'country'] =  'Greece'
data.loc[data["company_location"]=='HK', 'country'] =  'Hong Kong'
data.loc[data["company_location"]=='HN', 'country'] =  'Honduras'
data.loc[data["company_location"]=='HR', 'country'] =  'Croatia'
data.loc[data["company_location"]=='HU', 'country'] =  'Hungary'
data.loc[data["company_location"]=='ID', 'country'] =  'Indonesia'
data.loc[data["company_location"]=='IE', 'country'] =  'Ireland'
data.loc[data["company_location"]=='IL', 'country'] =  'Israel'
data.loc[data["company_location"]=='IN', 'country'] =  'India'
data.loc[data["company_location"]=='IQ', 'country'] =  'Iraq'
data.loc[data["company_location"]=='IR', 'country'] =  'Iran'
data.loc[data["company_location"]=='IT', 'country'] =  'Italy'
data.loc[data["company_location"]=='JP', 'country'] =  'Japan'
data.loc[data["company_location"]=='KE', 'country'] =  'Kenya'
data.loc[data["company_location"]=='LT', 'country'] =  'Lithuania'
data.loc[data["company_location"]=='LU', 'country'] =  'Luxembourg'
data.loc[data["company_location"]=='LV', 'country'] =  'Latvia'
data.loc[data["company_location"]=='MA', 'country'] =  'Morocco'
data.loc[data["company_location"]=='MD', 'country'] =  'Moldova'
data.loc[data["company_location"]=='MK', 'country'] =  'North Macedonia'
data.loc[data["company_location"]=='MT', 'country'] =  'Malta'
data.loc[data["company_location"]=='MX', 'country'] =  'Mexico'
data.loc[data["company_location"]=='MY', 'country'] =  'Malaysia'
data.loc[data["company_location"]=='NG', 'country'] =  'Nigeria'
data.loc[data["company_location"]=='NL', 'country'] =  'Netherlands'
data.loc[data["company_location"]=='NZ', 'country'] =  'New Zealand'
data.loc[data["company_location"]=='PH', 'country'] =  'Philippines'
data.loc[data["company_location"]=='PK', 'country'] =  'Pakistan'
data.loc[data["company_location"]=='PL', 'country'] =  'Poland'
data.loc[data["company_location"]=='PR', 'country'] =  'Puerto Rico'
data.loc[data["company_location"]=='PT', 'country'] =  'Portugal'
data.loc[data["company_location"]=='RO', 'country'] =  'Romania'
data.loc[data["company_location"]=='RU', 'country'] =  'Russian'
data.loc[data["company_location"]=='SE', 'country'] =  'Sweden'
data.loc[data["company_location"]=='SG', 'country'] =  'Singapore'
data.loc[data["company_location"]=='SI', 'country'] =  'Slovenia'
data.loc[data["company_location"]=='SK', 'country'] =  'Slovakia'
data.loc[data["company_location"]=='SM', 'country'] =  'San Marino'
data.loc[data["company_location"]=='TH', 'country'] =  'Thailand'
data.loc[data["company_location"]=='TR', 'country'] =  'Turkey'
data.loc[data["company_location"]=='UA', 'country'] =  'Ukraine'
data.loc[data["company_location"]=='US', 'country'] =  'United States of America'
data.loc[data["company_location"]=='VN', 'country'] =  'Vietnam'
data.loc[data["company_location"]=='ZA', 'country'] =  'South Africa'

data.reset_index()

# Listing the unique years and locations into the new variables
work_year = data["work_year"].sort_values().unique()
company_location = data["country"].sort_values().unique()


external_stylesheets = [
    {
        "href": (
            "https://fonts.googleapis.com/css2?"
            "family=Lato:wght@400;700&display=swap"
        ),
        "rel": "stylesheet",
    },
]
app = Dash(__name__, external_stylesheets=external_stylesheets)
app.title = "Career Analysis for Data Science Across the Globe"

summary_work_year = data.groupby('work_year').agg({'work_year':'size', 'salary':'mean'}).rename(columns={'work_year':'count','mean':'mean_sent'}).reset_index()
summary_work_year_sanitized_data=summary_work_year[summary_work_year['count'].ge(30)].sort_values(by=['salary'],  ascending=False).head(10)
summary_work_year_sanitized_data["work_year"]=summary_work_year_sanitized_data["work_year"].map(str)

fig = px.bar(summary_work_year_sanitized_data.sort_values(by=['work_year'],  ascending=True), x="work_year", y="count", title='2020-2023 Worldwide Employment Count Record for Data Science', color_discrete_sequence=px.colors.sequential.RdBu_r)

# Defines the dashboard format
app.layout = html.Div(
    children=[
        html.Div(
            children=[
                html.H1(
                    children="Career Analysis for Data Science Across the Globe", className="header-title"
                ),
                html.P(
                    children=(
                        "Discovering Career and Salary Trends between 2020 to 2023" 
                    ),
                    className="header-description",
                ),
            ],
            className="header",
        ),

        # Creating the filters
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(children="Work Year", className="menu-title"),
                        dcc.Dropdown(
                            id="work-year-filter",
                            options=[
                                {"label": year, "value": year}
                                for year in work_year
                            ],
                            value="All",
                            clearable=False,
                            className="dropdown",
                        ),
                    ]
                ),
                html.Div(
                    children=[
                        html.Div(children="Company Location", className="menu-title"),
                        dcc.Dropdown(
                            id="company-location-filter",
                            options=[
                                {
                                    "label": company.title(),
                                    "value": company,
                                }
                                for company in company_location
                            ],
                            value="All",
                            clearable=False,
                            searchable=False,
                            className="dropdown",
                        ),
                    ],
                ),
            ],
            className="menu",
        ),
        html.Div(
            children=[

                # Job count per year
                html.Div(
                    children=dcc.Graph(
                        id="bar-chart",
                        figure=fig
                    ),
                     className="card",
                ),

                # Remote or Non-remote Work Type (%) 
                html.Div(
                    children=dcc.Graph(
                        id="worktype-chart-figure",
                    ),
                     className="card",
                ),

                # Median Salary per work type
                html.Div(
                    children=dcc.Graph(
                        id="salary-chart-figure",
                        config={"displayModeBar": False},
                    ),
                    className="card",
                ),

                # Top 10 in demand high paying jobs 
                html.Div(
                    children=dcc.Graph(
                        id="top-ten-indemand-chart-figure",
                        config={"displayModeBar": False},
                    ),
                     className="card",
                ),

                # Top 10 highest paying jobs
                html.Div(
                    children=dcc.Graph(
                        id="top-ten-chart-figure",
                        config={"displayModeBar": False},
                    ),
                     className="card",
                ),

                # Top 10 highest paying jobs in table, sorted according to salary
                html.Div(
                    children=dcc.Graph(
                        id="top-ten-table-figure",
                        config={"displayModeBar": False},
                    ),
                     className="card",
                ),
                
            ],
            className="wrapper",
        ),
    ]
)

# Dash function to update 5 figures based on the user's choice of filters
@app.callback(
    Output("salary-chart-figure", "figure"),
    Output("worktype-chart-figure", "figure"),
    Output("top-ten-indemand-chart-figure", "figure"),
    Output("top-ten-chart-figure", "figure"),
    Output("top-ten-table-figure", "figure"),

    Input("work-year-filter", "value"),
    Input("company-location-filter", "value"),
)

def update_charts(work_year,company_location):

    print("workyear: " + str(work_year))
    print("company_location: " + str(company_location))

    if work_year == "All" and str(company_location) == "None":
        filtered_data=data
    elif work_year == "All" and str(company_location) != "None":
        filtered_data = data.query("country == @company_location")
    elif work_year != "All" and str(company_location) == "None":
        filtered_data = data.query("work_year == @work_year")
    else:
        filtered_data = data.query("work_year == @work_year and country == @company_location")


    fig_pie_chart = px.pie(filtered_data, values='salary_in_usd', names='work_type', title=' Remote or Non-remote Work Type (%)', color_discrete_sequence=px.colors.sequential.RdBu_r)

    # Designing plot for Median Salary per work type
    remote_ratio_plot = go.Figure()
    remote_ratio_plot.add_trace(go.Box(y=filtered_data['salary_in_usd'][(filtered_data['remote_ratio'] == 0)],  fillcolor="#042f66",marker=dict(color='#042f66'), quartilemethod="linear", name="Non-Remote Work (<20%)" ))
    remote_ratio_plot.add_trace(go.Box(y=filtered_data['salary_in_usd'][(filtered_data['remote_ratio'] == 50)], fillcolor="#eab676",marker=dict(color='#eab676'), quartilemethod="inclusive", name="Partially remote (~50%)"))
    remote_ratio_plot.add_trace(go.Box(y=filtered_data['salary_in_usd'][(filtered_data['remote_ratio'] == 100)], fillcolor="#e28743",marker=dict(color='#e28743'), quartilemethod="exclusive", name="Fully remote (>80%)"))
    remote_ratio_plot.update_traces(boxpoints='all', jitter=0)
    remote_ratio_plot.update_layout(title=dict(text="Median Salary per Work Type"))

    # Creating the data for job titles, their count, and their average salaries
    summary = filtered_data.groupby('job_title').agg({'job_title':'size', 'salary_in_usd':'mean'}).rename(columns={'job_title':'count','mean':'mean_sent'}).reset_index()
    sanitized_data=summary.sort_values(by=['salary_in_usd'],  ascending=False).head(10)
    count=sanitized_data["count"].values
    job_title=sanitized_data["job_title"].values
    salary_in_usd=sanitized_data["salary_in_usd"].values
    sanitized_data.rename(columns = {'count':'Count', 'job_title':'Job Description','salary_in_usd':'Salary'}, inplace = True)
    
    # Creating the table
    fig_table_data=ff.create_table(sanitized_data.round(2), height_constant=60, colorscale=px.colors.sequential.Blues_r,)

    # Creating the bar figure for job counts of the top 10 highest paying jobs
    fig_bar_line = go.Figure(
    data=go.Bar(
        x=job_title,
        y=count,
        name="Count of Jobs",
        marker=dict(color="#1e81b0"),
        )
    )
    # Adding a scatter line representing the average salary
    fig_bar_line.add_trace(
    go.Scatter(
        x=job_title,
        y=salary_in_usd,
        yaxis="y2",
        name="Average Salary",
        marker=dict(color="crimson"),
        )
    )
    # Setting the axis for job counts to the left
    fig_bar_line.update_layout(
    legend=dict(orientation="v"),
    yaxis=dict(
        title=dict(text="Count of Jobs"),
        side="left",
    ),
    # Setting the axis for average salary to the right, overlayed on the first axis.
    yaxis2=dict(
        title=dict(text="Average Salary"),
        side="right",
        overlaying="y",
        tickmode="auto",
        ),
        title=dict(text="Top 10 Highest Paying Jobs")
    )

    # This section creates the figure for top 10 High Demand Career in Data Science vs Salary
    sanitized_data2=summary.sort_values(by=['count'],  ascending=False).head(10)
    print(sanitized_data2)
    count=sanitized_data2["count"].values
    job_title=sanitized_data2["job_title"].values
    salary_in_usd=sanitized_data2["salary_in_usd"].values
    # Creating the bar figure for the job count
    fig_bar_line2 = go.Figure(
    data=go.Bar(
        x=job_title,
        y=count,
        name="Count of Jobs",
        marker=dict(color="#1e81b0"),
        )
    )
    # Creating the scatter line for the average salary
    fig_bar_line2.add_trace(
    go.Scatter(
        x=job_title,
        y=salary_in_usd,
        yaxis="y2",
        name="Average Salary",
        marker=dict(color="crimson"),
        )
    )
    # Layouting the figures
    # Setting the count of jobs to be the left vertical axis
    fig_bar_line2.update_layout(
    legend=dict(orientation="v"),
    yaxis=dict(
        title=dict(text="Count of Jobs"),
        side="left",
    ),
    # Setting the average salary to be the right vertical axis
    yaxis2=dict(
        title=dict(text="Average Salary"),
        side="right",
        overlaying="y",
        tickmode="auto",
        ),
        title=dict(text="Top 10 High Demand Career in Data Science vs Salary")
    )

    return fig_pie_chart, remote_ratio_plot, fig_bar_line2, fig_bar_line, fig_table_data

if __name__ == "__main__":
    app.run_server(debug=True)