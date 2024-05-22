# Matthew J Carr, Darren M Ashcroft, Evangelos Kontopantelis, David While, Yvonne Awenat, Jayne Cooper, Carolyn Chew-Graham, Nav Kapur, Roger T Webb, 2024.

import sys, csv, re

codes = [{"code":"TKx3.00","system":"readv2"},{"code":"TK52.00","system":"readv2"},{"code":"TKx0000","system":"readv2"},{"code":"TK03.00","system":"readv2"},{"code":"TK6z.00","system":"readv2"},{"code":"TK6..00","system":"readv2"},{"code":"TK1..00","system":"readv2"},{"code":"TKxz.00","system":"readv2"},{"code":"TK07.00","system":"readv2"},{"code":"TK1z.00","system":"readv2"},{"code":"TK7..00","system":"readv2"},{"code":"TK...14","system":"readv2"},{"code":"TK54.00","system":"readv2"},{"code":"TK3z.00","system":"readv2"},{"code":"U2...14","system":"readv2"},{"code":"TK1y.00","system":"readv2"},{"code":"TK0z.00","system":"readv2"},{"code":"TK2z.00","system":"readv2"},{"code":"TK01000","system":"readv2"},{"code":"TKx0.00","system":"readv2"},{"code":"TK...17","system":"readv2"},{"code":"TK71.00","system":"readv2"},{"code":"TK51.00","system":"readv2"},{"code":"TK0..00","system":"readv2"},{"code":"TK01.00","system":"readv2"},{"code":"TK10.00","system":"readv2"},{"code":"TK72.00","system":"readv2"},{"code":"U2...13","system":"readv2"},{"code":"TKz..00","system":"readv2"},{"code":"TK5..00","system":"readv2"},{"code":"TK61.00","system":"readv2"},{"code":"TK3y.00","system":"readv2"},{"code":"TK7z.00","system":"readv2"},{"code":"ZRn3.00","system":"readv2"},{"code":"TK60.00","system":"readv2"},{"code":"TKx2.00","system":"readv2"},{"code":"TK00.00","system":"readv2"},{"code":"TK11.00","system":"readv2"},{"code":"TKx1.00","system":"readv2"},{"code":"TKx7.00","system":"readv2"},{"code":"TK01100","system":"readv2"},{"code":"TK02.00","system":"readv2"},{"code":"U2...15","system":"readv2"},{"code":"TK...00","system":"readv2"},{"code":"TK...15","system":"readv2"},{"code":"TKx..00","system":"readv2"},{"code":"TKx5.00","system":"readv2"},{"code":"TK01400","system":"readv2"},{"code":"TK2..00","system":"readv2"},{"code":"TKx4.00","system":"readv2"},{"code":"TK31.00","system":"readv2"},{"code":"TKx6.00","system":"readv2"},{"code":"TK06.00","system":"readv2"},{"code":"TK20.00","system":"readv2"},{"code":"TK5z.00","system":"readv2"},{"code":"TK30.00","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('self-harm-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["self-harm-parasuicide---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["self-harm-parasuicide---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["self-harm-parasuicide---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
