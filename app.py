import streamlit as st
import numpy as np
import pickle
# Load Model & Scaler

model = pickle.load(open("best_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))



