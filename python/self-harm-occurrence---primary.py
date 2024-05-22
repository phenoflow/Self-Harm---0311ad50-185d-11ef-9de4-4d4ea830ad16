# Matthew J Carr, Darren M Ashcroft, Evangelos Kontopantelis, David While, Yvonne Awenat, Jayne Cooper, Carolyn Chew-Graham, Nav Kapur, Roger T Webb, 2024.

import sys, csv, re

codes = [{"code":"U274.00","system":"readv2"},{"code":"U29z.00","system":"readv2"},{"code":"U2C4.00","system":"readv2"},{"code":"U290.00","system":"readv2"},{"code":"U2A0.00","system":"readv2"},{"code":"U28z.00","system":"readv2"},{"code":"U250.00","system":"readv2"},{"code":"U2Bz.00","system":"readv2"},{"code":"U2B4.00","system":"readv2"},{"code":"U2B0.00","system":"readv2"},{"code":"U294.00","system":"readv2"},{"code":"U2A3.00","system":"readv2"},{"code":"U280.00","system":"readv2"},{"code":"U4Bz.00","system":"readv2"},{"code":"U27z.00","system":"readv2"},{"code":"U2zz.00","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('self-harm-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["self-harm-occurrence---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["self-harm-occurrence---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["self-harm-occurrence---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
