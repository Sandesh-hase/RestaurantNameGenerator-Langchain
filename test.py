import streamlit as st

# Menu dictionary for different cuisines
menu = {
    "Indian": ["Butter Chicken", "Biryani", "Paneer Tikka", "Naan", "Raita"],
    "Italian": ["Pizza", "Pasta", "Lasagne", "Tiramisu", "Bruschetta"],
    "Mexican": ["Tacos", "Burritos", "Quesadillas", "Guacamole", "Enchiladas"],
    "Arabic": ["Hummus", "Falafel", "Shawarma", "Tabbouleh", "Baklava"],
    "American": ["Burger", "Hot Dog", "French Fries", "Cheesecake", "Buffalo Wings"],
}

# Set the title and options in the sidebar
st.sidebar.title("Cuisine Selection")
selected_cuisine = st.sidebar.selectbox(
    "Select a cuisine", ["Indian", "Italian", "Mexican", "Arabic", "American"]
)

# Display the selected cuisine and the menu
st.title(f"Welcome to {selected_cuisine} Restaurant")

if selected_cuisine == "Indian":
    st.write("Menu:")
    for item in menu[selected_cuisine]:
        st.write("- " + item)
