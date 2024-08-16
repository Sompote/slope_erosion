import streamlit as st

def evaluate_erosion_protection(dispersive, sand, height, slope_angle):
    if dispersive:
        if sand:
            if height <= 6:
                if slope_angle <= 30:
                    return "sodding"
                else:
                    return "geofabric"
            else:
                return "geofabric"
        else:  # not sand
            if height <= 3:
                if slope_angle <= 15:
                    return "geofabric"
                else:
                    return "soil bag"
            else:  # height > 3
                if slope_angle <= 15:
                    return "mattress"
                else:
                    return "soil bag"
    else:  # not dispersive
        if sand:
            if height <= 3:
                return "geofabric"
            else:
                return "mattress"
        else:  # not sand
            return "Slope Angle"  # This branch is incomplete in the decision tree

st.title("Erosion Protection Method Evaluator")

st.write("This app helps you determine the recommended method for erosion protection based on soil and slope characteristics.")

dispersive = st.checkbox("Is the soil dispersive?")
sand = st.checkbox("Is the soil is  sand?")
height = st.number_input("Enter the height of the slope (in meters)", min_value=0.0, value=1.0)
slope_angle = st.number_input("Enter the slope angle (in degrees)", min_value=0.0, max_value=90.0, value=15.0)

if st.button("Evaluate"):
    result = evaluate_erosion_protection(dispersive, sand, height, slope_angle)
    st.write(f"The recommended erosion protection method is: **{result}**")

    if result == "Slope Angle":
        st.warning("Note: The decision for non-dispersive, non-sandy soil is incomplete in the current model.")

st.sidebar.header("About")
st.sidebar.info("This app uses a decision tree model to recommend erosion protection methods based on soil characteristics and slope geometry.")
st.sidebar.warning("Always consult with a geotechnical engineer for professional advice on erosion control measures.")