import streamlit as st
st.set_page_config(page_title="PROJECT", page_icon=None,layout="wide", initial_sidebar_state="auto",menu_items=None)
                #    {'About': "# This is a header. This is an *extremely* cool app!"}

import streamlit.components.v1 as components
import plotly.express as px 
import pandas as pd 
from datetime import datetime
st.set_option('deprecation.showPyplotGlobalUse', False)

menu = st.sidebar.selectbox("Sub menu",('Customizable Dashboard','Drag & Drop Custom Charts','Embedded Dashboard','Machine Learning App'))
if menu == 'Customizable Dashboard':
    pilihdata = st.sidebar.radio('Pilih Data',['Sample1','Upload Data'])
    # df = pd.read_excel('Rekap_wilayah.xlsx')
    if pilihdata=='Upload Data':
        upl = st.file_uploader('Upload data anda',type=['csv'])
        if upl is not None:
            df = pd.read_csv(upl)
            st.subheader("Summary & Correlation")
            z1, z2 = st.columns((5,7))
            with z1:
                with st.expander('Data Summary', expanded=True):
                    st.write(df.describe())
            with z2:
                with st.expander('Overview Data', expanded=True):
                    st.dataframe(df)
            with st.expander('Smart Charts', expanded=True):
                z4,z5,z6 = st.columns((3,1,8))
                with z4:
                    st.text("Configuration")
                    st.empty()
                    dfp = df
                    plot_type = st.selectbox('Select Type of Plot',["scatter","bar","line","pie","hist","box"])
                    all_columns = dfp.columns
                    y_columns = st.selectbox('Select Y Variable', all_columns)
                    x_column = st.selectbox('Select X Variable', all_columns,index=1)
                    dimension = st.selectbox('Color by', all_columns,index=2)
                    # dfp = df[df['nama_pemda'].isin(pemda)]
                    color_value = dfp[dimension]
                with z5:
                    st.empty()
                with z6:
                    if plot_type == "scatter":
                        fig = px.scatter(dfp,x=x_column,y=y_columns,color=color_value)
                        st.plotly_chart(fig)
                    elif plot_type == "bar":
                        mode = st.selectbox('Mode', ['group','stack'])
                        fig = px.bar(dfp,x=x_column,y=y_columns,color=color_value,barmode=mode)
                        st.plotly_chart(fig)
                    elif plot_type == "line":
                        fig = px.line(dfp,x=x_column,y=y_columns,color=color_value)
                        st.plotly_chart(fig)
                    elif plot_type == "pie":
                        fig = px.pie(dfp, values=y_columns, names=x_column, title='Pie Chart of Dataframe')
                    elif plot_type == "hist":
                        fig = px.histogram(dfp, x=x_column)
                        st.plotly_chart(fig)
                    elif plot_type == "box":
                        fig = px.box(dfp, y=y_columns, x=x_column)
                        st.plotly_chart(fig)
        else:
            st.subheader('Silakan Upload Data Anda (format CSV)')
    else:
        df = px.data.gapminder()
        z1, z2 = st.columns((5,7))
        with z1:
            with st.expander('Data Summary', expanded=True):
                st.write(df.describe())
        with z2:
            with st.expander('Overview Data', expanded=True):
                st.dataframe(df)
        with st.expander('Smart Charts', expanded=True):
            z4,z5,z6 = st.columns((3,1,8))
            with z4:
                st.text("Configuration")
                st.empty()
                dfp = df
                plot_type = st.selectbox('Select Type of Plot',["scatter","bar","line","pie","hist","box"])
                all_columns = dfp.columns
                y_columns = st.selectbox('Select Y Variable', all_columns)
                x_column = st.selectbox('Select X Variable', all_columns,index=1)
                dimension = st.selectbox('Color by', all_columns,index=2)
                # dfp = df[df['nama_pemda'].isin(pemda)]
                color_value = dfp[dimension]
            with z5:
                st.empty()
            with z6:
                if plot_type == "scatter":
                    fig = px.scatter(dfp,x=x_column,y=y_columns,color=color_value)
                    st.plotly_chart(fig)
                elif plot_type == "bar":
                    mode = st.selectbox('Mode', ['group','stack'])
                    fig = px.bar(dfp,x=x_column,y=y_columns,color=color_value,barmode=mode)
                    st.plotly_chart(fig)
                elif plot_type == "line":
                    fig = px.line(dfp,x=x_column,y=y_columns,color=color_value)
                    st.plotly_chart(fig)
                elif plot_type == "pie":
                    fig = px.pie(dfp, values=y_columns, names=x_column, title='Pie Chart of Dataframe')
                elif plot_type == "hist":
                    fig = px.histogram(dfp, x=x_column)
                    st.plotly_chart(fig)
                elif plot_type == "box":
                    fig = px.box(dfp, y=y_columns, x=x_column)
                    st.plotly_chart(fig)
        # Generate the HTML using Pygwalker
