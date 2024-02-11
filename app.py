import streamlit as st
from datetime import datetime, timedelta
import pytz

def get_time(location):
    try:
        tz = pytz.timezone(location)
        time_now = datetime.now(tz)
        formatted_time = time_now.strftime("%Y-%m-%d %H:%M:%S")
        return formatted_time
    except Exception as e:
        return str(e)

def main():
    st.title("World Clock")

    locations = st.multiselect(
        "Select locations (up to 4)",
        ["America/New_York", "Europe/London", "Asia/Tokyo", "Australia/Sydney"],
    )

    for location in locations:
        time = get_time(location)
        st.write(f"{location}: {time}")

if __name__ == "__main__":
    main()
