import requests
import streamlit as st
import pandas as pd
import numpy as np
import time

st.set_page_config(
	page_title="My first st_playground",
	initial_sidebar_state="expanded"
)

API_URL = "https://api-inference.huggingface.co/models/valhalla/distilbart-mnli-12-3"
API_TOKEN = st.secrets["API_TOKEN"]
headers = {"Authorization": f"Bearer {API_TOKEN}"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

with st.form(key="my_form"):
	labels = st.multiselect("Choose your labels", ["cat", "dog"])
	inputs = st.text_area('Enter your text for classification', "Hi, I recently bought a device from your company but it is not working as advertised and I would like to get reimbursed!")
	payload = {
		"inputs": inputs,
		"parameters": {"candidate_labels": labels}
    }
	submitted = st.form_submit_button("Classify!")
	if submitted:
		output = query(payload)
		st.write(output)