import streamlit as st
import pandas as pd

# Demo data for 10 properties
demo_data = {
    "Property ID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    "Address": ["123 Main St", "456 Elm St", "789 Oak St", "321 Pine St", "654 Maple St",
                "987 Cedar St", "234 Birch St", "567 Walnut St", "890 Spruce St", "123 Cherry St"],
    "City": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix",
             "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose"],
    "Price": [250000, 300000, 275000, 320000, 280000,
              310000, 290000, 330000, 270000, 350000]
}

# Create DataFrame from demo data
df_properties = pd.DataFrame(demo_data)

def main():
    st.title("Real Estate Investment Types Manager")
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox("Select Page", ["Home", "Investment Strategies"])
    
    if page == "Home":
        st.write("Welcome to the Real Estate Investment Types Manager app! Use the navigation sidebar to explore different investment strategies.")
        
    elif page == "Investment Strategies":
        st.subheader("Investment Strategies")
        investment_strategies = {
            "1. Buy and Hold": "Investors purchase a property with the intention of holding onto it for the long term, typically renting it out to tenants for ongoing income.",
            "2. Fix and Flip": "Investors purchase a property, renovate it to increase its value, and then sell it quickly for a profit.",
            "3. Wholesaling": "Investors contractually agree to buy a property and then sell the rights to purchase the property to another buyer at a higher price.",
            "4. Real Estate Investment Trusts (REITs)": "Investors buy shares in a company that owns and manages income-producing real estate.",
            "5. Real Estate Crowdfunding": "Multiple investors pool their money together to invest in real estate projects, typically through online platforms.",
            "6. Real Estate Syndication": "A group of investors pool their resources to purchase a property, typically led by a sponsor who manages the investment.",
            "7. Real Estate Development": "Investors purchase land and develop it into properties for sale or rent.",
            "8. Vacation Rentals": "Investors purchase properties in tourist destinations and rent them out to vacationers for short-term stays.",
            "9. Commercial Real Estate": "Investors purchase properties such as office buildings, retail centers, or industrial spaces for rental income or appreciation.",
            "10. Tax Lien Investing": "Investors purchase tax liens on properties with delinquent taxes, with the potential to acquire the property if the taxes remain unpaid."
        }
        
        selected_strategy = st.selectbox("Select an Investment Strategy", list(investment_strategies.keys()))
        st.write(investment_strategies[selected_strategy])
        
    elif page == "View Properties":
        st.subheader("View Properties")
        selected_property_id = st.selectbox("Select a Property ID", df_properties["Property ID"])
        selected_property = df_properties[df_properties["Property ID"] == selected_property_id]
        st.write(selected_property)

if __name__ == "__main__":
    main()
