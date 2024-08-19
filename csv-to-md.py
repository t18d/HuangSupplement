import csv
import operator

# read preface so that we can keep it before the table
preface_lines = []
with open("README.md", "r", encoding="utf8") as readme:
    for line in readme.readlines():
        preface_lines.append(line)
        if "</preface>" in line: # 2nd line because we need to keep the line with </preface> in
            break 
    
# open files to create new readers
with open("supplement.csv", "r", encoding="utf8") as supplement_csv:
        supplement_reader = csv.reader(supplement_csv)
        with open("README.md", "w", encoding="utf8") as conj_md: # WARNING: rewrites the file!
            conj_md.writelines(preface_lines)
            conj_md.write("\n")
            #first line is headers
            first_first_row = True
                first_row = True
                for row in supplement_reader:
                    if first_row and not first_first_row:
                        first_row = False
                        continue
                    new_row = "".join(col + "|" for col in row)[:-1] +"\n" # [:-1] to remove the unneeded | at the end
                    conj_md.write(new_row)
                    if first_first_row:
                        delimiter_row = "---|" * (len(new_row.split("|")))  
                        delimiter_row = delimiter_row[:-1] + "\n" # [:-1] as above
                        conj_md.write(delimiter_row)
                        first_first_row = False
                        first_row = False # delimiter needs to be written after headers (which are the first row)
