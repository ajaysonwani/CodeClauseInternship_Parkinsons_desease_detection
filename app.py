import numpy as np
import streamlit as st
import pickle
from sklearn.preprocessing import StandardScaler

st.title("Parkinson's Disease Prediction")

# Creating columns for input fields
col1, col2, col3, col4 = st.columns(4, vertical_alignment="bottom")

# Collecting input from the user
MDVP_Fo = col1.number_input("MDVP Fo(Hz) - Average vocal fundamental frequency", min_value=0.00001, step=0.00001)
MDVP_Fhi = col2.number_input("MDVP Fhi(Hz) - Maximum vocal fundamental frequency", min_value=0.00001, step=0.00001)
MDVP_Flo = col3.number_input("MDVP Flo(Hz) - Minimum vocal fundamental frequency", min_value=0.00001, step=0.00001)
MDVP_Jitter_per = col4.number_input("MDVP Jitter(%)", min_value=0.00001, step=0.00001)

MDVP_Jitter_abs = col1.number_input("MDVP Jitter(abs)", min_value=0.00001, step=0.00001)
MDVP_RAP = col2.number_input("MDVP RAP", min_value=0.00001, step=0.00001)
MDVP_PPQ = col3.number_input("MDVP PPQ", min_value=0.00001, step=0.00001)
Jitter_DDP = col4.number_input("Jitter DDP", min_value=0.00001, step=0.00001)

MDVP_Shimmer = col1.number_input("MDVP Shimmer", min_value=0.00001, step=0.00001)
MDVP_Shimmer_db = col2.number_input("MDVP Shimmer(db)", min_value=0.00001, step=0.00001)
Shimmer_APQ3 = col3.number_input("Shimmer APQ3", min_value=0.00001, step=0.00001)
Shimmer_APQ5 = col4.number_input("Shimmer APQ5", min_value=0.00001, step=0.00001)

MDVP_APQ = col1.number_input("MDVP APQ", min_value=0.00001, step=0.00001)
Shimmer_DDA = col2.number_input("Shimmer DDA", min_value=0.00001, step=0.00001)
NHR = col3.number_input("NHR", min_value=0.00001, step=0.00001)
HNR = col4.number_input("HNR", min_value=0.00001, step=0.00001)

RPDE = col1.number_input("RPDE", min_value=0.00001, step=0.00001)
D2 = col2.number_input("D2", min_value=0.00001, step=0.00001)
DFA = col3.number_input("DFA", min_value=0.00001, step=0.00001)
spread1 = col4.number_input("Spread1", min_value=-10.0, step=0.00001)

col5, col6 = st.columns(2, vertical_alignment="bottom")
spread2 = col5.number_input("Spread2", min_value=0.00001, step=0.00001)
PPE = col6.number_input("PPE", min_value=0.00001, step=0.00001)

# Creating an input array from the collected values
input_data = [
    MDVP_Fo, MDVP_Fhi, MDVP_Flo, MDVP_Jitter_per,
    MDVP_Jitter_abs, MDVP_RAP, MDVP_PPQ, Jitter_DDP,
    MDVP_Shimmer, MDVP_Shimmer_db, Shimmer_APQ3, Shimmer_APQ5,
    MDVP_APQ, Shimmer_DDA, NHR, HNR, RPDE, D2, DFA,
    spread1, spread2, PPE
]

# Converting input data to numpy array
input_as_arr = np.asarray(input_data)

# Reshaping the array for the model
input_reshape = input_as_arr.reshape(1, -1)

try:
    # Loading the scaler and model
    scaler = pickle.load(open('scaler.pkl', 'rb'))
    model = pickle.load(open('model.pkl', 'rb'))

    # Scaling input data
    scaled_input = scaler.transform(input_reshape)

    # Making prediction
    if st.button("Is diagnosed with Parkinson's?"):
        prediction = model.predict(scaled_input)
        if prediction[0] == 1:
            st.write("The patient is likely to have Parkinson's disease.")
        else:
            st.write("The patient is unlikely to have Parkinson's disease.")
except FileNotFoundError as e:
    st.error(f"Required file not found: {e}")
except Exception as e:
    st.error(f"An error occurred: {e}")
