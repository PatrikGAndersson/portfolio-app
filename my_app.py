import streamlit as st
from PIL import Image
from streamlit_lottie import st_lottie
import requests
from streamlit_player import st_player

st.set_page_config(
     page_title="Deus Ex Machina",
     page_icon="🧊",
     layout="centered",
     initial_sidebar_state="auto",
 )

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

add_selectbox = st.sidebar.selectbox(
	"",
    ("Start","Resume", "Projects")
)



image = Image.open('profilbild.jpg')

if add_selectbox == "Resume":


	body = """


	"""

	info = """ 
	### Contact Information

	Uggleberget 20\\
	43653 HOVÅS\\
	076-901 18 98\\
	patrik@deusexmachina.nu

	"""

	education_1 = """

	KYH **Systems Developer** IoT 2020-2022\\
	Curriculum includes: Programing in Java and Python, Big Data, Security, Algorithms and Network programming.

	"""

	education_2 = """

	Radboud University (Research)Master **Cognitive Neuroscience**  2016-2019\\
	Track “Action,Perception and Control”.\\
	Curriculum included: Advanced Math, EEG,fMRI och statistical methods

	"""

	education_3 = """

	University of Gothenburg BSc **Cognitive psychology**  2015-2016\\
	Curriculum included: Statistics,philosophy,cognitive psychology and research methods.

	"""

	work_1 = """

	University of Gothenburg **Research Assistant** 2015-2016\\
	Responsible for collecting data. Part of analysi and experimental design.\\
	Investigating the effect of affective touch upon cooperation and the effect of reward upon cooperation. The responsibilities included planning,recruitment, and changes to procedure when needed.


	"""

	work_2 = """

	University of Linkoping **Student reporter** 2013-2014\\
	Part of a group of students hired by the communication department of the university to act as communicators.\\
	Publishing articles to the university homepage about current events.



	"""

	work_3 = """

	Substorm **Machine Learning Developer Intern** 2021-2022\\
	Developing an algorithm for collective perception with ESP32 and TinyML.


	"""

	skills1 = """

	**Programming Languages** \\
	Advanced user in Python\\
	Intermediate user in R\\
	Intermediate user in C\\
	Beginner in Java and Rust

	"""

	skills2 = """

	**Machine Learning/Statictics** \\
	Experience using GANs,CNNs,NLP-models\\
	Experience using AWS(SageMaker) and GCP for ML\\
	Intermediate user in C\\
	Non-linear dynamics and chaos theory\\
	Advanced statictical methods\\
	Experience analysing fMRI-data\\
	Tiny Machine Learning

	"""

	skills3 = """

	**Library knowledge** \\
	Advanced user in Tensorflow\\
	Advanced user in Pandas\\
	Intermediate user in PyTorch\\
	Intermediate user in Sci-Kit Learn\\
	Intermediate user matplotlib
	

	"""

	certificates1 = """

	**Certificates** \\
	Tiny Machine Learning Professional Certificate **EdEx** 2021\\
	DeepLearning.AI TensorFlow Developer Specialization **Coursera** 2021
	

	"""

	courses1 = """

	**Courses** \\
	Advanced C-programming **Udemy** 2021\\
	Sequences, Time Series and Prediction **Coursera** 2020\\
	Natural Language Processing in TensorFlow **Coursera** 2020\\
	Introduction to embedded machine learning **Coursera** 2021\\
	TensorFlow: Advanced Techniques Specialization **Coursera** 2021\\
	Generative Deep Learning with TensorFlow **Coursera** 2021\\
	Device-based Models with TensorFlow Lite **Coursera** 2021\\
	Custom and Distributed Training with TensorFlow **Coursera** 2021\\
	Custom Models, Layers, and Loss Functions with TensorFlow **Coursera** 2021\\
	Advanced Computer Vision with TensorFlow **Coursera** 2021\\
	Datascientist with Python **Datacamp** 2018-2019\\
	Practical Data Science specialisation **Coursera** 2021\\
	Introduction to Machine Learning in Production **Coursera** 2021\\
	Hands-on Machine Learning with AWS and NVIDIA **Coursera** 2021


	"""

	



	st.markdown(body)
	st.markdown("***")

	col1, col2 = st.columns([2,2])

	with col1:
		st.markdown(info)
 

	with col2:

		st.image(image,width=350)

	st.markdown("***")
	st.markdown("#### Education")
	with st.expander("Show education",expanded=False):
		with st.container():
			st.markdown("***")
			st.markdown(education_1)
			st.markdown("***")
		with st.container():
			st.markdown(education_2)
			st.markdown("***")
		with st.container():
			st.markdown(education_3)
	st.markdown("***")
	st.markdown("#### Relevant work experience")
	with st.expander("Show relevant work experience",expanded=False):
		with st.container():
			st.markdown("***")
			st.markdown(work_1)
			st.markdown("***")
		with st.container():
			st.markdown(work_2)
			st.markdown("***")
		with st.container():
			st.markdown(work_3)
	st.markdown("***")
	st.markdown("#### Technical skills")
	with st.expander("Show technical skills",expanded=False):
		with st.container():
			st.markdown("***")
			st.markdown(skills1)
			st.markdown("***")
		with st.container():
			st.markdown(skills2)
			st.markdown("***")
		with st.container():
			st.markdown(skills3)
	st.markdown("***")
	st.markdown("#### Courses/Certificates")
	with st.expander("Show courses/certificate",expanded=False):
		with st.container():
			st.markdown("***")
			st.markdown(certificates1)
			st.markdown("***")
		with st.container():
			st.markdown(courses1)
			st.markdown("***")
	st.markdown("***")


	with open('cv.png', "rb") as file:
	   btn = st.download_button(
	           label="Download Resume as PDF",
	           data=file,
	           file_name="cv.pdf",
	           mime="application/pdf"
	         )

