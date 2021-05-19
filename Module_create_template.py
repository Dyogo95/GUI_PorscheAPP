import pandas as pd
import re
from get_TMs import get_TM_names_list as gtm

# display(df)

class CreateResponse():
    def __init__(self, topic, date, gender, name, subject_topic, case, PZ=""):
        self.topic = topic
        self.date = date
        self.gender = gender
        self.subject_topic = subject_topic
        self.case = case
        self.PZ = PZ

    def find_PZ(PZ):
        PZ_list = pd.read_excel(r"Porsche_Zentren.xlsx")
        df = pd.DataFrame(PZ_list)
        location = []
        Email = ""
        location = gtm.get_PZ_list()
        street = location == PZ, ['Strasse'].values[0]
        plz = df.loc[df['PZ-Name1'] == PZ, 'PLZ'].values[0]
        ort = df.loc[df['PZ-Name1'] == PZ, 'Ort'].values[0]
        tel = df.loc[df['PZ-Name1'] == PZ, 'PZ-Tel'].values[0]
        tel = re.sub('^[0]', '+49 ', tel)
        tel = clean_phone_number = re.sub('[/&-]', '', tel)
        self.Email = emails.loc[emails['PZ-Name1'] == PZ, 'E-mails'].values[0]

        location.append(plz)
        location.append(ort)
        location = f"{location[0]} {location[1]}"
        return ("{}\n\n{}\n\n{}\n\nTel:    {}\n\nE-Mail: {}".format(PZ, street, location, tel, Email))

# define the text_module functions with it's parameters
    def text_module(self, topic, date, gender, name, subject_topic, case, PZ=""):
        with open('Porsche_TM_vereinfacht.txt') as f:
            # Read the file fully and as string. Name it TM
            TM = f.read()
            # Split TM by "----------" to seperate each module
            modules = TM.split("----------")
        gname = ""
        mail = ""
        language = ""
        Subj = f"Ihre Anfrage {subject_topic} vom {date} ({case})"
        # Get's only the needed text module for the e-mail
        for module in modules:
            if topic in module:
                mail = module
        # Recognize the language to specify the greeting
        if "Sehr" in mail:
            language = "de"
        elif "Dear" in mail:
            language = "en"
        # Match the greeting to the correct gender in the right language
        if gender == "m" and language == "de":
            gname = f"r Herr {name}"
        elif gender == "f" and language == "de":
            gname = f" Frau {name}"
        elif gender == "m" and language == "en":
            gname = f". {name}"
            Subj = f"Your request regarding {subject_topic} dated {date} ({case})"
        elif gender == "f" and language == "en":
            gname = f"s. {name}"
            Subj = f"Your request regarding {subject_topic} dated {date} ({case})"
        # Create the Attachment name
        x = date.split(" ")
        print(x)
        att_part1 = x[0][:2]
        att_part2 = x[1][:3]
        attach1 = f"01_{att_part1.strip('.')} {att_part2} 21_KD an CIC"
        attach2 = f"02_{att_part1.strip('.')} {att_part2} 21_CIC an KD"
        print(attach1)
        print(attach2)
        # replacing the variables in the needed module
        mail = mail.replace(f"{topic}", f"{Subj}")
        #PZ Daten
        if PZ != "":
            PZ_stadt = PZ.split()
            PZ_stadt = PZ_stadt[-1]
            PZ_info = find_PZ(PZ)
            if language == "en":
                PZ_info = re.sub(r"Zentrum", "Centre", PZ_info)
                PZ_info = re.sub(r"Straße", "Street", PZ_info)
                PZ_info = re.sub(r"Ort", "City", PZ_info)
                PZ_info = re.sub(r"Telefonnummer", "Phonenumber", PZ_info)
            print(mail.format(name=gname, date=date, subject_topic=subject_topic, PZ_info=PZ_info, PZ_stadt=PZ_stadt))
        else:
            print(mail.format(name=gname, date=date, subject_topic=subject_topic))


# How the function should be called.
def main():
    # Open the file with all Textmodules in them

    # E-mail List
    # read E-mail list and extract needed e-mail addresses to return these
    EMails = pd.read_excel(r"E-Mail_Porsche_Zentren.xlsx")
    emails = pd.DataFrame(EMails)

    mail_address = emails['E-mails']
    # print(mail_address)

    # CreateResponse.text_module(topic, date, gender, name, subject_topic, case)

    CreateResponse.text_module(' ',"TM - Bewerbung", "12. Mai 2021", "m", "Hilal Sharifi", "zur Bewerbung", "63426932", "Porsche Zentrum Braunschweig")


if __name__ == "__main__":
    main()
