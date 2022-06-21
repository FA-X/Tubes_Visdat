import numpy as np
import pandas as pd
from bokeh.plotting import figure, ColumnDataSource
from bokeh.transform import factor_mark
from bokeh.models.tools import HoverTool
from bokeh.models import Spinner, ColorPicker, Panel
from bokeh.layouts import column, row


def marker_map(df):
    source = ColumnDataSource(df)

    # Movie list
    movies = sorted(df.MOVIE)

    MARKERS = ['asterisk', 'circle', 'circle_cross', 'circle_dot', 'circle_x', 'circle_y', 
    'cross', 'diamond', 'diamond_cross','dash','diamond_dot','dot','hex','hex_dot','inverted_triangle',
    'plus','square','square_cross','square_dot','square_pin','square_x','star','star_dot','triangle',
    'triangle_dot','triangle_pin','x','y']

    p2 = figure(
        plot_width=1500,
        plot_height=800,
        title='MOVIES INCOME BY TICKETS SOLD',
        x_axis_label='TICKETS SOLD',
        y_axis_label='TOTAL FOR YEAR (k $)',
    )

    points = p2.scatter(
        'TICKETSSOLD',
        'TOTALFORYEAR',
        size=20,
        color='grey',
        fill_alpha=0.5,
        marker=factor_mark('MOVIE',MARKERS, movies),
        legend_group='MOVIE',
        source=source,
    )

    p2.legend.orientation = "vertical"
    p2.legend.background_fill_color = "#fafafa"
    p2.legend.location = 'bottom_right'

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
    p2.add_tools(hover)

    #spinner points size
    spinner1 = Spinner(title="Points Size", low=1, high=50, step=2, value=20, width=100)
    spinner1.js_link('value', points.glyph, 'size')

    #spinner points fill alpha
    spinner2 = Spinner(title="Points Fill Alpha", low=0.1, high=1, step=0.1, value=0.5, width=100)
    spinner2.js_link('value', points.glyph, 'fill_alpha')

    #picker points color
    picker = ColorPicker(title="Points Color", width = 100)
    picker.js_link('color', points.glyph, 'fill_color')

    widgets = column(spinner1, spinner2, picker)

    layout = row(widgets, p2)

    tab2 = Panel(child=layout, title="MARKER MAP")

    return tab2


