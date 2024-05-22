# Matthew J Carr, Darren M Ashcroft, Evangelos Kontopantelis, David While, Yvonne Awenat, Jayne Cooper, Carolyn Chew-Graham, Nav Kapur, Roger T Webb, 2024.

import sys, csv, re

codes = [{"code":"U205y00","system":"readv2"},{"code":"U29y.00","system":"readv2"},{"code":"U2y0.00","system":"readv2"},{"code":"U25..00","system":"readv2"},{"code":"U20Cy00","system":"readv2"},{"code":"U2yz.00","system":"readv2"},{"code":"U2Cy.00","system":"readv2"},{"code":"U202y00","system":"readv2"},{"code":"TKxy.00","system":"readv2"},{"code":"U20By00","system":"readv2"},{"code":"U2z..00","system":"readv2"},{"code":"U2zy.00","system":"readv2"},{"code":"U2By.00","system":"readv2"},{"code":"U204y00","system":"readv2"},{"code":"U2y..00","system":"readv2"},{"code":"U208y00","system":"readv2"},{"code":"U209y00","system":"readv2"},{"code":"U45..00","system":"readv2"},{"code":"U200y00","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('self-harm-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["self-harm-specified---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["self-harm-specified---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["self-harm-specified---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
