import pandas as pd
import numpy as np
import streamlit as st
from google.oauth2 import service_account
from google.cloud import storage

st.title("PNU Making Machine")

a = st.text_input("시/도: ")
b = st.text_input("시/군/구: ")
c = st.text_input("읍/면/동: ")
d = st.text_input("리: ")
e = st.text_input("일반/산: ")
f = st.text_input("본번: ")
g = st.text_input("부번: ")

# Create API client.
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"]
)
client = storage.Client(credentials=credentials)

# Retrieve file contents.
# Uses st.experimental_memo to only rerun when the query changes or after 10 min.
@st.experimental_memo(ttl=600)
def read_file(bucket_name, file_path):
    bucket = client.bucket(bucket_name)
    content = bucket.blob(file_path).download_as_string().decode("utf-8")
    return content

bucket_name = "loosebooster"
file_path = "code10.txt"

content = read_file(bucket_name, file_path)

for line in content.strip().split("\n"):
    name, pet = line.split(",")
    st.write(f"{name} has a :{pet}:")
    

'''
data = []
file = open(content, "r", encoding="cp949")
while True:
    line = file.readline()
    line = line.split()
    t = line[:-1]
    data.append(t)
    if not line:
        break
file.close()

for q in range(len(data)):
    if a in data[q]:
        if b in data[q]:
            if c in data[q]:
                if d == '' :
                    num = data[q][0]
                else:
                    if d in data[q]:
                        num = data[q][0]

if e == '산':
    num_e = '2'
else:
    num_e = '1'

num_f = '{:04d}'.format(int(f))
num_g = '{:04d}'.format(int(g))

output = num + num_e + num_f + num_g
output = int(output)


if st.button('PNU로 변경') :
    con = st.container()
    con.caption('PNU')
    con.write(output)
'''