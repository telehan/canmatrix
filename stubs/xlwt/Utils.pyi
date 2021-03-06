# Stubs for xlwt.Utils (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

def col_by_name(colname: Any): ...
def cell_to_rowcol(cell: Any): ...
def cell_to_rowcol2(cell: Any): ...
def rowcol_to_cell(row: Any, col: Any, row_abs: bool = ..., col_abs: bool = ...): ...
def rowcol_pair_to_cellrange(row1: Any, col1: Any, row2: Any, col2: Any, row1_abs: bool = ..., col1_abs: bool = ..., row2_abs: bool = ..., col2_abs: bool = ...): ...
def cellrange_to_rowcol_pair(cellrange: Any): ...
def cell_to_packed_rowcol(cell: Any): ...
def valid_sheet_name(sheet_name: Any): ...
def quote_sheet_name(unquoted_sheet_name: Any): ...
