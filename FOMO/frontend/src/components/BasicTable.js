import React, {useMemo, useState} from 'react'
import { useTable, useSortBy } from 'react-table'
import MOCK_DATA from './mock-data.json'
import { COLUMNS } from './columns'
import {Modal}  from "./Modal";

import './deadlineTable.css'
export const BasicTable = () => {
    
    const columns  = useMemo(() => COLUMNS, [])
    const data = useMemo(() => MOCK_DATA, [])
    
    const tableInstance = useTable({
        columns,
        data
    }, useSortBy)
    
const {
    getTableProps,
    getTableBodyProps,
    headerGroups,
    rows,
    prepareRow,
} = tableInstance

const [selectedRowData, setSelectedRowData] = useState([]);
const [modalOpen, setModalOpen] = useState(false);


const getSelectedRowwValues = selectedRow => {
    setSelectedRowData({ ...selectedRow.values });
    console.log({ ...selectedRow.values })
    setModalOpen(true);

  };

return (
  <div>
                {modalOpen && <Modal setOpenModal={setModalOpen} courseName={selectedRowData.courseName} />}


    <table {...getTableProps()}>
      <thead>
        {// Loop over the header rows
        headerGroups.map(headerGroup => (
          // Apply the header row props
          <tr {...headerGroup.getHeaderGroupProps()}>
            {// Loop over the headers in each row
            headerGroup.headers.map(column => (
              // Apply the header cell props
              <th {...column.getHeaderProps(column.getSortByToggleProps())}>
                  {column.render('Header')}
                  {/* Add a sort direction indicator */}
                  <span>
                    {column.isSorted
                      ? column.isSortedDesc
                        ? ' 🔺'
                        : ' 🔻'
                      : ''}
                  </span>
              </th>
            ))}
          </tr>
        ))}
      </thead>
      {/* Apply the table body props */}
      <tbody {...getTableBodyProps()}>
        {// Loop over the table rows
        rows.map(row => {
          // Prepare the row for display
          prepareRow(row)
          return (
            // Apply the row props
            <tr {...row.getRowProps()}
            onClick={() => getSelectedRowwValues(row)}
            >
              {// Loop over the rows cells
              row.cells.map(cell => {
                // Apply the cell props
                return (
                  <td {...cell.getCellProps()}>
                    {// Render the cell contents
                    cell.render('Cell')}
                  </td>
                )
              })}
            </tr>
          )
        })}
      </tbody>
      
    </table>
    <pre>Selected row: {JSON.stringify(selectedRowData, null, 2)}</pre>


    </div>
  )
}

