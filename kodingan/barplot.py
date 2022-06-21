from bokeh.plotting import figure, ColumnDataSource
from bokeh.models.tools import HoverTool
from bokeh.models import Panel, Spinner, ColorPicker
from bokeh.layouts import column, row
import pandas as pd


def barplot(df):
    # Create ColumnDataSource from data frame
    source = ColumnDataSource(df)

    # Movie list
    movie_list = source.data['MOVIE'].tolist()
    movie_list.reverse()

    # Add plot
    p1 = figure(
        y_range=movie_list,
        plot_width=1800,
        plot_height=1000,
        title='MOVIES TOP TICKETS SOLD PER YEAR',
        x_axis_label='TICKETS SOLD',
        y_axis_label='TITLE',
        tools="zoom_in,zoom_out,save,reset",
        toolbar_location='above'
    )

    # Render glyph
    bar =  p1.hbar(
        y='MOVIE',
        right='TICKETSSOLD',
        left=0,
        height=0.6,
        fill_color='orange',
        color = 'black',
        fill_alpha=0.5,
        source=source,
    )


    # Add Tooltips
    hover = HoverTool()
    hover.tooltips = """
      <div>
        <h3>@MOVIE</h3>
        <div><strong>Year: </strong>@YEAR</div>
        <div><strong>Genre: </strong>@GENRE</div>
        <div><strong>MPAA: </strong>@MPAARATING</div>
        <div><strong>Distributor: </strong>@DISTRIBUTOR</div>
        <div><strong>Total $ For Year: $</strong>@TOTALFORYEAR</div>
        <div><strong>Tickets Sold: </strong>@TICKETSSOLD</div>
      </div>
    """
    p1.add_tools(hover)

    #spinner bar height
    spinner1 = Spinner(title="Bar Height", low=0.1, high=1, step=0.1, value=0.6, width=100)
    spinner1.js_link('value', bar.glyph, 'height')

    #spinner bar fill alpha
    spinner2 = Spinner(title="Bar Fill Alpha", low=0.1, high=1, step=0.1, value=0.5, width=100)
    spinner2.js_link('value', bar.glyph, 'fill_alpha')

    #picker bar color
    picker = ColorPicker(title="Bar Color", width = 100)
    picker.js_link('color', bar.glyph, 'fill_color')

    widgets = column(spinner1, spinner2, picker)

    layout = row(widgets, p1)

    tab1 = Panel(child=layout, title="BAR PLOT")

    return tab1