elif menu =='Drag & Drop Custom Charts':
    import pygwalker as pyg
    pilihdata = st.sidebar.radio('Pilih Data',['Sample1','Upload Data'])
    # df = pd.read_excel('Rekap_wilayah.xlsx')
    if pilihdata=='Upload Data':
        upl = st.file_uploader('Upload data anda',type=['csv'])
        if upl is not None:
            df = pd.read_csv(upl)
            pyg_html = pyg.walk(df, return_html=True)
            components.html(pyg_html, height=1000, scrolling=True) 
        else:
            st.subheader('Silakan Upload Data Anda (format CSV)') 
    else:
        df = px.data.gapminder()
        pyg_html = pyg.walk(df, return_html=True)
        components.html(pyg_html, height=1000, scrolling=True)
elif menu =='Embedded Dashboard':
    st.subheader('Analisis Awal Data Sample BPJS')
    components.html('''
                    <div style="position: relative; width: 100%; height: 0; padding-top: 56.2500%;
                    padding-bottom: 0; box-shadow: 0 2px 8px 0 rgba(63,69,81,0.16); margin-top: 1.6em; margin-bottom: 0.9em; overflow: hidden;
                    border-radius: 8px; will-change: transform;">
                    <iframe loading="lazy" style="position: absolute; width: 100%; height: 100%; top: 0; left: 0; border: none; padding: 0;margin: 0;"
                        src="https:&#x2F;&#x2F;www.canva.com&#x2F;design&#x2F;DAFu0pQ4-iM&#x2F;view?embed" allowfullscreen="allowfullscreen" allow="fullscreen">
                    </iframe>
                    </div>
                    ''',
                    height=900)
    components.html('''
    <div class="flourish-embed flourish-map" data-src="visualisation/15066948"><script src="https://public.flourish.studio/resources/embed.js"></script></div>
    ''',height=650)
    components.html('''
        <div class='tableauPlaceholder' id='viz1695126013832' style='position: relative'><noscript><a href='#'><img alt='Dashboard 4 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;gr&#47;grip_faskes&#47;Dashboard4&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='grip_faskes&#47;Dashboard4' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;gr&#47;grip_faskes&#47;Dashboard4&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1695126013832');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else { vizElement.style.width='100%';vizElement.style.height='400px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>
        ''',height=400)
elif menu == 'Machine Learning App':
    st.subheader("Classification Prediction")
    import joblib
    import numpy as np
    model= open("model.pkl", "rb")
    knn_clf=joblib.load(model)

    st.sidebar.title("Features")
    #Intializing
    sl = st.sidebar.slider(label="Sepal Length (cm)",value=5.2,min_value=0.0, max_value=8.0, step=0.1)
    sw = st.sidebar.slider(label="Sepal Width (cm)",value=3.2,min_value=0.0, max_value=8.0, step=0.1)
    pl = st.sidebar.slider(label="Petal Length (cm)",value=4.2,min_value=0.0, max_value=8.0, step=0.1)
    pw = st.sidebar.slider(label="Petal Width (cm)",value=1.2,min_value=0.0, max_value=8.0, step=0.1)

    if st.button("Click Here to Classify"):
        dfvalues = pd.DataFrame(list(zip([sl],[sw],[pl],[pw])),columns =['sepal_length', 'sepal_width', 'petal_length', 'petal_width'])
        input_variables = np.array(dfvalues[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']])
        prediction = knn_clf.predict(input_variables)
        if prediction == 1:
            st.write('setosa')
        elif prediction == 2:
            st.write('versicolor')
        elif prediction == 3:
            st.write('virginica')

