import streamlit as st
import pandas as pd
import base64

# Function to encode image to base64
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Data for the companies
data = {
    'Company Name': [
        'The Honest Home', 'Adil Qadri', 'The Cinnamon Kitchen', 'Intervue', 'Rodbez',
        'Blix', 'TURMS', 'Mintree', 'Dil foods', 'Kalakaram', 'Tramboo', 'WeHear',
        'Tiggle', 'WYLD Card', 'Goenchi Feni', 'Arata', 'Vecros', 'Gud Gum',
        'Eva Scalp Cooling', 'HoneyTwigs', 'Koparo', 'JewelBox', 'Daak Room', 
        'Walking Company', 'Decode Age', 'A Little Extra', 'Nasher Miles', 
        'Without', 'Kibo by Trestle Labs', 'VOLD', 'HyperLab', 'Yes Madam', 
        'Toffee Coffee Roasters', 'Push Sports', 'ORBO AI', 'D\'chica', 'Refit', 
        'Artinci'
    ],
    'Description': [
        'Sustainable home products', 'Luxury fragrances', 'Specialty foods', 
        'Interview platforms', 'E-commerce for auto parts', 'Electronics and gadgets', 
        'Performance clothing', 'Luxury skincare', 'Traditional foods', 
        'Art supplies', 'Sports equipment', 'Hearing aids', 
        'Chocolate drinks', 'Fitness products', 'Spirits and liquors', 
        'Personal care', 'Drone technology', 'Eco-friendly gum', 
        'Scalp cooling systems', 'Honey-based products', 'Household cleaning products', 
        'Jewelry storage', 'Photography services', 'Footwear', 
        'Health supplements', 'Gourmet snacks', 'Luggage', 
        'Live-streaming platform', 'Assistive technology', 'Energy solutions', 
        'Lab equipment', 'Personal care services', 
        'Coffee roasters', 'Sportswear', 'AI technology', 
        'Girls\' apparel', 'Healthcare products', 
        'Healthy snacks'
    ],
    'Website': [
        'https://honesthome.in/', 'https://www.adilqadri.com/', 'https://cinnamon.kitchen/', 
        'https://www.intervue.io/', 'https://www.rodbez.in/', 'https://blix.in/', 
        'https://urturms.com/', 'https://mintree.us/', 'https://dilfoods.in/', 
        'https://kalakaram.com/', 'https://tramboosports.com/', 'https://wehearglobal.com/', 
        'https://thetiggle.com/', 'https://www.getwyld.in/', 'https://www.goenchi.com', 
        'https://www.arata.in/', 'https://vecros.com/', 'https://gudgum.in/', 
        'https://evascalpcooling.co.in/', 'https://honeytwigs.co/', 'https://koparoclean.com/', 
        'https://jewelbox.co.in/', 'https://daakroom.com/', 'https://www.thewalkingcompany.com/', 
        'https://decodeage.com/', 'https://alittleextra.co.in/', 'https://nashermiles.com/', 
        'https://without.live/', 'https://www.trestlelabs.com/', 'https://www.voldenergy.in/', 
        'https://www.hyperlab.life/', 'https://www.yesmadam.com/', 
        'https://toffeecoffeeroasters.com/', 'https://pushsports.in/', 
        'https://www.orbo.ai/', 'https://www.dchica.in/', 'https://refitglobal.com/', 
        'https://www.artinci.com/'
    ],
    'Email': [
        'admin@honesthome.in', 'info@adilqadri.com', 'hey@cinnamon.kitchen', 
        'support@intervue.io', 'rodbeztech@gmail.com', 'contact@blix.in', 
        'support@URturms.com', 'tanushree@premier-lifestyle.com', 'hello@dilfoods.in', 
        'info@kalakaram.com', 'contact@tramboosports.com', 'ccare@wehearglobal.com', 
        'happy@thetiggle.com', 'hello@getwyld.in', 'goenchifeni@gmail.com', 
        'info@arata.in', 'contact@vecros.com', 'founders@gudgum.in', 
        'info@stemtech.in', 'info@honeytwigs.co', 'help@koparoclean.com', 
        'support@jewelbox.co.in', 'INFO@DAAKROOM.COM', 'press@thewalkingcompany.com', 
        'care@decodeage.com', 'help.alittleextra@gmail.com', 'jobs@nashermiles.com', 
        'hello@without.live', 'info@trestlelabs.com', 'info@voldenergy.in', 
        'contact@hyperlab.life', 'support@yesmadam.com', 
        'toffeecoffeeroasters@gmail.com', 'nitin@pushsports.in', 
        'support@orbo.ai', 'customercare@dchica.in', 'support@refitglobal.com', 
        'team@artinci.com'
    ]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Background image setup
img = get_img_as_base64("des.jpg")
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("data:image/png;base64,{img}");
background-size: cover;
background-position: center;
}}
[data-testid="stHeader"] {{
background: rgba(0, 0, 0, 0);
}}
[data-testid="stSidebar"] > div:first-child {{
background-image: url("data:image/png;base64,{img}");
background-size: cover;
background-position: center;
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# First page content - List of companies with descriptions
if 'page' not in st.session_state:
    st.session_state.page = 1

if st.session_state.page == 1:
    st.title("Shark Tank Season Three Startups")
    st.subheader("List of Companies with Descriptions")

    # Display companies and their descriptions
    for index, row in df.iterrows():
        st.write(f"**{row['Company Name']}**")
        st.write(row['Description'])
        st.write("---")

    # Button to go to the next page
    if st.button("Go to Links and Emails"):
        st.session_state.page = 2
        switch_page("page2")

elif st.session_state.page == 2:
    st.title("Shark Tank Season Three Startups")
    st.subheader("Links and Emails")

    # Search by Company Name
    company_name = st.text_input("Search by Company Name")

    # Filter DataFrame by search input
    if company_name:
        filtered_df = df[df['Company Name'].str.contains(company_name, case=False)]
    else:
        filtered_df = df

    # Display filtered data
    st.dataframe(filtered_df[['Company Name', 'Website', 'Email']])

    # Option to download data as CSV
    st.subheader("Download Data")
    csv = filtered_df.to_csv(index=False)
    st.download_button(label="Download as CSV", data=csv, file_name='shark_tank_startups.csv', mime='text/csv')
    url = "https://app.napkin.ai/page/CgoiCHByb2Qtb25lEiwKBFBhZ2UaJGQ5M2IxNDkwLWI0OTctNDVkMy04MDY3LTJjMTJjZjBiNmI3Yg"

# Create a link button
st.link_button("GET MAIL TEMPLATES!!!", url)