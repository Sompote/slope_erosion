import streamlit as st

def evaluate_erosion_protection(dispersive, sand, height, slope_angle):
    if dispersive:
        if height <= 3:
            return "mattress"
        else:  # height > 3
            if slope_angle <= 15:
                return "mattress"
            else:
                return "soil bag"
    else:  # not dispersive
        if sand:
            if height <= 3:
                return "geofabric"
            else:  # height > 3
                if slope_angle <= 15:
                    return "geofabric"
                else:
                    return "soil bag"
        else:  # not sand
            if height <= 6:
                if slope_angle <= 30:
                    return "sodding"
                else:
                    return "geofabric"
            else:  # height > 6
                return "geofabric"

st.title("Erosion Protection Method Evaluator")

st.write("This app helps you determine the recommended method for erosion protection based on soil and slope characteristics.")

dispersive = st.checkbox("Is the soil dispersive?")
sand = st.checkbox("Is the soil sand?")
height = st.number_input("Enter the height of the slope (in meters)", min_value=0.0, value=1.0, step=0.1)
slope_angle = st.number_input("Enter the slope angle (in degrees)", min_value=0.0, max_value=90.0, value=15.0, step=0.1)

if st.button("Evaluate"):
    method = evaluate_erosion_protection(dispersive, sand, height, slope_angle)
    st.write(f"The recommended erosion protection method is: **{method}**")

st.sidebar.header("About")
st.sidebar.info("This app uses a decision tree model to recommend erosion protection methods based on soil characteristics and slope geometry.")
st.sidebar.warning("Always consult with a geotechnical engineer for professional advice on erosion control measures.")