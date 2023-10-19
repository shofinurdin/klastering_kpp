import streamlit as st 
import streamlit.components.v1 as stc 
from eda_app import run_eda_app
from prep_app import run_prep_app
from klaster_app import run_cl_app


from simulasi_app import run_simulasi_app

st.set_page_config(page_title="ML & DEA",
		   page_icon="🚢",
		   layout="wide")


html_temp = """
		<div style="background-color:#3872fb;padding:5px;border-radius:10px">
		<h3 style="color:white;text-align:center;font-family:arial;">Klastering Kantor Pelayanan Pajak</h3>
		<h3 style="color:white;text-align:center;"></h3>
		<h4 style="color:white;text-align:center;font-family:arial;">--Prototype--</h4>
		</div>
		"""

def main():
	#st.title("ML Web App with Streamlit")
	stc.html(html_temp)

	menu = ["Home","EDA","Preparation","Klastering"]
	choice = st.sidebar.selectbox("Menu",menu)

	if choice == "Home":
		st.subheader("Home")
		st.write("""
			#### Klastering Kantor Pelayanan Pajak
			
			#### App Content
				- EDA Section: Exploratory Data Analysis of Data
				- Preparation: Data preparation
				- Clustering Section: ML Clustering App
				

			""")
	elif choice == "EDA":
		run_eda_app()

	elif choice == "Preparation":
		run_prep_app()


	elif choice == "Klastering":
		run_cl_app()
	


	else:
		st.subheader("About")
		st.text("Prototype ini dibuat menggunakan framework streamlit dengan bahasa pemrograman python")
		st.text("Shofinurdin : 2111600272")
		st.text("Shofinurdin@gmail.com")

if __name__ == '__main__':
	main()