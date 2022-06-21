import pandas as pd

from bokeh.models import ColumnDataSource, Panel
from bokeh.models.widgets import TableColumn, DataTable

def table(df):
        source = ColumnDataSource(df)

	    # Columns of table
        columns = [TableColumn(field='YEAR', title='Year'),
					 TableColumn(field='MOVIE', title='Movie Title'),
					 TableColumn(field='MPAARATING', title='MPAA Rating'),
					 TableColumn(field='DISTRIBUTOR', title='Distributor'),
					 TableColumn(field='TOTALFORYEAR', title='Total For Year ($)'),
					 TableColumn(field='TOTALIN2019DOLLARS', title='Total in 2019 Dollars'),
                     TableColumn(field='TICKETSSOLD', title='Tickets Sold')]

        data_table = DataTable(source=source, columns=columns, width=1000, height=700)
        tab4 = Panel(child = data_table, title = 'TABLE')

        return tab4