if add_selectbox == "Start":
	column1,column2,column3 = st.columns([1,8,1])
	with column2:
		url = "https://assets2.lottiefiles.com/private_files/lf30_qrvv8h4p.json"
		url2 = "https://assets1.lottiefiles.com/packages/lf20_eKikFJ.json"
		url3 = "https://assets10.lottiefiles.com/private_files/lf30_UVTtPi.json"
		url4 ="https://assets7.lottiefiles.com/packages/lf20_b9gvmvhz.json"
		url5 = "https://assets8.lottiefiles.com/datafiles/QeC7XD39x4C1CIj/data.json"
		lottie_test = load_lottieurl(url4)
		st_lottie(lottie_test, key="hello")
		#st.image("logo.png")
if add_selectbox == "Projects":

	st.markdown("## Projects")

	with st.container():
			st.markdown("***")
			st.markdown("### Tiny Swarm")
			st.markdown("**Scope of Project:**")
			st.markdown("Using the contextual information in a mesh of MCUs with Tensorflow Micro. In effect imitating the behavior of bees seeking a new hive")
			st.markdown("**Hardware used:**")
			st.markdown("ESP32,IMU-sensors,D1Mini")
			st.markdown("**Language:**")
			st.markdown("Python,C++")
			st.markdown("**Relevant skills/techniques:**")
			st.markdown("Arduino,Autoencoder,Tiny Machine Learning, Data Analysis,Data Collection")
			st.markdown("https://github.com/PatrikGAndersson/TinySwarm")
			st.markdown("***")

	with st.container():
			st.markdown("***")
			st.markdown("### Automatic Water Fountain for cats")
			st.markdown("**Scope of Project:**")
			st.markdown("Classifying which of my two cats is in the vicinity of a water fountain(using TinyYolo) and use the information to provide a customised jet of water in water fountain.")
			st.markdown("**Hardware used:**")
			st.markdown("Sipeed M1 dock with k210 processor")
			st.markdown("**Language:**")
			st.markdown("Micropython/C")
			st.markdown("**Relevant skills/techniques:**")
			st.markdown("Python,Computer vision,Data Augmentation,Data Collection,CNN,C,Embedded")
			st.markdown("git link")
			st_player("https://www.youtube.com/watch?v=5Ryy1W-IImU")
			st.markdown("***")

	with st.container():
			st.markdown("***")
			st.markdown("### Vaccination appointment web scraper")
			st.markdown("**Scope of Project:**")
			st.markdown("Find available dates for COVID-19 vaccination in the district of Västra Götaland,Sweden")
			st.markdown("**Hardware used:**")
			st.markdown("AWS virtual machine")
			st.markdown("**Language:**")
			st.markdown("Python")
			st.markdown("**Relevant skills/techniques:**")
			st.markdown("Webscraping,Scripting,Beautiful Soup")
			st.markdown("https://github.com/PatrikGAndersson/Vaxxdater")
			st.markdown("***")
	
	with st.container():
			st.markdown("***")
			st.markdown("### PyFrame")
			st.markdown("**Scope of Project:**")
			st.markdown("Get frames from videoclip")
			st.markdown("**Hardware used:**")
			st.markdown("NA")
			st.markdown("**Language:**")
			st.markdown("Python")
			st.markdown("**Relevant skills/techniques:**")
			st.markdown("Data Collection,Scripting")
			st.markdown("https://github.com/PatrikGAndersson/PyFrame")
			st.markdown("***")

			



	

