
import pandas as pd
import re
from get_TMs import get_TM_names_list as gtm


class GetResponse():
    def __init__(self, topic, date, gender, name, subject_topic, case, PZ=""):
        self.topic = topic
        self.date = date
        self.gender = gender
        self.name = name
        self.subject_topic = subject_topic
        self.case = case
        self.PZ = PZ

    def get_PZ_info(PZ):
        # Email info from PZ excel
        PZ_list = pd.read_excel(r"E-Mail_Porsche_Zentren.xlsx")
        df = pd.DataFrame(PZ_list)
        # Info from PZ Excel
        location = []
        street = ''
        tel = ''
        Email = ''
        for index, row in df.iterrows():
            if PZ == row[1]:
                street = row['Strasse']
                plz = row['PLZ']
                ort = row['Ort']
                location = str(plz) + str(ort)
                tel = row['PZ-Tel']
                tel = re.sub('^[0]', '+49 ', tel)
                tel = re.sub('[/&-]', '', tel)
                Email = row['E-mails']

        # location = f"{location[0]} {location[1]}"

        return ("{}\n\n{}\n\n{}\n\nTel:    {}\n\nE-Mail: {}".format(PZ, street, location, tel, Email))


PZ_info = GetResponse.get_PZ_info('Porsche Zentrum Berlin')
print(PZ_info)
