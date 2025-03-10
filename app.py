import streamlit as st
import os

class A320Checklist:

    def __init__(self):

        self.image_path = os.path.realpath(os.path.dirname(__file__))+"/images/"
        
        # initialization of the streamlit app
        self.app_init()

        # cockpit pre-flight operations section
        self.cockpit_pre_flight_operations()
        st.divider()

        # cockpit preparation operations section
        st.divider()

        # start-up operations section
        st.divider()

        # before taxi operations section
        st.divider()

        # before takeoff operations section
        st.divider()

        # takeoff operations section
        st.divider()

        # after takeoff operations section
        st.divider()

        # climb operations section
        st.divider()

        # cruise/descent operations section
        st.divider()

        # approach operations section
        st.divider()

        # landing operations section
        st.divider()

        # after landing operations section
        st.divider()

        # shutdown operations section
        st.divider()

        # securing aircraft operations section
        st.divider()

    def app_init(self):
        st.title("A-320 Neo Checklist 🛫")
        st.write("Based on u/rarapute checklist")
        st.image(os.path.join(self.image_path, "a320_neo.jpg"))
        st.divider()

    def cockpit_pre_flight_operations(self):
        with st.expander("COCKPIT PRE-FLIGHT", expanded = True):
            
            if 
            st.progress(0, "")

            col1, col2 = st.columns(2, vertical_alignment="center")
            
            col1.write("__Weather Radar__", use_container_width=True)
            weather_radar_checkbox = col2.checkbox("OFF", key=1)

            col1.write("__Pred. Windshear__", use_container_width=True)
            windshear_checkbox = col2.checkbox("OFF", key=2)

            col1.write("__Parking Breake__", use_container_width=True)
            parking_brake_checkbox = col2.checkbox("ON", key=3)

            col1.write("__Spoilers__", use_container_width=True)
            spoilers_checkbox = col2.checkbox("RETRATTED", key=4)

            col1.write("__Flaps__", use_container_width=True)
            flaps_checkbox = col2.checkbox("RETRATTED", key=5)

            col1.write("__Engine Masters__", use_container_width=True)
            engine_masters_checkbox = col2.checkbox("OFF", key=6)

            col1.write("__Engine Mode Selector__", use_container_width=True)
            engine_mode_selector_checkbox = col2.checkbox("NORM", key=7)

            col1.write("__Thrust Levers__", use_container_width=True)
            thrust_levers_checkbox = col2.checkbox("IDLE", key=8)

            col1.write("__Landing Gear__", use_container_width=True)
            landing_gear_checkbox = col2.checkbox("DOWN", key=9)

            col1.write("__Anti-Skid__", use_container_width=True)
            anti_skid_checkbox = col2.checkbox("ON", key=10)
            
            col1.write("__Whipers__", use_container_width=True)
            whipers_checkbox = col2.checkbox("OFF", key=11)

            

    def cockpit_preparation_operations(self):
        pass

    def startup_operations(self):
        pass

    def before_taxi_operations(self):
        pass

    def before_takeoff_operations(self):
        pass
    
    def takeoff_operations(self):
        pass

    def after_takeoff_operations(self):
        pass

    def climb_operations(self):
        pass

    def cruise_descent_operations(self):
        pass

    def approach_operations(self):
        pass

    def landing_operations(self):
        pass

    def after_landing_operations(self):
        pass

    def shutdown_operations(self):
        pass

    def securing_aircraft_operations(self):
        pass



if __name__ == "__main__":

    app = A320Checklist()

