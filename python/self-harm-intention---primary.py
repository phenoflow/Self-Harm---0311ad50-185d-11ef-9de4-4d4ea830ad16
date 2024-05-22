# Matthew J Carr, Darren M Ashcroft, Evangelos Kontopantelis, David While, Yvonne Awenat, Jayne Cooper, Carolyn Chew-Graham, Nav Kapur, Roger T Webb, 2024.

import sys, csv, re

codes = [{"code":"U20y000","system":"readv2"},{"code":"U201z00","system":"readv2"},{"code":"U20yz00","system":"readv2"},{"code":"U26..00","system":"readv2"},{"code":"U205000","system":"readv2"},{"code":"U207000","system":"readv2"},{"code":"U200500","system":"readv2"},{"code":"U2z0.00","system":"readv2"},{"code":"U202000","system":"readv2"},{"code":"U2C..00","system":"readv2"},{"code":"U207.00","system":"readv2"},{"code":"U2A..00","system":"readv2"},{"code":"U2...00","system":"readv2"},{"code":"U201.00","system":"readv2"},{"code":"U201000","system":"readv2"},{"code":"U205.00","system":"readv2"},{"code":"U200400","system":"readv2"},{"code":"U202.00","system":"readv2"},{"code":"U27..00","system":"readv2"},{"code":"U200.00","system":"readv2"},{"code":"U200000","system":"readv2"},{"code":"U2B..00","system":"readv2"},{"code":"U20Bz00","system":"readv2"},{"code":"U202400","system":"readv2"},{"code":"U29..00","system":"readv2"},{"code":"U202z00","system":"readv2"},{"code":"U20y.00","system":"readv2"},{"code":"U270.00","system":"readv2"},{"code":"U204000","system":"readv2"},{"code":"U204z00","system":"readv2"},{"code":"U200z00","system":"readv2"},{"code":"U204.00","system":"readv2"},{"code":"U207z00","system":"readv2"},{"code":"U205z00","system":"readv2"},{"code":"U20B.00","system":"readv2"},{"code":"U20B000","system":"readv2"},{"code":"U720.00","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('self-harm-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["self-harm-intention---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["self-harm-intention---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["self-harm-intention---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
