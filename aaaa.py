import qrcode
qr = qrcode.QRCode(
    version=3,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=1,
    border=0,
)

qr.add_data("Click Select File Button and then start streaming")
qr_matrix = qr.get_matrix()
matrix = [["██" if each else "  " for each in rows] for rows in qr_matrix]
with open ("Welcom.txt",'a',encoding="utf-8") as f:
    for row in matrix:
        print("".join(row))
        f.writelines("<pre>"+"".join(row)+"</pre>"+'\n')
