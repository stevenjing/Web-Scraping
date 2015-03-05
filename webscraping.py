#!/usr/bin/env python

import glob
import re
from bs4 import BeautifulSoup

all_html = glob.glob("seminars/*.html")
print len(all_html)

for html_file in all_html:
    with open(html_file, "r") as rfile:
        soup = BeautifulSoup(rfile)
        section_div = soup.find("div", class_="section")
        if is_ecoevopub(section_div):
            eep_date = extract_date(section_div)
            print "Found an EcoEvoPub on", eep_date
            summary_text = get_summary_text(section_div)
            for line in summary_text.strings:
                search_name = re.search(r"([A-Z-]{3,}) ([A-Z-]{3,})", line)
                if search_name and search_name.group(0) != "BIOMEDICAL SCIENCES":
                    print search_name.group(0)
