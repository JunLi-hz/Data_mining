# Cut HA sequences into HA1, including H1N1dpm09 and seasonal H3N2 viruses
# Put the sequences in the first sheet and Column A
import xlrd
import xlwt
book = xlrd.open_workbook("HAseq.xls")
wb = xlwt.Workbook()
ws = wb.add_sheet('results')
ws.write(0,0,'Column A')
sh = book.sheet_by_index(0)
for i in range(1,sh.nrows): #skips first row.
    seq_full = sh.cell_value(rowx=i, colx=0)
    seq_HA1 = seq_full[16:345]
    ws.write(i,0,seq_HA1)
wb.save('HA1seq.xls')
#cut the sequences of HA(HAseq.xls) to HA1(HA1seq.xls)
#H1N1pdm09 HA1[17:344], H3N2 HA1[16:345]
