html = open('Box_HTML.txt', 'w+')
css = open('Box_CSS.txt', 'w+')
for col in range(1,145):
    for row in range(1,91):
        if col < 10:
            col_text = '00' + str(col)
        elif col < 100:
            col_text = '0' + str(col)
        else:
            col_text = str(col)
        if row < 10:
            row_text = '00' + str(row)
        elif row < 100:
            row_text = '0' + str(row)
        else:
            row_text = str(row)
        cell_id = 'Cell' + col_text + row_text

        #odd colunm
        if col%2 == 1:
            col_ref = 5
            col_shift = ((col - 1)/2) * 21
            rack_shift = (((col - 1)/2) // 12) * 5
            col_px = col_ref + col_shift + rack_shift

            row_ref = 500
            #odd row
            if row % 2 == 1:
                row_chift = (row - 1)/2 * 11
            #event row
            else:
                row_chift = ((row - 2)/2 * 11) + 5
            row_px = row_ref - row_chift

            html.write('<box class = \"' + cell_id + '\" id = \"' + cell_id + '\" ></box>' + '\r\n')
            css.write('box.' + cell_id + ' {top: ' + str(int(row_px)) + 'px;left: ' + str(int(col_px))
                      + 'px;}' + '\r\n')


        #event colunm
        else:
            col_shift = (((col - 2) /2) % 12) * 21
            rack_shift = (((col - 2) / 2) // 12) * 5
            col_ref = (((((col - 2) / 2) // 12) + 1 ) * 12 * 21) + 5 + rack_shift - 21
            col_px = col_ref - col_shift

            row_ref = 520
            # odd row
            if row % 2 == 1:
                row_chift = (row - 1) / 2 * 11
            # event row
            else:
                row_chift = ((row - 2) / 2 * 11) + 5
            row_px = row_ref + row_chift

            html.write('<box class = \"' + cell_id + '\" id = \"' + cell_id + '\" ></box>' + '\r\n')
            css.write('box.' + cell_id + ' {top: ' + str(int(row_px)) + 'px;left: ' + str(int(col_px))
                      + 'px;}' + '\r\n')

html.close()
css.close()

