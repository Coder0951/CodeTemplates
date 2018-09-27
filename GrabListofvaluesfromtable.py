from System.Collections.Generic import List
from Spotfire.Dxp.Data import *
from Spotfire.Dxp.Application.Visuals import VisualContent
from Spotfire.Dxp.Data import RowSelection
from Spotfire.Dxp.Data import DataValueCursor
from Spotfire.Dxp.Data import DataManager 
from Spotfire.Dxp.Data import IndexSet 

dataTable = Document.ActiveDataTableReference
rows = Document.ActiveFilteringSelectionReference.GetSelection(dataTable).AsIndexSet()

vc = vis.As[VisualContent]()
dataTable = vc.Data.DataTableReference

for filter in Document.FilteringSchemes[Document.ActiveFilteringSelectionReference]:
	filteredRows = filter.FilteredRows
	marking = vc.Data.MarkingReference

marking.SetSelection(RowSelection(rows),dataTable)

# Create a cursor for the table column to get the values from.
# Add a reference to the data table in the script.
dataTable = Document.Data.Tables["AllData"]
cursor = DataValueCursor.CreateFormatted(dataTable.Columns["LookUpID"])

# Retrieve the marking selection
markings = Document.ActiveMarkingSelectionReference.GetSelection(dataTable)

# Create a List object to store the retrieved data marking selection
markedata = List [str]();

# Iterate through the data table rows to retrieve the marked rows
for row in dataTable.GetRows(markings.AsIndexSet(),cursor):
	#rowIndex = row.Index ##un-comment if you want to fetch the row index into some defined condition
	value = cursor.CurrentValue
	if value <> str.Empty and value <> "(Empty)":
		markedata.Add(value)

# Get only unique values
valData = List [str](set(markedata))

# Store in a document property
yourVariableName = ', '.join(valData)
Document.Properties["NPSIDs"] = yourVariableName
#print(yourVariableName)

marking=Application.GetService[DataManager]().Markings[markingName]
selectRows = IndexSet(dataTable.RowCount, False)
marking.SetSelection(RowSelection(selectRows),dataTable)


