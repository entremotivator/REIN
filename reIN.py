import streamlit as st

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

if __name__ == "__main__":
    main()
